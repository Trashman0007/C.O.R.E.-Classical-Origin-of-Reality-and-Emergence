# **Dispersion of Gravitational Waves in the C.O.R.E. Refractive Vacuum**

**David Barbeau, Independent Researcher**  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
July 6, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.  
©2026 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

## Abstract

In the C.O.R.E. (Classical Origin of Reality and Emergence) framework, gravity is modeled not as spacetime curvature, but as a physical, elastic refractive medium governed by symmetric variations in vacuum permittivity and permeability (CUGE). Gravitational waves are therefore formalized as propagating strain perturbations \(\delta n(\mathbf{r}, t)\) within this medium. By treating the vacuum as an effective continuum interacting with its underlying micro-structural Vacuum Shielding Stress (VSS) fluctuations, we derive its macroscopic viscoelastic response. This interaction introduces a temporal memory kernel that manifests in Fourier space as a resonant Lorentz-type susceptibility, where the characteristic resonance frequency \(\Omega_0\) is explicitly fixed by the inverse vacuum relaxation time \(\Omega_0 \equiv 1/\tau_{\rm vac}\). In the high-frequency eikonal regime relevant to ground-based interferometry (\(\omega \gg \Omega_0\)), this constitutive wave equation yields a real, subluminal group velocity deviation proportional to \(\omega^{-2}\). Evaluated with untuned, ZEUS-calibrated galactic background parameters, the fractional group velocity modification is \(|v_g - c|/c \approx 3.2 \times 10^{-16}\). This result is strictly consistent with the GW170817 multi-messenger observational bound while providing a distinct, frequency-dependent signature for future high-precision space-based interferometers.

---

## 1. Introduction: Gravitational Waves as Medium Strain

General Relativity treats gravitational waves as ripples in the metric tensor of spacetime, propagating strictly at the invariant speed \(c\) in vacuum with zero dispersion. The C.O.R.E. framework—encompassing the Classical Unification of Gravity and Electromagnetism (CUGE), the Refractive Foundation of Relativity and Mechanics (REFORM), and the ZigZag Eternal Universe System (ZEUS)—replaces this geometric abstraction with a physical ontology: the vacuum is a polarizable, elastic physical medium.

Mass induces a static strain gradient in this medium, altering its electromagnetic constitutive parameters \(\varepsilon(\mathbf{r})\) and \(\mu(\mathbf{r})\). This generates a position-dependent coordinate refractive index \(n(\mathbf{r}) = 1 + \Phi(\mathbf{r})/(2c^2)\), where \(\Phi(\mathbf{r})\) is the classical gravitational potential. As demonstrated in *Tensors as Coordinate Encoding of Geometric Force*, gravitational phenomena—including light bending, perihelion precession, and orbital mechanics—are the kinematic and elastic responses of matter and light propagating through this refractive gradient.

Consequently, a gravitational wave is not a distortion of geometric spacetime; it is a **dynamic, propagating strain perturbation** \(\delta n(\mathbf{r}, t)\) in the vacuum substrate. Because the vacuum is a physical continuum, it possesses an effective inertial mass density \(\rho_\infty\) and a finite phase-coherence relaxation time \(\tau_{\rm vac}\) (representing internal viscosity and dissipation). Any wave propagating through a viscoelastic medium necessarily experiences dispersion. This paper derives that dispersion explicitly from the constitutive mechanics of the C.O.R.E. vacuum.

---

## 2. The Viscoelastic Vacuum and the Effective Wave Equation

### 2.1 Micro-Structural Origin of the Memory Kernel

The bare C.O.R.E. Lagrangian for the scalar gravitational potential field \(\Phi\) yields a local, dissipationless d'Alembert wave equation \(\Box \Phi = 0\) in an idealized, homogeneous environment. However, the physical vacuum substrate is not a featureless void; as established in the ZEUS cosmology, it is continuously saturated by a steady-state thermal sea of sub-resolution fluctuations responsible for the Vacuum Shielding Stress (VSS).

When a macroscopic strain perturbation \(\delta n(\mathbf{r}, t)\) propagates through this active substrate, it couples to these sub-resolution degrees of freedom. In continuum field mechanics, integrating out sub-resolution stochastic background modes transforms a local field equation into an effective non-local wave equation governed by a temporal memory kernel:

\[
\nabla^2 \delta n(\mathbf{r}, t) - \frac{1}{c^2}\frac{\partial^2 \delta n(\mathbf{r}, t)}{\partial t^2} - \int_{-\infty}^{t} \chi(t - t') \frac{\partial^2 \delta n(\mathbf{r}, t')}{\partial t'^2} dt' = 0
\]

where \(\chi(t)\) represents the causal relaxation response of the vacuum medium resisting dynamic shear deformation.

### 2.2 The Constitutive Wave Equation in Fourier Space

Transforming this integro-differential equation into Fourier space \((\mathbf{k}, \omega)\) yields the homogeneous constitutive wave equation:

\[
-\omega^2 \delta \tilde{n} + c^2 k^2 \delta \tilde{n} - \omega^2 A(\omega) \delta \tilde{n} = 0 \implies \omega^2 \bigl( 1 - A(\omega) \bigr) = c^2 k^2
\]

where \(A(\omega) = \tilde{\chi}(\omega)\) is the dimensionless complex reactive susceptibility of the vacuum medium.

To model the mechanical response of the VSS substrate without introducing arbitrary fitting parameters, we employ a standard Lorentz-type viscoelastic solid formulation. The vacuum possesses a fundamental spatial correlation scale—the VSS length scale \(\ell_{\rm VSS}\)—which dictates the characteristic phase-coherence relaxation time \(\tau_{\rm vac} = \ell_{\rm VSS}/c \approx 63\text{ s}\). The underlying structural resonance frequency of the medium is therefore fixed directly by this relaxation rate, \(\Omega_0 \equiv 1/\tau_{\rm vac} \approx 0.0158\text{ rad/s}\), with an intrinsic damping parameter \(\Gamma = 2/\tau_{\rm vac}\). The resulting susceptibility is:

\[
A(\omega) = -\beta \frac{\Omega_0^2}{\Omega_0^2 - \omega^2 - i\omega\Gamma}
\]

where \(\beta = \frac{U_0}{\rho_\infty c^2} = \frac{|\nabla\Phi_0|^2}{8\pi G \rho_\infty c^2} \ll 1\) represents the dimensionless ratio of the localized background gravitational strain energy density \(U_0\) to the rest-mass energy density of the cosmic vacuum substrate.

---

## 3. Extraction of High-Frequency Dispersion and Group Velocity

### 3.1 The High-Frequency Eikonal Regime

For astrophysical gravitational waves detected by ground-based interferometers like LIGO/Virgo (\(f \sim 100\text{ Hz} \implies \omega \sim 630\text{ rad/s}\)), the wave frequency is vastly higher than the sub-Hz structural resonance of the vacuum (\(\omega \gg \Omega_0\)).

To extract the leading-order dispersive behavior, we factor \(-\omega^2\) from the denominator of the Lorentzian susceptibility:

\[
A(\omega) = -\beta \frac{\Omega_0^2}{-\omega^2 \left( 1 - \frac{\Omega_0^2}{\omega^2} + i\frac{\Gamma}{\omega} \right)} = +\beta \frac{\Omega_0^2}{\omega^2} \left( 1 - \frac{\Omega_0^2}{\omega^2} + i\frac{\Gamma}{\omega} \right)^{-1}
\]

Expanding this expression via binomial series for \(\omega \gg \Omega_0, \Gamma\) separates the real reactive response from the imaginary dissipative attenuation:

\[
A(\omega) \approx +\beta \frac{\Omega_0^2}{\omega^2} \left( 1 + \frac{\Omega_0^2}{\omega^2} - i\frac{\Gamma}{\omega} \right) \approx \beta \frac{\Omega_0^2}{\omega^2} - i\beta \frac{\Omega_0^2 \Gamma}{\omega^3}
\]

The real part, \(\operatorname{Re}[A(\omega)] \approx +\beta \left(\frac{\Omega_0}{\omega}\right)^2\), governs the phase velocity and frequency dispersion of the propagating wave, while the imaginary part dictates the negligible spatial attenuation over cosmological distances.

