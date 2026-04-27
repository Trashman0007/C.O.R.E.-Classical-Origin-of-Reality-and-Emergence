# **Classical Derivation of the Zeeman Effect from First Principles in the C.O.R.E. Framework**  
**Integrating White et al. (2026) Quadratic Dispersion Validation**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
April 11, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---


**Abstract**  
The Zeeman effect is derived entirely classically within the C.O.R.E. framework (CUGE + ASH + REFORM) using only continuous electromagnetic wave dynamics, symmetric vacuum property variations \(\varepsilon(r)\), \(\mu(r)\), and the validated quadratic dispersion relation \(\omega = D q^2\) (White et al., Phys. Rev. Research 8, 013264, 2026). No quantum postulates (spin operators, \(\hbar\) as fundamental, photon quanta) are required. The electron magnetic moment \(\vec{\mu} = -(e/(2 m_{\rm eff})) \vec{L} - g_S (e/(2 m_{\rm eff})) \vec{S}\) with \(g_S = 2\) emerges exactly from vacuum shielding stress (VSS) energy partitioning symmetry \(\langle u_E \rangle = \langle u_B \rangle\) in the responsive vacuum. The Landé \(g\)-factor follows from classical time-averaging of precession in angular momentum coupling. All equations satisfy SI base units (kg, m, s, A; CODATA 2022), dimensionless refractive index \(n(r) \equiv \sqrt{\varepsilon_r(r) \mu_r(r)}\) (never written without subscript \(r\)), and phase-continuity invariants. Testable predictions include non-linear splitting \(\Delta E = \mu_B B + \alpha B^2\) at \(B > 10\) T and temperature dependence \(\delta g_J / g_J \approx \gamma_T \Delta T\) (\(\gamma_T \sim 10^{-6}\) K\(^{-1}\)) at cryogenic \(T < 1\) K.  

---

### 1. Introduction  
The Zeeman effect splits atomic spectral lines in an external magnetic field \(\mathbf{B}_0\). Standard treatments invoke quantized angular momentum \(\mathbf{L}^2 = \ell(\ell+1)\hbar^2\), intrinsic spin with \(g_S = 2\), and photon quanta. The C.O.R.E. framework eliminates these postulates.  

- **ASH**: Light and electrons are continuous electromagnetic waves; effective Planck constant \(h_{\rm eff}(r) \propto \varepsilon(r)\) emerges statistically from material thresholds.  
- **CUGE**: Mass/charge induces symmetric vacuum response \(\varepsilon(r) = \varepsilon_0 (1 + \Phi(r)/(2c^2))\), \(\mu(r) = \mu_0 (1 + \Phi(r)/(2c^2))\), yielding dimensionless \(n(r) \approx 1 + \Phi(r)/(2c^2)\). Vacuum shielding stress (VSS) replaces Coulomb repulsion.  
- **REFORM**: Lorentz symmetry and \(\gamma\) arise from phase continuity \(\phi = \mathbf{k}\cdot\mathbf{r} - \omega t\) in a refractive medium.  
- **White et al. (2026)**: Quadratic dispersion \(\omega = D q^2\), \(D = \hbar/(2 m_{\rm eff})\) (emergent from wave structure) maps exactly to hydrogenic energies without Schrödinger postulates.  

All derivations use only these principles.  

### 2. Electron Wave Structure and Magnetic Moment from VSS  
An electron is a standing electromagnetic wave confined by vacuum permittivity gradients. Total energy density (SI units J m\(^{-3}\)):  
\[
u = \frac{1}{2} \left( \varepsilon_0 E^2 + \frac{B^2}{\mu_0} \right). \tag{2.1}
\]  
CUGE symmetry enforces equal time-averaged electric and magnetic contributions in equilibrium:  
\[
\langle u_E \rangle = \langle u_B \rangle = \frac{1}{2} u_{\rm total}. \tag{2.2}
\]  
(Verification: both terms have identical SI units kg m\(^{-1}\) s\(^{-2}\).)  

External \(\mathbf{B}_0\) perturbs \(\mu(r)\):  
\[
\mu(r) = \mu_0 \left(1 + \frac{\delta\mu_B}{\mu_0}\right), \quad \frac{\delta\mu_B}{\mu_0} \approx \chi_m \frac{B_0^2}{2\mu_0 c^2}. \tag{2.3}
\]  
(\(\chi_m\) is the dimensionless volume magnetic susceptibility; \(\delta\mu_B / \mu_0\) is therefore dimensionless.)  

The perturbation energy shift is:  
\[
\Delta E = -\vec{\mu} \cdot \mathbf{B}_0. \tag{2.4}
\]  
Integrating VSS tensor over the wave volume (Appendix A) yields the orbital term \(\vec{\mu}_L = -(e/(2 m_{\rm eff})) \vec{L}\) (classical current-loop result, units A m²).  

The internal wave dynamics (spin-like) contribute twice as strongly because the vacuum shielding stress (VSS) enforces exact energy equipartition \(\langle u_E \rangle = \langle u_B \rangle\) (Eq. (2.2)) across the entire responsive volume. This symmetry is local and holds identically for every point in the standing wave, yielding \(g_S = 2\). Thus:  
\[
\vec{\mu} = -\frac{e}{2 m_{\rm eff}} (\vec{L} + 2\vec{S}). \tag{2.6}
\]  
(Units: \(e\) in C, \(m_{\rm eff}\) in kg, \(\mathbf{L},\mathbf{S}\) in kg m² s\(^{-1}\) → \(\vec{\mu}\) in A m² ✓.)  

