# **Material-dependent \( h_{\rm eff} \) vs. Planck universality**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
April 22, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

ASH derives the effective Planck constant from the continuous-wave Poynting flux in the responsive vacuum (CUGE) and statistical threshold crossing at the detector. In the CUGE vacuum, impedance \( Z_0 = \sqrt{\mu(r)/\varepsilon(r)} \) is globally constant by symmetric scaling. Therefore the time-averaged intensity of a monochromatic plane wave is

\[
I = \frac12 \frac{E_0^2}{Z_0} \qquad (\rm W\,m^{-2}),
\]

independent of local \( \varepsilon(r) \) (the \( \varepsilon \) in energy density and the \( 1/n \) phase-velocity factor cancel exactly). The energy delivered per unit area per optical cycle is \( I/\nu \), also independent of local \( \varepsilon(r) \).

The work function scales as \( \phi(r) \propto 1/\varepsilon(r)^2 \). Classical threshold analysis (ponderomotive energy gain per cycle \( \propto E_0^2 / \nu^2 \propto I / \nu^2 \)) at cutoff, combined with the phenomenological Einstein threshold relation near cutoff, yields the effective Planck constant for photoelectric detection:

\[
h_{\rm eff}(r) \propto \frac{\phi(r)}{\nu_{\rm th}} \propto \frac{1}{\varepsilon(r)}.
\tag{5.1}
\]

(This matches the corrected derivation in the dedicated note “Derivation of \( h_{\rm eff} \) Scaling.md”. The earlier incorrect \( I \propto \varepsilon E_0^2 \) assumption is superseded; with constant \( Z_0 \) the intensity is independent of \( \varepsilon(r) \), producing the physically consistent \( h_{\rm eff} \propto 1/\varepsilon \).)

**Dimensional verification:** Left side has units of action (J s). Right side: \( \phi \propto 1/\varepsilon^2 \) combined with the frequency factor from the threshold condition yields exactly J s, preserving consistency with SI base units.

**Local invariance of measured speed of light (internal standards).**  
For *internal atomic transitions* (clocks, rulers, bound-state emission/absorption), use the universal bare Planck constant \( h \) (no effective scaling). Atomic transition energies scale as \( E \propto 1/\varepsilon(r)^2 \). The coordinate frequency is \( \nu_{\rm coord} \propto 1/\varepsilon^2 \). The Bohr radius (local ruler) scales as \( a_0(r) \propto \varepsilon(r) \).

Local observers measure wavelengths in their own ruler units and frequencies with their own (slowed) clocks. The factors cancel exactly:

- Measured wavelength \( \lambda_{\rm meas} \propto \varepsilon / \varepsilon = \) constant,
- Local clock rate compensates the coordinate frequency slowdown (\( \propto \varepsilon^2 \)),

yielding \( c_{\rm local} = \lambda_{\rm meas} \cdot f_{\rm meas} = c = 299\,792\,458~\rm m\,s^{-1} \) exactly, independent of gravitational potential or direction. No \( h_{\rm eff} \) is required for internal standards (see dedicated correction “Derivation of \( h_{\rm eff} \) Scaling.md” for full details).

\( h_{\rm eff}(r) \propto 1/\varepsilon(r) \) applies *only* to external detection thresholds (photoelectric effect, ASH statistics, Bell correlations). It does not affect local \( c \)-invariance of atomic clocks and rulers.

**Planck universality as statistical average.**  
Laboratory measurements of \( h \) (e.g., Cs clocks, Na photoelectric effect, Kibble balance) average over vast ensembles of identical atoms/detectors. The effective value is the statistical mean

\[
\langle h \rangle = \int P(\phi)\, h(\phi)\, d\phi,
\]

where \( P(\phi) \) is the normalized threshold distribution of the specific material. For macroscopic, homogeneous detectors this average is indistinguishable from the universal CODATA value. Material dependence appears only when thresholds differ significantly (e.g., proposed Na vs. Cs photoelectric test near sodium’s cutoff). No contradiction arises; universality is phenomenological, not fundamental.

**Connection to full QED limit.**  
The classical ASH derivation is pre-QED. In the full quantum regime the vacuum response \( \varepsilon(\Phi) \) would enter the QED Lagrangian via the same \( \varepsilon(\Phi) F_{\mu\nu} F^{\mu\nu} \) term already present in the C.O.R.E. action; material-dependent thresholds emerge as effective low-energy operators. This remains an open extension, but the phenomenological reconciliation is complete and consistent with all existing C.O.R.E. documents.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---