### 3.2 Phase Velocity and Dispersive Wave Propagation

Substituting the real part of the susceptibility back into the exact constitutive dispersion relation yields:

\[
\omega^2 \left( 1 - \beta \frac{\Omega_0^2}{\omega^2} \right) = c^2 k^2 \implies \omega^2 - \beta \Omega_0^2 = c^2 k^2
\]

Solving explicitly for the wave vector \(k\) as a function of frequency \(\omega\):

\[
k(\omega) = \frac{\omega}{c} \sqrt{1 - \beta \frac{\Omega_0^2}{\omega^2}} \approx \frac{\omega}{c} \left( 1 - \frac{\beta \Omega_0^2}{2\omega^2} \right)
\]

This confirms that the phase velocity \(v_p\) of the strain wave satisfies:

\[
v_p = \frac{\omega}{k} \approx c \left( 1 + \frac{\beta \Omega_0^2}{2\omega^2} \right) > c
\]

As required by classical continuum mechanics for wave propagation above a medium's resonant cutoff, the phase velocity is superluminal (\(v_p > c\)). This does not violate causality, as physical information is transmitted strictly at the group velocity.

### 3.3 Derivation of Group Velocity Deviation

The propagation velocity of a localized wave packet is governed by the group velocity \(v_g = \frac{d\omega}{dk} = \left( \frac{dk}{d\omega} \right)^{-1}\). Differentiating our wave vector expansion with respect to frequency:

\[
\frac{dk}{d\omega} = \frac{1}{c} \frac{d}{d\omega} \left[ \omega - \frac{\beta \Omega_0^2}{2\omega} \right] = \frac{1}{c} \left( 1 + \frac{\beta \Omega_0^2}{2\omega^2} \right)
\]

Inverting this derivative yields the high-frequency group velocity:

\[
v_g = c \left( 1 + \frac{\beta \Omega_0^2}{2\omega^2} \right)^{-1} \approx c \left( 1 - \frac{\beta \Omega_0^2}{2\omega^2} \right) < c
\]

Expressing this result in terms of the observer's measured frequency \(\omega_0\), we obtain the dimensionless fractional group velocity modification:

\[
\frac{\Delta v_g}{c} = \frac{v_g - c}{c} \approx -\frac{\beta \Omega_0^2}{2\omega_0^2}
\]

The negative sign confirms that the medium exhibits anomalous dispersion in this regime: lower-frequency wave components experience a slight inertial lag relative to higher frequencies due to the finite viscoelastic relaxation time of the vacuum substrate.

---

## 4. Physical Interpretation and Observational Consistency

### 4.1 Emergent Massive-Field Phenomenology

The dispersion relation derived in Section 3.2, \(\omega^2 - \beta\Omega_0^2 = c^2k^2\), is mathematically identical in form to the dispersion profile of a relativistic massive scalar field, \(\omega^2 = c^2k^2 + (m_{\rm eff} c^2 / \hbar)^2\).

In standard gravitational wave astronomy, deviations from general relativity are often parameterized by bounding the hypothetical rest mass of the graviton. The C.O.R.E. framework demonstrates that such observational signatures do not require an intrinsic particle rest mass. Instead, an effective mass profile emerges naturally from the macroscopic memory kernel of the viscoelastic vacuum:

\[
m_{\rm eff} = \frac{\hbar \sqrt{\beta} \Omega_0}{c^2}
\]

This establishes a bridge between classical refractive continuum mechanics and standard gravitational-wave data analysis pipelines, proving that a relaxing elastic substrate mimics massive-field propagation without invoking quantum particle ontologies.

### 4.2 Numerical Evaluation and GW170817 Consistency

The multi-messenger observation of the binary neutron star merger GW170817 provides a stringent empirical benchmark for gravitational wave dispersion. The near-simultaneous detection of the gravitational wave signal and the electromagnetic gamma-ray burst across a baseline of \(d \approx 40\text{ Mpc}\) constrains the fractional group velocity difference to:

\[
\left| \frac{v_g - c}{c} \right| \lesssim 5 \times 10^{-16}
\]

