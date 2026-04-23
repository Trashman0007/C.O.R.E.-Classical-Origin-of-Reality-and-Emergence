import cupy as cp
import numpy as np
import matplotlib.pyplot as plt
import time
import csv
from functools import lru_cache

#==============================================================================
# CONFIGURATION (256^3 Grid for RTX 3090 - Dual Physics Comparison)
#==============================================================================
# Grid Dimensions
NX, NY, NZ = 256, 256, 256
Lx, Ly, Lz = 2.0 * np.pi, 2.0 * np.pi, 2.0 * np.pi
dx = Lx / NX
dy = Ly / NY
dz = Lz / NZ

# Time Stepping
dt = 0.01
steps = 200000
plot_interval = 1000

# Physical Parameters
G = 1.0
c_sim = 30.0
MASS_SCALE = 10.0
N_PARTICLES = 10000

# Output Files
CSV_FILENAME = 'cuge_vs_newton_256_results.csv'
PNG_FILENAME = 'cuge_vs_newton_256_comparison.png'

#==============================================================================
# SPECTRAL OPERATORS (FFT Wavenumbers)
#==============================================================================
def get_wavenumbers(N, L):
    k = cp.fft.fftfreq(N, d=L/(2*cp.pi*N))
    kx, ky, kz = cp.meshgrid(k, k, k, indexing='ij')
    k_mag_sq = kx**2 + ky**2 + kz**2
    k_mag_sq = cp.where(k_mag_sq == 0, 1, k_mag_sq)
    return kx, ky, kz, k_mag_sq

@lru_cache(maxsize=1)
def get_spectral_operators():
    kx, ky, kz, k_mag_sq = get_wavenumbers(NX, Lx)
    green_func = 1.0 / k_mag_sq
    green_func = green_func.astype(cp.complex128)
    green_func[0, 0, 0] = 0
    return kx, ky, kz, green_func

#==============================================================================
# MASS DEPOSITION (Particle-to-Grid)
#==============================================================================
def deposit_mass_gpu(pos, masses, shape, L):
    rho = cp.zeros(shape, dtype=cp.float64)
    N = pos.shape[0]
    
    ix = (pos[:, 0] / L[0] * shape[2]).astype(cp.int32) % shape[2]
    iy = (pos[:, 1] / L[1] * shape[1]).astype(cp.int32) % shape[1]
    iz = (pos[:, 2] / L[2] * shape[0]).astype(cp.int32) % shape[0]
    
    cp.add.at(rho, (iz, iy, ix), masses)
    
    return rho

#==============================================================================
# POTENTIAL SOLVER (Poisson Equation)
#==============================================================================
def solve_potential_gpu(rho, green_func, G):
    rho_hat = cp.fft.fftn(rho)
    phi_hat = 4 * cp.pi * G * rho_hat * green_func
    phi = cp.fft.ifftn(phi_hat).real
    return phi

#==============================================================================
# VACUUM STRAIN ENERGY (CUGE Only)
#==============================================================================
def compute_vacuum_energy_gpu(phi, c, dx, dy, dz):
    grad_phi_x = (cp.roll(phi, -1, axis=2) - cp.roll(phi, 1, axis=2)) / (2.0 * dx)
    grad_phi_y = (cp.roll(phi, -1, axis=1) - cp.roll(phi, 1, axis=1)) / (2.0 * dy)
    grad_phi_z = (cp.roll(phi, -1, axis=0) - cp.roll(phi, 1, axis=0)) / (2.0 * dz)
    
    grad_phi_sq = grad_phi_x**2 + grad_phi_y**2 + grad_phi_z**2
    e_vac = cp.sum(grad_phi_sq) * dx * dy * dz * (NX * NY * NZ)
    
    return e_vac

