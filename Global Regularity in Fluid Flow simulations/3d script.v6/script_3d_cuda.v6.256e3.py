import cupy as cp
import numpy as np
import matplotlib.pyplot as plt
import csv
import time
from functools import lru_cache

# ==============================================================================
# CONFIGURATION
# ==============================================================================
CONFIG = {
    'NX': 256, 'NY': 256, 'NZ': 256,
    'Lx': 2.0 * np.pi, 'Ly': 2.0 * np.pi, 'Lz': 2.0 * np.pi,
    'dt': 1e-7,          # Reduced slightly for RK2 CFL stability
    'steps': 200000,        # Total steps
    'plot_interval': 1000,
    'c_sim': 50.0,         # Effective speed of light
    'nu': 1e-4,            # Kinematic viscosity
    'beta': 1.0,           # Refractive coupling constant
    'u0_amp': 40.0,        # Initial velocity amplitude
    'beta_zero_control': False,  # Set True to run classical NS control case
    'abort_threshold': 60.0     # Safety: stop if |v| > 100 * c_sim
}

# Apply control flag override
if CONFIG['beta_zero_control']:
    CONFIG['beta'] = 0.0
    print("⚠️  RUNNING CONTROL CASE: beta = 0.0 (Classical NS limit)")

# Grid spacing
dx = CONFIG['Lx'] / CONFIG['NX']
dy = CONFIG['Ly'] / CONFIG['NY']
dz = CONFIG['Lz'] / CONFIG['NZ']

GPU_SLEEP_TIME = 0.1

# ==============================================================================
# GPU KERNELS & OPERATORS
# ==============================================================================
def get_wavenumbers(N, L):
    """Create wavenumber grids for spectral methods."""
    k = cp.fft.fftfreq(N, d=L/(2*cp.pi*N))
    kx, ky, kz = cp.meshgrid(k, k, k, indexing='ij')
    k_mag_sq = kx**2 + ky**2 + kz**2
    k_mag_sq = cp.where(k_mag_sq == 0, 1, k_mag_sq)
    return kx, ky, kz, k_mag_sq

@lru_cache(maxsize=1)
def get_spectral_operators():
    """Pre-calculate spectral operators for Poisson solving."""
    kx, ky, kz, k_mag_sq = get_wavenumbers(CONFIG['NX'], CONFIG['Lx'])
    inv_laplacian = -1.0 / k_mag_sq
    inv_laplacian = inv_laplacian.astype(cp.complex128)
    inv_laplacian[0, 0, 0] = 0
    return kx, ky, kz, inv_laplacian

def compute_cuge_terms_gpu(u, v, w, n, n_prev, c, beta, dx, dy, dz, dt):
    # 1. Velocity magnitude squared
    v_sq = u**2 + v**2 + w**2
    
    # 2. Refractive Index
    n[:] = 1.0 + beta * v_sq / (c**2)
    
    # 3. Time derivative of n
    if n_prev is not None:
        n_dot = (n - n_prev) / dt
    else:
        n_dot = cp.zeros_like(n)
    
    # 4. Gradient of n
    grad_nx = (cp.roll(n, -1, axis=0) - cp.roll(n, 1, axis=0)) / (2.0 * dx)
    grad_ny = (cp.roll(n, -1, axis=1) - cp.roll(n, 1, axis=1)) / (2.0 * dy)
    grad_nz = (cp.roll(n, -1, axis=2) - cp.roll(n, 1, axis=2)) / (2.0 * dz)
    
    # 5. CUGE Acceleration Terms
    n_safe = cp.where(n > 1e-6, n, 1.0)
    
    # Refractive Force (NEGATIVE for damping)
    force_x = -(c**2) * grad_nx / n_safe  # ❌ Added negative sign
    force_y = -(c**2) * grad_ny / n_safe
    force_z = -(c**2) * grad_nz / n_safe
    
    # Damping (DON'T CLAMP SIGN)
    damping = n_dot / n_safe
    denom = cp.maximum(1.0 + dt * damping, 0.1)  # Clamp denominator only
    
    acc_x = force_x / denom
    acc_y = force_y / denom
    acc_z = force_z / denom
    
    # EXPLICIT QUARTIC DAMPING (Lemma 2.3)
    quartic_coeff = beta / (c**2)
    acc_x -= quartic_coeff * v_sq * u
    acc_y -= quartic_coeff * v_sq * v
    acc_z -= quartic_coeff * v_sq * w
    
    return acc_x, acc_y, acc_z, n