We evaluate our derived group velocity deviation using untuned parameters natively calibrated within the ZEUS framework:

*   Local galactic background strain energy ratio: \(\beta \sim 10^{-6}\)
*   Vacuum structural resonance: \(\Omega_0 = \tau_{\rm vac}^{-1} = (63\text{ s})^{-1} \approx 0.01587\text{ rad/s} \implies \Omega_0^2 \approx 2.52 \times 10^{-4}\text{ s}^{-2}\)
*   Representative LIGO detection frequency: \(f = 100\text{ Hz} \implies \omega_0 = 2\pi f \approx 628.3\text{ rad/s} \implies \omega_0^2 \approx 3.95 \times 10^5\text{ s}^{-2}\)

Substituting these parameters into our fractional deviation expression yields:

\[
\left| \frac{\Delta v_g}{c} \right| \approx \frac{10^{-6} \times (2.52 \times 10^{-4})}{2 \times (3.95 \times 10^5)} \approx \mathbf{3.2 \times 10^{-16}}
\]

This untuned, localized calculation falls comfortably within the empirical upper bound established by GW170817. Furthermore, across cosmological distances, gravitational waves propagate predominantly through vast intergalactic voids where the ambient matter density—and consequently the background potential gradient \(|\nabla\Phi_0|^2\)—is orders of magnitude lower than within galactic halos. As a result, the path-averaged value of \(\beta\) across a \(40\text{ Mpc}\) baseline is significantly reduced, ensuring that the integrated cosmological dispersion remains well below current experimental thresholds.

### 4.3 Predictions for Next-Generation Interferometry

A defining signature of the C.O.R.E. refractive vacuum is the inverse-square frequency scaling of the group velocity deviation (\(\Delta v_g / c \propto \omega^{-2}\)). While this dispersion is highly suppressed at high terrestrial interferometry frequencies (\(10\text{ Hz} - 1\text{ kHz}\)), it scales inversely with frequency.

For future space-based interferometers such as the Laser Interferometer Space Antenna (LISA), which will observe supermassive black hole mergers in the milli-Hertz band (\(f \sim 10^{-3}\text{ Hz} \implies \omega_0 \sim 6.3 \times 10^{-3}\text{ rad/s}\)), wave propagation occurs near the resonant transition of the vacuum substrate (\(\omega_0 \sim \Omega_0\)). In this regime, the C.O.R.E. framework predicts a significant, frequency-dependent phase shift and waveform broadening that will be directly distinguishable from classical general relativity.

---

## 5. Conclusion

By treating the vacuum as a physical, viscoelastic refractive continuum interacting with a sub-resolution Vacuum Shielding Stress background, the dispersion of gravitational waves is derived without ad-hoc Lagrangian modifications or arbitrary parameters. Integrating out background fluctuations yields a temporal memory kernel that, in the high-frequency eikonal limit, generates an effective massive-field dispersion profile \(\omega^2 - \beta\Omega_0^2 = c^2k^2\).

Evaluated with untuned, ZEUS-calibrated parameters, the framework predicts a fractional group velocity deviation of \(|v_g - c|/c \approx 3.2 \times 10^{-16}\), strictly consistent with multi-messenger constraints while providing a clear, frequency-dependent signature for future space-based detectors. This result reinforces the C.O.R.E. ontology: gravitational phenomena are governed not by geometric spacetime curvature, but by the emergent classical optics and elasticity of a responsive vacuum.

---

**References**

1. Barbeau, D. (2025). *Classical Unification of Gravity and Electromagnetism via Symmetric Vacuum Property Variations (CUGE)*.
2. Barbeau, D. (2025). *REFORM: REfractive Foundation of Relativity and Mechanics*.
3. Barbeau, D. (2025). *The ZigZag Eternal Universe System (ZEUS)*.
4. Barbeau, D. (2025). *Tensors as Coordinate Encoding of Geometric Force*.
5. Abbott, B. P., et al. (LIGO Scientific Collaboration and Virgo Collaboration). (2017). Gravitational Waves and Gamma-Rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A. *The Astrophysical Journal Letters*, 848(2), L13.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2026 David Barbeau | david@bigbadaboom.ca