#==============================================================================
# CUGE ACCELERATION FIELD
#==============================================================================
def compute_cuge_acceleration_gpu(phi, phi_prev, c, dt, dx, dy, dz):
    n = 1.0 + phi / (2.0 * c**2)
    
    if phi_prev is not None:
        n_prev = 1.0 + phi_prev / (2.0 * c**2)
        n_dot = (n - n_prev) / dt
    else:
        n_dot = cp.zeros_like(n)
    
    grad_nx = (cp.roll(n, -1, axis=2) - cp.roll(n, 1, axis=2)) / (2.0 * dx)
    grad_ny = (cp.roll(n, -1, axis=1) - cp.roll(n, 1, axis=1)) / (2.0 * dy)
    grad_nz = (cp.roll(n, -1, axis=0) - cp.roll(n, 1, axis=0)) / (2.0 * dz)
    
    n_safe = cp.where(n > 1e-6, n, 1.0)
    
    force_x = (c**2) * grad_nx / n_safe
    force_y = (c**2) * grad_ny / n_safe
    force_z = (c**2) * grad_nz / n_safe
    
    damping_coeff = n_dot / n_safe
    
    return force_x, force_y, force_z, damping_coeff

#==============================================================================
# NEWTONIAN ACCELERATION FIELD (Standard Gravity)
#==============================================================================
def compute_newton_acceleration_gpu(phi, dx, dy, dz):
    grad_phi_x = (cp.roll(phi, -1, axis=2) - cp.roll(phi, 1, axis=2)) / (2.0 * dx)
    grad_phi_y = (cp.roll(phi, -1, axis=1) - cp.roll(phi, 1, axis=1)) / (2.0 * dy)
    grad_phi_z = (cp.roll(phi, -1, axis=0) - cp.roll(phi, 1, axis=0)) / (2.0 * dz)
    
    # Newtonian: a = -grad(Phi)
    acc_x = -grad_phi_x
    acc_y = -grad_phi_y
    acc_z = -grad_phi_z
    
    return acc_x, acc_y, acc_z

#==============================================================================
# FORCE INTERPOLATION (Grid-to-Particle)
#==============================================================================
def interpolate_force_gpu(force_x, force_y, force_z, damp_coeff, pos, vel, use_damping=True):
    N = pos.shape[0]
    acc = cp.zeros_like(pos)
    
    ix = (pos[:, 0] / Lx * NX).astype(cp.int32) % NX
    iy = (pos[:, 1] / Ly * NY).astype(cp.int32) % NY
    iz = (pos[:, 2] / Lz * NZ).astype(cp.int32) % NZ
    
    fx = force_x[iz, iy, ix]
    fy = force_y[iz, iy, ix]
    fz = force_z[iz, iy, ix]
    
    if use_damping and damp_coeff is not None:
        dc = damp_coeff[iz, iy, ix]
        ax = fx - dc * vel[:, 0]
        ay = fy - dc * vel[:, 1]
        az = fz - dc * vel[:, 2]
    else:
        ax = fx
        ay = fy
        az = fz
    
    acc[:, 0] = ax
    acc[:, 1] = ay
    acc[:, 2] = az
    
    return acc