def compute_imex_cuge_step(u, v, w, n, n_prev, c, beta, dx, dy, dz, dt, 
                           ns_u, ns_v, ns_w, max_iters=4, omega=0.6, tol=1e-8):
    """
    IMEX fixed-point corrector for stiff CUGE refractive terms.
    ns_u/v/w: Explicit Navier-Stokes terms (advection + diffusion)
    omega: Under-relaxation factor (0.5–0.7 recommended for stability)
    """
    # Initial guess = explicit update
    u_imp = u + dt * ns_u
    v_imp = v + dt * ns_v
    w_imp = w + dt * ns_w
    
    for k in range(max_iters):
        v_sq = u_imp**2 + v_imp**2 + w_imp**2
        n_imp = 1.0 + beta * v_sq / (c**2)
        n_dot = (n_imp - n_prev) / dt if n_prev is not None else cp.zeros_like(n_imp)
        n_safe = cp.maximum(n_imp, 1e-6)
        
        # Gradients of n_imp
        grad_nx = (cp.roll(n_imp, -1, axis=0) - cp.roll(n_imp, 1, axis=0)) / (2.0 * dx)
        grad_ny = (cp.roll(n_imp, -1, axis=1) - cp.roll(n_imp, 1, axis=1)) / (2.0 * dy)
        grad_nz = (cp.roll(n_imp, -1, axis=2) - cp.roll(n_imp, 1, axis=2)) / (2.0 * dz)
        
        # Refractive force
        force_x = (c**2) * grad_nx / n_safe
        force_y = (c**2) * grad_ny / n_safe
        force_z = (c**2) * grad_nz / n_safe
        
        # Implicit damping denominator - CRITICAL STABILITY FIX
        damping = n_dot / n_safe
        denom = cp.maximum(1.0 + dt * damping, 0.5)  # Prevent sign flip
        
        acc_x = force_x / denom
        acc_y = force_y / denom
        acc_z = force_z / denom
        
        # IMEX update
        u_new = u + dt * (ns_u + acc_x)
        v_new = v + dt * (ns_v + acc_y)
        w_new = w + dt * (ns_w + acc_z)
        
        # Under-relaxation for convergence stability
        u_imp = omega * u_new + (1.0 - omega) * u_imp
        v_imp = omega * v_new + (1.0 - omega) * v_imp
        w_imp = omega * w_new + (1.0 - omega) * w_imp
        
        # Convergence check
        err = cp.sqrt(cp.mean((u_imp - u_new)**2 + (v_imp - v_new)**2 + (w_imp - w_new)**2)).get()
        if err < tol:
            break
            
    return u_imp, v_imp, w_imp, n_imp

