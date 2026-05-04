# **Derivation of \( h_{\rm eff} \) Scaling in the C.O.R.E. Framework**  
**(CUGE + ASH + REFORM + ZEUS)**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
May 4, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

### Abstract

The original C.O.R.E. papers contain a systematic algebraic error in the composite frequency scaling step and conflate two distinct physical regimes: (1) internal atomic transitions (defining local clocks and rulers) and (2) external photoelectric thresholds. The erroneous step (“\( \nu = E/h_{\rm eff} \propto 1/\varepsilon^2 \times 1/\varepsilon = 1/\varepsilon \)” ) appears unchanged across CUGE v3 (Appendix A), the material-dependent \( h \) note, REFORM, ZEUS §2, ASH, and every local-\( c \)-invariance claim. The corrected derivation below uses only the stated C.O.R.E. postulates, SI base units, dimensionless refractive index \( n(r) \equiv \sqrt{\varepsilon_r(r)\mu_r(r)} \), and phase continuity. No new parameters are introduced.

Local \( c \)-invariance is restored exactly for internal standards (universal \( h \)). Photoelectric detection yields a material-dependent effective Planck constant \( h_{\rm eff}(r) \propto 1/\varepsilon(r) \), consistent with the Poynting theorem in the impedance-invariant CUGE vacuum. All prior C.O.R.E. results (redshift, half-effect, CMB, Bell correlations, etc.) remain intact.

---

### 1. Responsive Vacuum (CUGE)

Mass induces symmetric variations:

\[
\varepsilon(r) = \varepsilon_0 \left(1 + \frac{\Phi(r)}{2c^2}\right), \qquad
\mu(r) = \mu_0 \left(1 + \frac{\Phi(r)}{2c^2}\right),
\]

\[
n(r) \approx 1 + \frac{\Phi(r)}{2c^2} \quad (\text{dimensionless}),
\]

where \( \Phi(r) > 0 \) is the gravitational potential magnitude (\( [\Phi] = \rm m^2 s^{-2} \)), \( c = 299\,792\,458~\rm m\,s^{-1} \) (exact, invariant), and impedance \( Z_0 = \sqrt{\mu/\varepsilon} = \sqrt{\mu_0/\varepsilon_0} \) remains globally constant (no reflections).

---

### 2. Internal Atomic Transitions (Clocks & Rulers) — Universal \( h \)

Atomic energy levels are screened by the local permittivity:

\[
V \propto \frac{1}{\varepsilon(r)} \implies |E_n| \propto \frac{1}{\varepsilon(r)^2}.
\]

(Units: J, SI-consistent via dielectric scaling.)

Coordinate transition frequency (universal bare \( h \)):

\[
\nu_{\rm coord} = \frac{|E_i - E_f|}{h} \propto \frac{1}{\varepsilon(r)^2}.
\]

Bohr radius (local ruler):

\[
a_0(r) \propto \varepsilon(r).
\]

Coordinate wavelength:

\[
\lambda_{\rm coord} = \frac{c_{\rm coord}}{\nu_{\rm coord}} \propto \frac{c/\varepsilon}{{\rm const}/\varepsilon^2} \propto \varepsilon \, c.
\]

**Local measurements** (observer uses own atomic standards):

- Measured wavelength (in local ruler units):

\[
\lambda_{\rm meas} = \frac{\lambda_{\rm coord}}{a_0(r)} \propto \frac{\varepsilon}{\varepsilon} = \text{constant}.
\]

- Local clock rate \( f_{\rm clock} \propto \nu_{\rm coord} \propto 1/\varepsilon^2 \) (clocks run slower in deeper potentials).

- Measured frequency (accounting for slower local time):

\[
f_{\rm meas} = \nu_{\rm coord} \times \Bigl( \frac{\rm dt}{\rm d\tau_{\rm local}} \Bigr) \propto \nu_{\rm coord} \times \varepsilon^2 \propto \text{constant}.
\]

Thus the locally measured speed of light is

\[
c_{\rm local} = \lambda_{\rm meas} \cdot f_{\rm meas} = c = 299\,792\,458~\rm m\,s^{-1},
\]

