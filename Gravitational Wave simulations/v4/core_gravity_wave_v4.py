#!/usr/bin/env python3
"""
core_gravity_wave_v4.py
C.O.R.E. Framework - Gravitational Wave Simulation (GW v3 §3, §4, §5, §6)
FIXED: Correct dispersion phase calculation (frequency-dependent, not time-accumulated)
Author: David Barbeau + Grok (v3 corrected version)
Date: April 29, 2026
"""
import numpy as np
import matplotlib.pyplot as plt
import json
import csv
from datetime import datetime

# ========================= C.O.R.E. CONSTANTS =========================
G = 6.67430e-11
c = 299792458.0

# ========================= BINARY PARAMETERS =========================
M_tot = 30.0 * 1.989e30      # 30 solar masses
mu = 10.0 * 1.989e30         # reduced mass
r_obs = 1e25                 # ~1 Gpc (3.26 billion light years)

# Chirp Mass (GLOBAL)
M_chirp = mu**(3/5) * M_tot**(2/5)

# ========================= DISPERSION PARAMETERS (Section 3) =========================
ENABLE_DISPERSION = True     # Toggle C.O.R.E. dispersion effect
ENABLE_GR_COMPARISON = True  # Plot GR baseline vs. C.O.R.E. for comparison

# Quadratic dispersion coefficient (White et al. 2026)
# Physical value from C.O.R.E. framework
D_g_physical = 1.0e-20       # m^2/s (realistic physical scale)
D_g_sim = 1.0e-15            # m^2/s (enhanced for visualization, still small)
D_g = D_g_sim if ENABLE_DISPERSION else 0.0

# ========================= ISCO LIMIT (Merger) =========================
f_isco = c**3 / (6 * np.sqrt(6) * np.pi * G * M_tot)
print(f"Physical ISCO Limit (Merger): {f_isco:.2f} Hz")

# ========================= INSPIRAL DYNAMICS =========================
def inspiral_evolution(t, f_start):
    """
    Compute orbital frequency f(t) during inspiral up to ISCO.
    Uses quadrupole formula for orbital decay (C.O.R.E. Section 5).
    """
    omega_start = 2 * np.pi * f_start
    tau_merge = (5/256) * (c**5 / G**(5/3)) * (omega_start**(-8/3)) * M_chirp**(-5/3)
    
    tau_remaining = tau_merge - t
    tau_remaining = np.maximum(tau_remaining, 0)
    
    with np.errstate(divide='ignore', invalid='ignore'):
        f_t = f_start * (tau_merge / tau_remaining)**(3/8)
    
    f_t = np.minimum(f_t, f_isco)
    merger_mask = (tau_remaining <= 0)
    f_t[merger_mask] = f_isco
    
    return f_t, tau_merge, merger_mask

def calculate_amplitude(f_gw):
    """
    Calculate strain amplitude using standard PN formula (Calibrated).
    Formula: h = (4/r) * (G*M_c/c^2)^(5/3) * (pi*f/c)^(2/3)
    """
    amp = (4.0 / r_obs) * \
          (G * M_chirp / c**2)**(5/3) * \
          (np.pi * f_gw / c)**(2/3)
    return amp

def calculate_dispersion_phase(f_gw, D_g_coeff):
    """
    Calculate dispersion phase shift from quadratic dispersion ω = D_g k^2.
    Phase shift accumulates over propagation distance r_obs.
    
    ΔΦ(f) = D_g * k^2 * (r_obs / c)
          = D_g * (2πf/c)^2 * (r_obs / c)
    """
    if D_g_coeff == 0:
        return np.zeros_like(f_gw)
    
    k = 2 * np.pi * f_gw / c  # wavenumber
    delta_phi = D_g_coeff * (k**2) * (r_obs / c)
    
    return delta_phi

