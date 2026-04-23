import numpy as np
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from numba import njit

print("✅ C.O.R.E. n-body simulation with Energy Tracking starting...")

# ================== CONFIGURATION ==================
# Simulation Parameters
G = 1.0
c = 30.0                  # Effective propagation speed
MASS_SCALE = 10.0
SOFTENING_EPS = 0.0       # ZERO — Softening-free run
TOTAL_TIME = 10_000_000_000.0 # 1e10 steps
NUM_STEPS = int(TOTAL_TIME)
PROGRESS_INTERVAL = 10_000_000
SAVE_INTERVAL = 10_000_000
PERTURBATION = 1e-8

# File Names
OUTPUT_FILE = "core_nbody_energy_1e9.csv"
PLOT_FILE = "CUGE_Energy_Trajectory_1e9.png"

# Initial Conditions (Figure-8)
INITIAL_STATE_UNPERTURBED = np.array([
    [0.97000436, -0.24308753],
    [-0.97000436, 0.24308753],
    [0.0, 0.0],
    [0.4662036850, 0.4323657300],
    [0.4662036850, 0.4323657300],
    [-0.93240737, -0.86473146]
], dtype=np.float64)

MASSES = np.array([1.0, 1.0, 1.0], dtype=np.float64) * MASS_SCALE
N_BODIES = 3
DIM = 2

# ================== CUGE PHYSICS (JIT) ==================

@njit(fastmath=True)
def rhs_cuge_numba(pos, vel, masses, c_val):
    """
    CUGE Equation of Motion:
    a = (c^2/n) * grad_n - (dn_dt/n) * v
    """
    phi_total = np.zeros(N_BODIES)
    grad_phi = np.zeros((N_BODIES, DIM))
    
    # Calculate Potential and Gradient
    for i in range(N_BODIES):
        dpos = pos[i] - pos
        # Guard against division by zero
        dist_sq = np.sum(dpos**2, axis=1) + 1e-12 
        dist = np.sqrt(dist_sq)
        
        mask = np.ones(N_BODIES, dtype=np.bool_)
        mask[i] = False
        
        # Potential
        phi_total[i] = np.sum(G * masses * mask / dist)
        
        # Gradient of Potential (Acceleration contribution)
        grad_phi[i] = np.sum(
            (G * masses[:, None] * dpos * mask[:, None]) / (dist_sq[:, None] * dist[:, None]),
            axis=0
        )
    
    # Refractive Index and its derivatives
    n_vals = 1.0 + phi_total / (2.0 * c_val**2)
    grad_n = grad_phi / (2.0 * c_val**2)
    dn_dt = np.sum(grad_n * vel, axis=1)
    
    acceleration = np.zeros_like(vel)
    for i in range(N_BODIES):
        # The CUGE acceleration equation
        acceleration[i] = (
            (c_val**2) * (grad_n[i] / n_vals[i])
            - (dn_dt[i] / n_vals[i]) * vel[i]
        )
    return acceleration

# ================== ENERGY TRACKING (JIT) ==================

@njit(fastmath=True)
def compute_energies(pos, vel, masses, c_val):
    """
    Calculates:
    1. E_kin: Kinetic Energy
    2. E_pot: CUGE Potential Energy (m * Phi / n)
    3. E_vac: Vacuum Strain Energy Proxy (sum of |grad_Phi|^2)
    """
    e_kin = 0.0
    e_pot = 0.0
    e_vac = 0.0
    
    N = len(masses)
    
    # Kinetic Energy
    for i in range(N):
        e_kin += 0.5 * masses[i] * np.sum(vel[i]**2)
        
    # Potential & Vacuum Energy
    for i in range(N):
        phi_i = 0.0
        grad_phi_sq = 0.0
        
        # Sum over other bodies
        for j in range(N):
            if i == j: continue
            
            dx = pos[i, 0] - pos[j, 0]
            dy = pos[i, 1] - pos[j, 1]
            dist_sq = dx*dx + dy*dy
            dist = np.sqrt(dist_sq + 1e-12)
            
            # Potential
            phi_i += masses[j] / dist
            
            # Gradient Magnitude squared (|grad_Phi|^2)
            # |grad_Phi| = GM/r^2. Squared is G^2 M^2 / r^4
            # We use dist_sq^2 for r^4
            grad_phi_sq += (masses[j] / dist_sq)**2
            
        n_i = 1.0 + phi_i / (2.0 * c_val**2)
        
        # CUGE Potential Energy Term
        e_pot += masses[i] * phi_i / n_i
        
        # Vacuum Strain Energy
        e_vac += grad_phi_sq

    return e_kin, e_pot, e_vac

# ================== MAIN LOOP ==================