def compute_advection_diffusion_gpu(u, v, w, nu, dx, dy, dz):
    r"""
    Computes standard NS terms: \( -(v \cdot \nabla)v + \nu \Delta v \)
    Uses 2nd order central differences (vectorized).
    """
    # Advection (v . grad) v
    adv_u = u * (cp.roll(u, -1, axis=0) - cp.roll(u, 1, axis=0)) / (2.0 * dx) + \
            v * (cp.roll(u, -1, axis=1) - cp.roll(u, 1, axis=1)) / (2.0 * dy) + \
            w * (cp.roll(u, -1, axis=2) - cp.roll(u, 1, axis=2)) / (2.0 * dz)
            
    adv_v = u * (cp.roll(v, -1, axis=0) - cp.roll(v, 1, axis=0)) / (2.0 * dx) + \
            v * (cp.roll(v, -1, axis=1) - cp.roll(v, 1, axis=1)) / (2.0 * dy) + \
            w * (cp.roll(v, -1, axis=2) - cp.roll(v, 1, axis=2)) / (2.0 * dz)
            
    adv_w = u * (cp.roll(w, -1, axis=0) - cp.roll(w, 1, axis=0)) / (2.0 * dx) + \
            v * (cp.roll(w, -1, axis=1) - cp.roll(w, 1, axis=1)) / (2.0 * dy) + \
            w * (cp.roll(w, -1, axis=2) - cp.roll(w, 1, axis=2)) / (2.0 * dz)

    # Diffusion (Laplacian)
    if nu > 0:
        lap_u = (cp.roll(u, -1, axis=0) - 2*u + cp.roll(u, 1, axis=0)) / (dx*dx) + \
                (cp.roll(u, -1, axis=1) - 2*u + cp.roll(u, 1, axis=1)) / (dy*dy) + \
                (cp.roll(u, -1, axis=2) - 2*u + cp.roll(u, 1, axis=2)) / (dz*dz)
                
        lap_v = (cp.roll(v, -1, axis=0) - 2*v + cp.roll(v, 1, axis=0)) / (dx*dx) + \
                (cp.roll(v, -1, axis=1) - 2*v + cp.roll(v, 1, axis=1)) / (dy*dy) + \
                (cp.roll(v, -1, axis=2) - 2*v + cp.roll(v, 1, axis=2)) / (dz*dz)
                
        lap_w = (cp.roll(w, -1, axis=0) - 2*w + cp.roll(w, 1, axis=0)) / (dx*dx) + \
                (cp.roll(w, -1, axis=1) - 2*w + cp.roll(w, 1, axis=1)) / (dy*dy) + \
                (cp.roll(w, -1, axis=2) - 2*w + cp.roll(w, 1, axis=2)) / (dz*dz)
    else:
        lap_u, lap_v, lap_w = 0.0, 0.0, 0.0

    rhs_u = -adv_u + nu * lap_u
    rhs_v = -adv_v + nu * lap_v
    rhs_w = -adv_w + nu * lap_w

    return rhs_u, rhs_v, rhs_w

def project_velocity_gpu(u, v, w, inv_laplacian):
    r"""Solves Pressure Poisson Equation using FFT. Enforces \( \nabla \cdot v = 0 \)."""
    div = (cp.roll(u, -1, axis=0) - cp.roll(u, 1, axis=0)) / (2.0 * dx) + \
          (cp.roll(v, -1, axis=1) - cp.roll(v, 1, axis=1)) / (2.0 * dy) + \
          (cp.roll(w, -1, axis=2) - cp.roll(w, 1, axis=2)) / (2.0 * dz)
          
    div_hat = cp.fft.fftn(div)
    p_hat = div_hat * inv_laplacian
    p = cp.fft.ifftn(p_hat).real

    grad_px = (cp.roll(p, -1, axis=0) - cp.roll(p, 1, axis=0)) / (2.0 * dx)
    grad_py = (cp.roll(p, -1, axis=1) - cp.roll(p, 1, axis=1)) / (2.0 * dy)
    grad_pz = (cp.roll(p, -1, axis=2) - cp.roll(p, 1, axis=2)) / (2.0 * dz)

    u -= grad_px
    v -= grad_py
    w -= grad_pz
    return u, v, w

def apply_spectral_filter(u, v, w, k_mag_sq, cutoff=0.75):
    """Exponential filter to suppress grid-scale aliasing without affecting low-k physics."""
    kx, ky, kz, _ = get_wavenumbers(CONFIG['NX'], CONFIG['Lx'])
    k_mag = cp.sqrt(k_mag_sq)
    k_max = cp.max(k_mag)
    
    # Sharp exponential cutoff: exp(-36 * (k/k_max)^8)
    alpha, p = 36.0, 8
    factor = cp.exp(-alpha * (k_mag / k_max)**p)
    factor = cp.where(k_mag > cutoff * k_max, factor, 1.0)
    
    u = cp.fft.ifftn(cp.fft.fftn(u) * factor).real
    v = cp.fft.ifftn(cp.fft.fftn(v) * factor).real
    w = cp.fft.ifftn(cp.fft.fftn(w) * factor).real
    return u, v, w

