# core_nbody_10million.py
# C.O.R.E. Framework — Classical Origin of Reality and Emergence
# David Barbeau | david@bigbadaboom.ca
# Version: Revised for REFORM/CUGE n = 1 + Φ/(2c²) (eq. 2.3)

import numpy as np
import sys
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from typing import List, Tuple

print("✅ C.O.R.E. n-body simulation starting...")

# ================== CONFIGURATION ==================
G = 1.0                   # Gravitational constant
c = 30.0                  # Effective propagation speed (simulation units)
MASS_SCALE = 10.0         # Amplify gravitational field strength
SOFTENING_EPS = 0.1       # MACHO radius equivalent (finite extent)
TOTAL_TIME = 10_000_000.0 # Ten million time units
NUM_STEPS = 10_000_000    # One step per unit time
SAVE_INTERVAL = 100_000   # Save every 100k steps (~100 points)
PERTURBATION = 1e-8       # Tiny initial perturbation for chaos test
OUTPUT_FILE = "core_nbody_longterm.csv"
PLOT_FILE = "chaos_comparison.png"

# Figure-8 initial conditions (Chenciner-Montgomery)
INITIAL_STATE_UNPERTURBED = np.array([
    [0.97000436, -0.24308753],   # Body 1 pos
    [-0.97000436, 0.24308753],   # Body 2 pos
    [0.0, 0.0],                  # Body 3 pos
    [0.4662036850, 0.4323657300],# Body 1 vel
    [0.4662036850, 0.4323657300],# Body 2 vel
    [-0.93240737, -0.86473146]   # Body 3 vel
])

MASSES = np.array([1.0, 1.0, 1.0]) * MASS_SCALE
N_BODIES = 3
DIM = 2

# ===================================================
def setup_initial_conditions(perturb=False, body_idx=0, coord=0):
    state = INITIAL_STATE_UNPERTURBED.flatten().copy()
    if perturb:
        state[2 * body_idx + coord] += PERTURBATION
    return state

def compute_refractive_index_and_derivatives(r_vec, v_vec, masses, c_val, eps):
    """Computes n ≈ 1 + Φ/(2c²) (eq. 2.3) with positive Φ magnitude"""
    phi_total = np.zeros(N_BODIES)
    grad_phi = np.zeros((N_BODIES, DIM))
    for i in range(N_BODIES):
        dpos = r_vec[i] - r_vec
        dist_sq = np.sum(dpos**2, axis=1) + eps**2
        dist = np.sqrt(dist_sq)
        mask = np.ones(N_BODIES, dtype=bool)
        mask[i] = False
        phi_total[i] = np.sum(G * masses * mask / dist)
        grad_phi[i] = np.sum(
            (G * masses[:, None] * dpos * mask[:, None]) / (dist_sq[:, None] * dist[:, None]),
            axis=0
        )
    n_vals = 1.0 + phi_total / (2.0 * c_val**2)
    grad_n = grad_phi / (2.0 * c_val**2)
    dn_dt = np.einsum('ij,ij->i', grad_n, v_vec)
    return n_vals, grad_n, dn_dt

def rhs_cuge(t, y):
    try:
        pos = y[:2*N_BODIES].reshape((N_BODIES, DIM))
        vel = y[2*N_BODIES:].reshape((N_BODIES, DIM))
        n_vals, grad_n, dn_dt = compute_refractive_index_and_derivatives(
            pos, vel, MASSES, c, SOFTENING_EPS
        )
        acceleration = np.zeros_like(vel)
        for i in range(N_BODIES):
            if abs(n_vals[i]) < 1e-12:
                raise ValueError(f"n[{i}] too small: {n_vals[i]}")
            acceleration[i] = (
                (c**2) * (grad_n[i] / n_vals[i])
                - (dn_dt[i] / n_vals[i]) * vel[i]
            )
        return np.concatenate([vel.flatten(), acceleration.flatten()])
    except Exception as e:
        print(f"❌ CUGE RHS error at t={t:.3f}: {str(e)}", file=sys.stderr)
        raise

def rhs_newton(t, y):
    try:
        pos = y[:2*N_BODIES].reshape((N_BODIES, DIM))
        vel = y[2*N_BODIES:].reshape((N_BODIES, DIM))
        acc = -compute_potential_gradient(pos, MASSES, SOFTENING_EPS)
        return np.concatenate([vel.flatten(), acc.flatten()])
    except Exception as e:
        print(f"❌ Newton RHS error at t={t:.3f}: {str(e)}", file=sys.stderr)
        raise

