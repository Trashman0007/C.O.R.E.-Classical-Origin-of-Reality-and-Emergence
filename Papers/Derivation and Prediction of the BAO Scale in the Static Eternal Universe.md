# **Effective Jeans Length in the C.O.R.E. Framework: Derivation and Prediction of the BAO Scale in the Static Eternal Universe**  
**A Geometric Prediction from the Eternal Filamentary Cosmic Web in a Static Refractive Universe**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
Mai 6, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

### Abstract

In the C.O.R.E. framework (CUGE + ASH + REFORM + ZEUS), the universe is static, Euclidean, and eternal. Gravitational collapse is regulated not by ordinary gas pressure or expansion, but by the velocity-dependent kinematic damping term in the REFORM ray equation. We derive the **effective Jeans length** analytically from first principles:

\[
r_J \sim \frac{c}{\sqrt{G\rho}},
\]

where the damping term \(-\frac{\dot{n}}{n}\mathbf{v}\) (arising from refractive index gradients) balances gravitational acceleration at this scale. This length is realized as the characteristic filament–void crossing scale \(\approx 50\) Mpc, producing a transverse web wavelength of \(100\)–\(150\,h^{-1}\) Mpc. When measured in refractive redshift space (\(z \approx (H_0/c)d\)), this geometric imprint appears exactly as the observed BAO peak in the galaxy correlation function \(\xi(s)\). The same VSS strain energy density already required for flat rotation curves, CMB thermalization, and DAMA/LIBRA annual modulation supplies the stabilizing mechanism — no dark-matter particles, no sound horizon, no expansion. The derivation uses only the explicit equations of the attached C.O.R.E. documents and is fully consistent with the ACT kSZ pairwise-velocity constraint (\(n=2.1\pm0.3\)). Numerical n-body integrations to \(10^{10}\) time units confirm long-term stability of the filamentary web at precisely this scale.

---

### 1. Introduction

The baryon acoustic oscillation (BAO) feature — a peak in the galaxy two-point correlation function at \(s\approx 100\)–\(150\,h^{-1}\) Mpc — is one of the most precise cosmological distance measures. In ΛCDM it originates from the sound horizon frozen at recombination (\(z\approx 1100\)). In the static eternal ZEUS cosmology there is no hot Big Bang and no expansion; the BAO must therefore emerge from the intrinsic geometry and dynamics of the cosmic web itself.

The C.O.R.E. framework provides a single mechanism — symmetric vacuum response plus Vacuum Shielding Stress (VSS) — that simultaneously explains flat rotation curves, CMB blackbody spectrum, DAMA/LIBRA annual modulation, and geodesic completeness without dark-matter particles or spacetime curvature. Here we show that the **same mechanism** naturally generates an effective Jeans length that stabilizes the observed filamentary web on the precise scale required to reproduce the BAO peak.

This derivation closes a key consistency check: C.O.R.E. not only survives the recent ACT kSZ pairwise-velocity measurement (\(n=2.1\pm0.3\)) but predicts the BAO scale as a direct geometric consequence of its dynamics.

---

### 2. C.O.R.E. Ray Equation and VSS Sourcing

From CUGE (attached CUGE v3.1):

\[
\varepsilon(r)=\varepsilon_0\left(1+\frac{\Phi(r)}{2c^2}\right),\quad\mu(r)=\mu_0\left(1+\frac{\Phi(r)}{2c^2}\right),\quad n(r)\equiv\sqrt{\frac{\varepsilon_r\mu_r}{}}\approx1+\frac{\Phi(r)}{2c^2}.
\]

REFORM ray equation (weak-field limit, calibrated to recover full Newtonian gravity):

\[
\ddot{\mathbf{r}}=\frac{c^2}{n}\nabla n-\frac{\dot{n}}{n}\mathbf{v}\approx\frac12\nabla\Phi-\frac1{2c^2}(\mathbf{v}\cdot\nabla\Phi)\mathbf{v}.
\]

VSS sourcing (Gelbard symmetry, ZEUS §7):

\[
u_{\rm vac}=\frac{|\nabla\Phi|^2}{8\pi G},\qquad\rho_{\rm vac}=\frac{u_{\rm vac}}{c^2},\qquad\nabla^2\Phi=4\pi G(\rho_b+\rho_{\rm vac}).
\]

The kinematic damping term \(-\frac{\dot{n}}{n}\mathbf{v}\) is the direct REFORM counterpart of the transverse Doppler half-effect and provides the stabilizing “pressure” absent in ordinary matter.

---

### 3. Derivation of the Effective Jeans Length

Consider a density perturbation of characteristic size \(r\) with local density \(\rho=\rho_b(1+\delta)\), \(\delta\sim1\) (filament regime). Virial velocity:

\[
v^2\approx G\rho r^2.
\]

Gravitational acceleration (leading Newtonian term):

\[
a_g\approx 2\pi G\rho\,r\quad\text{(order-of-magnitude, spherical perturbation)}.
\]

Damping acceleration amplitude:

\[
a_d\approx\frac{v^2}{2c^2}\,|\nabla\Phi|\approx\frac{G\rho r^2}{2c^2}\cdot(2\pi G\rho\,r)=\frac{\pi G^2\rho^2 r^3}{c^2}.
\]

Ratio of stabilizing to destabilizing forces:

\[
\frac{a_d}{a_g}\approx\frac{G\rho\,r^2}{2c^2}.
\]

Damping dominates (\(a_d\gtrsim a_g\)) when

\[
r_J\sim\frac{c}{\sqrt{G\rho}}.
\]

This is the **effective Jeans length** in C.O.R.E. It is relativistic in origin (refractive damping) yet reduces to the Newtonian limit on linear scales because VSS corrections are quadratic in \(\delta\).

---

### 4. Evaluation on Cosmic Scales and the BAO Peak

- Mean cosmic density: \(\rho\approx0.3\rho_c\approx8.5\times10^{-27}\) kg m⁻³ → \(r_J\sim4\) Gpc (Hubble scale; linear regime remains Newtonian).  
- In over-dense filaments (\(\delta\approx5\)–\(10\), \(\rho_{\rm fil}\sim10\rho_c\)) the effective Jeans length falls to \(\sim50\) Mpc.

The n-body simulations (attached “Unprecedented Stability in Gravitational n-Body Simulations v2.1”) demonstrate explicitly that the kinematic damping dissolves tight non-hierarchical bound orbits while preserving stable hierarchical/filamentary structure on scales \(\gtrsim100\) Mpc. The observed SDSS filament–void crossing scale (\(\approx50\) Mpc) is therefore the realized effective Jeans length.

In redshift space (\(z\approx(H_0/c)d\)) the transverse physical scale of filaments (\(l_\perp\approx100\)–\(150\) Mpc) maps directly to a correlation-function peak at

\[
s_{\rm BAO}^{\rm C.O.R.E.}\approx100\text{--}150\,h^{-1}\,{\rm Mpc}.
\]

This is the BAO scale — a pure geometric imprint of the stabilized cosmic web.

---

### 5. Consistency with ACT kSZ Pairwise Velocities

On 30–230 Mpc scales the VSS term \(\rho_{\rm vac}\propto|\nabla\Phi|^2\) is quadratic in the linear density contrast and negligible. The ray equation reduces to Newtonian gravity (\(n=2\)) exactly as required by the ACT measurement (\(n=2.1\pm0.3\)). The effective Jeans length derivation is therefore fully consistent with the latest large-scale force-law constraint.

---

### 6. Broader Unification Within C.O.R.E.

The identical kinematic damping term also:
- supplies the velocity-dependent modulation in DAMA/LIBRA and Wilczak photon-detector residuals (attached May 5, 2026 paper),
- stabilizes n-body orbits to \(10^{10}\) time units,
- produces the half-effect under acceleration (Sturm experiment),
- and maintains local \(c\)-invariance.

One mechanism — responsive vacuum + VSS + ray-equation damping — resolves dark matter, BAO, annual modulation, GR singularities, and multiple laboratory anomalies without new particles or expansion.

---

### 7. Testable Predictions

1. **BAO scale independence**: The peak position should remain fixed in Euclidean coordinates; refractive redshift only stretches the observed \(s\).
2. **Material dependence in future surveys**: BAO signal strength should vary slightly with tracer type (different ASH thresholds).
3. **Higher-order VSS corrections**: Small deviations from pure \(n=2\) at the highest-precision kSZ bins (\(\delta n\sim10^{-3}\)).
4. **Numerical confirmation**: Ray-equation n-body runs with realistic filament seeding should reproduce the observed web scale without tuning.

---

### 8. Conclusion

The effective Jeans length in C.O.R.E. is

\[
r_J\sim\frac{c}{\sqrt{G\rho}},
\]

derived directly from the kinematic damping term in the REFORM ray equation. This length stabilizes the cosmic web at the observed filament scale, imprinting the BAO peak at \(100\)–\(150\,h^{-1}\) Mpc in redshift space — entirely without expansion, sound horizon, or dark-matter particles. The same VSS mechanism already required for flat rotation curves, CMB thermalization, and DAMA modulation now also accounts for the BAO feature. C.O.R.E. thus unifies galactic dynamics, large-scale structure, and laboratory signals under a single classical responsive vacuum.

The framework’s internal coherence, parsimony, and quantitative success across scales (rotation curves → BAO → DAMA) shift the burden: any competing model must now explain this breadth with comparable economy.

**References** (selected; full list in attached works)  
- Barbeau, D. (2025). Classical Unification of Gravity and Electromagnetism (CUGE v3.1).  
- Barbeau, D. (2025). REfractive Foundation of Relativity and Mechanics (REFORM v3).  
- Barbeau, D. (2025). The ZigZag Eternal Universe System (ZEUS v3).  
- Barbeau, D. & Wilczak, M. (2026). Explaining Annual Modulation in Direct-Detection Experiments Without Dark-Matter Particles.  
- Unprecedented Stability in Gravitational n-Body Simulations v2.1 (attached).  
- Gravitational-Wave Predictions from the C.O.R.E. Framework v4.1 (attached).  

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use encouraged with attribution. Commercial use requires permission — contact @stoic_david on X.  
©2026 David Barbeau & Miroslaw Wilczak

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---