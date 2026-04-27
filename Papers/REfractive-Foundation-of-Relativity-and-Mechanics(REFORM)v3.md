# REFORM: REfractive Foundation of Relativity and Mechanics

**David Barbeau, Independent Researcher**  
david@bigbadaboom.ca | www.bigbadaboom.ca  

March 30, 2026, Revision 3

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.  
©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

## Abstract

This paper presents a classical, singularity-free derivation of Lorentz symmetry from the physical requirement that the phase of a continuous electromagnetic wave must remain continuous across reference frames. We show that relativistic effects—including time dilation, length contraction, Doppler shifts—emerge not from abstract postulates, but as the sum of two physical effects: (1) refractive path delay governed by Snell's law and the eikonal equation, and (2) kinematic time dilation due to transverse motion. By integrating the ray equation \( \frac{d}{ds} (n \hat{t}) = \nabla n \) along paths with relative motion, we recover a Lorentz-type transformation where the refractive index \( n(r) \equiv \sqrt{\varepsilon_r(r)\mu_r(r)} \) plays the role of a coordinate-dependent speed regulator. This refractive foundation unifies gravity and motion under a single electromagnetic framework, consistent with the C.O.R.E. paradigm. Crucially, real gravity alters \( \varepsilon(r) \) and \( \mu(r) \), while acceleration does not—explaining the "half-effect" in lab experiments and falsifying the strict Equivalence Principle.

---

## 1. Introduction: The Need for Reform

The postulates of Special Relativity (SR)—invariant light speed and frame symmetry—are empirically robust, yet their geometric interpretation has led physics toward abstraction: spacetime curvature, singularities, and unobservable fields. However, as demonstrated in the C.O.R.E. framework, a classical alternative exists: one where light is a continuous wave, gravity emerges from vacuum property variations, and cosmology is static.

In this paper, we show that Lorentz symmetry itself is not fundamental, but emergent from wave propagation in a responsive vacuum medium. Specifically, we derive a Lorentz-like transformation by integrating the eikonal equation along paths with relative motion—demonstrating that relativistic effects arise as the sum of:

1. Refractive delay (Snell's law in a medium with \( n(r) > 1 \)), and
2. Kinematic time dilation (transverse Doppler effect).

This refractive foundation explains why SR works in flat space, why GR doubles its predictions in gravity, and why acceleration fails to mimic gravity—resolving the "half-effect" observed in laboratory experiments [Space Curvature on the Labdesk - Wolfgang Sturm].

---

## 2. The Eikonal Equation in a Responsive Vacuum

In the CUGE framework, mass induces symmetric variations in vacuum permittivity and permeability:

\[
\varepsilon(r) = \varepsilon_0 \left(1 + \frac{GM}{2c^2 r}\right), \quad \mu(r) = \mu_0 \left(1 + \frac{GM}{2c^2 r}\right). \tag{2.1}
\]

This yields an effective refractive index (strictly dimensionless):

\[
n(r) \equiv \sqrt{\varepsilon_r(r)\mu_r(r)} \approx 1 + \frac{GM}{2c^2 r}, \tag{2.2}
\]

and a coordinate speed of light:

\[
c_{\rm coord}(r) = \frac{c}{n(r)} < c. \tag{2.3}
\]

The propagation of a continuous electromagnetic wave (per ASH) is governed by the eikonal equation:

\[
|\nabla S(r)| = k_0 n(r), \quad k_0 = \omega/c, \tag{2.4}
\]

where \( S(r) \) is the phase. The ray equation (from Fermat's principle) is:

\[
\frac{d}{ds} (n \hat{t}) = \nabla n, \tag{2.5}
\]

where \( \hat{t} \) is the unit tangent to the ray path.

This is the classical analog of geodesic motion—refraction replaces curvature.

---

## 3. The Origin of \(\gamma\): Phase Delay Over a 2D Inverse-Square Field

The Lorentz factor,
\[
\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}, \tag{3.1}
\]
has been historically interpreted as a geometric scaling arising from postulates of special relativity. We show this is incorrect.

Instead, \(\gamma\) emerges as a measure of accumulated phase delay across the two-dimensional transverse plane of a wavefront propagating through a physical vacuum whose electromagnetic properties respond to sources governed by the inverse-square law.

Consider a continuous electromagnetic wave with phase:
\[
\phi(\vec{r}, t) = \vec{k} \cdot \vec{r} - \omega t. \tag{3.2}
\]
Physical reality demands phase continuity: no spontaneous jumps in \(\phi\). When two observers are in relative motion or separated by a gravitational potential, their measurements must preserve the coherence of this phase across space and time.

A continuous electromagnetic wave spreads over spherical surface area \(A = 4\pi r^2\), so intensity \(\propto 1/r^2\). Gauss’s law for gravity gives
\[
g(r) = \frac{GM}{r^2} \implies \Phi(r) = -\frac{GM}{r}. \tag{3.3}
\]
A transverse slice of the wavefront has projected area element
\[
dA_\perp = 2\pi\rho\,d\rho, \quad 0 \le \rho \le R. \tag{3.4}
\]
Phase continuity across every point on this 2D surface is the physical invariant:
\[
|\nabla\phi| = k_0 n(r), \quad k_0 = \omega/c. \tag{3.5}
\]

**Kinematic half (always present):** For an observer moving transversely at velocity \(v\), the wavefront arrives at oblique angle \(\theta\) where \(\tan\theta \approx v/c_{\rm coord} \approx v/c\) (weak field). The effective path length becomes
\[
L_{\rm eff} = \frac{L}{\cos\theta} \approx L\left(1 + \frac{v^2}{2c^2}\right). \tag{3.6}
\]
The kinematic time delay is
\[
\delta t_{\rm kin} = \frac{L_{\rm eff}}{c} - \frac{L}{c} \approx L \cdot \frac{v^2}{2c^3}. \tag{3.7}
\]
(Dimensional check: \(L\) (m), \(v^2/c^3\) (s/m) → \(\delta t_{\rm kin}\) (s) ✓.)

**Refractive half (gravity only):** Vacuum strain modifies \(\varepsilon_r = \mu_r = 1 + \frac{GM}{2c^2 r}\), so
\[
n(r) \equiv \sqrt{\varepsilon_r(r)\mu_r(r)} \approx 1 + \frac{GM}{2c^2 r}. \tag{3.8}
\]
Extra optical path length:
\[
\delta L_{\rm ref} = (n-1)L \approx L \cdot \frac{GM}{2c^2 r}. \tag{3.9}
\]
Under pure acceleration (\(\varepsilon_r = \mu_r = 1\)) this term is identically zero; light receives only the kinematic half.

**Phase accumulation over the full 2D area — geometric doubling:**  
Total phase across the wavefront:
\[
\Delta\Phi_{\rm total} = \int_{r_{\min}}^R k_0 n(\rho) \cdot 2\pi\rho\,d\rho. \tag{3.10}
\]
With \(n(\rho) \approx 1 + GM/(2c^2\rho)\) and \(R \gg r_{\min}\):
\[
\Delta\Phi_{\rm total} \approx k_0 \left[ \pi R^2 + \frac{\pi GM R}{c^2} \right]. \tag{3.11}
\]
The refractive correction is \(\Delta\Phi_{\rm ref} \approx \pi k_0 GM R / c^2\). A 1D central-ray baseline yields only a logarithmic term, whereas the 2D area weighting produces a linear term. In the weak-field limit the ratio of refractive contributions is exactly 2:
\[
\Delta\Phi_{\rm 2D, ref} \approx 2 \times \Delta\Phi_{\rm 1D, ref}. \tag{3.12}
\]

**Total delay:** Converting kinematic delay to optical path length gives
\[
\delta L_{\rm total} = \underbrace{L \cdot \frac{v^2}{2c^2}}_{\rm kinematic\ (always)} + \underbrace{L \cdot \frac{GM}{2c^2 r}}_{\rm refractive\ (gravity\ only)}. \tag{3.13}
\]
Phase invariance
\[
kx - \omega t = k'x' - \omega't' \tag{3.14}
\]
with dispersion \(\omega = c k / n\) then forces
\[
\gamma = \frac{1}{\sqrt{1 - v^2/(n^2 c^2)}}. \tag{3.15}
\]
For \(n \approx 1\) this recovers (3.1). In real gravity the observer’s own apparatus is scaled by the same strain (\(n>1\)), so the measured redshift is the *full* \(-GM/(c^2 r)\). Under acceleration (\(n=1\)) only the kinematic half appears — the half-effect observed by Sturm.

**Experimental distinction**

| Scenario                  | Kinematic Half on Light | Refractive Half on Light | Observer Apparatus Scaled? | Measured Redshift                  |
|---------------------------|--------------------------|---------------------------|-----------------------------|------------------------------------|
| Real Gravity              | Present (½)             | Present (½)              | Yes (by same strain)       | Full (\(-gh/c^2\))                 |
| Acceleration (horizontal) | Present (½)             | Absent                   | No                         | Half-effect                        |
| Acceleration (vertical)   | First-order Doppler + kinematic | Absent            | No                         | Coincidental full numerical value* |

*Matches GR numerically via first-order Doppler, but mechanism differs from gravity (no vacuum strain).

This 2D geometric closure eliminates the need for postulates: \(\gamma\) is simply the normalized phase delay integrated over the projected area of any inverse-square field. The kinematic half is always present; the refractive half requires real vacuum strain and is therefore gravity-only. All equations satisfy SI base units, dimensionless \(n\), and distinguish local gradients (m⁻¹) from integrated phase (dimensionless).



---

## 4. Phase Continuity: The Physical Invariant Behind Symmetry

In contrast to Einstein's postulate-driven approach, we begin with a physical requirement: the phase of a continuous wave must be continuous across reference frames.

In the C.O.R.E. framework, light is not a stream of photons, but a continuous electromagnetic wave (per the Atomic Statistical Hypothesis, ASH). Its most fundamental physical property is its phase:

\[
\phi(\mathbf{r}, t) = \mathbf{k} \cdot \mathbf{r} - \omega t. \tag{4.1}
\]

This phase determines:

- Where wave crests and troughs are located,
- How interference patterns form,
- When and where energy is absorbed by matter.

At the moment of detection, the phase must be consistent. Otherwise, the wave would "break" or fail to transfer energy coherently. Therefore, phase is a physical invariant: all observers must agree on the phase at a given point in spacetime.

### 4.1 Deriving Lorentz Symmetry from Phase Continuity

Consider a plane wave in frame \( S \):

\[
\phi(x, t) = kx - \omega t. \tag{4.2}
\]

In a moving frame \( S' \), the phase must be the same:

\[
\phi'(x', t') = k' x' - \omega' t' = kx - \omega t. \tag{4.3}
\]

Using the dispersion relation in vacuum, \( \omega = c k \), we substitute:

\[
k' x' - c k' t' = k x - c k t \implies k' (x' - c t') = k (x - c t). \tag{4.4}
\]

This suggests a transformation that preserves \( (x - c t) \) and \( (x + c t) \). Assuming linearity:

\[
x' = A x + B t, \quad t' = C x + D t. \tag{4.5}
\]

Solving with boundary conditions (e.g., \( x' = 0 \implies x = v t \)) and matching Doppler shifts leads to:

\[
x' = \gamma (x - v t), \quad t' = \gamma \left( t - \frac{v x}{c^2} \right), \quad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}. \tag{4.6}
\]

The Lorentz transformation is not assumed—it emerges from the continuity of a wave.

---

## 5. Generalization to Refractive Media: The Full CUGE-SR Bridge

Now allow \( n(r) > 1 \). The dispersion relation becomes:

\[
\omega = \frac{c}{n} k. \tag{5.1}
\]

Phase invariance now implies:

\[
\frac{n}{c} x - t = \frac{n'}{c} x' - t'. \tag{5.2}
\]

Leading to a generalized transformation:

\[
x' = \gamma_n (x - v t), \quad t' = \gamma_n \left( t - \frac{v x}{n^2 c^2} \right), \quad \gamma_n = \frac{1}{\sqrt{1 - \frac{v^2}{n^2 c^2}}}. \tag{5.3}
\]

When \( n = 1 \), this reduces to SR. When \( n = 1 + \frac{GM}{2 c^2 r} \), the \( n^2 \) term introduces the factor observed in GR.

Thus, the "doubling" in gravitational effects relative to pure kinematics is split: half from kinematics (SR), half from refractive delay (CUGE).

---

## 6. Comparison of Predictions

| Phenomenon | SR Prediction | GR Prediction | CUGE/REFORM Prediction |
|------------|---------------|---------------|------------------------|
| Light bending (Sun) | \( 0.87'' \) | \( 1.75'' \) | \( 1.75'' \) ✓ |
| Perihelion precession | None | Full value | Full value ✓ |
| Time dilation (weak field) | Kinematic only | Gravitational + Kinematic | Gravitational + Kinematic ✓ |
| Shapiro delay | No prediction | Full prediction | Full prediction ✓ |
| Half-effect (acceleration) | No distinction | Falsified | Explained ✓ |

Table 6.1: Experimental agreement between GR and CUGE/REFORM frameworks, with distinctive testable difference for acceleration scenarios.

---

## 7. The Two Halves of Gravitational Redshift

In real gravity:

- **Kinematic half**: Transverse Doppler shift due to time dilation:

\[
\frac{\Delta f}{f} = -\frac{1}{2} \frac{v^2}{c^2} \approx -\frac{1}{2} \frac{GM}{c^2 r}. \tag{7.1}
\]

- **Refractive half**: Phase delay from \( n(r) > 1 \):

\[
\Delta t = \int \frac{n - 1}{c} \, dl \implies \frac{\Delta f}{f} = -\frac{1}{2} \frac{GM}{c^2 r}. \tag{7.2}
\]

Total redshift:

\[
\left( \frac{\Delta f}{f} \right)_{\rm gravity} = -\frac{GM}{c^2 r}, \tag{7.3}
\]

matching GR.

Under acceleration, only the kinematic half exists—confirming that acceleration ≠ gravity.

Local invariance of the measured speed of light \( c = 299\,792\,458~{\rm m~s^{-1}} \) is ensured by the co-variation of atomic clocks and rulers in the responsive vacuum, as derived in the updated CUGE framework (Section 2). According to the Atomic Statistical Hypothesis (ASH), the effective Planck constant is a material-dependent statistical average \( h_{\rm eff}(r) \) that scales linearly as \( h_{\rm eff}(r) \propto \varepsilon(r) \). Combined with the standard dielectric scaling of transition energies \( E \propto 1/\varepsilon(r)^2 \), this yields atomic frequencies \( \nu = E/h_{\rm eff} \propto 1/\varepsilon(r) \). Consequently the locally measured wavelength and frequency satisfy \( \lambda_{\rm meas} \propto \varepsilon(r) \) and \( f_{\rm meas} \propto 1/\varepsilon(r) \), restoring

\[
c_{\rm local} = \lambda_{\rm meas} \cdot f_{\rm meas} \propto \varepsilon(r) \cdot \frac{1}{\varepsilon(r)} = c = \text{constant}. \tag{7.4}
\]

This is independent of gravitational potential and direction. This completes the physical mechanism behind the kinematic half-effect under acceleration and the full redshift under real gravity, all within the same refractive foundation.

---

## 8. Conclusion: Relativity Without Geometry

We have shown that the Lorentz transformation is not a fundamental symmetry of spacetime, but an emergent consequence of wave propagation in a medium with variable \( \varepsilon(r) \) and \( \mu(r) \). The full relativistic effect is the sum:

\[
\text{SR} = \text{Snell's Law} + \text{Transverse Doppler}. \tag{8.1}
\]

This refractive foundation:

- Reproduces SR and GR predictions without curvature,
- Explains the half-effect in lab experiments,
- Falsifies the strict Equivalence Principle,
- Unifies gravity and motion under classical electromagnetism,
- Aligns with C.O.R.E.'s rejection of photons, dark entities, and singularities.

The era of abstract spacetime is ending. The era of classical emergence has begun.

---

## Related Works in the C.O.R.E. Framework

- CUGE: Classical Unification of Gravity and Electromagnetism
- ASH: The Atomic Statistical Hypothesis
- ZEUS: ZigZag Eternal Universe System
- Space Curvature on the Labdesk - Wolfgang Sturm

---

## References

[1] D. Barbeau, *Classical Unification of Gravity and Electromagnetism via Symmetric Vacuum Property Variations*, 2025.

[2] D. Barbeau, *Preservation of Two-Way Light Speed Isotropy in CUGE vs General Relativity*, 2025.

[3] D. Barbeau, *Experimental Validation of the Atomic Statistical Hypothesis*, 2025.

[4] D. Barbeau, *C.O.R.E.: The Classical Origin of Reality and Emergence*, 2025.

[5] W. Sturm, *Space Curvature on the Labdesk*, 2025.

[6] A. Einstein, *Erklärung der Perihelbewegung des Merkur*, Sitzungsberichte der Preussischen Akademie der Wissenschaften, 1915.

[7] C. M. Will, *The confrontation between GR and experiment*, Living Rev. Relativ., 2014.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---