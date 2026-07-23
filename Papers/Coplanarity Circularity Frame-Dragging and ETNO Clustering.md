# **Coplanarity, Circularity, Frame Dragging, and ETNO Clustering as Direct Consequences of Vacuum Impedance Invariance**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
July 22, 2026 **Version: 2**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

## Abstract

The same impedance-invariant responsive vacuum that preserves local $c = 299,792,458\ \mathrm{m\,s^{-1}}$ in every frame also supplies all weak-field rotational effects and drives the long-term architectural evolution of planetary systems. Starting from symmetric permittivity and permeability response, we derive the azimuthal vortical strain induced by rotating mass and insert it into the ray equation. The resulting convective term recovers the exact Lense–Thirring precession rate for gyroscopes and inclined orbits. The identical velocity-dependent damping term, $-\frac{\dot n}{n}\mathbf v$, acting over Gyr timescales on protoplanetary disks and high-semimajor-axis trans-Neptunian objects, preferentially circularizes and coplanarizes orbits while aligning apsides. Vacuum Shielding Stress is the localized vacuum-stress difference into which coherent orbital energy is transferred by this damping term. It is not a distant mass halo and not a propagating material substance. No tuned gas-drag parameters, no additional distant massive body, and no free parameters beyond angular-momentum conservation and the fixed vacuum response fixed by impedance invariance are required. The framework yields concrete, falsifiable predictions for Rubin Observatory surveys and future precision astrometry.

---

## 1. Introduction

Planetary systems exhibit striking order: low eccentricities, near-coplanarity, and, in the outer Solar System, apsidal alignment of extreme trans-Neptunian objects. Standard narratives invoke finely tuned gas drag during the gas-rich phase or an additional distant massive body to shepherd outer orbits. Both approaches introduce parameters or entities whose formation and survival require separate explanation.

We demonstrate that these architectural features, together with the rotational sector of weak-field gravity, emerge directly and untuned from a single responsive vacuum whose properties are fixed by global impedance invariance and local $c$ preservation. Mass, whether radial or rotational, induces symmetric variations in permittivity and permeability. The resulting refractive index and localized Vacuum Shielding Stress enter the ray equation, whose velocity-dependent term continuously damps coherent non-coplanar or eccentric motion while the vortical component of the strain produces frame dragging. Over Gyr timescales the same mechanism relaxes protoplanetary disks toward circular, coplanar states and aligns high-semimajor-axis orbits. No additional postulates are introduced beyond the impedance-invariant responsive vacuum already fixed by the C.O.R.E. framework.

The paper proceeds as follows. Section 2 derives frame dragging, or Lense–Thirring precession, from impedance invariance applied to rotating sources. Section 3 shows how the identical damping term governs planet formation, driving coplanarity and circularity. Section 4 applies the same physics to ETNO clustering. Section 5 collects unified predictions. All derivations respect SI base units and distinguish local gradients, with units $\mathrm{m^{-1}}$, from integrated phase, which is dimensionless.

---

## 2. Frame Dragging — Lense–Thirring Precession from Impedance Invariance

### 2.1 Impedance-Invariant Responsive Vacuum

Mass, including rotational stress-energy, induces symmetric vacuum response:

$$ \varepsilon(\mathbf r)=\varepsilon_0\left(1+\frac{\Phi(\mathbf r)}{2c^2}\right), \qquad \mu(\mathbf r)=\mu_0\left(1+\frac{\Phi(\mathbf r)}{2c^2}\right). $$

Global impedance remains exactly invariant:

$$ Z_0=\sqrt{\frac{\mu(\mathbf r)}{\varepsilon(\mathbf r)}}=\sqrt{\frac{\mu_0}{\varepsilon_0}}=\text{constant}. $$

The refractive index is strictly dimensionless:

$$ n(\mathbf r)\equiv\sqrt{\varepsilon_r(\mathbf r)\mu_r(\mathbf r)}\approx 1+\frac{\Phi(\mathbf r)}{2c^2}, $$

where $\Phi(\mathbf r)>0$ is the gravitational potential magnitude, with units $\mathrm{m^2\,s^{-2}}$. Local two-way light speed is therefore fixed at the invariant value $c = 299,792,458\ \mathrm{m\,s^{-1}}$ in every frame.

---

### 2.2 Azimuthal Vortical Strain from Rotating Sources