def h_plus_cross_chirp(t, f_start, use_dispersion=False, D_g_coeff=0.0):
    """Compute h_+ and h_× with inspiral chirp (C.O.R.E. Section 4 & 5)."""
    f_t, tau_merge, merger_mask = inspiral_evolution(t, f_start)
    
    # Amplitude (Calibrated)
    amp_t = calculate_amplitude(f_t)
    
    # GR Phase accumulation: φ_GR(t) = ∫ 2π f(t) dt
    phase_gr = np.zeros_like(t)
    dt = t[1] - t[0]
    for i in range(1, len(t)):
        phase_gr[i] = phase_gr[i-1] + 2 * np.pi * f_t[i-1] * dt
    
    # C.O.R.E. Dispersion: frequency-dependent phase offset
    # Applied AFTER propagation, not accumulated during inspiral
    if use_dispersion:
        dispersion_phase = calculate_dispersion_phase(f_t, D_g_coeff)
        total_phase = phase_gr + dispersion_phase
    else:
        total_phase = phase_gr
    
    h_plus  = -amp_t * np.cos(total_phase)
    h_cross = -amp_t * np.sin(total_phase)
    
    # Ringdown damping (Section 6)
    if np.any(merger_mask):
        merger_idx = np.argmax(merger_mask)
        decay_time = t - t[merger_idx]
        decay_time[decay_time < 0] = 0
        tau_ringdown = 0.01
        h_plus[merger_mask] *= np.exp(-decay_time[merger_mask] / tau_ringdown)
        h_cross[merger_mask] *= np.exp(-decay_time[merger_mask] / tau_ringdown)
    
    return h_plus, h_cross, amp_t, f_t, phase_gr