def compute_diagnostics_gpu(u, v, w, n, c, beta):
    """
    Computes diagnostics matching paper theory:
    - Kinetic Energy: 1/2 int |v|^2
    - Weighted Energy: 1/2 int n |v|^2
    - Vacuum Energy (VSS): 1/2 int (n-1) |v|^2 = (beta/2c^2) int |v|^4
    """
    v_sq = u**2 + v**2 + w**2
    
    ke = cp.sum(0.5 * v_sq)
    max_v = cp.sqrt(cp.max(v_sq))
    
    # Weighted Energy E(t) = 1/2 int n |v|^2
    weighted_energy = cp.sum(0.5 * n * v_sq)
    
    # Vacuum Energy = 1/2 int (n-1) |v|^2 
    # Since n-1 = beta*v^2/c^2, this is proportional to |v|^4
    vacuum_energy = cp.sum(0.5 * (n - 1.0) * v_sq)
    
    # Quartic Dissipation Term (for Lemma 2.3 check)
    quartic_diss = cp.sum((beta / (c**2)) * v_sq**2)
    
    return ke, max_v, weighted_energy, vacuum_energy, quartic_diss

def compute_energy_spectrum_gpu(u, v, w, k_mag_sq):
    r"""Computes 3D Energy Spectrum \( E(k) \) using FFT."""
    u_hat = cp.fft.fftn(u)
    v_hat = cp.fft.fftn(v)
    w_hat = cp.fft.fftn(w)
    energy_hat = 0.5 * (cp.abs(u_hat)**2 + cp.abs(v_hat)**2 + cp.abs(w_hat)**2)
    
    energy_hat = cp.fft.fftshift(energy_hat)
    kx, ky, kz, _ = get_wavenumbers(CONFIG['NX'], CONFIG['Lx'])
    k_mag = cp.sqrt(cp.fft.fftshift(k_mag_sq))
    
    k_max = cp.max(k_mag).get()
    num_bins = int(CONFIG['NX'] / 2)
    k_bins = cp.linspace(0, k_max, num_bins + 1)
    k_centers = 0.5 * (k_bins[:-1] + k_bins[1:])
    
    k_flat = k_mag.flatten()
    E_flat = energy_hat.flatten()
    indices = cp.digitize(k_flat, k_bins) - 1
    
    valid_mask = (indices >= 0) & (indices < num_bins)
    valid_indices = indices[valid_mask].astype(cp.int32)
    valid_energy = E_flat[valid_mask]
    
    E_k = cp.bincount(valid_indices, weights=valid_energy, minlength=num_bins)
    counts = cp.bincount(valid_indices, minlength=num_bins).astype(cp.float64)
    counts = cp.where(counts > 0, counts, 1.0)
    E_k = E_k / counts
    
    return k_centers.get(), E_k.get()

