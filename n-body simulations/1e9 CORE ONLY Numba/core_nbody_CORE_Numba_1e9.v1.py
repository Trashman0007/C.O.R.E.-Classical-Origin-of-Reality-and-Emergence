# core_nbody_CORE_Numba_1e9.py
# C.O.R.E. Framework — Numba JIT optimized CORE-only run
# David Barbeau | david@bigbadaboom.ca

import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from numba import njit

print("✅ C.O.R.E. n-body simulation (Numba CORE-only) starting...")

# ================== CONFIGURATION ==================
G = 1.0
c = 30.0
MASS_SCALE = 10.0
SOFTENING_EPS = 0.1

TOTAL_TIME = 1_000_000_000.0      # 10^9 time units
NUM_STEPS = int(TOTAL_TIME)
PROGRESS_INTERVAL = 1_000_000     # print every 1 million steps
SAVE_INTERVAL = 10_000_000        # save CSV/plot every 10 million steps

PERTURBATION = 1e-8
OUTPUT_FILE = "core_nbody_CORE_Numba.csv"
PLOT_FILE = "CUGE_trajectory_Numba.png"

# Figure-8 initial conditions
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

@njit(fastmath=True)
def rhs_cuge_numba(pos, vel, masses, c_val, eps):
    """Numba-accelerated ray equation"""
    phi_total = np.zeros(N_BODIES)
    grad_phi = np.zeros((N_BODIES, DIM))
    for i in range(N_BODIES):
        dpos = pos[i] - pos
        dist_sq = np.sum(dpos**2, axis=1) + eps**2
        dist = np.sqrt(dist_sq)
        mask = np.ones(N_BODIES, dtype=np.bool_)
        mask[i] = False
        phi_total[i] = np.sum(G * masses * mask / dist)
        grad_phi[i] = np.sum(
            (G * masses[:, None] * dpos * mask[:, None]) / (dist_sq[:, None] * dist[:, None]),
            axis=0
        )
    n_vals = 1.0 + phi_total / (2.0 * c_val**2)
    grad_n = grad_phi / (2.0 * c_val**2)
    dn_dt = np.sum(grad_n * vel, axis=1)          # ← fixed line
    acceleration = np.zeros_like(vel)
    for i in range(N_BODIES):
        acceleration[i] = (
            (c_val**2) * (grad_n[i] / n_vals[i])
            - (dn_dt[i] / n_vals[i]) * vel[i]
        )
    return np.concatenate((vel.ravel(), acceleration.ravel()))

def main():
    print(f"⚙️  Configuration: G={G}, c={c}, mass×{MASS_SCALE}, eps={SOFTENING_EPS}")
    print(f"   Using corrected refractive index n = 1 + Φ/(2c²) [eq. 2.3]")
    print(f"   Numba CORE-only run to {TOTAL_TIME:,.0f} time units on 24-core CPU")

    y = INITIAL_STATE_UNPERTURBED.flatten().copy()
    y[0] += PERTURBATION

    states = []
    start_time = datetime.now()

    print(f"🚀 Starting Numba CORE integration: {NUM_STEPS:,} steps")

    for i in range(NUM_STEPS + 1):
        if i % PROGRESS_INTERVAL == 0 or i == NUM_STEPS:
            states.append(y.copy())
            if i > 0:
                elapsed = datetime.now() - start_time
                est_total = elapsed * (NUM_STEPS / i)
                remaining = est_total - elapsed
                print(f"📊 Progress: t = {i:,} / {NUM_STEPS:,} ({100*i/NUM_STEPS:.1f}%) | ETA: {remaining}")

        if i < NUM_STEPS:
            pos = y[:2*N_BODIES].reshape((N_BODIES, DIM))
            vel = y[2*N_BODIES:].reshape((N_BODIES, DIM))
            dydt = rhs_cuge_numba(pos, vel, MASSES, c, SOFTENING_EPS)
            y += dydt

    # Save CSV
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ["Time", "x1_CUGE", "y1_CUGE", "x2_CUGE", "y2_CUGE", "x3_CUGE", "y3_CUGE"]
        writer.writerow(header)
        for idx, t in enumerate(np.arange(0, NUM_STEPS + 1, SAVE_INTERVAL)):
            s = states[idx][:6].reshape((3, 2))
            row = [f"{t:.3f}"] + [f"{s[i,j]:+.6f}" for i in range(3) for j in range(2)]
            writer.writerow(row)
    print(f"💾 Results saved to {OUTPUT_FILE}")

    # Plot
    x_cuge = [s[0] for s in states]
    plt.figure(figsize=(14, 8))
    plt.plot(np.arange(0, NUM_STEPS + 1, SAVE_INTERVAL), x_cuge, '-', lw=1.2, label='CUGE - Body 1 x(t)', color='blue')
    plt.ylabel("x Position")
    plt.title(f"CUGE Trajectory (Numba CORE-only, t = 0 → {TOTAL_TIME:,.0f})")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(PLOT_FILE, dpi=300)
    plt.close()
    print(f"🎨 Plot saved to {PLOT_FILE}")

    print("\n🎉 Numba CORE simulation finished successfully!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n💥 Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
    finally:
        input("\nPress Enter to exit...")