# ========================= DATA EXPORT =========================
def export_to_csv(filename, t, h_plus, h_cross, amp_t, f_t):
    """Export waveform data to CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time_s', 'h_plus', 'h_cross', 'amplitude', 'frequency_Hz'])
        for i in range(len(t)):
            writer.writerow([f'{t[i]:.10e}', f'{h_plus[i]:.10e}', 
                           f'{h_cross[i]:.10e}', f'{amp_t[i]:.10e}', 
                           f'{f_t[i]:.6f}'])
    print(f"✓ CSV data exported: {filename}")

def export_metadata(filename, params):
    """Export simulation metadata to JSON file."""
    with open(filename, 'w') as jsonfile:
        json.dump(params, jsonfile, indent=2)
    print(f"✓ Metadata exported: {filename}")

# ========================= GENERATE WAVEFORM =========================
if __name__ == "__main__":
    print("="*60)
    print("C.O.R.E. Gravitational Wave Simulator (v4 CORRECTED)")
    print("2D transverse projector → emergent tensor polarizations")
    print("Dispersion: Frequency-dependent phase offset (Section 3)")
    print("="*60)
    
    # Start frequency
    f_start = 30.0  # Hz
    
    # Time array (high resolution)
    t_max = 1.0
    t = np.linspace(0, t_max, 50000)
    
    # Generate C.O.R.E. waveform (with dispersion)
    h_plus_core, h_cross_core, amp_t, f_t, phase_gr = h_plus_cross_chirp(
        t, f_start, use_dispersion=ENABLE_DISPERSION, D_g_coeff=D_g
    )
    
    # Generate GR baseline (no dispersion)
    if ENABLE_GR_COMPARISON:
        h_plus_gr, h_cross_gr, _, _, _ = h_plus_cross_chirp(
            t, f_start, use_dispersion=False, D_g_coeff=0.0
        )
    
    # Find merger time
    merger_idx = np.argmax(f_t >= f_isco)
    t_merger = t[merger_idx] if merger_idx > 0 else t_max
    
    # Calculate phase difference at merger
    if ENABLE_DISPERSION:
        dispersion_phase_at_merger = calculate_dispersion_phase(np.array([f_isco]), D_g)
        print(f"Dispersion phase shift at ISCO: {dispersion_phase_at_merger[0]:.4f} radians")
        print(f"Dispersion phase shift at ISCO: {np.degrees(dispersion_phase_at_merger[0]):.2f} degrees")
    
    # Print diagnostics
    print(f"Start GW Frequency:   {f_start:.2f} Hz")
    print(f"Merger GW Frequency:  {f_isco:.2f} Hz")
    print(f"Time to Merger:       {t_merger:.4f} s")
    print(f"Peak Amplitude:       {np.max(amp_t):.2e} (Expected ~10^-21 at 1 Gpc)")
    print(f"Dispersion Enabled:   {ENABLE_DISPERSION}")
    print(f"D_g Coefficient:      {D_g:.2e} m^2/s")
    
    # Export data
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_filename = f"core_gw_waveform_v4_{timestamp}.csv"
    json_filename = f"core_gw_metadata_v4{timestamp}.json"
    
    export_to_csv(csv_filename, t, h_plus_core, h_cross_core, amp_t, f_t)
    
    metadata = {
        "framework": "C.O.R.E.",
        "version": "4.0 (Corrected Dispersion)",
        "author": "David Barbeau",
        "date": datetime.now().isoformat(),
        "binary_parameters": {
            "M_tot_solar": 30.0,
            "mu_solar": 10.0,
            "r_obs_Mpc": r_obs / 3.086e22,
            "f_start_Hz": f_start,
            "f_isco_Hz": float(f_isco)
        },
        "dispersion_parameters": {
            "enabled": ENABLE_DISPERSION,
            "D_g_physical": D_g_physical,
            "D_g_simulation": D_g_sim,
            "formula": "ΔΦ(f) = D_g * (2πf/c)^2 * (r_obs/c)"
        },
        "simulation": {
            "t_max_s": t_max,
            "num_points": len(t),
            "t_merger_s": float(t_merger),
            "peak_amplitude": float(np.max(amp_t))
        },
        "core_sections": {
            "section_3": "Quadratic dispersion test (White et al. 2026) - FIXED",
            "section_4": "2D transverse projector → tensor polarizations",
            "section_5": "VSS orbital decay",
            "section_6": "Frequency-dependent ringdown damping"
        },
        "files_generated": {
            "csv_data": csv_filename,
            "json_metadata": json_filename
        }
    }
    
    export_metadata(json_filename, metadata)
    
    # Plot
    plt.figure(figsize=(14, 7))
    
    # Zoom to last 0.15 seconds before merger for visibility
    t_zoom_mask = (t >= max(0, t_merger - 0.15)) & (t <= t_merger + 0.05)
    t_zoom = t[t_zoom_mask]
    hp_core_zoom = h_plus_core[t_zoom_mask]
    hx_core_zoom = h_cross_core[t_zoom_mask]
    
    # Plot C.O.R.E.
    plt.plot(t_zoom, hp_core_zoom,  label=r'\(h_+\) (C.O.R.E.)',  lw=1.5, alpha=0.8, color='tab:blue')
    plt.plot(t_zoom, hx_core_zoom, label=r'\(h_\times\) (C.O.R.E.)', lw=1.5, alpha=0.8, color='tab:orange')
    
    # Plot GR Baseline (Overlay)
    if ENABLE_GR_COMPARISON:
        hp_gr_zoom = h_plus_gr[t_zoom_mask]
        plt.plot(t_zoom, hp_gr_zoom, label=r'\(h_+\) (GR Baseline)', lw=1.5, alpha=0.5, color='purple', linestyle='--')
    
    plt.axvline(x=t_merger, color='k', linestyle='--', alpha=0.5, label='Merger (ISCO)')
    plt.xlabel('Time (s)')
    plt.ylabel('Strain (dimensionless)')
    plt.title(f'C.O.R.E. Emergent Tensor GW Waveform (v4 Corrected)\nPeak: {np.max(amp_t):.2e} at {t_merger:.4f}s | Dispersion: {ENABLE_DISPERSION} (D_g = {D_g:.1e})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save plot
    plot_filename = f"core_gw_plot_v4_{timestamp}.png"
    plt.savefig(plot_filename, dpi=150, bbox_inches='tight')
    print(f"✓ Plot saved: {plot_filename}")
    
    plt.show()
    
    print("="*60)
    print("✓ Waveform generation complete (v4 CORRECTED)")
    print("✓ Dispersion: Frequency-dependent phase offset (not time-accumulated)")
    print("✓ Ready for parameter estimation studies")
    print("="*60)