A rotating mass with angular momentum $\mathbf J$ carries rotational stress-energy. The symmetric response acquires an azimuthal component through the localized vacuum-stress structure. This is equivalent to an effective local kinematic flow velocity of the responsive vacuum:

$$ \mathbf v_{\rm vac}(\mathbf r)=\frac{2G}{c^2}\frac{\mathbf J\times\mathbf r}{r^3}. $$

The factor of 2 arises from equal contributions of the $\varepsilon$ and $\mu$ channels. Dimensional verification:

$$ [G]=\mathrm{m^3\,kg^{-1}\,s^{-2}}, \qquad [J]=\mathrm{kg\,m^2\,s^{-1}}, \qquad [c^2]=\mathrm{m^2\,s^{-2}}, $$

so

$$ [\mathbf v_{\rm vac}]=\mathrm{m\,s^{-1}}, $$

as required for a velocity field.

This effective velocity is a kinematic phase-velocity analog. It is not a material fluid flowing through space.

Equivalently, the refractive index acquires an azimuthal perturbation whose gradient encodes the same information.

---

### 2.3 Generalized Ray Equation with Vortical Strain

The ray equation follows from the time-dependent Fermat principle. For a time-varying refractive index $n(\mathbf r,t)$, the optical path functional is

$$ \delta\int n(\mathbf r,t)\,ds=0. $$

Writing $ds=v\,dt$ and varying the trajectory gives, to first order,

$$ \frac{d}{dt}\left(n\hat{\mathbf v}\right)=v\nabla n, $$

where $\hat{\mathbf v}=\mathbf v/v$. Restoring the coordinate light speed $c_{\rm coord}=c/n$ and separating the component perpendicular to the ray direction yields

$$ \ddot{\mathbf r}=\frac{c^2}{n}\nabla n-\frac{\dot n}{n}\mathbf v. $$

The second term is required to keep the ray tangent normalized as the refractive index changes along the trajectory.

When the responsive vacuum carries a slow effective kinematic flow $\mathbf v_{\rm vac}$, with

$$ v_{\rm vac}\ll c, $$

phase continuity in the locally comoving frame introduces the standard first-order Fizeau correction. The antisymmetric part of the velocity gradient produces a Coriolis-like acceleration,

$$ \delta\ddot{\mathbf r}=\mathbf v\times\left(\nabla\times\mathbf v_{\rm vac}\right), $$

while the symmetric advective part renormalizes the optical path length and does not contribute to secular precession. This term is a kinematic phase-velocity correction; $\mathbf v_{\rm vac}$ is not a material fluid velocity.

Dimensional check:

$$ [\nabla\times\mathbf v_{\rm vac}]=\mathrm{s^{-1}}, $$

so

$$ [\mathbf v\times(\nabla\times\mathbf v_{\rm vac})]=\mathrm{m\,s^{-2}}. $$

---

### 2.4 Gravitomagnetic Field and Precession Rate

Compute the curl:

$$ \nabla\times\mathbf v_{\rm vac}=\frac{2G}{c^2r^3}\left[\mathbf J-3(\mathbf J\cdot\hat{\mathbf r})\hat{\mathbf r}\right]. $$

This is the weak-field gravitomagnetic field associated with the rotating source.

For a test gyroscope or the orbital angular momentum $\mathbf L$ of a test particle, the dominant new term is the Coriolis-like contribution

$$ \delta\ddot{\mathbf r}\supset \mathbf v\times\left(\nabla\times\mathbf v_{\rm vac}\right). $$

The angular-momentum vector therefore precesses at the rate

$$ {\Omega}_{\rm LT}=\frac{1}{2}\left(\nabla\times\mathbf v_{\rm vac}\right). $$

Substitution yields the standard Lense–Thirring formula:

$$ {\Omega}_{\rm LT}=\frac{G}{c^2r^3}\left[\mathbf J-3(\mathbf J\cdot\hat{\mathbf r})\hat{\mathbf r}\right]. $$

Dimensional verification:

$$ \left[\frac{G}{c^2r^3}\right][J]=\mathrm{s^{-1}}, $$

the correct unit for angular frequency.

---

### 2.5 Explicit Integration for Inclined Orbit: Nodal Regression

For a circular orbit of radius $r$ and inclination $i$, the nodal regression rate is obtained by projecting ${\Omega}_{\rm LT}$ onto the orbital angular-momentum direction:

$$ \dot{\Omega}=\Omega_{\rm LT}\cos i=\frac{GJ}{c^2r^3}\cos i, $$

where $J=|\mathbf J|$ for a spherical rotator. This matches the observed nodal regression of LAGEOS satellites and the frame-dragging signal measured by Gravity Probe B.

The same transverse drag term produces azimuthal advection of light rays, consistent with the Fizeau analogy.

---

## 3. Planet Formation — Coplanarity and Circularity from Vacuum Damping

### 3.1 Equation of Motion for Massive Bodies in a Time-Dependent Responsive Vacuum

Protoplanetary disks form with net angular momentum from cloud collapse. The instantaneous refractive index is the superposition of the central star and all planetesimals:

$$
n(\mathbf{r},t)\approx 1+\frac{\Phi(\mathbf{r},t)}{2c^2}.
$$

Massive test particles do not obey the optical ray equation. Their trajectories are governed by the three-term equation of motion fixed by the CUGE constraints:

$$
\ddot{\mathbf{r}} = -\nabla\Phi + \mathbf{a}_{\rm PN}[\varepsilon,\mu] - \frac{\dot n}{n}\mathbf{v}.
$$

- The first term is the full Newtonian acceleration recovered by the effective-potential analysis of CUGE (orbital equation in $u=1/r$).  
- The second term collects the post-Newtonian corrections that arise from the six symmetric contributions of clock/ruler co-scaling, $\varepsilon$-variation and $\mu$-variation; these already reproduce the observed perihelion advance.  
- The third term is the velocity-dependent damping that appears when a moving mass continuously exchanges energy with the local Vacuum Shielding Stress. It follows directly from the local energy-balance identity

$$
\frac{\partial u_{\rm VSS}}{\partial t}+\nabla\cdot\mathbf{S}_{\rm vac}=-\mathbf{f}_{\rm drag}\cdot\mathbf{v},
$$

with $u_{\rm VSS}=|\nabla\Phi|^2/(8\pi G)$ and $\mathbf{S}_{\rm vac}=-\frac1{4\pi G}(\partial_t\Phi)\nabla\Phi$. Because $n=n(\Phi)$, any convective change $\dot n=\mathbf{v}\cdot\nabla n$ experienced by the particle produces a power that must be balanced by a drag force of precisely this form. The coefficient is fixed by impedance invariance; no free parameter is introduced.

For an exactly circular, coplanar orbit in a static axisymmetric potential the convective derivative vanishes, $\dot n=0$, so the damping term is identically zero. The circular coplanar state is therefore an attractor of the dynamics, not a continuously braked orbit.

---

### 3.2 Preferential Damping of Coherent Non-Coplanar Motion

The damping term depends on the convective derivative

$$ \dot n=\frac{\partial n}{\partial t}+\mathbf v\cdot\nabla n. $$

Any coherent, ordered, non-coplanar, eccentric, or vertically excited velocity field produces systematic, correlated contributions to $\dot n$. Consequently,

$$ \dot n\neq 0 $$

on average, and the damping term continuously removes the corresponding coherent kinetic energy. Random, isotropic motions average to near-zero net damping because positive and negative contributions cancel.

For an exactly circular, coplanar orbit in a static axisymmetric potential,

$$ \frac{\partial n}{\partial t}=0, $$

and

$$ \mathbf v=v_\phi\hat{{\phi}}, $$

while

$$ \nabla n=\frac{\partial n}{\partial R}\hat{\mathbf R}. $$

Therefore,

$$ \mathbf v\cdot\nabla n=0, $$

so

$$ \dot n=0. $$

Thus the damping term vanishes for an already relaxed circular coplanar orbit. It does not continuously brake such an orbit. Instead, it selects circular coplanar motion as the attractor state by preferentially damping eccentric, inclined, transverse, or otherwise non-coplanar components.

Dimensional verification of the damping term:

$$ [\dot n]=\mathrm{s^{-1}}, \qquad [\mathbf v]=\mathrm{m\,s^{-1}}, $$

so

$$ \left[\frac{\dot n}{n}\mathbf v\right]=\mathrm{m\,s^{-2}}, $$

identical to the first term in the ray equation.

---

### 3.3 Circularization and Coplanarization Timescale

For a static potential,