def main():
    print(f"⚙️  Configuration: G={G}, c={c}, MassScale={MASS_SCALE}")
    print(f"   Refractive index: n = 1 + Φ/(2c²)")
    print(f"   Integrator: Leapfrog (Symplectic)")
    print(f"   Steps: {NUM_STEPS:,} | Save every: {SAVE_INTERVAL:,}")
    
    # Initialize State
    y = INITIAL_STATE_UNPERTURBED.flatten().copy()
    y[0] += PERTURBATION  # Perturb to test stability
    
    # Storage for Energy & State
    saved_times = []
    saved_states = []
    saved_energies = []
    
    start_time = datetime.now()
    
    # Initial Energy
    pos = y[:2*N_BODIES].reshape((N_BODIES, DIM))
    vel = y[2*N_BODIES:].reshape((N_BODIES, DIM))
    ek, ep, ev = compute_energies(pos, vel, MASSES, c)
    saved_energies.append([ek, ep, ev, ek+ep+ev])
    saved_states.append(y.copy())
    saved_times.append(0.0)
    
    print(f"🚀 Starting integration: t = 0 → {TOTAL_TIME:,.0f}")
    
    # Main Loop
    for i in range(1, NUM_STEPS + 1):
        pos = y[:2*N_BODIES].reshape((N_BODIES, DIM))
        vel = y[2*N_BODIES:].reshape((N_BODIES, DIM))
        
        # Leapfrog Step (Kick-Drift-Kick)
        acc = rhs_cuge_numba(pos, vel, MASSES, c)
        vel_half = vel + 0.5 * acc
        pos_new = pos + vel_half
        acc_new = rhs_cuge_numba(pos_new, vel_half, MASSES, c)
        vel_new = vel_half + 0.5 * acc_new
        
        # Update state
        y = np.concatenate((pos_new.ravel(), vel_new.ravel()))
        
        # Progress & Saving
        if i % PROGRESS_INTERVAL == 0 or i == NUM_STEPS:
            print(f"📊 Progress: t = {i:,} / {NUM_STEPS:,} ({100*i/NUM_STEPS:.1f}%)")
        
        if i % SAVE_INTERVAL == 0 or i == NUM_STEPS:
            saved_times.append(float(i))
            saved_states.append(y.copy())
            
            # Compute Energy
            pos = y[:2*N_BODIES].reshape((N_BODIES, DIM))
            vel = y[2*N_BODIES:].reshape((N_BODIES, DIM))
            ek, ep, ev = compute_energies(pos, vel, MASSES, c)
            saved_energies.append([ek, ep, ev, ek+ep+ev])
            
            # Progress
            if i % PROGRESS_INTERVAL == 0:
                elapsed = datetime.now() - start_time
                est_total = elapsed * (NUM_STEPS / i)
                print(f"   ⏱️  Est. Remaining: {est_total - elapsed}")

    # ================== SAVE DATA ==================
    print(f"💾 Saving data to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        header = [
            "Time", 
            "x1", "y1", "x2", "y2", "x3", "y3",
            "E_kin", "E_pot", "E_vac", "E_total", "Drift_pct"
        ]
        writer.writerow(header)
        
        # Compute initial total for drift
        E0 = saved_energies[0][3]
        
        for idx, t in enumerate(saved_times):
            s = saved_states[idx][:6].reshape((3, 2))
            row = [f"{t:.3f}"]
            row += [f"{s[i,j]:+.8f}" for i in range(3) for j in range(2)]
            
            ek, ep, ev, etot = saved_energies[idx]
            
            # Drift Calculation
            drift = 0.0
            if abs(E0) > 1e-12:
                drift = ((etot - E0) / abs(E0)) * 100.0
                
            row += [f"{ek:.6f}", f"{ep:.6f}", f"{ev:.6f}", f"{etot:.6f}", f"{drift:.8e}"]
            writer.writerow(row)

    # ================== PLOT RESULTS ==================
    print(f"🎨 Generating plots to {PLOT_FILE}...")
    
    times = np.array(saved_times)
    
    # Extract Trajectories
    x1_cuge = [s[0] for s in saved_states]
    
    # Extract Energies
    energies = np.array(saved_energies)
    E_kin = energies[:, 0]
    E_pot = energies[:, 1]
    E_vac = energies[:, 2]
    E_tot = energies[:, 3]
    
    # Normalized Drift
    E0 = E_tot[0]
    drift = np.zeros_like(E_tot)
    if abs(E0) > 1e-12:
        drift = (E_tot - E0) / abs(E0)

    plt.figure(figsize=(15, 10))
    
    # Panel 1: Trajectory
    plt.subplot(2, 1, 1)
    plt.plot(times, x1_cuge, 'b-', lw=1.5, label='Body 1 x(t) - CUGE')
    plt.ylabel('x Position', fontsize=12)
    plt.title(f'CUGE Trajectory (Softening-Free, t=0 → {TOTAL_TIME:.0e})', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Panel 2: Energy
    plt.subplot(2, 1, 2)
    ax1 = plt.gca()
    ax1.plot(times, E_kin, 'r-', lw=1.5, label='Kinetic ($E_K$)', alpha=0.7)
    ax1.plot(times, E_pot, 'g--', lw=1.5, label='CUGE Potential ($E_P$)', alpha=0.7)
    ax1.plot(times, E_vac, 'm-.', lw=1.5, label='Vacuum Strain ($E_{vac}$)', alpha=0.7)
    ax1.set_xlabel('Time (steps)', fontsize=12)
    ax1.set_ylabel('Energy (Arbitrary Units)', fontsize=12)
    ax1.set_title('CUGE Energy Partitioning', fontsize=14)
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)

    # Secondary Axis for Drift
    ax2 = ax1.twinx()
    ax2.plot(times, drift, 'k:', lw=2, label=f'Total Energy Drift ($\\Delta E/E_0$)')
    ax2.set_ylabel('Drift (%)', fontsize=12, color='k')
    ax2.tick_params(axis='y', labelcolor='k')
    
    # Combine Legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='best')

    plt.tight_layout()
    plt.savefig(PLOT_FILE, dpi=300)
    plt.close()
    
    print("✅ Simulation and Energy Analysis finished!")
    print(f"   📁 Data: {OUTPUT_FILE}")
    print(f"   📈 Chart: {PLOT_FILE}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n💥 Error: {e}")
        import traceback
        traceback.print_exc()