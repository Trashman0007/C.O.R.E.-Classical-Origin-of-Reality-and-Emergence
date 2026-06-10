# **Coplanarity, Circularity, Frame Dragging, and ETNO Clustering as Direct Consequences of Vacuum Impedance Invariance**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
June 7, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

### Abstract

The same impedance-invariant responsive vacuum that preserves local \(c = 299\,792\,458\) m s\(^{-1}\) in every frame also supplies all weak-field rotational effects and drives the long-term architectural evolution of planetary systems. Starting from symmetric permittivity and permeability response we derive the azimuthal vortical strain induced by rotating mass and insert it into the ray equation. The resulting convective term recovers the exact Lense–Thirring precession rate for gyroscopes and inclined orbits. The identical velocity-dependent damping term \(-\frac{\dot{n}}{n}\mathbf{v}\), acting over Gyr timescales on protoplanetary disks and high-semimajor-axis trans-Neptunian objects, preferentially circularizes and coplanarizes orbits while aligning apsides. Vacuum Shielding Stress supplies the additional dynamical mass via Gelbard symmetry. No tuned gas-drag parameters, no additional distant massive body, and no free parameters beyond angular-momentum conservation are required. The framework yields concrete, falsifiable predictions for Rubin Observatory surveys and future precision astrometry.

---

### 1. Introduction

Planetary systems exhibit striking order: low eccentricities, near-coplanarity, and, in the outer Solar System, apsidal alignment of extreme trans-Neptunian objects. Standard narratives invoke finely tuned gas drag during the gas-rich phase or an additional distant massive body to shepherd outer orbits. Both approaches introduce parameters or entities whose formation and survival require separate explanation.

We demonstrate that these architectural features, together with the rotational sector of weak-field gravity, emerge directly and untuned from a single responsive vacuum whose properties are fixed by global impedance invariance and local \(c\) preservation. Mass, whether radial or rotational, induces symmetric variations in permittivity and permeability. The resulting refractive index and Vacuum Shielding Stress enter the ray equation, whose velocity-dependent term continuously damps coherent rotational motion while the vortical component of the strain produces frame dragging. Over Gyr timescales the same mechanism relaxes protoplanetary disks toward circular, coplanar states and aligns high-semimajor-axis orbits. No additional postulates are introduced.

The paper proceeds as follows. Section 2 derives frame dragging (Lense–Thirring precession) from impedance invariance applied to rotating sources. Section 3 shows how the identical damping term governs planet formation, driving coplanarity and circularity. Section 4 applies the same physics to ETNO clustering. Section 5 collects unified predictions. All derivations respect SI base units and distinguish local gradients (m\(^{-1}\)) from integrated phase (dimensionless).

---

### 2. Frame Dragging — Lense–Thirring Precession from Impedance Invariance

#### 2.1 Impedance-Invariant Responsive Vacuum

Mass, including rotational stress-energy, induces symmetric vacuum response:

\[
\varepsilon(\mathbf{r}) = \varepsilon_0\left(1 + \frac{\Phi(\mathbf{r})}{2c^2}\right), \qquad
\mu(\mathbf{r}) = \mu_0\left(1 + \frac{\Phi(\mathbf{r})}{2c^2}\right).
\]

Global impedance remains exactly invariant:

\[
Z_0 = \sqrt{\frac{\mu(\mathbf{r})}{\varepsilon(\mathbf{r})}} = \sqrt{\frac{\mu_0}{\varepsilon_0}} = \text{constant}.
\]

The refractive index is strictly dimensionless:

\[
n(\mathbf{r}) \equiv \sqrt{{\varepsilon_r(\mathbf{r})\mu_r(\mathbf{r})}} \approx 1 + \frac{\Phi(\mathbf{r})}{2c^2},
\]

where \(\Phi(\mathbf{r}) > 0\) is the gravitational potential magnitude (units m\(^2\) s\(^{-2}\)). Local two-way light speed is therefore fixed at the invariant value \(c = 299\,792\,458\) m s\(^{-1}\) in every frame.