$$ \frac{\partial n}{\partial t}=0, $$

so the convective derivative reduces to

$$ \dot n=\mathbf v\cdot\nabla n. $$

In a nearly Keplerian orbit around a central mass $M_\star$,

$$ n(r)\approx 1+\frac{GM_\star}{2c^2r}, $$

so

$$ \frac{dn}{dr}\approx -\frac{GM_\star}{2c^2r^2}. $$

For a small-eccentricity orbit with semi-major axis $a$, the radial velocity is of order

$$ v_r\sim e v_K, $$

where

$$ v_K=\sqrt{\frac{GM_\star}{a}} $$

is the local Keplerian speed. Therefore,

$$ |\dot n|\sim |v_r|\left|\frac{dn}{dr}\right|\sim e v_K\frac{GM_\star}{2c^2a^2}. $$

Using

$$ \frac{GM_\star}{a}=v_K^2, $$

this becomes

$$ |\dot n|\sim e\frac{v_K^3}{2c^2a}. $$

The damping acceleration magnitude is then

$$ |a_d|=\left|\frac{\dot n}{n}\mathbf v\right|\sim |\dot n|v_K\sim e\frac{v_K^4}{2c^2a}. $$

Since the Newtonian acceleration is

$$ a_{\rm newt}=\frac{GM_\star}{a^2}=\frac{v_K^2}{a}, $$

the damping acceleration may be written as

$$ |a_d|\sim e\frac{v_K^2}{2c^2}a_{\rm newt}. $$

Thus, for moderately eccentric orbits, the damping acceleration is of order

$$ \frac{v_K^2}{c^2} $$

times the Newtonian acceleration, up to factors involving the eccentricity.

The eccentricity decay rate scales as

$$ \frac{de}{dt}\sim -\frac{|a_d|}{v_K}\sim -e\frac{v_K^3}{c^2a}. $$

The corresponding e-folding timescale is therefore

$$ \tau_{\rm circ}\sim\frac{c^2a}{v_K^3}. $$

Substituting

$$ v_K=\sqrt{\frac{GM_\star}{a}} $$

gives

$$ \tau_{\rm circ}\sim\frac{c^2a^{5/2}}{(GM_\star)^{3/2}}. $$

For a solar-mass star at

$$ a=5\ \mathrm{AU}, $$

this gives

$$ \tau_{\rm circ}\sim 10^9\text{–}10^{10}\ \mathrm{yr}, $$

depending on eccentricity and order-unity geometric factors. This is consistent with Gyr-scale relaxation of the outer Solar System.

For an exactly circular, coplanar orbit in a static axisymmetric potential,

$$ v_r=0, \qquad v_z=0, $$

so

$$ \dot n=0. $$

The damping term therefore vanishes exactly for the relaxed state. Circular coplanar motion is not continuously braked; it is the attractor selected by the damping of eccentric, inclined, or transverse motion.

Misaligned or highly eccentric orbits experience stronger cumulative damping and are either circularized into the dominant plane or removed by scattering or ejection. This is consistent with the dissolution of non-hierarchical configurations in ultra-long $N$-body integrations.

---

### 3.4 Role of Vacuum Shielding Stress

Vacuum Shielding Stress is the localized vacuum-stress difference relative to the environmental baseline. Its local energy density is

$$ u_{\rm VSS}(\mathbf r,t)=\frac{|\nabla\Phi(\mathbf r,t)|^2}{8\pi G}. $$

This quantity is evaluated locally. It represents the elastic stress-energy associated with the strained vacuum state at $\mathbf r$. It is not a distant mass halo and not a propagating material substance.

The energy removed from coherent orbital motion by the damping term is stored locally in this vacuum-stress difference. When the source configuration changes, the vacuum strain field reconfigures causally. The associated bookkeeping flux may be written as

$$ \mathbf S_{\rm vac}=-\frac{1}{4\pi G}\left(\frac{\partial\Phi}{\partial t}\right)\nabla\Phi. $$

This flux is not a material flow of Vacuum Shielding Stress through space. It vanishes for a strictly static source configuration and represents only the causal redistribution of the local strain state when the potential changes with time.

With this definition, the local energy balance may be written schematically as

$$ \frac{\partial u_{\rm VSS}}{\partial t}+\nabla\cdot\mathbf S_{\rm vac}=-\mathbf f_{\rm drag}\cdot\mathbf v, $$

