import cupy as cp
import numpy as np
import matplotlib.pyplot as plt
import time
import csv
from functools import lru_cache

#==============================================================================
# CONFIGURATION (256^3 Grid for RTX 3090)
#==============================================================================
# Grid Dimensions (Power of 2 for FFT efficiency)
NX, NY, NZ = 256, 256, 256
Lx, Ly, Lz = 2.0 * np.pi, 2.0 * np.pi, 2.0 * np.pi
dx = Lx / NX
dy = Ly / NY
dz = Lz / NZ

# Time Stepping
dt = 0.01                 # Time step (Monitor stability with finer grid)
steps = 50000             # Total steps
plot_interval = 1000      # Logging frequency

# Physical Parameters (CUGE/REFORM)
G = 1.0                   # Gravitational constant
c_sim = 30.0              # Effective speed of light
MASS_SCALE = 10.0         # Mass per particle
N_PARTICLES = 10000       # Number of bodies

# Output Files
CSV_FILENAME = 'cuge_nbody_3d_256_results.csv'
PNG_FILENAME = 'cuge_nbody_3d_256_energy.png'

#==============================================================================
# SPECTRAL OPERATORS (FFT Wavenumbers)
#==============================================================================
def get_wavenumbers(N, L):
    """
    Create wavenumber grids for spectral methods.
    """
    k = cp.fft.fftfreq(N, d=L/(2*cp.pi*N))
    kx, ky, kz = cp.meshgrid(k, k, k, indexing='ij')
    k_mag_sq = kx**2 + ky**2 + kz**2
    k_mag_sq = cp.where(k_mag_sq == 0, 1, k_mag_sq)
    return kx, ky, kz, k_mag_sq

@lru_cache(maxsize=1)
def get_spectral_operators():
    """
    Pre-calculate spectral operators for Poisson solving.
    """
    kx, ky, kz, k_mag_sq = get_wavenumbers(NX, Lx)
    green_func = 1.0 / k_mag_sq
    green_func = green_func.astype(cp.complex128)
    green_func[0, 0, 0] = 0
    return kx, ky, kz, green_func

#==============================================================================
# MASS DEPOSITION (Particle-to-Grid)
#==============================================================================
def deposit_mass_gpu(pos, masses, shape, L):
    """
    Maps particle positions to grid density rho(r).
    """
    rho = cp.zeros(shape, dtype=cp.float64)
    N = pos.shape[0]
    
    # Normalize positions to grid indices
    ix = (pos[:, 0] / L[0] * shape[2]).astype(cp.int32) % shape[2]
    iy = (pos[:, 1] / L[1] * shape[1]).astype(cp.int32) % shape[1]
    iz = (pos[:, 2] / L[2] * shape[0]).astype(cp.int32) % shape[0]
    
    # Scatter add masses to grid
    cp.add.at(rho, (iz, iy, ix), masses)
    
    return rho

#==============================================================================
# POTENTIAL SOLVER (Poisson Equation)
#==============================================================================
def solve_potential_gpu(rho, green_func, G):
    """
    Solves Poisson Equation using FFT.
    Eq: nabla^2 Phi = -4*pi*G*rho
    """
    rho_hat = cp.fft.fftn(rho)
    phi_hat = 4 * cp.pi * G * rho_hat * green_func
    phi = cp.fft.ifftn(phi_hat).real
    return phi

#==============================================================================
# VACUUM STRAIN ENERGY (Grid-Based)
#==============================================================================
def compute_vacuum_energy_gpu(phi, c, dx, dy, dz):
    """
    Computes Vacuum Strain Energy from potential field gradients.
    
    Based on CUGE/REFORM framework (Section 2.1-2.2):
    \\[
    E_{\\text{vac}} \\propto \\int |\\nabla \\Phi|^2 \\, \\mathrm{d}V
    \\]
    """
    # Compute gradient of potential (Central Differences)
    grad_phi_x = (cp.roll(phi, -1, axis=2) - cp.roll(phi, 1, axis=2)) / (2.0 * dx)
    grad_phi_y = (cp.roll(phi, -1, axis=1) - cp.roll(phi, 1, axis=1)) / (2.0 * dy)
    grad_phi_z = (cp.roll(phi, -1, axis=0) - cp.roll(phi, 1, axis=0)) / (2.0 * dz)
    
    # Squared gradient magnitude
    grad_phi_sq = grad_phi_x**2 + grad_phi_y**2 + grad_phi_z**2
    
    # Vacuum energy (proportional to |grad_Phi|^2 integrated over volume)
    e_vac = cp.sum(grad_phi_sq) * dx * dy * dz
    
    return e_vac