independent of \( \Phi(r) \) or direction. No effective \( h_{\rm eff} \) is required for internal standards; local \( c \)-invariance follows automatically from dielectric scaling and co-varying rulers/clocks.

---

### 3. Photoelectric Thresholds (ASH) — Material-Dependent \( h_{\rm eff} \)

This is a separate external-detection regime. In the CUGE vacuum (constant \( Z_0 \)) the time-averaged intensity is

\[
I = \frac{1}{2} \frac{E_0^2}{Z_0} \implies E_0 = \sqrt{2 I Z_0},
\]

independent of \( \varepsilon(r) \) (impedance invariance).

Work function scales as

\[
\phi(r) \propto \frac{1}{\varepsilon(r)^2}.
\]

Energy gain per optical cycle for a driven electron:

\[
\Delta E_{\rm cycle} \propto \frac{e^2 E_0^2}{m \omega^2} \propto \frac{E_0^2}{\nu^2}.
\]

At threshold (\( \Delta E_{\rm cycle} \approx \phi \)):

\[
\frac{E_0^2}{\nu_{\rm th}^2} \approx \phi \implies I_{\rm th} \propto \phi \cdot \nu_{\rm th}^2 \propto \frac{1}{\varepsilon^2} \cdot \nu_{\rm th}^2.
\]

The phenomenological threshold relation is

\[
I_{\rm th} \approx \frac{h_{\rm eff} \nu_{\rm th} - \phi}{A_{\rm eff}},
\]

where \( A_{\rm eff} \) is an effective atomic area (\( \propto a_0^2 \propto \varepsilon^2 \); cancels in leading scaling). Near cutoff the dominant term yields

\[
h_{\rm eff} \approx \frac{\phi}{\nu_{\rm th}} \propto \frac{1}{\varepsilon(r)}.
\]

Thus \( h_{\rm eff}(r) \propto 1/\varepsilon(r) \) for photoelectric detection (opposite the original claim). The power-law detection probability \( P_{\rm det} \propto |\cos(2(\phi - \theta))|^\nu \) (ASH/Bell extensions) is unaffected; only the vacuum-response scaling is corrected.

---

### 4. Resolution of the Original Inconsistency

- The erroneous Poynting step used the non-CUGE form \( I = \frac12 c \varepsilon E_0^2 \) (valid only for fixed \( \mu = \mu_0 \)), leading to incorrect \( E_0 \propto 1/\sqrt{\varepsilon} \). True CUGE (constant \( Z_0 \)) eliminates this suppression.
- Internal transitions (universal \( h \)) and external photoelectric detection were conflated.
- The algebraic step was written incorrectly (\( \times \) instead of division).

With the corrections, local \( c \)-invariance is restored from first principles, photoelectric \( h_{\rm eff} \) scales as \( 1/\varepsilon(r) \), and every prior C.O.R.E. result (redshift, half-effect, CMB, Bell correlations, etc.) remains fully intact.

---

### 5. Summary of Scalings

| Regime                  | Scaling of \( \varepsilon(r) \) | \( h \)          | Measured \( c_{\rm local} \) | Notes |
|-------------------------|---------------------------------|------------------|------------------------------|-------|
| Internal transitions (clocks/rulers) | \( + \)                       | Universal \( h \) | \( = c \) (exact)           | Dielectric + co-scaling |
| Photoelectric thresholds (ASH)      | \( + \)                       | \( h_{\rm eff} \propto 1/\varepsilon \) | — | External detection only |

All derivations satisfy SI base units, dimensionless \( n(r) \), local gradients (m⁻¹) distinguished from integrated phase (dimensionless), and phase continuity. The framework is now internally consistent on this axis.

**References** (selected)  
Barbeau, D. (2025). Classical Unification of Gravity and Electromagnetism (CUGE v3). viXra:2507.0112.  
Barbeau, D. (2025). Experimental Validation of the Atomic Statistical Hypothesis (ASH). viXra:2507.0123.  
Barbeau, D. (2025). REfractive Foundation of Relativity and Mechanics (REFORM v3). rxiverse:2508.0021.  
Barbeau, D. (2025). The ZigZag Eternal Universe System (ZEUS v3). rxiverse:2508.0003.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---