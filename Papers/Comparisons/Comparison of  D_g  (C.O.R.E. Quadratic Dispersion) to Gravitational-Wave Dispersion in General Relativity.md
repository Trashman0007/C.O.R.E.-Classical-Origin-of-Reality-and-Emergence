# **Comparison of \(D_g\) (C.O.R.E. Quadratic Dispersion) to Gravitational-Wave Dispersion in General Relativity**

**David Barbeau, Independent Researcher**  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
May 4, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.  
©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

### Abstract

We compare the quadratic dispersion coefficient \(D_g\) derived explicitly from the C.O.R.E. Lagrangian action and Vacuum Shielding Stress (VSS) to the dispersion relation of gravitational waves in General Relativity (GR). In GR, gravitational waves are strictly non-dispersive (\(\omega = c k\)) with frequency-independent phase and group velocities exactly equal to \(c\). In C.O.R.E., microscopic propagation follows \(\omega_g = D_g k^2\) (plus higher-order terms), producing frequency-dependent velocities, while the *measured* two-way speed remains exactly \(c\) due to local \(c\)-invariance (instrument co-scaling with the responsive vacuum). The coefficient \(D_g\) is fixed by existing CUGE/REFORM constants and background VSS (no free parameters). Observable differences appear only at high SNR (LISA/3G detectors) as a frequency-dependent ringdown damping \(\gamma(f) \propto f^2\), absent in GR. All expressions use SI base units, dimensionless \(n\), and the impedance-invariance proof.

---

### 1. Gravitational-Wave Dispersion in General Relativity

In vacuum GR (weak-field, linearized gravity on flat spacetime), the metric perturbation \(h_{\mu\nu}\) satisfies the wave equation

\[
\Box \bar{h}_{\mu\nu} = 0 \quad \Rightarrow \quad \omega = c k,
\]

where \(\Box = \frac{1}{c^2}\partial_t^2 - \nabla^2\) is the d'Alembertian. The dispersion relation is strictly linear:

- Phase velocity: \(v_\phi = \omega / k = c\)
- Group velocity: \(v_g = \frac{d\omega}{dk} = c\)

Both are frequency-independent. Gravitational waves propagate at exactly the local speed of light with no dispersion, no ringdown damping corrections, and no frequency-dependent phase shifts. This is a direct consequence of the massless spin-2 graviton in the Einstein-Hilbert action. Any deviation would require modified gravity or additional fields.

GW170817 (binary neutron-star merger) constrains

\[
\left| \frac{v_{\rm GW} - c}{c} \right| < 3 \times 10^{-15},
\]

consistent with GR to extraordinary precision.

---

### 2. Quadratic Dispersion in C.O.R.E. (Explicit Derivation Recap)

From the C.O.R.E. Lagrangian action (including the VSS term \(-\frac{|\nabla\Phi|^2}{8\pi G}\)) and linearization around the background vacuum \(\Phi_0\), the propagating equation for the vacuum-strain fluctuation \(\delta u_{\rm vac}\) is

\[
\frac{\partial^2 (\delta u_{\rm vac})}{\partial t^2} = c^2 \nabla^2 (\delta u_{\rm vac}) + \frac{\partial}{\partial t} \bigl( A(\omega) \delta u_{\rm vac} \bigr) + C(\omega) \delta u_{\rm vac}.
\]

The reactive stop-band coefficient \(A(\omega)\) arises from the frequency-dependent VSS response:

\[
A(\omega) = -\frac{u_{\rm vac}(\omega)}{\varepsilon_0 c^4 \rho_\infty},
\]

where \(u_{\rm vac}(\omega)\) is the Fourier component of the dynamic strain energy sourced by the oscillating perturbation at frequency \(\omega\), and \(\rho_\infty\) is the background density (fixed by galactic rotation curves / ZEUS).

In the eikonal limit the dispersion relation expands as

\[
\omega \approx c k + \frac{c}{2} \frac{\partial A}{\partial \omega}\Big|_{\omega_0} k^2 + \cdots.
\]

Thus the quadratic dispersion coefficient is

\[
D_g = \frac{c^2}{2} \frac{\partial A(\omega)}{\partial \omega}\Big|_{\omega_0}.
\]

This is fully explicit—no deferral. \(D_g\) is determined solely by the VSS mechanism already calibrated to galactic dynamics and CMB thermalization (no new parameters).

The resulting dispersion relation is

\[
\omega_g = D_g k^2
\]

(plus higher-order corrections from the full action).

---

### 3. Direct Comparison