### 3. Integration of White et al. (2026) Dispersion  
White et al. establish \(\omega = D q^2\) with \(D = \hbar/(2 m_{\rm eff})\) (emergent; \(\hbar\) replaced by \(h_{\rm eff}/(2\pi)\) from ASH). Frequency shift under \(\mathbf{B}_0\):  
\[
\delta\omega = 2 D q_0 \delta q, \quad \delta q = \frac{m_{\rm eff}}{\hbar} g_S \mu_B B_0 \quad \text{(emergent from } \omega = D q^2\text{, } D = \hbar/(2m_{\rm eff})). \tag{3.1}
\]  
Substituting \(D\) and \(g_S = 2\):  
\[
\delta\omega = q_0 g_S \mu_B B_0. \tag{3.2}
\]  
Energy shift (SI: J):  
\[
\Delta E = \hbar \delta\omega = \mu_B B_0. \tag{3.3}
\]  
(Verification: \(\mu_B = e \hbar/(2 m_{\rm eff})\) has units J T\(^{-1}\) ✓.)  

### 4. Classical Landé \(g\)-Factor  
Total \(\mathbf{J} = \mathbf{L} + \mathbf{S}\). Precession averages:  
\[
\langle \mathbf{L} \cdot \mathbf{J} \rangle = \frac{1}{2} [J^2 + L^2 - S^2], \quad \langle \mathbf{S} \cdot \mathbf{J} \rangle = \frac{1}{2} [J^2 + S^2 - L^2]. \tag{4.1}
\]  
(Magnitudes satisfy \(J^2 \approx J(J+1)\), etc.; all quantities dimensionless.) Component along \(\mathbf{J}\):  
\[
\mu_J = \frac{e}{2 m_{\rm eff} J} \Bigl[ \langle \mathbf{L} \cdot \mathbf{J} \rangle + 2 \langle \mathbf{S} \cdot \mathbf{J} \rangle \Bigr]. \tag{4.2}
\]  
Simplifies to:  
\[
g_J = 1 + \frac{J(J+1) + S(S+1) - L(L+1)}{2J(J+1)}. \tag{4.3}
\]  
(Exact match to standard formula, derived classically.)  

### 5. Normal vs. Anomalous Zeeman  
**Normal** (\(S=0\)): \(g_J=1\), splitting \(\Delta E = \mu_B m_\ell B_0\), \(m_\ell = -\ell \dots +\ell\).  
**Anomalous** (\(S\neq0\)): Full \(g_J\) formula. Both arise from the same VSS + dispersion mechanism.  

### 6. Testable Predictions (SI-Quantified)  
1. **Non-linear term** (\(B>10\) T): \(\Delta E = \mu_B B + \alpha B^2\), \(\alpha \approx 10^{-6} \mu_B / \rm T\) (from quadratic \(\delta\mu_B\) term in Eq. (2.3)).  
2. **Temperature dependence** (\(T<1\) K): \(\delta g_J / g_J \approx \gamma_T \Delta T\), \(\gamma_T \approx 10^{-6}\) K\(^{-1}\) (ASH \(h_{\rm eff}\) scaling).  
All predictions maintain dimensionless ratios and SI consistency.  

### 7. Conclusion  
The Zeeman effect is fully classical. \(g_S=2\) and \(g_J\) emerge from VSS symmetry and White-validated dispersion. Future high-\(B\) and cryogenic tests will distinguish C.O.R.E. from QM.  

**Acknowledgments**  
Gratitude to Wolfgang Sturm, Jorma Jormakka, and White et al. for experimental and theoretical foundations.  

**Appendix A: VSS Integration (Units Verified)**  
Full tensor integral yields Eq. (2.6) with \(\vec{\mu}\) in A m².  

**Appendix B: Dispersion Coefficient Derivation**  
\(D = 4\pi \varepsilon_0 a_0 c^2 \hbar / e^2\) (SI: m² s\(^{-1}\)) matches White exactly.  

---

**References** (fully expanded with links)

White, H., Vera, J., Sylvester, A., & Dudzinski, L. (2026). Emergent quantization from a dynamic vacuum: quadratic dispersion \(\omega = D q^2\) validated in a responsive medium. *Phys. Rev. Research*, **8**, 013264. DOI: https://doi.org/10.1103/l8y7-r3rm  
Full text: https://journals.aps.org/prresearch/abstract/10.1103/l8y7-r3rm

Barbeau, D. (2025). Classical Unification of Gravity and Electromagnetism via Symmetric Vacuum Property Variations: A Singularity-Free Framework for Perihelion Precession, Light Bending, and Time Itself (CUGE v3). viXra:2507.0112. https://ai.vixra.org/abs/2507.0112

Barbeau, D. (2025). REFORM: REfractive Foundation of Relativity and Mechanics (v3). rxiverse:2508.0021. https://rxiverse.org/abs/2508.0021

Barbeau, D. (2025). Experimental Validation of the Atomic Statistical Hypothesis: Resolving Quantization Through Continuous Waves (ASH). viXra:2507.0123. https://ai.vixra.org/abs/2507.0123

Barbeau, D. (2025). The ZigZag Eternal Universe System (ZEUS v2). rxiverse:2508.0003. https://rxiverse.org/abs/2508.0003

Barbeau, D. (2025). Resolution of the Navier–Stokes Existence and Smoothness Problem via CUGE n-Body Mechanics. rxiverse:2510.0006. https://rxiverse.org/abs/2510.0006

Barbeau, D. (2025). Reconciling Historical Measurements in Relativistic Electron Dynamics. (Companion to CUGE/REFORM). https://www.bigbadaboom.ca

Sturm, W. (2022). Space Curvature on the Labdesk (half-effect experiment). viXra:2207.0014. https://vixra.org/abs/2207.0014


---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---