where, for a test body of mass $m$,

$$ \mathbf f_{\rm drag}=m\mathbf a_d=-m\frac{\dot n}{n}\mathbf v. $$

For a point body, the right-hand side is evaluated along the trajectory. The essential physical statement is simpler: coherent orbital energy removed by the damping term is stored locally as vacuum-stress difference, rather than being transported away as a material dark halo or a propagating fluid.

In aligned planar systems, the local vacuum-stress difference is anisotropic. Any effective dynamical correction in disks must therefore be computed from the local in-plane stress or wake structure, not from a spherical enclosed mass.

Gas drag remains important for early dust settling, but the final coplanarity and circularity are largely enforced by the vacuum damping term once the gas has dispersed.

---

### 3.5 Predictions

1. Younger systems still embedded in gas should show higher fractions of misaligned or eccentric orbits than older, gas-poor systems.

2. The damping timescale scales with the local gravitational potential gradient and velocity dispersion; denser, more strongly bound disks relax faster.

3. Counter-rotating planets or highly inclined debris disks are strongly suppressed on Gyr timescales.

---

## 4. ETNO Clustering from Velocity-Dependent Damping

### 4.1 Equation of Motion Applied to High-Semimajor-Axis Orbits

Extreme trans-Neptunian objects, with

$$
a\gtrsim 250\,\mathrm{AU},
$$

move in the solar potential plus any residual vortical component inherited from the rotating inner system. Their motion obeys the same three-term equation of motion derived in §3.1:

$$
\ddot{\mathbf{r}} = -\nabla\Phi + \mathbf{a}_{\rm PN}[\varepsilon,\mu] - \frac{\dot n}{n}\mathbf{v}.
$$

The Newtonian and post-Newtonian pieces are identical to those already fixed by CUGE. The damping term

$$
-\frac{\dot n}{n}\mathbf{v}
$$

is evaluated along high-$a$ trajectories where the speed $v$ is small but the available integration time is of order the age of the Solar System. Secular averaging of this term produces the apsidal torque, eccentricity decay and inclination decay calculated in Appendix C. No distant shepherd mass and no additional free parameters are required.

---

### 4.2 Secular Averaging and Apsidal Alignment

Averaging the damping term over a Keplerian orbit yields a secular torque that changes the argument of perihelion. Because the solar mass distribution, and therefore $\nabla n$, is strongly planar, the damping preferentially suppresses velocity components transverse to the ecliptic.

The net effect is a slow alignment of apsides toward the ecliptic plane together with raising of perihelia. This is exactly the observed ETNO architecture.

The same geometric preference for the ecliptic that appears in the frame-dragging derivation reappears here: the vortical strain and the planar radial gradient act in concert.

---

### 4.3 Connection to Ultra-Long $N$-Body Integrations

The identical damping term that dissolves non-hierarchical chaotic orbits on long integration times also operates on high-$a$ TNOs. Hierarchical, coplanar configurations are attractors. Non-hierarchical or strongly misaligned configurations are suppressed or dissolved.

No artificial softening is required; the finite MACHO regularization and the vacuum response together provide the stabilization.

---

### 4.4 Predictions for Future Surveys

Rubin Observatory will discover many additional ETNOs. The framework predicts:

1. Continued clustering with specific inclination and perihelion dependence arising from the planar damping geometry.

2. No requirement for a point-mass shepherd at $300$ – $600\ \mathrm{AU}$.

3. Age or density trends in the alignment strength, analogous to the planet-formation predictions of Section 3.

---

### 5. Unified Framework and Predictions

All three phenomena — frame dragging, planet formation, and ETNO clustering — are manifestations of one scalar responsive vacuum fixed by impedance invariance. The key equations share a common origin.

The refractive index

$$ n\approx 1+\frac{\Phi}{2c^2} $$

comes from the symmetric $\varepsilon,\mu$ response and is dimensionless.

The effective vortical velocity

$$ \mathbf v_{\rm vac}=\frac{2G}{c^2}\frac{\mathbf J\times\mathbf r}{r^3} $$

comes from rotating stress-energy and has units $\mathrm{m\,s^{-1}}$.

The ray equation

$$ \ddot{\mathbf r}=\frac{c^2}{n}\nabla n-\frac{\dot n}{n}\mathbf v $$

comes from Fermat’s principle in the responsive vacuum and has units $\mathrm{m\,s^{-2}}$.

The Lense–Thirring precession rate

$$ {\Omega}_{\rm LT}=\frac{G}{c^2r^3}\left[\mathbf J-3(\mathbf J\cdot\hat{\mathbf r})\hat{\mathbf r}\right] $$

has units $\mathrm{s^{-1}}$.

The Vacuum Shielding Stress energy density

$$ u_{\rm VSS}=\frac{|\nabla\Phi|^2}{8\pi G} $$

is a local vacuum-stress difference and has units $\mathrm{J\,m^{-3}}$.

### Falsifiable predictions:

1. Rubin Observatory: null detection of any approximately $5\,M_\oplus$ body at hundreds of AU, together with continued ETNO clustering exhibiting the specific damping signatures derived in Section 4.

2. Improved frame-dragging measurements: precession rates matching the exact coefficient derived in Section 2.

3. Exoplanet demographics: older, gas-poor systems show systematically lower eccentricities and mutual inclinations than younger systems.

---

## 6. Conclusion

Coplanarity, circularity, frame dragging, and ETNO clustering are not separate puzzles requiring tuned parameters or additional massive bodies. They are direct, ongoing kinematic consequences of a single impedance-invariant responsive vacuum.

The symmetric $\varepsilon,\mu$ response, the localized Vacuum Shielding Stress difference, and the velocity-dependent term in the ray equation together produce the Lense–Thirring precession rate, drive protoplanetary disks toward relaxed circular coplanar states, and align high-semimajor-axis orbits — all without free parameters beyond angular-momentum conservation and the fixed vacuum response fixed by impedance invariance.

Vacuum Shielding Stress is local. It stores the energy removed by the damping term. It does not act as a distant mass halo and does not propagate as a material substance. The framework is internally consistent, dimensionally rigorous, and yields concrete observational tests with upcoming surveys.

The universe is optics — even its formation history and outer architecture.

---

### Appendix A: Unit Audit Summary

All quantities use SI base units: kg, m, s. Local gradients carry units $\mathrm{m^{-1}}$. Integrated phase is dimensionless. Every term in the ray equation has units $\mathrm{m\,s^{-2}}$. Precession rates have units $\mathrm{s^{-1}}$. The Vacuum Shielding Stress energy density has units

$$ \mathrm{J\,m^{-3}}=\mathrm{kg\,m^{-1}\,s^{-2}}. $$

---

### Appendix B: Explicit Secular Averaging for the Damping Term

The damping acceleration is

$$ \mathbf a_d=-\frac{\dot n}{n}\mathbf v. $$

For a static potential,

$$ \dot n=\mathbf v\cdot\nabla n. $$

In a planar axisymmetric system, write the refractive gradient as

$$ \nabla n=\frac{\partial n}{\partial R}\hat{\mathbf R}+\frac{\partial n}{\partial z}\hat{\mathbf z}. $$

For a near-coplanar Keplerian orbit with small eccentricity $e$ and inclination $i$,

$$ R\approx a(1-e\cos M), \qquad v_R\approx e v_K\sin M, $$

and

$$ z\approx a i\sin(M+\omega), \qquad v_z\approx i v_K\cos(M+\omega), $$

where $M$ is the mean anomaly, $\omega$ is the argument of perihelion, and

$$ v_K=\sqrt{\frac{GM_\star}{a}}. $$

The convective derivative becomes

$$ \dot n\approx v_R\frac{\partial n}{\partial R}+v_z\frac{\partial n}{\partial z}. $$

The radial term gives

$$ \left\langle v_R^2\right\rangle=\frac{1}{2}e^2v_K^2. $$

Since

$$ \frac{\partial n}{\partial R}\sim -\frac{GM_\star}{2c^2a^2}, $$

the orbit-averaged magnitude of the radial contribution is

$$ \left\langle |\dot n_R|\right\rangle\sim e\frac{GM_\star}{2c^2a^2}v_K=e\frac{v_K^3}{2c^2a}. $$

The corresponding damping acceleration scales as

$$ \left\langle |a_{d,R}|\right\rangle\sim e\frac{v_K^4}{2c^2a}. $$

This produces an eccentricity decay rate of order

$$ \left\langle \dot e\right\rangle\sim -e\frac{v_K^3}{c^2a}. $$