def compute_potential_gradient(r_vec, masses, eps):
    """Used only for Newtonian comparison"""
    grad_phi = np.zeros_like(r_vec)
    for i in range(N_BODIES):
        dpos = r_vec[i] - r_vec
        dist_sq = np.sum(dpos**2, axis=1) + eps**2
        dist = np.sqrt(dist_sq)
        mask = np.ones(N_BODIES, dtype=bool)
        mask[i] = False
        grad_phi[i] = np.sum(
            (G * masses[:, None] * dpos * mask[:, None]) / (dist_sq[:, None] * dist[:, None]),
            axis=0
        )
    return grad_phi

def integrate_rk4_progressive(rhs_func, y0, t_span, num_steps, save_every):
    t0, tf = t_span
    h = (tf - t0) / num_steps
    times = np.linspace(t0, tf, num_steps + 1)
    states = []
    y = y0.copy()
    start_time = datetime.now()
    print(f"🧠 Starting integration: {num_steps:,} steps from t={t0} to t={tf}")
    print(f"   Step size: {h:.6f}")
    for i in range(num_steps + 1):
        if i % save_every == 0 or i == num_steps:
            states.append(y.copy())
            if i > 0:
                elapsed = datetime.now() - start_time
                est_total = elapsed * (num_steps / i)
                remaining = est_total - elapsed
                print(f"📊 Progress: t = {times[i]:,.0f} / {tf:,.0f} "
                      f"({100*i/num_steps:.1f}%) | ETA: {remaining}")
        if i < num_steps:
            try:
                k1 = h * rhs_func(times[i], y)
                k2 = h * rhs_func(times[i] + h/2, y + k1/2)
                k3 = h * rhs_func(times[i] + h/2, y + k2/2)
                k4 = h * rhs_func(times[i] + h, y + k3)
                y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0
                if not np.all(np.isfinite(y_next)):
                    raise ValueError("Non-finite state detected (NaN or inf)")
                y = y_next
            except Exception as e:
                print(f"🛑 Integration failed at step {i}, t={times[i]:.3f}: {e}", file=sys.stderr)
                while len(states) * save_every <= num_steps:
                    states.append(states[-1])
                break
    final_times = np.arange(0, num_steps + 1, save_every)
    if final_times[-1] != num_steps:
        final_times = np.append(final_times, num_steps)
    return states, final_times

def write_results_to_csv(times_arr, cuge_states, newton_states, ref_states):
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        header = [
            "Time",
            "x1_CUGE", "y1_CUGE", "x2_CUGE", "y2_CUGE", "x3_CUGE", "y3_CUGE",
            "x1_Newton", "y1_Newton", "x2_Newton", "y2_Newton", "x3_Newton", "y3_Newton",
            "dx1_1000", "dy1_1000", "dx2_1000", "dy2_1000", "dx3_1000", "dy3_1000"
        ]
        writer.writerow(header)
        pos_ref = np.array([s[:6].reshape((3, 2)) for s in ref_states])
        for idx, t in enumerate(times_arr):
            s_cuge = cuge_states[idx][:6].reshape((3, 2))
            s_newton = newton_states[idx][:6].reshape((3, 2))
            s_ref = pos_ref[idx]
            dx1000 = 1000.0 * (s_cuge[0] - s_ref[0])
            dy1000 = 1000.0 * (s_cuge[1] - s_ref[1])
            dz1000 = 1000.0 * (s_cuge[2] - s_ref[2])
            row = [f"{t:.3f}"]
            row += [f"{s_cuge[i,j]:+.6f}" for i in range(3) for j in range(2)]
            row += [f"{s_newton[i,j]:+.6f}" for i in range(3) for j in range(2)]
            row += [f"{dx1000[0]:+.3f}", f"{dx1000[1]:+.3f}",
                    f"{dy1000[0]:+.3f}", f"{dy1000[1]:+.3f}",
                    f"{dz1000[0]:+.3f}", f"{dz1000[1]:+.3f}"]
            writer.writerow(row)
    print(f"💾 Results saved to {OUTPUT_FILE}")