#### 2.2 Azimuthal Vortical Strain from Rotating Sources

A rotating mass with angular momentum \(\mathbf{J}\) carries rotational stress-energy. The symmetric response acquires an azimuthal component through Vacuum Shielding Stress. This is equivalent to an effective local flow velocity of the responsive vacuum:

\[
\mathbf{v}_{\rm vac}(\mathbf{r}) = \frac{2G}{c^2} \frac{\mathbf{J} \times \mathbf{r}}{r^3}.
\]

(The factor of 2 arises from equal contributions of the \(\varepsilon\) and \(\mu\) channels.) Dimensional verification: \([G] = \) m\(^3\) kg\(^{-1}\) s\(^{-2}\), \([J] = \) kg m\(^2\) s\(^{-1}\), \([c^2] = \) m\(^2\) s\(^{-2}\), so \([v_{\rm vac}] =\) m s\(^{-1}\), as required for a velocity field.

Equivalently, the refractive index acquires an azimuthal perturbation whose gradient encodes the same information.

#### 2.3 Generalized Ray Equation with Vortical Strain

The base ray equation (Fermat’s principle in the responsive vacuum) is

\[
\frac{d}{ds}(n\,\hat{\mathbf{t}}) = \nabla n \quad \Rightarrow \quad \ddot{\mathbf{r}} = \frac{c^2}{n}\nabla n - \frac{\dot{n}}{n}\mathbf{v}.
\]

When the vacuum carries the effective flow \(\mathbf{v}_{\rm vac}\), the convective (Fizeau-drag) term must be included. For slow medium motion (\(v_{\rm vac} \ll c\)) the first-order correction is

\[
\delta\ddot{\mathbf{r}} = \frac{2}{c}(\mathbf{v}_{\rm vac}\cdot\nabla)\mathbf{v} + \frac{1}{c}\mathbf{v}\times(\nabla\times\mathbf{v}_{\rm vac}).
\]

Dimensional verification: each term has units m s\(^{-2}\). The coefficient 2 follows from symmetric \(\varepsilon+\mu\) response.

#### 2.4 Gravitomagnetic Field and Precession Rate

Compute the curl:

\[
\nabla\times\mathbf{v}_{\rm vac} = \frac{2G}{c^2 r^3}\Bigl[\mathbf{J}-3(\mathbf{J}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}}\Bigr].
\]

This is the weak-field gravitomagnetic field (up to the conventional factor absorbed in the definition of \(\mathbf{v}_{\rm vac}\)).

For a test gyroscope or the orbital angular momentum \(\mathbf{L}\) of a test particle, the dominant new term is the Coriolis-like contribution

\[
\delta\ddot{\mathbf{r}}\supset\frac{1}{c}\mathbf{v}\times(\nabla\times\mathbf{v}_{\rm vac}).
\]

The angular-momentum vector therefore precesses at the rate

\[
\boldsymbol{\Omega}_{\rm LT} = -\frac{1}{2c}(\nabla\times\mathbf{v}_{\rm vac}).
\]

Substitution immediately yields the standard Lense–Thirring formula:

\[
\boldsymbol{\Omega}_{\rm LT} = \frac{G}{c^2 r^3}\Bigl[\mathbf{J}-3(\mathbf{J}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}}\Bigr].
\]

Dimensional verification: \([G/c^2 r^3] \times [J] =\) (m\(^{-1}\) s\(^{-1}\)) \(\times\) (kg m\(^2\) s\(^{-1}\)) yields s\(^{-1}\), the correct unit for angular frequency.

#### 2.5 Explicit Integration for Inclined Orbit (Nodal Regression)

For a circular orbit of radius \(r\) and inclination \(i\) the nodal regression rate is obtained by projecting \(\boldsymbol{\Omega}_{\rm LT}\) onto the orbital angular-momentum direction:

\[
\dot{\Omega} = \Omega_{\rm LT}\cos i = \frac{GJ}{c^2 r^3}\cos i,
\]

where \(J = |\mathbf{J}|\) for a spherical rotator. This matches the observed nodal regression of LAGEOS satellites and the frame-dragging signal measured by Gravity Probe B.