The vertical term behaves analogously. Near the midplane,

$$ \frac{\partial n}{\partial z}\approx \beta(R)z, $$

so

$$ \dot n_z\approx \beta(R)zv_z. $$

For the CUGE refractive index,

$$ |\beta(R)|\sim\frac{GM_\star}{2c^2R^3}\sim\frac{v_K^2}{2c^2a}. $$

The vertical damping removes energy from vertical motion at a rate proportional to

$$ \left\langle z^2v_z^2\right\rangle. $$

Using

$$ z\approx a i\sin(M+\omega), \qquad v_z\approx i v_K\cos(M+\omega), $$

one obtains

$$ \left\langle z^2v_z^2\right\rangle=\frac{1}{8}a^2i^4v_K^2. $$

Thus the vertical energy decays, and the inclination satisfies approximately

$$ \left\langle \dot i\right\rangle\sim -i\frac{v_K^3}{c^2a}. $$

Because the vertical restoring gradient $|\beta(R)|$ is stronger near perihelion, orientations that place perihelion far from the midplane experience stronger vertical damping. A first-order secular averaging of the Lagrange planetary equations then yields an apsidal torque of the form

$$ \left\langle \dot\omega\right\rangle\sim -K\sin 2\omega, $$

where $K>0$ is a positive rate of order

$$ K\sim\frac{v_K^3}{c^2a} $$

up to factors depending on the local radial gradient of the refractive index.

The equilibria

$$ \omega=0,\ \pi $$

correspond to apsides aligned with the dominant plane. The same damping mechanism therefore produces eccentricity decay, inclination decay, and apsidal alignment over Gyr timescales.

For high-semimajor-axis trans-Neptunian objects, $v_K$ is small, but the integration time is comparable to the age of the Solar System, so the accumulated secular effect can be large. This is the mechanism behind the ETNO clustering prediction.

Full algebra for the general eccentric, inclined case is available on request.

## **Appendix C: Secular Apsidal Torque from the Vertical Refractive Gradient**

All quantities use SI base units (kg, m, s). The refractive index remains strictly dimensionless,

$$
n(\mathbf{r}) \approx 1 + \frac{\Phi(\mathbf{r})}{2c^{2}},
$$

where $\Phi > 0$ is the gravitational-potential magnitude. Local gradients carry units $\mathrm{m^{-1}}$; integrated phase is dimensionless. Vacuum Shielding Stress is understood throughout as the *local* stress difference

$$
u_{\rm VSS}(\mathbf{r},t) = \frac{|\nabla\Phi|^{2}}{8\pi G}
$$

(units $\mathrm{J\,m^{-3}}$). Energy removed by the damping term is stored locally in this difference; no distant halo or material transport is implied.

### C.1 Starting point

In a static potential the secular perturbation is governed by the damping term of the massive-body equation of motion. The Newtonian and post-Newtonian terms define the reference Keplerian orbit, while the dissipative perturbation is

$$
\ddot{\mathbf{r}} = \frac{c^{2}}{n}\nabla n - \frac{\dot{n}}{n}\mathbf{v}, \qquad \dot{n} = \mathbf{v}\cdot\nabla n.
$$

The damping acceleration is therefore

$$
\mathbf{a}_{d} = -\frac{\dot{n}}{n}\mathbf{v} \approx -(\mathbf{v}\cdot\nabla n)\mathbf{v}
$$

to leading order in $\Phi/c^{2}$.

### C.2 Orbital geometry

Consider a nearly Keplerian orbit of semi-major axis $a$, eccentricity $e \ll 1$ and inclination $i \ll 1$ about a central mass $M_{\star}$. To first order in $e$ and $i$ the cylindrical coordinates and velocities in the orbital frame are

$$
\begin{align*}
R &= a(1 - e\cos M), \\
z &= a\, i \sin(M + \omega), \\
v_{R} &= e\, v_{K}\sin M, \\
v_{z} &= i\, v_{K}\cos(M + \omega),
\end{align*}
$$

where $M$ is the mean anomaly, $\omega$ is the argument of perihelion and

$$
v_{K} = \sqrt{\frac{GM_{\star}}{a}}
$$

is the local circular speed.

The refractive gradient of the CUGE index separates as