#==============================================================================
# CUGE ACCELERATION FIELD (Grid-Based)
#==============================================================================
def compute_cuge_acceleration_gpu(phi, phi_prev, c, dt, dx, dy, dz):
    """
    Computes CUGE Acceleration on Grid based on Refractive Index n.
    
    Physics (Ref: Unprecedented-Stability...md Eq 2.6):
    \\[
    \\frac{\\mathrm{d}\\mathbf{v}}{\\mathrm{d}t}=\\frac{c^2}{n}\\nabla n-\\frac{\\dot{n}}{n}\\mathbf{v}
    \\]
    Where:
    \\[
    n(\\mathbf{r},t)\\approx1+\\frac{\\Phi(\\mathbf{r},t)}{2c^2}
    \\]
    """
    # 1. Refractive Index
    n = 1.0 + phi / (2.0 * c**2)
    
    # 2. Time derivative of n (explicit finite difference)
    if phi_prev is not None:
        n_prev = 1.0 + phi_prev / (2.0 * c**2)
        n_dot = (n - n_prev) / dt
    else:
        n_dot = cp.zeros_like(n)
    
    # 3. Gradient of n (Central Differences)
    grad_nx = (cp.roll(n, -1, axis=2) - cp.roll(n, 1, axis=2)) / (2.0 * dx)
    grad_ny = (cp.roll(n, -1, axis=1) - cp.roll(n, 1, axis=1)) / (2.0 * dy)
    grad_nz = (cp.roll(n, -1, axis=0) - cp.roll(n, 1, axis=0)) / (2.0 * dz)
    
    # 4. CUGE Acceleration Terms
    n_safe = cp.where(n > 1e-6, n, 1.0)
    
    # Refractive Force term: c^2 * grad_n / n
    force_x = (c**2) * grad_nx / n_safe
    force_y = (c**2) * grad_ny / n_safe
    force_z = (c**2) * grad_nz / n_safe
    
    # Damping coefficient: dot_n / n
    damping_coeff = n_dot / n_safe
    
    return force_x, force_y, force_z, damping_coeff

#==============================================================================
# FORCE INTERPOLATION (Grid-to-Particle)
#==============================================================================
def interpolate_force_gpu(force_x, force_y, force_z, damp_coeff, pos, vel):
    """
    Interpolates grid forces back to particle positions.
    
    Logic:
    \\[
    \\mathbf{a}_p = \\mathbf{F}_{\\text{grid}}(\\mathbf{r}_p) - \\text{coeff}_{\\text{grid}}(\\mathbf{r}_p) \\cdot \\mathbf{v}_p
    \\]
    """
    N = pos.shape[0]
    acc = cp.zeros_like(pos)
    
    # Normalize positions to grid indices
    ix = (pos[:, 0] / Lx * NX).astype(cp.int32) % NX
    iy = (pos[:, 1] / Ly * NY).astype(cp.int32) % NY
    iz = (pos[:, 2] / Lz * NZ).astype(cp.int32) % NZ
    
    # Gather field values
    fx = force_x[iz, iy, ix]
    fy = force_y[iz, iy, ix]
    fz = force_z[iz, iy, ix]
    dc = damp_coeff[iz, iy, ix]
    
    # Apply damping using particle velocity
    ax = fx - dc * vel[:, 0]
    ay = fy - dc * vel[:, 1]
    az = fz - dc * vel[:, 2]
    
    acc[:, 0] = ax
    acc[:, 1] = ay
    acc[:, 2] = az
    
    return acc