# ==============================================================================
# MAIN SIMULATION
# ==============================================================================
def run_simulation():
    print(f"Starting CUGE/REFORM 3D Fluid Simulation (CUDA, {CONFIG['NX']}^3)")
    print(f"Parameters: c={CONFIG['c_sim']}, nu={CONFIG['nu']}, beta={CONFIG['beta']}, dt={CONFIG['dt']}")
    print(f"Device: {cp.cuda.runtime.getDeviceProperties(0)['name']}")
    
    # === FIX: Unpack CONFIG variables to local scope ===
    steps = CONFIG['steps']
    plot_interval = CONFIG['plot_interval']
    c_sim = CONFIG['c_sim']
    beta = CONFIG['beta']
    nu = CONFIG['nu']
    dt = CONFIG['dt']
    u0_amp = CONFIG['u0_amp']
    NX = CONFIG['NX']
    Lx = CONFIG['Lx']
    Ly = CONFIG['Ly']
    Lz = CONFIG['Lz']
    # ================================================

    # Initialize Fields
    u = cp.zeros((CONFIG['NZ'], CONFIG['NY'], CONFIG['NX']))
    v = cp.zeros((CONFIG['NZ'], CONFIG['NY'], CONFIG['NX']))
    w = cp.zeros((CONFIG['NZ'], CONFIG['NY'], CONFIG['NX']))
    n = cp.ones((CONFIG['NZ'], CONFIG['NY'], CONFIG['NX']))
    n_prev = None

    # Initial Condition: 3D Taylor-Green Vortex
    x = cp.linspace(0, CONFIG['Lx'], CONFIG['NX'])
    y = cp.linspace(0, CONFIG['Ly'], CONFIG['NY'])
    z = cp.linspace(0, CONFIG['Lz'], CONFIG['NZ'])
    X, Y, Z = cp.meshgrid(x, y, z, indexing='ij')
    
    u[:] = CONFIG['u0_amp'] * cp.sin(X) * cp.cos(Y) * cp.cos(Z)
    v[:] = -CONFIG['u0_amp'] * cp.cos(X) * cp.sin(Y) * cp.cos(Z)
    w[:] = 0.0

    _, _, _, inv_laplacian = get_spectral_operators()

    # Storage
    time_log, ke_log, max_v_log, weighted_log, quartic_log, vss_log = [], [], [], [], [], []
    csv_data = [["Time", "Kinetic_Energy", "Max_Velocity", "Weighted_Energy", "Quartic_Dissipation", "VSS_Energy", "Step"]]
    spec_k_init = spec_E_init = spec_k_final = spec_E_final = None

    start_time = time.time()
    print("Warming up CUDA kernels...")
    _ = compute_cuge_terms_gpu(u, v, w, n, n_prev, CONFIG['c_sim'], CONFIG['beta'], dx, dy, dz, CONFIG['dt'])
    cp.cuda.Stream.null.synchronize()

    for step in range(steps):
        # Cache current state
        n_prev_step = n.copy() if n_prev is not None else None
        
        # 1. Compute Explicit NS Terms (advection + diffusion)
        ns_x, ns_y, ns_z = compute_advection_diffusion_gpu(u, v, w, nu, dx, dy, dz)
        
        # 2. IMEX Corrector (handles stiff CUGE terms implicitly)
        u, v, w, n = compute_imex_cuge_step(
            u, v, w, n, n_prev_step, c_sim, beta, dx, dy, dz, dt,
            ns_x, ns_y, ns_z, max_iters=10, omega=0.5
        )
        
        # Update n_prev for next step
        n_prev = n_prev_step
        
        # 3. Projection Step (Enforce Incompressibility)
        u, v, w = project_velocity_gpu(u, v, w, inv_laplacian)
        
        if step % 100 == 0:
            ke, max_v, weighted_energy, vacuum_energy, quartic_diss = compute_diagnostics_gpu(u, v, w, n, c_sim, beta)
            
            # Check energy growth rate
            if len(ke_log) > 10:
                ke_growth = (ke_log[-1] - ke_log[-10]) / ke_log[-10]
                if ke_growth > 0.01:  # >1% growth per 1000 steps
                    print(f"⚠️ WARNING: Energy growing too fast: {ke_growth:.4f}")
                    if ke_growth > 0.05:
                        print("🛑 ABORT: Unstable energy growth")
                        break
        
        # Apply filter every 10 steps to kill aliasing before it triggers stiffness
        if step % 1 == 0:
            _, _, _, k_mag_sq = get_wavenumbers(CONFIG['NX'], CONFIG['Lx'])
            u, v, w = apply_spectral_filter(u, v, w, k_mag_sq, cutoff=0.5)
        
        # === GPU THROTTLING FOR COOLING ===
        if step % 10 == 0:  # Sync every 10 steps
            cp.cuda.Stream.null.synchronize()
            time.sleep(GPU_SLEEP_TIME)
        
        # 4. Diagnostics
        if step % plot_interval == 0:
            # FIX: Correct function name typo and unpack all 5 returned values
            ke, max_v, weighted_energy, vacuum_energy, quartic_diss = compute_diagnostics_gpu(u, v, w, n, c_sim, beta)
            
            # Transfer to CPU for logging
            ke_cpu = ke.get()
            max_v_cpu = max_v.get()
            weighted_energy_cpu = weighted_energy.get()
            vacuum_energy_cpu = vacuum_energy.get()
            quartic_diss_cpu = quartic_diss.get()
            current_time = step * dt
            
            time_log.append(current_time)
            ke_log.append(ke_cpu)
            max_v_log.append(max_v_cpu)
            weighted_log.append(weighted_energy_cpu)
            quartic_log.append(quartic_diss_cpu)
            vss_log.append(vacuum_energy_cpu)
            
            # Matches CSV headers: Time, Kinetic, MaxV, Weighted, Quartic, VSS, Step
            csv_data.append([current_time, ke_cpu, max_v_cpu, weighted_energy_cpu, quartic_diss_cpu, vacuum_energy_cpu, step])
            
            # Spectrum & Print Logic (unchanged)
            if step == 0:
                spec_k_init, spec_E_init = compute_energy_spectrum_gpu(u, v, w, get_wavenumbers(NX, Lx)[3])
                print(f"Step {step}: KE={ke_cpu:.4f}, MaxV={max_v_cpu:.4f} (Spectrum Computed)")
            elif step == steps - plot_interval:
                spec_k_final, spec_E_final = compute_energy_spectrum_gpu(u, v, w, get_wavenumbers(NX, Lx)[3])
                print(f"Step {step}: KE={ke_cpu:.4f}, MaxV={max_v_cpu:.4f} (Spectrum Computed)")
            else:
                print(f"Step {step}: KE={ke_cpu:.4f}, MaxV={max_v_cpu:.4f}")
            
            # Stability Check
            if max_v_cpu > c_sim * 1.05:
                print(f"WARNING: Velocity exceeded c_sim by >5%")
                break
            if cp.isnan(ke).any():
                print("ERROR: NaN detected")
                break

    cp.cuda.Stream.null.synchronize()
    print(f"Simulation completed in {time.time() - start_time:.2f} seconds.")

    # Save CSV
    with open('simulation_results_3d_v2.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
    print("Data saved to 'simulation_results_3d_v2.csv'")

    # Plotting
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1, 3, 1)
    plt.plot(time_log, ke_log, label='Kinetic Energy')
    # FIX: Raw string with modern LaTeX delimiters
    plt.plot(time_log, weighted_log, label=r'Weighted Energy \(E(t)\)', linestyle='--')
    plt.xlabel('Time')
    plt.ylabel('Energy Density')
    plt.title('Energy Partitioning (Eq 2.1)')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 3, 2)
    plt.plot(time_log, max_v_log, label='Max Velocity', color='red')
    plt.axhline(y=CONFIG['c_sim'], color='k', linestyle=':', label='c_sim limit')
    plt.xlabel('Time')
    # FIX: Raw string with modern LaTeX delimiters
    plt.ylabel(r'Max \(|v|\)')
    plt.title('Velocity Evolution')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 3, 3)
    # FIX: Raw string with modern LaTeX delimiters
    plt.plot(time_log, quartic_log, label=r'Quartic Dissipation \(D_{\text{quartic}}\)', color='purple')
    plt.xlabel('Time')
    plt.ylabel('Dissipation Rate')
    plt.title('Theoretical Damping (Lemma 2.3)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

    # Energy Spectrum
    if spec_k_init is not None and spec_k_final is not None:
        plt.figure(figsize=(8, 6))
        plt.loglog(spec_k_init, spec_E_init, 'b-', label='Initial Spectrum (t=0)', alpha=0.5)
        plt.loglog(spec_k_final, spec_E_final, 'r-', label=f'Final Spectrum (t={CONFIG["steps"]*CONFIG["dt"]:.3f})', linewidth=2)
        
        k_ref = spec_k_final[5:20]
        E_ref = spec_k_final[5:20]
        idx = np.argmin(np.abs(k_ref - 1.0))
        if idx < len(k_ref):
            C = E_ref[idx] * (k_ref[idx]**(5/3))
            k_line = np.linspace(spec_k_final[1], spec_k_final[-1], 100)
            plt.loglog(k_line, C / k_line**(5/3), 'k--', label=r'Reference \(k^{-5/3}\) (Kolmogorov)')
            
        # FIX: Raw strings with modern LaTeX delimiters
        plt.xlabel(r'Wavenumber \(k\)')
        plt.ylabel(r'Energy Density \(E(k)\)')
        plt.title('3D Energy Spectrum Analysis')
        plt.legend()
        plt.grid(True, which='both', alpha=0.3)
        plt.show()

if __name__ == "__main__":
    run_simulation()