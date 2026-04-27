# **Material-dependent \( h_{\rm eff} \) vs. Planck universality**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
April 22, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

ASH derives the effective Planck constant from the continuous-wave Poynting flux in the responsive vacuum (CUGE) and statistical threshold crossing at the detector. The time-averaged intensity of a monochromatic wave is

\[
I = \frac12 c\, \varepsilon(r)\, E_0^2 \qquad (\rm W\,m^{-2}),
\]

with \(c = 299\,792\,458~\rm m\,s^{-1}\) (exact, invariant) and \(\varepsilon(r)\) the local permittivity (F m⁻¹). The energy delivered per unit area per optical cycle (\(T = 1/\nu\)) is

\[
\frac{I}{\nu} = \frac12 c\, \varepsilon(r)\, E_0^2 / \nu \qquad (\rm J\,m^{-2}).
\]

Photo-emission occurs statistically when this quantity exceeds the material work-function threshold \(\phi\) (energy per electron, J). Matching to the phenomenological threshold relation

\[
\frac{I_{\rm min}}{\nu} = \frac{h_{\rm eff} \nu - \phi}{A}
\]

(where \(A\) is an effective area factor, dimensionless after normalization) immediately requires

\[
h_{\rm eff}(r) \propto \varepsilon(r).
\tag{5.1}
\]

**Dimensional verification:** Left side has units of action (J s). Right side: \(\varepsilon\) (F m⁻¹) scaled by constants from \(I/\nu\) yields exactly J s when combined with the frequency factor, preserving consistency with SI base units (kg m² s⁻¹).

**Local invariance of measured speed of light.**  
Atomic transition energy scales as \(E \propto 1/\varepsilon(r)^2\) (standard dielectric scaling). With \(h_{\rm eff}(r) \propto \varepsilon(r)\), the observed frequency is

\[
\nu_{\rm meas} = \frac{E}{h_{\rm eff}} \propto \frac{1}{\varepsilon(r)^2} \cdot \frac{1}{\varepsilon(r)} = \frac{1}{\varepsilon(r)}.
\]

The measured wavelength (Bohr radius) scales as

\[
\lambda_{\rm meas} \propto a_0 \propto \varepsilon(r).
\]

Thus the locally measured speed of light is

\[
c_{\rm local} = \lambda_{\rm meas} \cdot \nu_{\rm meas} \propto \varepsilon(r) \cdot \frac{1}{\varepsilon(r)} = c = 299\,792\,458~\rm m\,s^{-1},
\]

independent of gravitational potential or material. All quantities dimensionless after normalization; local gradients of \(\varepsilon\) (m⁻¹) distinguished from integrated phase (dimensionless).

**Planck universality as statistical average.**  
Laboratory measurements of \(h\) (e.g., Cs clocks, Na photoelectric effect, Kibble balance) average over vast ensembles of identical atoms/detectors. The effective value is the statistical mean

\[
\langle h \rangle = \int P(\phi)\, h(\phi)\, d\phi,
\]

where \(P(\phi)\) is the normalized threshold distribution of the specific material. For macroscopic, homogeneous detectors this average is indistinguishable from the universal CODATA value. Material dependence appears only when thresholds differ significantly (e.g., proposed Na vs. Cs photoelectric test near sodium’s cutoff). No contradiction arises; universality is phenomenological, not fundamental.

**Connection to full QED limit.**  
The classical ASH derivation is pre-QED. In the full quantum regime the vacuum response \(\varepsilon(\Phi)\) would enter the QED Lagrangian via the same \(\varepsilon(\Phi) F_{\mu\nu} F^{\mu\nu}\) term already present in the C.O.R.E. action; material-dependent thresholds emerge as effective low-energy operators. This remains an open extension, but the phenomenological reconciliation is complete and consistent with all existing C.O.R.E. documents.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---