#==============================================================================
# MAIN SIMULATION LOOP
#==============================================================================
def run_simulation():
    print(f"Starting CUGE/REFORM 3D n-Body Simulation (CUDA, {NX}x{NY}x{NZ})")
    print(f"Particles: {N_PARTICLES}, Steps: {steps}, dt: {dt}")
    print(f"Device: {cp.cuda.runtime.getDeviceProperties(0)['name']}")
    
    # --- Initialize Particles ---
    rng = cp.random.default_rng(12345)
    pos = rng.uniform(-Lx/2, Lx/2, size=(N_PARTICLES, 3))
    vel = rng.uniform(-1.0, 1.0, size=(N_PARTICLES, 3))
    masses = cp.ones(N_PARTICLES) * MASS_SCALE
    
    # --- Initialize Fields ---
    phi = cp.zeros((NZ, NY, NX))
    phi_prev = None
    
    # --- Storage for Diagnostics & CSV ---
    time_log = []
    ke_log = []
    max_v_log = []
    e_vac_log = []
    e_total_log = []
    csv_data = []
    csv_data.append(["Time", "Kinetic_Energy", "Vacuum_Energy", "Total_Energy", "Max_Velocity", "Step"])
    
    start_time = time.time()
    
    # --- Pre-compute Spectral Operators ---
    _, _, _, green_func = get_spectral_operators()
    
    # --- Warm-up Kernels ---
    rho = deposit_mass_gpu(pos, masses, (NZ, NY, NX), (Lx, Ly, Lz))
    phi = solve_potential_gpu(rho, green_func, G)
    fx, fy, fz, dc = compute_cuge_acceleration_gpu(phi, phi_prev, c_sim, dt, dx, dy, dz)
    e_vac = compute_vacuum_energy_gpu(phi, c_sim, dx, dy, dz)
    cp.cuda.Stream.null.synchronize()
    
    print("Kernels warmed up. Starting integration...")
    
    for step in range(steps):
        # 1. Deposit Mass to Grid
        rho = deposit_mass_gpu(pos, masses, (NZ, NY, NX), (Lx, Ly, Lz))
        
        # 2. Solve Potential (Poisson)
        phi = solve_potential_gpu(rho, green_func, G)
        
        # 3. Compute Grid Acceleration Fields (CUGE)
        force_x, force_y, force_z, damp_coeff = compute_cuge_acceleration_gpu(
            phi, phi_prev, c_sim, dt, dx, dy, dz
        )
        
        # 4. Leapfrog Integration (Kick-Drift-Kick)
        # Kick (Half Step)
        acc = interpolate_force_gpu(force_x, force_y, force_z, damp_coeff, pos, vel)
        vel += 0.5 * dt * acc
        
        # Drift (Full Step)
        pos += dt * vel
        
        # Re-evaluate fields at new position for second Kick (Symplectic)
        rho_new = deposit_mass_gpu(pos, masses, (NZ, NY, NX), (Lx, Ly, Lz))
        phi_new = solve_potential_gpu(rho_new, green_func, G)
        
        force_x2, force_y2, force_z2, damp_coeff2 = compute_cuge_acceleration_gpu(
            phi_new, phi, c_sim, dt, dx, dy, dz
        )
        
        # Kick (Half Step)
        acc_new = interpolate_force_gpu(force_x2, force_y2, force_z2, damp_coeff2, pos, vel)
        vel += 0.5 * dt * acc_new
        
        # Update phi for next step time derivative
        phi = phi_new
        phi_prev = phi.copy()
        
        # --- Diagnostics & CSV Logging ---
        if step % plot_interval == 0:
            v_sq = cp.sum(vel**2, axis=1)
            ke = cp.sum(0.5 * masses * v_sq)
            max_v = cp.sqrt(cp.max(v_sq))
            e_vac = compute_vacuum_energy_gpu(phi, c_sim, dx, dy, dz)
            e_total = ke + e_vac
            
            # Transfer to CPU for logging
            ke_cpu = ke.get()
            e_vac_cpu = e_vac.get()
            e_total_cpu = e_total.get()
            max_v_cpu = max_v.get()
            current_time = step * dt
            
            time_log.append(current_time)
            ke_log.append(ke_cpu)
            e_vac_log.append(e_vac_cpu)
            e_total_log.append(e_total_cpu)
            max_v_log.append(max_v_cpu)
            csv_data.append([current_time, ke_cpu, e_vac_cpu, e_total_cpu, max_v_cpu, step])
            
            print(f"Step {step}: KE={ke_cpu:.4f}, E_vac={e_vac_cpu:.4f}, E_tot={e_total_cpu:.4f}, MaxV={max_v_cpu:.4f}")
            
            # Stability Check
            if max_v_cpu > c_sim * 1.5:
                print("WARNING: Velocity exceeded limit.")
                break

    end_time = time.time()
    print(f"Simulation completed in {end_time - start_time:.2f} seconds.")
    
    # --- Save CSV ---
    try:
        with open(CSV_FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)
        print(f"Data saved to '{CSV_FILENAME}'")
    except Exception as e:
        print(f"Failed to save CSV: {e}")
    
    # --- Plotting Results ---
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Panel 1: Kinetic Energy Evolution
    axes[0, 0].plot(time_log, ke_log, 'b-', linewidth=1.5, label='Kinetic Energy')
    axes[0, 0].set_xlabel('Time')
    axes[0, 0].set_ylabel('Energy')
    axes[0, 0].set_title('Kinetic Energy Evolution')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Panel 2: Vacuum Energy Evolution
    axes[0, 1].plot(time_log, e_vac_log, 'm-.', linewidth=1.5, label='Vacuum Strain Energy')
    axes[0, 1].set_xlabel('Time')
    axes[0, 1].set_ylabel('Energy')
    axes[0, 1].set_title('Vacuum Strain Energy ($E_{vac} \\propto \\int |\\nabla \\Phi|^2 dV$)')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Panel 3: Total Energy (Conservation Check)
    axes[1, 0].plot(time_log, e_total_log, 'g-', linewidth=1.5, label='Total Energy (KE + E_vac)')
    axes[1, 0].set_xlabel('Time')
    axes[1, 0].set_ylabel('Energy')
    axes[1, 0].set_title('Total Energy Conservation')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Panel 4: Velocity Stability
    axes[1, 1].plot(time_log, max_v_log, 'r-', linewidth=1.5, label='Max Velocity')
    axes[1, 1].axhline(y=c_sim, color='k', linestyle=':', linewidth=2, label='c_sim limit')
    axes[1, 1].set_xlabel('Time')
    axes[1, 1].set_ylabel('Max |v|')
    axes[1, 1].set_title('Velocity Stability')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(PNG_FILENAME, dpi=300)
    print(f"Figure saved to '{PNG_FILENAME}'")
    plt.show()

if __name__ == "__main__":
    try:
        run_simulation()
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()