#==============================================================================
# MAIN SIMULATION LOOP (Dual Physics)
#==============================================================================
def run_simulation():
    print(f"Starting CUGE vs Newtonian 3D n-Body Comparison (CUDA, {NX}x{NY}x{NZ})")
    print(f"Particles: {N_PARTICLES}, Steps: {steps}, dt: {dt}")
    print(f"Device: {cp.cuda.runtime.getDeviceProperties(0)['name']}")
    
    # --- Initialize Particles (SAME INITIAL CONDITIONS FOR BOTH) ---
    rng = cp.random.default_rng(12345)
    
    # CUGE Particles
    pos_cuge = rng.uniform(-Lx/2, Lx/2, size=(N_PARTICLES, 3))
    vel_cuge = rng.uniform(-1.0, 1.0, size=(N_PARTICLES, 3))
    
    # Newtonian Particles (IDENTICAL initial state)
    pos_newt = pos_cuge.copy()
    vel_newt = vel_cuge.copy()
    
    masses = cp.ones(N_PARTICLES) * MASS_SCALE
    
    # --- Initialize Fields ---
    phi_cuge = cp.zeros((NZ, NY, NX))
    phi_newt = cp.zeros((NZ, NY, NX))
    phi_prev_cuge = None
    
    # --- Storage for Diagnostics & CSV ---
    time_log = []
    ke_cuge_log = []
    ke_newt_log = []
    max_v_cuge_log = []
    max_v_newt_log = []
    e_vac_cuge_log = []
    e_total_cuge_log = []
    csv_data = []
    csv_data.append(["Time", "KE_CUGE", "KE_Newton", "E_vac_CUGE", "E_total_CUGE", 
                     "MaxV_CUGE", "MaxV_Newton", "Step"])
    
    start_time = time.time()
    
    # --- Pre-compute Spectral Operators ---
    _, _, _, green_func = get_spectral_operators()
    
    # --- Warm-up Kernels ---
    rho = deposit_mass_gpu(pos_cuge, masses, (NZ, NY, NX), (Lx, Ly, Lz))
    phi_cuge = solve_potential_gpu(rho, green_func, G)
    phi_newt = solve_potential_gpu(rho, green_func, G)
    fx, fy, fz, dc = compute_cuge_acceleration_gpu(phi_cuge, phi_prev_cuge, c_sim, dt, dx, dy, dz)
    e_vac = compute_vacuum_energy_gpu(phi_cuge, c_sim, dx, dy, dz)
    cp.cuda.Stream.null.synchronize()
    
    print("Kernels warmed up. Starting dual integration...")
    
    for step in range(steps):
        # === CUGE PHYSICS ===
        rho_cuge = deposit_mass_gpu(pos_cuge, masses, (NZ, NY, NX), (Lx, Ly, Lz))
        phi_cuge = solve_potential_gpu(rho_cuge, green_func, G)
        
        force_x_c, force_y_c, force_z_c, damp_c = compute_cuge_acceleration_gpu(
            phi_cuge, phi_prev_cuge, c_sim, dt, dx, dy, dz
        )
        
        # Leapfrog CUGE
        acc_c = interpolate_force_gpu(force_x_c, force_y_c, force_z_c, damp_c, pos_cuge, vel_cuge, use_damping=True)
        vel_cuge += 0.5 * dt * acc_c
        pos_cuge += dt * vel_cuge
        
        rho_cuge_new = deposit_mass_gpu(pos_cuge, masses, (NZ, NY, NX), (Lx, Ly, Lz))
        phi_cuge_new = solve_potential_gpu(rho_cuge_new, green_func, G)
        
        force_x_c2, force_y_c2, force_z_c2, damp_c2 = compute_cuge_acceleration_gpu(
            phi_cuge_new, phi_cuge, c_sim, dt, dx, dy, dz
        )
        
        acc_c2 = interpolate_force_gpu(force_x_c2, force_y_c2, force_z_c2, damp_c2, pos_cuge, vel_cuge, use_damping=True)
        vel_cuge += 0.5 * dt * acc_c2
        
        phi_prev_cuge = phi_cuge.copy()
        phi_cuge = phi_cuge_new
        
        # === NEWTONIAN PHYSICS ===
        rho_newt = deposit_mass_gpu(pos_newt, masses, (NZ, NY, NX), (Lx, Ly, Lz))
        phi_newt = solve_potential_gpu(rho_newt, green_func, G)
        
        acc_x_n, acc_y_n, acc_z_n = compute_newton_acceleration_gpu(phi_newt, dx, dy, dz)
        
        # Leapfrog Newtonian (No damping term)
        acc_n = interpolate_force_gpu(acc_x_n, acc_y_n, acc_z_n, None, pos_newt, vel_newt, use_damping=False)
        vel_newt += 0.5 * dt * acc_n
        pos_newt += dt * vel_newt
        
        rho_newt_new = deposit_mass_gpu(pos_newt, masses, (NZ, NY, NX), (Lx, Ly, Lz))
        phi_newt_new = solve_potential_gpu(rho_newt_new, green_func, G)
        
        acc_x_n2, acc_y_n2, acc_z_n2 = compute_newton_acceleration_gpu(phi_newt_new, dx, dy, dz)
        
        acc_n2 = interpolate_force_gpu(acc_x_n2, acc_y_n2, acc_z_n2, None, pos_newt, vel_newt, use_damping=False)
        vel_newt += 0.5 * dt * acc_n2
        
        phi_newt = phi_newt_new
        
        # === Diagnostics & CSV Logging ===
        if step % plot_interval == 0:
            # CUGE Metrics
            v_sq_c = cp.sum(vel_cuge**2, axis=1)
            ke_c = cp.sum(0.5 * masses * v_sq_c)
            max_v_c = cp.sqrt(cp.max(v_sq_c))
            e_vac_c = compute_vacuum_energy_gpu(phi_cuge, c_sim, dx, dy, dz)
            e_total_c = ke_c + e_vac_c
            
            # Newtonian Metrics
            v_sq_n = cp.sum(vel_newt**2, axis=1)
            ke_n = cp.sum(0.5 * masses * v_sq_n)
            max_v_n = cp.sqrt(cp.max(v_sq_n))
            
            # Transfer to CPU
            ke_c_cpu = ke_c.get()
            ke_n_cpu = ke_n.get()
            e_vac_c_cpu = e_vac_c.get()
            e_total_c_cpu = e_total_c.get()
            max_v_c_cpu = max_v_c.get()
            max_v_n_cpu = max_v_n.get()
            current_time = step * dt
            
            time_log.append(current_time)
            ke_cuge_log.append(ke_c_cpu)
            ke_newt_log.append(ke_n_cpu)
            max_v_cuge_log.append(max_v_c_cpu)
            max_v_newt_log.append(max_v_n_cpu)
            e_vac_cuge_log.append(e_vac_c_cpu)
            e_total_cuge_log.append(e_total_c_cpu)
            csv_data.append([current_time, ke_c_cpu, ke_n_cpu, e_vac_c_cpu, e_total_c_cpu, 
                            max_v_c_cpu, max_v_n_cpu, step])
            
            print(f"Step {step}: CUGE MaxV={max_v_c_cpu:.4f}, Newton MaxV={max_v_n_cpu:.4f}")
            
            # Stability Check
            if max_v_c_cpu > c_sim * 1.5:
                print("WARNING: CUGE velocity exceeded limit.")
            if max_v_n_cpu > c_sim * 1.5:
                print("WARNING: Newtonian velocity exceeded limit.")

    end_time = time.time()
    print(f"Simulation completed in {end_time - start_time:.2f} seconds.")
    
    # === Save CSV ===
    try:
        with open(CSV_FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(csv_data)
        print(f"Data saved to '{CSV_FILENAME}'")
    except Exception as e:
        print(f"Failed to save CSV: {e}")
    
    # === Plotting Comparison ===
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Panel 1: Kinetic Energy Comparison
    axes[0, 0].plot(time_log, ke_cuge_log, 'b-', linewidth=1.5, label='CUGE Kinetic')
    axes[0, 0].plot(time_log, ke_newt_log, 'r--', linewidth=1.5, label='Newtonian Kinetic')
    axes[0, 0].set_xlabel('Time')
    axes[0, 0].set_ylabel('Energy')
    axes[0, 0].set_title('Kinetic Energy: CUGE vs Newtonian')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Panel 2: Max Velocity Comparison
    axes[0, 1].plot(time_log, max_v_cuge_log, 'b-', linewidth=1.5, label='CUGE Max Velocity')
    axes[0, 1].plot(time_log, max_v_newt_log, 'r--', linewidth=1.5, label='Newtonian Max Velocity')
    axes[0, 1].axhline(y=c_sim, color='k', linestyle=':', linewidth=2, label='c_sim limit')
    axes[0, 1].set_xlabel('Time')
    axes[0, 1].set_ylabel('Max |v|')
    axes[0, 1].set_title('Velocity Stability: CUGE vs Newtonian')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)
    
    # Panel 3: CUGE Energy Partitioning
    axes[1, 0].plot(time_log, ke_cuge_log, 'b-', linewidth=1.5, label='Kinetic')
    axes[1, 0].plot(time_log, e_vac_cuge_log, 'm-.', linewidth=1.5, label='Vacuum Strain')
    axes[1, 0].plot(time_log, e_total_cuge_log, 'g-', linewidth=1.5, label='Total (KE + E_vac)')
    axes[1, 0].set_xlabel('Time')
    axes[1, 0].set_ylabel('Energy')
    axes[1, 0].set_title('CUGE Energy Partitioning')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)
    
    # Panel 4: Velocity Difference (Stability Metric)
    vel_diff = np.array(max_v_newt_log) - np.array(max_v_cuge_log)
    axes[1, 1].plot(time_log, vel_diff, 'k-', linewidth=1.5, label='MaxV_Newton - MaxV_CUGE')
    axes[1, 1].set_xlabel('Time')
    axes[1, 1].set_ylabel('Velocity Difference')
    axes[1, 1].set_title('Stability Gap (Newtonian - CUGE)')
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