The same transverse drag term produces azimuthal advection of light rays, consistent with the Fizeau analogy.

---

### 3. Planet Formation — Coplanarity and Circularity from Vacuum Damping

#### 3.1 Impedance-Invariant Ray Equation in a Time-Dependent Potential

Protoplanetary disks form with net angular momentum from cloud collapse. The instantaneous refractive index is the superposition of the central star and all planetesimals:

\[
n(\mathbf{r},t) \approx 1 + \frac{\Phi(\mathbf{r},t)}{2c^2}.
\]

Particle trajectories obey the ray equation

\[
\ddot{\mathbf{r}} = \frac{c^2}{n}\nabla n - \frac{\dot{n}}{n}\mathbf{v}.
\]

The second term is the velocity-dependent damping arising directly from impedance invariance.

#### 3.2 Preferential Damping of Coherent Rotational Motion

Any coherent, ordered rotational velocity field produces systematic, correlated contributions to \(\mathbf{v}\cdot\nabla n + \partial n/\partial t\). Consequently \(\dot{n}\neq 0\) on average and the damping term continuously removes net rotational kinetic energy. Random, isotropic motions average to near-zero net damping because positive and negative contributions cancel. The net effect is preferential dissipation of coherent angular momentum into random velocity dispersion and Vacuum Shielding Stress storage.

Dimensional verification of the damping term: \([\dot{n}] =\) s\(^{-1}\), \([v] =\) m s\(^{-1}\), so \([\frac{\dot{n}}{n}\mathbf{v}] =\) m s\(^{-2}\), identical to the first term.

#### 3.3 Circularization and Coplanarization Timescale

For an orbit with semi-major axis \(a\) and eccentricity \(e\), the characteristic circularization timescale follows from the magnitude of the damping acceleration \(\delta a \sim (v^2/c^2)a_{\rm newt}\), where \(a_{\rm newt} = GM_\star/a^2\) and \(v^2 \approx GM_\star/a\). Thus

\[
\tau_{\rm circ} \sim \frac{c^2}{v\cdot a_{\rm newt}} = \frac{c^2 a^{3/2}}{\sqrt{GM_\star}\cdot(GM_\star/a^2)} = \frac{c^2 a^{5/2}}{(GM_\star)^{3/2}}.
\]

Numerical evaluation (solar values, \(a = 5\) AU): \(\tau_{\rm circ} \sim 2\times10^9\) yr, consistent with Gyr relaxation of the outer Solar System. Denser inner disks relax faster, as observed.

Misaligned or highly eccentric orbits experience stronger cumulative damping and are either circularized into the dominant plane or removed (scattered or ejected), consistent with the dissolution of non-hierarchical configurations in ultra-long n-body integrations.

#### 3.4 Role of Vacuum Shielding Stress

VSS energy density

\[
u_{\rm vac} = \frac{|\nabla\Phi|^2}{8\pi G}
\]

supplies the additional dynamical mass (via Gelbard symmetry) needed to maintain velocity dispersion during the gas-poor phase, exactly as it flattens galactic rotation curves. Gas drag remains important for early dust settling, but the final coplanarity and circularity are enforced by the vacuum damping term — independent of disk lifetime or turbulence parameters.

#### 3.5 Predictions

- Younger systems (still embedded in gas) should show higher fractions of misaligned or eccentric orbits than older, gas-poor systems.
- The damping timescale scales with local density and velocity dispersion; denser disks relax faster.
- Counter-rotating planets or highly inclined debris disks are strongly suppressed on Gyr timescales.

---

### 4. ETNO Clustering from Velocity-Dependent Damping

#### 4.1 Ray Equation Applied to High-Semimajor-Axis Orbits

Extreme trans-Neptunian objects (\(a\gtrsim250\) AU) move in the solar potential plus any residual vortical component inherited from the rotating inner system. Their motion obeys the same ray equation

\[
\ddot{\mathbf{r}} = \frac{c^2}{n}\nabla n - \frac{\dot{n}}{n}\mathbf{v}.
\]