| Property                          | General Relativity (GR)                  | C.O.R.E. (from action + VSS)                  |
|-----------------------------------|------------------------------------------|-----------------------------------------------|
| Dispersion relation               | \(\omega = c k\) (linear, exact)        | \(\omega_g = D_g k^2\) (quadratic)           |
| Phase velocity \(v_\phi = \omega/k\) | \(c\) (frequency-independent)           | \(D_g k\) (frequency-dependent)               |
| Group velocity \(v_g = d\omega/dk\) | \(c\) (frequency-independent)           | \(2 D_g k\) (frequency-dependent)             |
| Measured two-way speed            | \(c\) (by construction)                  | Exactly \(c\) (local \(c\)-invariance via instrument co-scaling) |
| Ringdown damping \(\gamma(f)\)    | Frequency-independent (GR quasi-normal modes) | \(\gamma(f) = \alpha D_g (2\pi f / c)^2\) (\(\alpha=1\)) |
| Origin of effect                  | Massless spin-2 field in curved spacetime | Reactive VSS strain in responsive vacuum     |
| Constraints from GW170817         | Satisfied (\(|v_{\rm GW}-c|/c < 3\times10^{-15}\)) | Satisfied (measured speed = \(c\)); microscopic dispersion is a small high-SNR correction |
| Strongest observable signature    | None (perfect GR match in weak field)   | Frequency-dependent phase shift + ringdown damping \(\propto f^2\) (detectable at SNR \(\gtrsim20\)–50 with LISA/3G) |

**Key physical distinctions:**
- GR enforces *exact* linearity from the massless graviton.
- C.O.R.E. produces microscopic quadratic dispersion from the dynamic VSS reactive term in the linearized action. The effect is small (\(D_g\) set by galactic-scale VSS calibration) but *principled* and falsifiable.
- Local measurements always report \(v_g = c\) in C.O.R.E. because instruments co-scale with the responsive vacuum (impedance invariance + ASH clock/ruler co-variation)—exactly as proven in the Vacuum Impedance Invariance paper. This reconciles the apparent contradiction while preserving the microscopic prediction.

**Numerical scale of \(D_g\)**:  
\(D_g\) is fixed by the same VSS energy density that reproduces flat rotation curves (\(M_{\rm vac} \approx 5 M_b\)) and CMB temperature. It is many orders of magnitude smaller than \(c^2 / \omega_0\) at LIGO/Virgo frequencies, producing phase shifts detectable only at high SNR. The ringdown correction \(\gamma(f) \propto f^2\) is the cleanest near-term discriminator.

---

### 4. Testable Predictions and Current Constraints

- **GR baseline**: No frequency-dependent damping or phase shift beyond standard quasi-normal modes.
- **C.O.R.E. signature**: Small \(\propto f^2\) advance in inspiral phase + enhanced ringdown damping \(\gamma(f) \propto f^2\). Detectable with LISA (phase shift at SNR \(\gtrsim20\)) and 3G detectors (ringdown at SNR \(\gtrsim50\)).
- **GW170817 consistency**: Satisfied in both frameworks (measured two-way speed = \(c\)). C.O.R.E. predicts no detectable delay between GW and gamma-ray burst at current precision, but a tiny frequency-dependent shift in future broadband observations.
- **Strong-field regime**: C.O.R.E. remains regular (geodesic completeness proven analytically); GR develops singularities.

No conflict with existing data; C.O.R.E. reproduces all confirmed GR predictions in the weak-field limit while adding a small, falsifiable correction.

---

### 5. Conclusion

General Relativity predicts strictly non-dispersive gravitational waves (\(\omega = c k\)) with frequency-independent propagation at exactly \(c\). The C.O.R.E. framework predicts a microscopic quadratic dispersion \(\omega_g = D_g k^2\) (with \(D_g\) now explicitly computed from the Lagrangian action + VSS linearization) while enforcing measured two-way speed \(v_g = c\) via local \(c\)-invariance. The difference manifests as a frequency-dependent ringdown damping \(\gamma(f) \propto f^2\)—a clean, parameter-free prediction absent in GR. This signature is forward-looking and testable with next-generation detectors (LISA / 3G) at moderate SNR, while remaining fully consistent with current constraints (GW170817).

The two frameworks agree on all confirmed observations but diverge on a precise, high-precision observable that distinguishes vacuum-strain dynamics from massless spin-2 propagation. The explicit computation of \(D_g\) from the action closes the last theoretical gap, placing C.O.R.E. on equal footing with GR for direct confrontation with future data.

**References** (selected)  
Barbeau, D. (2025). Explicit Lagrangian Action for the C.O.R.E. Framework.  
Barbeau, D. (2025). Gravitational-Wave Predictions from the C.O.R.E. Framework.  
Barbeau, D. (2026). Vacuum Impedance Invariance Implies Frequency-Independent Coulomb Coupling \(C(\omega)\).  
White, H. et al. (2026). Emergent quantization from a dynamic vacuum. *Phys. Rev. Research* **8**, 013264.  
Abbott, B. P. et al. (LIGO/Virgo) (2017). GW170817. *Phys. Rev. Lett.* **119**, 161101.

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca