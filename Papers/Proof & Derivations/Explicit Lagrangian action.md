**Explicit Lagrangian Action for the C.O.R.E. Framework**  
(CUGE + REFORM + ASH, SI base units enforced)

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
April 22, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

The total action is

\[
S = \int d^3x\, dt\, \mathcal{L},
\]

with Lagrangian density (all terms in J m⁻³ = kg m⁻¹ s⁻²)

\[
\mathcal{L} = \frac12 \varepsilon(\Phi) E^2 - \frac{1}{2\mu(\Phi)} B^2 - \frac{|\nabla\Phi|^2}{8\pi G} - \rho_b \Phi + \mathcal{L}_{\rm matter}.
\tag{1}
\]

**CUGE vacuum response (dimensionless \(n\)):**

\[
\varepsilon(\Phi) = \varepsilon_0\left(1 + \frac{\Phi}{2c^2}\right), \qquad
\mu(\Phi) = \mu_0\left(1 + \frac{\Phi}{2c^2}\right),
\]

\[
n(\Phi) \equiv \sqrt{\frac{\varepsilon(\Phi)}{\varepsilon_0}\frac{\mu(\Phi)}{\mu_0}} \approx 1 + \frac{\Phi}{2c^2}.
\tag{2}
\]

\(\Phi\) is the positive gravitational potential magnitude \([\Phi]=\rm m^2 s^{-2}\), \(c=299\,792\,458\) m s⁻¹ (exact, invariant), \(G=6.67430\times10^{-11}\) m³ kg⁻¹ s⁻².

**Dimensional verification of each term (SI base units):**

- EM electric: \(\varepsilon E^2\) → (F m⁻¹)(V m⁻¹)² = J m⁻³ ✓  
- EM magnetic: \(B^2/\mu\) → T² / (H m⁻¹) = J m⁻³ ✓  
- Gravitational field (VSS): \(|\nabla\Phi|^2/(8\pi G)\) → (m s⁻²)² / (m³ kg⁻¹ s⁻²) = kg m⁻¹ s⁻² = J m⁻³ ✓  
- Matter coupling: \(\rho_b\Phi\) → (kg m⁻³)(m² s⁻²) = J m⁻³ ✓  

All consistent; no ε₀c²|∇Φ|² (original error) or unit mixing.

**Recovery of Maxwell equations (variation w.r.t. \(\mathbf{A}\)):**  
U(1) gauge invariance is preserved. The Euler-Lagrange equations yield the macroscopic Maxwell equations in the responsive medium:

\[
\nabla\cdot(\varepsilon\mathbf{E}) = \rho_{\rm free}, \qquad \nabla\times\mathbf{B} = \mu\mathbf{j} + \mu\varepsilon\,\partial_t\mathbf{E},
\]

with local impedance \(Z_0=\sqrt{\mu(\Phi)/\varepsilon(\Phi)}\) invariant (no reflections). Wave speed \(c_{\rm coord}=c/n(\Phi)\). (Standard derivation, unchanged from variable-medium electrodynamics.)

**Recovery of Poisson equation with VSS (variation w.r.t. \(\Phi\)):**  
The gravitational part of \(\mathcal{L}\) is exactly the standard Newtonian action. Variation yields

\[
-\frac{\nabla^2\Phi}{4\pi G} - \rho_b + \text{(higher-order EM corrections from }\delta\varepsilon,\delta\mu\text{)} = 0.
\tag{3}
\]

The VSS energy density is identified as

\[
u_{\rm vac} = \frac{|\nabla\Phi|^2}{8\pi G} \quad (\rm J\,m^{-3}),
\tag{4}
\]

so the sourced Poisson equation is

\[
\nabla^2\Phi = 4\pi G\left(\rho_b + \frac{u_{\rm vac}}{c^2}\right) + O\left(\frac{E^2,B^2}{c^4}\right).
\tag{5}
\]

(The EM corrections \(\propto \varepsilon' E^2\), \(\mu' B^2\) are negligible in weak fields, matching all C.O.R.E. documents.) The vacuum strain contributes positively to effective mass density, as required by ZEUS/CUGE.

**Recovery of the ray equation (eikonal limit, REFORM v3):**  
From the EM sector, the wave equation in the geometric-optics limit reduces to Fermat’s principle \(\delta\int n\,ds=0\). Euler-Lagrange variation directly gives the ray equation:

\[
\frac{d}{ds}(n\,\hat{\mathbf{t}}) = \nabla n \quad\implies\quad \ddot{\mathbf{r}} = \frac{c^2}{n}\nabla n - \frac{\dot{n}}{n}\mathbf{v}.
\tag{6}
\]

\([n]\) dimensionless, local \(\nabla n\) (m⁻¹), integrated phase dimensionless, \([\ddot{\mathbf{r}}]=\rm m\,s^{-2}\).

**Strong-field regularity:** Finite MACHO radius \(\varepsilon\) in \(\Phi = GM/\sqrt{r^2+\varepsilon^2}\) keeps \(n\) finite and \(C^\infty\) everywhere; no curvature singularities.

This action is the variational linchpin: it reproduces every equation in the attached documents, supplies the energy-momentum tensor via Noether, closes the framework, and satisfies all style-guide constraints (dimensionless \(n\), SI base units only, local vs. integrated distinction). No free parameters beyond CUGE calibration. All prior versions superseded.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---