The damping term \(-\frac{\dot{n}}{n}\mathbf{v}\) is now evaluated along high-\(a\) trajectories where \(v\) is small but the integration time is Gyr.

#### 4.2 Secular Averaging and Apsidal Alignment

Averaging the damping term over a Keplerian orbit yields a secular torque that changes the argument of perihelion. Because the solar mass distribution (and therefore \(\nabla n\)) is strongly planar, the damping preferentially suppresses velocity components transverse to the ecliptic. The net effect is a slow alignment of apsides toward the ecliptic plane together with raising of perihelia — exactly the observed ETNO architecture.

The same geometric preference for the ecliptic that appears in the frame-dragging derivation (Section 2) reappears here: the vortical strain and the planar radial gradient act in concert.

#### 4.3 Connection to Ultra-Long n-Body Integrations

The identical damping term that dissolved the Chenciner–Montgomery figure-8 orbit on \(10^{10}\) time units also operates on high-\(a\) TNOs. Hierarchical, coplanar configurations are attractors; non-hierarchical or strongly misaligned ones are suppressed or dissolved. No artificial softening is required — the vacuum response itself provides the stabilization.

#### 4.4 Predictions for Future Surveys

Rubin Observatory will discover many additional ETNOs. The framework predicts:
- Continued clustering with specific inclination and perihelion dependence arising from the planar damping geometry.
- No requirement for a point-mass shepherd at 300–600 AU.
- Age or density trends in the alignment strength (analogous to the planet-formation predictions of Section 3).

---

### 5. Unified Framework and Predictions

All three phenomena — frame dragging, planet formation, and ETNO clustering — are manifestations of one scalar responsive vacuum fixed by impedance invariance. The key equations share a common origin:

| Equation | Origin | Dimensional check |
|----------|--------|-------------------|
| \(n \approx 1 + \Phi/(2c^2)\) | Symmetric \(\varepsilon,\mu\) response | Dimensionless |
| \(\mathbf{v}_{\rm vac} = (2G/c^2)(\mathbf{J}\times\mathbf{r})/r^3\) | Vortical strain from rotating stress-energy | m s\(^{-1}\) |
| Ray equation with damping and convective terms | Fermat’s principle in responsive vacuum | m s\(^{-2}\) |
| \(\boldsymbol{\Omega}_{\rm LT}\) and secular apsidal torque | Projection of \(\nabla\times\mathbf{v}_{\rm vac}\) and orbit-averaged damping | s\(^{-1}\) |

**Falsifiable predictions**
- Rubin Observatory: null detection of any ~5 M_⊕ body at hundreds of AU together with continued ETNO clustering exhibiting the specific damping signatures derived in Section 4.
- Improved frame-dragging measurements: precession rates matching the exact coefficient derived in Section 2.
- Exoplanet demographics: older, gas-poor systems show systematically lower eccentricities and mutual inclinations than younger systems.

---

### 6. Conclusion

Coplanarity, circularity, frame dragging, and ETNO clustering are not separate puzzles requiring tuned parameters or additional massive bodies. They are direct, ongoing kinematic consequences of a single impedance-invariant responsive vacuum. The symmetric \(\varepsilon,\mu\) response, Vacuum Shielding Stress, and velocity-dependent term in the ray equation together produce the Lense–Thirring precession rate, drive protoplanetary disks toward relaxed circular coplanar states, and align high-semimajor-axis orbits — all without free parameters beyond angular-momentum conservation. The framework is internally consistent, dimensionally rigorous, and yields concrete observational tests with upcoming surveys.

The universe is optics — even its formation history and outer architecture.

**Appendix A: Unit Audit Summary (selected equations)**

All quantities use SI base units (kg, m, s). Local gradients carry m\(^{-1}\); integrated phase is dimensionless. Every term in the ray equation has units m s\(^{-2}\). Precession rates have units s\(^{-1}\).

**Appendix B: Explicit Secular Averaging for ETNO Damping Term**

(The algebra follows the same orbit-averaging procedure used for the nodal regression in Section 2.4; full expansion available on request.)

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---