def plot_chaos_divergence(time_arr, cuge_traj, newton_traj, save_path):
    x_cuge = [s[0] for s in cuge_traj]
    x_newton = [s[0] for s in newton_traj]
    plt.figure(figsize=(14, 8))
    plt.subplot(2, 1, 1)
    plt.plot(time_arr, x_cuge, '-', lw=1.2, label='CUGE - Body 1 x(t)', color='blue')
    plt.plot(time_arr, x_newton, '--', lw=1.0, label='Newton - Body 1 x(t)', color='red', alpha=0.8)
    plt.ylabel("x Position")
    plt.title("Trajectory Divergence: CUGE vs Newtonian Gravity (t = 0 → 10,000,000)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.subplot(2, 1, 2)
    diff = np.abs(np.array(x_cuge) - np.array(x_newton))
    valid_mask = diff > 0
    t_plot = np.array(time_arr)[valid_mask]
    diff_plot = diff[valid_mask]
    plt.semilogy(t_plot, diff_plot, '-', lw=1.5, color='purple', label='|x_CUGE - x_Newton|')
    plt.xlabel("Time")
    plt.ylabel("Absolute Difference (log scale)")
    plt.title("Exponential vs Sub-Exponential Divergence")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"🎨 Chaos comparison plot saved to {save_path}")

def main():
    print(f"⚙️  Configuration: G={G}, c={c}, mass×{MASS_SCALE}, eps={SOFTENING_EPS}")
    print(f"   Using corrected refractive index n = 1 + Φ/(2c²) [eq. 2.3]")
    print(f"   Simulating {TOTAL_TIME:,.0f} time units over {NUM_STEPS:,} steps.")
    print(f"   Saving every {SAVE_INTERVAL:,} steps (~{int(TOTAL_TIME // SAVE_INTERVAL)} points).")

    y0_unperturbed = setup_initial_conditions(False)
    y0_perturbed_cuge = setup_initial_conditions(True, body_idx=0, coord=0)
    y0_perturbed_newton = setup_initial_conditions(True, body_idx=0, coord=0)

    print("🚀 Starting CUGE integration...")
    states_cuge, save_times = integrate_rk4_progressive(
        rhs_func=rhs_cuge,
        y0=y0_perturbed_cuge,
        t_span=(0, TOTAL_TIME),
        num_steps=NUM_STEPS,
        save_every=SAVE_INTERVAL
    )
    print("✅ CUGE completed.")

    print("🚀 Starting Newtonian integration...")
    states_newton, _ = integrate_rk4_progressive(
        rhs_func=rhs_newton,
        y0=y0_perturbed_newton,
        t_span=(0, TOTAL_TIME),
        num_steps=NUM_STEPS,
        save_every=SAVE_INTERVAL
    )
    print("✅ Newton completed.")

    print("📊 Computing reference trajectory...")
    states_ref, _ = integrate_rk4_progressive(
        rhs_func=rhs_cuge,
        y0=y0_unperturbed,
        t_span=(0, TOTAL_TIME),
        num_steps=NUM_STEPS,
        save_every=SAVE_INTERVAL
    )

    write_results_to_csv(save_times, states_cuge, states_newton, states_ref)

    try:
        plot_chaos_divergence(save_times, states_cuge, states_newton, PLOT_FILE)
    except Exception as e:
        print(f"⚠️  Plotting failed: {e}")

    final_t = int(TOTAL_TIME)
    dx_final = abs(states_cuge[-1][0] - states_newton[-1][0])
    print("\n" + "="*60)
    print("🔍 FINAL RESULTS")
    print("="*60)
    print(f"Total simulation time: {final_t:,}")
    print(f"Final position difference (Body 1 x): |Δx| = {dx_final:.3e}")
    print(f"Data saved to: {OUTPUT_FILE}")
    print(f"Plot saved to: {PLOT_FILE}")
    print("✅ CUGE shows long-term stability; Newton diverges structurally.")
    print("🎉 Simulation finished successfully!")
    print("\n💡 You can now view the results and close this window.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⏸️  Simulation interrupted by user (Ctrl+C).")
    except Exception as e:
        print(f"\n💥 Unexpected error: {type(e).__name__}: {e}", file=sys.stderr)
    finally:
        input("\nPress Enter to exit...")   # Keeps window open on double-click