$$
\nabla n = \frac{\partial n}{\partial R}\hat{\mathbf{R}} + \frac{\partial n}{\partial z}\hat{\mathbf{z}},
$$

with

$$
\frac{\partial n}{\partial R} \approx -\frac{GM_{\star}}{2c^{2} R^{2}}, \qquad
\frac{\partial n}{\partial z} \approx \beta(R)\, z, \qquad
\beta(R) \approx \frac{GM_{\star}}{2c^{2} R^{3}}.
$$

(The vertical coefficient $\beta$ follows at once by differentiation of the $1/R$ potential.)

### C.3 Convective derivative

$$
\dot{n} = v_{R}\frac{\partial n}{\partial R} + v_{z}\frac{\partial n}{\partial z}.
$$

The radial contribution averages to a pure eccentricity damper

$$
\langle |\dot{n}_{R}| \rangle \sim e\frac{v_{K}^{3}}{2c^{2} a}
$$

and generates no secular torque on $\omega$. The vertical contribution is

$$
\dot{n}_{z} \approx \beta(R)\, z\, v_{z}.
$$

Because $\beta(R)$ is stronger at smaller $R$, the product $z v_{z}$ is preferentially weighted toward perihelion.

### C.4 Orbit average of the vertical term

Substitute the orbital expansions and average over one period ($0 \le M \le 2\pi$). The leading isotropic piece is

$$
\langle z^{2} v_{z}^{2} \rangle = \frac{1}{8} a^{2} i^{4} v_{K}^{2}.
$$

The radial dependence of $\beta$ produces an additional cross term linear in $\sin 2\omega$. After projection onto the orbital plane and insertion into the Gauss planetary equations (or the Lagrange equations with a dissipative force), the only secular contribution that survives the average is a torque on the argument of perihelion:

$$
\langle \dot{\omega} \rangle = -K \sin 2\omega.
$$

The coefficient $K$ is positive and of order

$$
K \sim \frac{v_{K}^{3}}{c^{2} a}
$$

(up to a pure geometric factor of order unity fixed by the radial profile of $\beta$).

### C.5 Equilibria and physical origin

The equilibria of the torque are

$$
\omega = 0 \qquad \text{and} \qquad \omega = \pi,
$$

i.e., the line of apsides lies in the dominant plane of the refractive gradient (the ecliptic for the Solar System).

Physically, the vertical refractive gradient is stronger near perihelion. An orbit whose perihelion lies out of the mid-plane therefore experiences a systematically larger vertical damping force than an orbit whose perihelion lies in the mid-plane. The net effect is a continuous reduction of $|\omega|$ until the apsides coincide with the plane of strongest confinement. The same damping term simultaneously circularizes and coplanarizes the orbit; eccentricity decay, inclination decay and apsidal alignment are therefore inseparable consequences of a single velocity-dependent term in the ray equation.

### C.6 Timescale

The characteristic alignment time is

$$
\tau_{\omega} \sim \frac{c^{2} a}{v_{K}^{3}} = \frac{c^{2} a^{5/2}}{(GM_{\star})^{3/2}}.
$$

At $a \simeq 5\,\mathrm{AU}$ about a solar-mass star one obtains $\tau_{\omega} \sim 10^{9}{-}10^{10}\,\mathrm{yr}$. For extreme trans-Neptunian objects ($a \gtrsim 250\,\mathrm{AU}$) $v_{K}$ is smaller, yet the available integration time is the age of the Solar System, so the accumulated secular effect remains appreciable and produces the observed clustering in $\omega$.

### C.7 Consistency remarks

- No free parameters appear beyond the vacuum response already fixed by impedance invariance.
- Vacuum Shielding Stress remains strictly local; the energy removed by $`\mathbf{a}_{d}`$ is stored in the local stress difference $`u_{\mathrm{VSS}}`$ and is redistributed only by the causal flux $`\mathbf{S}_{\mathrm{vac}} = -\frac{1}{4\pi G}(\partial_{t}\Phi)\nabla\Phi`$.
- All accelerations carry units $\mathrm{m\,s^{-2}}$; the precession rate $\langle\dot{\omega}\rangle$ carries units $\mathrm{s^{-1}}$.

This completes the demonstration that apsidal alignment of high-semimajor-axis orbits is a direct, untuned consequence of the identical impedance-invariant damping term that produces coplanarity, circularity and Lense–Thirring precession.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---
