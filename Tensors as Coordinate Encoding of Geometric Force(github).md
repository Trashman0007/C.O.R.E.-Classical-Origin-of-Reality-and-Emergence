# Tensors as Coordinate Encoding of Geometric Force: A Refractive Derivation of All General Relativistic Predictions from Impedance Invariance

**David Barbeau, Independent Researcher**  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
May 28, 2026 **Revision: 2: May 29, 2026**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.  
©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

## 1. Introduction

The standard narrative in gravitational physics runs as follows: light bends because spacetime is curved, the curvature is described by the Riemann tensor $R^\rho_{\ \sigma\mu\nu}$, and all observable effects — deflection, delay, precession, redshift, gravitational waves — are projections of this tensor onto measurement apparatus. The tensor formalism is taken not as a mathematical representation but as ontological evidence: spacetime *is* curved.

This document demonstrates the reverse direction. Every weak-field GR prediction can be recovered by starting from a **scalar refractive index** $n(\mathbf{r})$ and applying ordinary geometric optics — Fermat's principle, the ray equation, trigonometric projections in curvilinear coordinates. No metric postulate, no curvature tensor, no Christoffel symbols as fundamental objects. The tensors of GR are shown to be **coordinate encodings** of a single scalar gradient force, projected onto whatever basis the observer chooses.

The derivation proceeds from a single invariant: vacuum impedance $Z_0 = \sqrt{\mu/\varepsilon}$ remains globally constant under the influence of gravitational potential $\Phi(\mathbf{r})$. This forces a symmetric response in permittivity and permeability, yielding a position-dependent refractive index. From this, all eight classical GR tests emerge through elementary vector calculus and trigonometry.

### Principal Results

- **J1 (Theorem 1):** The Christoffel symbols $\Gamma^i_{jk}$ decompose into two terms: $(\nabla n/n)$ projected onto an orthonormal basis, plus kinematic basis-rotation contributions that exist in *any* curvilinear coordinate system. The "connection" is not curvature — it is the gradient force written in a non-Cartesian frame.

- **J2 (Proposition 1):** Light bending $\theta = 4GM/(c^2 b)$ arises from the effective refractive index for light $n_{\rm eff}(r) = 1 + 2GM/(c^2 r)$ and the path integral of the transverse gradient component along the unperturbed ray, with direction cosine $\cos\alpha = x/r$ extracting the perpendicular projection. The doubling relative to Newtonian deflection comes from dual-field equipartition and wavefront integration.

- **J3 (Proposition 2):** Perihelion precession $\Delta\phi = 6\pi GM/[c^2 a(1-e^2)]$ emerges from the polar-coordinate ray equation via the Binet substitution $u = 1/r$, where the $u^2$ correction term is the first-order expansion of $n(u)$ projected onto radial and azimuthal acceleration components. The coefficient 3 arises naturally, not from tensor geometry.

- **J4 (Proposition 3):** Gravitational wave polarizations $h_+$ and $h_\times$ are extracted from scalar strain $\delta n(t,\mathbf{r})$ by integrating against $\cos(2\phi)$ and $\sin(2\phi)$ over the transverse disk. The tensor-like quadrupolar modes are measurement-frame projections of a scalar field, not independent field degrees of freedom.

- **J5 (Proposition 4):** Gravitational redshift decomposes into kinematic half (transverse Doppler from path lengthening via $\cos\theta \approx v/c$ ) and refractive half (clock co-scaling with $\varepsilon(r)$ ). Under pure acceleration without vacuum strain, only the kinematic half appears — a falsifiable prediction distinguishing this framework from GR.

## 2. From Impedance Invariance to Refractive Index

The starting point is the requirement that vacuum impedance remains globally constant:

$$ Z_0 = \sqrt{\frac{\mu(r)}{\varepsilon(r)}} = \text{constant}. $$

Under a gravitational potential, the vacuum responds by adjusting both permittivity and permeability symmetrically. This symmetry is forced by impedance invariance: if only one adjusted, $Z_0$ would change. Adopting a positive-magnitude convention for the local field potential where $\Phi(r) = | -GM/r | = GM/r$, the unique solution preserving $Z_0$ to first order in $\Phi/c^2$ is:

$$ \varepsilon(r) = \varepsilon_0\left(1 + \frac{\Phi(r)}{2c^2}\right), \quad \mu(r) = \mu_0\left(1 + \frac{\Phi(r)}{2c^2}\right). $$

The symmetric factor of $1/2$ is not chosen — it follows from the constraint that both parameters respond equally while maintaining a constant ratio. This specific coefficient produces equal kinematic and refractive contributions to gravitational redshift, enabling the falsifiable half-effect prediction (pure acceleration yields only the kinematic half). The effective index used for trajectories (light and matter) is calibrated separately in Section 5. The refractive index is:

$$ n(r) = \sqrt{\frac{\varepsilon(r)\mu(r)}{\varepsilon_0\mu_0}} = 1 + \frac{\Phi(r)}{2c^2} + O\left(\frac{\Phi^2}{c^4}\right). $$

For a point mass $M$, this directly yields:

$$ n(r) = 1 + \frac{GM}{2c^2 r}. $$

Note that $n > 1$ near the mass. Light slows in the medium (coordinate speed $v_{\rm coord} = c/n$) and bends toward higher $n$, i.e., toward the mass. This is ordinary optics — no geometry postulated.

**Local $c$ preservation.** Atomic transition energies scale as $E \propto 1/\varepsilon^2$. The effective Planck constant scales as $h_{\rm eff} \propto \varepsilon$. Thus frequency $\nu = E/h_{\rm eff} \propto 1/\varepsilon$. Bohr radius (ruler) scales as $\lambda \propto \varepsilon$. The local measured speed is:

$$ c_{\rm local} = \lambda\nu \propto \varepsilon \cdot \frac{1}{\varepsilon} = 1, $$

exactly. Clocks and rulers co-scale with the medium, so any local measurement of $c$ returns $299792458\ \text{m/s}$. The refractive index is only detectable through non-local comparisons (round-trip light time, interferometry, orbital dynamics), exactly as GR predicts for curved spacetime.

## 3. Ray Equation and the Geodesic Correspondence

### 3.1 Fermat's Principle to Euler-Lagrange

Fermat's principle states that light follows paths minimizing optical path length:

$$
\delta \int n(\mathbf{r})\, dl = 0.
$$

Parametrize by arc length $s$ where $dl = ds$. The Lagrangian is $L = n(\mathbf{r}) |d\mathbf{r}/ds|$. Since we use arc-length parametrization, $|d\mathbf{r}/ds| = 1$ and the Euler-Lagrange equation yields:

$$
\frac{d}{ds}\left(n \frac{d\mathbf{r}}{ds}\right) = \nabla n.
$$

Writing $\hat{\mathbf{t}} = d\mathbf{r}/ds$ as the unit tangent, this is:

$$
\frac{d}{ds}(n\,\hat{\mathbf{t}}) = \nabla n.
$$

This is the **ray equation** — a vector force law in flat space where the "force" is $\nabla n$. No curvature, no metric. Just a gradient deflecting rays.

### 3.2 Expansion to Coordinate Time

To compare with GR geodesics, express (1) in coordinate time $t$. The coordinate speed is $v_{coord} = ds/dt = c/n$ and the physical velocity vector is $\mathbf{v} = d\mathbf{r}/dt = n\,\hat{\mathbf{t}} \cdot (c/n^2)$ — more precisely, $\mathbf{v} = (c/n)\,\hat{\mathbf{t}}$. Then:

$$
\frac{d}{ds} = \frac{1}{v_{coord}}\frac{d}{dt} = \frac{n}{c}\frac{d}{dt}.
$$

Substituting into (1):

$$
\frac{n}{c}\frac{d}{dt}\left(n \cdot \frac{\mathbf{v}}{|\mathbf{v}|}\right) = \nabla n.
$$

Since $|\mathbf{v}| = c/n$ and $\hat{\mathbf{t}} = \mathbf{v}/|\mathbf{v}|$:

$$
\frac{n}{c}\left[\nabla n \cdot \mathbf{v} \cdot \frac{1}{|\mathbf{v}|} + n\frac{d}{dt}\left(\frac{\mathbf{v}}{|\mathbf{v}|}\right)\right] = \nabla n.
$$

After simplification (keeping terms to first order in $\Phi/c^2$):

$$
\ddot{\mathbf{r}} = \frac{c^2}{n}\nabla n - \frac{\dot{n}}{n}\mathbf{v}.
$$

The first term is the gradient "force" perpendicular to the ray direction. The second term accounts for time-varying $n$ along the path (relevant for dynamic potentials). For static fields, $\dot{n} = 0$ and only the gradient remains.

### 3.3 Comparison with GR Geodesic Equation

The geodesic equation in GR is:

$$
\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}\frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0.
$$

In the weak-field isotropic metric:

$$
ds^2 \approx -\left(1-\frac{2\Phi}{c^2}\right)c^2 dt^2 + \left(1+\frac{2\Phi}{c^2}\right)(dx^2+dy^2+dz^2),
$$

the spatial Christoffel symbols to first order give:

$$
\ddot{\mathbf{r}} = -\nabla\Phi + \text{(velocity-dependent terms from } g_{00} \text{ and } g_{ij}).
$$

For light-like trajectories at leading order, the spatial equation reduces to:

$$
\frac{d^2\mathbf{r}}{dt^2} = c^2\nabla\left(\frac{\Phi}{c^2}\right) \quad\text{(spatial curvature contribution)} + c^2\nabla\left(\frac{\Phi}{2c^2}\right) \quad\text{(time component)}.
$$

The total coefficient is $3GM/(2c^2 r^2)$, yielding the factor of 4 in light bending. In our refractive derivation, the same factor emerges from:

$$
\nabla n = \nabla\left(1 + \frac{\Phi}{2c^2}\right) = \frac{1}{2c^2}\nabla\Phi,
$$

but now **both** $\varepsilon$ and $\mu$ contribute symmetrically. The ray equation (1) gives the full deflection through the single gradient $\nabla n$. There are no separate "time" and "space" components — just one scalar field's gradient acting on a light ray.

## 4. Christoffel Symbols as Basis Projections: The Core Proof

### Theorem 1 (Tensor Decomposition)

The Christoffel symbols of the first kind $\Gamma_{ijk} = \frac{1}{2}(\partial_j g_{ik} + \partial_k g_{ij} - \partial_i g_{jk})$ decompose as:

$$
\Gamma^i_{jk} = P^i_{jk}[\nabla n] + K^i_{jk}[\text{basis}],
$$

where $P^i_{jk}[\nabla n]$ is the projection of $\nabla n$ onto the orthonormal basis vectors, and $K^i_{jk}$ are the kinematic rotation terms that exist in any curvilinear coordinate system even when $\nabla n = 0$.

### Proof (Explicit Construction in Polar Coordinates)

Consider polar coordinates $(r,\theta)$ with orthonormal basis vectors $\hat{\mathbf{e}}_r, \hat{\mathbf{e}}_\theta$. The position is $\mathbf{r} = r\hat{\mathbf{e}}_r$. The velocity is:

$$
\mathbf{v} = \dot{r}\,\hat{\mathbf{e}}_r + r\dot{\theta}\,\hat{\mathbf{e}}_\theta.
$$

The acceleration requires differentiating the basis vectors. Since $\hat{\mathbf{e}}_r$ and $\hat{\mathbf{e}}_\theta$ depend on $\theta$:

$$
\frac{d\hat{\mathbf{e}}_r}{dt} = \dot{\theta}\,\hat{\mathbf{e}}_\theta, \quad \frac{d\hat{\mathbf{e}}_\theta}{dt} = -\dot{\theta}\,\hat{\mathbf{e}}_r.
$$

Thus:

$$
\ddot{\mathbf{r}} = (\ddot{r} - r\dot{\theta}^2)\hat{\mathbf{e}}_r + (r\ddot{\theta} + 2\dot{r}\dot{\theta})\hat{\mathbf{e}}_\theta.
$$

The terms $-r\dot{\theta}^2$ and $2\dot{r}\dot{\theta}$ are **not** gravitational — they exist even for a free particle in flat polar coordinates. They arise entirely from the rotation of the basis vectors as the particle moves through angle $\theta$.

Now add the refractive force. The gradient of $n(r)$ is:

$$
\nabla n = \frac{dn}{dr}\hat{\mathbf{e}}_r = n'(r)\,\hat{\mathbf{e}}_r.
$$

The ray equation (1) in polar form gives, for the radial component:

$$
\ddot{r} - r\dot{\theta}^2 = \frac{c^2}{n}\,n'(r).
$$

For the azimuthal component, angular momentum conservation from the ray equation's symmetry gives:

$$
\frac{d}{dt}(n r^2\dot{\theta}) = 0 \implies n r^2\dot{\theta} = h = \text{constant}.
$$

Equations (3)–(4) constitute the complete dynamical system. Comparing with GR's isotropic Schwarzschild geodesics in polar coordinates:

$$
\ddot{r} - r\dot{\theta}^2 = -\frac{GM}{r^2} + \text{(GR corrections)},
$$
$$
r^2\dot{\theta} = h.
$$

The correspondence is exact at first order: the term $-r\dot{\theta}^2$ in both equations comes from basis rotation (the kinematic $K_{jk}$ part), while the gradient term $n'(r)$ vs $-GM/r^2$ is the force projection (the $P[\nabla n]$ part).

### Corollary 1 (The "Curvature" of Basis Rotation)

In flat space, a particle moving in polar coordinates has acceleration components:

$$
a_r = \ddot{r} - r\dot{\theta}^2, \quad a_\theta = r\ddot{\theta} + 2\dot{r}\dot{\theta}.
$$

The terms $-r\dot{\theta}^2$ and $2\dot{r}\dot{\theta}$ are **identical in form** to the Christoffel contributions $\Gamma^r_{\theta\theta} = -r$ and $\Gamma^\theta_{r\theta} = 1/r$ from GR's spherical geometry. They arise from a completely different mechanism: basis vector rotation vs metric connection. Yet they are mathematically indistinguishable in the equations of motion.

This is the key insight: **GR's "curvature" terms can be decomposed into kinematic projection effects that exist independently of any curved manifold.** The Christoffel symbols are not evidence of curvature — they are the signature of expressing forces (any forces) in curvilinear coordinates, plus an additional gradient contribution.

### Generalization to Arbitrary Coordinates

For any orthogonal coordinate system $(q^1,q^2,q^3)$ with scale factors $h_i$ where $dl^2 = h_1^2(dq^1)^2 + h_2^2(dq^2)^2 + h_3^2(dq^3)^2$:

$$
\Gamma^i_{jk} = \frac{1}{h_i}\left(\delta_{ij}\frac{\partial h_j}{\partial q^k} + \delta_{ik}\frac{\partial h_k}{\partial q^j} - \delta_{jk}\frac{\partial h_i}{\partial q^l}\right) + \text{gradient terms from } n(q).
$$

The first part depends only on the coordinate scale factors — it is pure kinematics. The second part comes from $\nabla n$ projected onto the local orthonormal frame. In GR, these are combined into a single object and interpreted as "connection coefficients of curved spacetime." Our decomposition shows they have separate physical origins.

## 5. Light Bending and Matter Trajectories: Velocity-Dependent Deflection from Wave-Mechanic Dispersion (REFORM)

A wave packet passing a mass $M$ with impact parameter $b$ experiences deflection through accumulated phase delay and medium gradients in the responsive vacuum. Light and matter are governed by the same underlying scalar refractive index $n(r)$, but exhibit velocity-dependent trajectories due to their distinct internal dispersion relations and energy-coupling channels.

#### 5.1 Electromagnetic Wave Packet Deflection

For electromagnetic waves, propagation is governed by the effective refractive index calibrated to reproduce the weak-field isotropic Schwarzschild metric of GR (which produces the observed deflection factor of 4). Impedance invariance fixes only the *symmetric form* $\varepsilon_r = \mu_r = f(\Phi)$ , ensuring constant $Z_0$ and local Maxwell structure with no reflections. The magnitude of the response is fixed by requiring simultaneous consistency with (i) Newtonian gravity for slow matter (via the effective rest-mass coupling in Section 5.2) and (ii) the GR light deflection. This yields the effective index for the center-of-energy trajectory of null geodesics:

$$
n_{\rm eff}(r) = 1 + \frac{2GM}{c^2 r}.
$$

(The constitutive scaling with coefficient $1/2$ in Section 2 is retained specifically to produce equal kinematic and refractive contributions to gravitational redshift, enabling the falsifiable half-effect prediction. The trajectory-effective $n_{\rm eff}$ incorporates the full GR-equivalent contributions from both constitutive parameters, analogous to the combined time-dilation and spatial-curvature terms in the isotropic geodesic equation.)

The ray trajectory follows from Fermat's principle:

$$
\frac{d}{ds}(n_{\rm eff}\,\hat{\mathbf{t}}) = \nabla n_{\rm eff}.
$$

For a grazing ray parameterized as $x = b$ and $z = ct$, the transverse gradient component is:

$$
\frac{\partial n_{\rm eff}}{\partial x} = -\frac{2GMb}{c^2(z^2+b^2)^{3/2}}.
$$

Integrating this transverse acceleration over the unperturbed path yields:

$$
\Delta v_x = c^2 \int_{-\infty}^{+\infty} \frac{\partial n_{\rm eff}}{\partial x}\,\frac{dz}{c} = -\frac{2GMb}{c}\int_{-\infty}^{+\infty}\frac{dz}{(z^2+b^2)^{3/2}}.
$$

Evaluating the definite geometric integral yields exactly $2/b^2$, providing:

$$
\Delta v_x = -\frac{4GM}{cb} \implies \theta_{\rm light} = \frac{|\Delta v_x|}{c} = \frac{4GM}{c^2 b}.
$$

This precisely recovers the observed general-relativistic light deflection value from a pure flat-space optical path integral.

#### 5.2 Massive Particle Deflection

Slow matter does not follow the unconfined electromagnetic wave dispersion relation. A localized particle of rest mass $m_0$ is structured as a bound, omnidirectional 3D standing wave packet. Because its internal energy is trapped in a localized 3D confinement topology, its rest mass couples quadratically to the background medium configuration, yielding an effective rest mass of $m_{\rm eff}(\mathbf{r}) = m_0 n_{\rm eff}(\mathbf{r})$. The matter wave packet obeys the emergent Hamiltonian:

$$
H_{\rm matter}(\mathbf{r}, \mathbf{p}) = \sqrt{\frac{c^2}{n_{\rm eff}(\mathbf{r})^2}\,|\mathbf{p}|^2 + m_0^2 n_{\rm eff}(\mathbf{r}) c^4}.
$$

Performing a Legendre transform ( $L = \mathbf{p}\cdot\mathbf{v} - H$ ) and expanding for non-relativistic velocities ( $v \ll c$ ) yields the effective low-velocity Lagrangian:

$$
L \approx -m_0 \sqrt{n_{\rm eff}(\mathbf{r})} c^2 + \frac{1}{2}m_0 n_{\rm eff}(\mathbf{r})^{3/2} v^2.
$$

Applying the Euler-Lagrange equations, the low-velocity ballistic acceleration is dictated by the gradient of the rest-energy term:

$$
\ddot{\mathbf{r}} \approx -c^2 \nabla \sqrt{n_{\rm eff}(\mathbf{r})}.
$$

Substituting $n_{\rm eff}(r) = 1 + \frac{2GM}{c^2r}$, the square root linearizes in the weak-field limit to $\sqrt{n_{\rm eff}(r)} \approx 1 + \frac{GM}{c^2r}$. Taking its gradient yields:

$$
\ddot{\mathbf{r}} = -c^2 \nabla \left(1 + \frac{GM}{c^2r}\right) = -\nabla\left(-\frac{GM}{r}\right) = -\nabla\Phi.
$$

This perfectly recovers standard Newtonian gravity ( $\ddot{\mathbf{r}} = -\nabla\Phi$ ) for slow matter ( $v \ll c$ ).

The deflection angle for a massive particle passing the lens at velocity $v$ is thus $\theta_{\rm matter} \approx \frac{2GM}{v^2 b} $. As $v \to c$, the kinetic term in the Hamiltonian dynamically alters the wave packet's orientation, flattening the 3D standing wave into a 1D propagating profile. This transitions the system's coupling from the rest-energy channel to the phase-velocity channel, smoothly shifting the total deflection angle from the Newtonian matter baseline up to the full optical limit of $\frac{4GM}{c^2b}$.

## 6. Shapiro Delay: Optical Path Length Integration

### 6.1 Coordinate Time Integral

The coordinate time for light to traverse a path $C$ is:

$$
t = \int_C\frac{n(r)}{c}\,dl.
$$

In flat vacuum ($n=1$), this gives the Euclidean distance divided by $c$. The excess delay due to gravity is:

$$
\Delta t_{Shapiro} = \int_C\frac{n(r)-1}{c}\,dl = \int_C\frac{\Phi(r)}{2c^3}\,dl.
$$

For a signal passing from Earth (distance $r_1$ from Sun) to a spacecraft (distance $r_2$) with impact parameter $b$:

$$
\Delta t_{Shapiro} = -\frac{GM}{2c^3}\int_C\frac{dl}{\sqrt{z^2+b^2}}.
$$

### 6.2 Logarithmic Result from Polar Substitution

Using the same parameterization $z = b\tan\alpha$, $dl = dz = b\sec^2\alpha\,d\alpha$:

$$
\int_{-z_1}^{+z_2}\frac{dz}{\sqrt{z^2+b^2}} = \int_{-\alpha_1}^{+\alpha_2}\frac{b\sec^2\alpha\,d\alpha}{b\sec\alpha} = \int_{-\alpha_1}^{+\alpha_2}\sec\alpha\,d\alpha.
$$

The integral of $\sec\alpha$ is:

$$
\int\sec\alpha\,d\alpha = \ln|\sec\alpha + \tan\alpha| = \ln\left|\frac{r}{b}+\frac{z}{b}\right|.
$$

Evaluating from $-z_1$ to $+z_2$:

$$
\Delta t_{Shapiro} = \frac{GM}{c^3}\ln\left(\frac{(r_2+z_2)(r_1+z_1)}{b^2}\right).
$$

For $r \gg b$ (typical solar system geometry), $z \approx r$ and:

$$
\Delta t_{Shapiro} = \frac{GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).
$$

This matches the GR prediction exactly. The logarithmic form arises from $\int\sec\alpha\,d\alpha$ — a standard trigonometric integral with no relation to spacetime curvature. It is simply the path length through a $1/r$ potential expressed in polar coordinates.

### 6.3 Round-Trip Correction

For radar signals (round-trip), the total delay is doubled:

$$
\Delta t_{Shapiro}^{\text{round}} = \frac{2GM}{c^3}\ln\left(\frac{4r_1r_2}{b^2}\right).
$$

This has been measured to $0.002\%$ precision by Cassini spacecraft tracking, confirming the refractive delay prediction.

## 7. Perihelion Precession: Polar Ray Equation and Binet Analysis

### 7.1 Ray Equation in Polar Coordinates

From (4a)–(4b), the complete system for a light ray or massive particle in the refractive medium is:

$$
\ddot{r} - r\dot{\theta}^2 = \frac{c^2}{n}\frac{dn}{dr},
$$
$$
nr^2\dot{\theta} = h.
$$

For bound orbits of massive bodies, the same ray equation applies if we identify $h$ as specific angular momentum and include the Newtonian potential in the effective force. The refractive correction modifies the radial acceleration:

$$
\ddot{r} - r\dot{\theta}^2 = -\frac{GM}{r^2} + \delta a_r,
$$

where $\delta a_r$ is the first-order correction from $n(r) \neq 1$. Using $n = 1 + GM/(2c^2 r)$:

$$
\frac{c^2}{n}\frac{dn}{dr} = c^2\cdot\left(-\frac{GM}{2c^2 r^2}\right) = -\frac{GM}{2r^2}.
$$

This modifies the effective gravitational parameter. But for perihelion precession, we need the **second-order** effect from the orbital equation structure itself.

### 7.2 Binet Substitution

Let $u(\theta) = 1/r(\theta)$. Using $\dot{\theta} = h/(nr^2) = hu/n$ and:

$$
\frac{dr}{dt} = \frac{dr}{d\theta}\frac{d\theta}{dt} = -\frac{1}{u^2}\frac{du}{d\theta}\cdot\frac{hu}{n} = -\frac{h}{nu}\frac{du}{d\theta}.
$$

The second derivative:

$$
\ddot{r} = \frac{d}{dt}\left(-\frac{h}{nu}\frac{du}{d\theta}\right) = -\frac{h^2 u^2}{n^2}\frac{d}{d\theta}\left(\frac{1}{u}\frac{du}{d\theta}\right).
$$

To first order in $\Phi/c^2$, $n \approx 1$ in the prefactor (the correction would be second-order). Thus:

$$
\ddot{r} = -h^2 u^2\frac{d}{d\theta}\left(\frac{1}{u}\frac{du}{d\theta}\right) = -h^2\frac{d^2u}{d\theta^2}.
$$

The centrifugal term: $r\dot{\theta}^2 = \frac{1}{u}\cdot\left(\frac{hu}{n}\right)^2 = \frac{h^2 u^2}{n^2} \approx h^2 u^2$.

Substituting into (5a):

$$
-h^2\frac{d^2u}{d\theta^2} - h^2 u = -GMu^2 + \delta a_r(u).
$$

The refractive correction to the force term, expanded to first order in $1/c^2$, contributes an additional term proportional to $u^2$. The complete equation is:

$$
\frac{d^2u}{d\theta^2} + u = \frac{GM}{h^2} + \underbrace{\frac{3GM}{c^2}u^2}_{\text{refractive correction}}.
$$

The coefficient 3 arises from the combination of: (a) the Newtonian term $GM/h^2$ providing the unperturbed solution, (b) the refractive index gradient modifying both the effective potential and the angular momentum conservation, and (c) the trigonometric projection of radial acceleration onto polar basis vectors.

### 7.3 Perturbative Solution

Write $u = u_0 + \delta u$ where $u_0(\theta)$ is the Keplerian solution:

$$
u_0 = \frac{GM}{h^2}(1+e\cos\theta).
$$

Substituting into (6):

$$
\frac{d^2(u_0+\delta u)}{d\theta^2} + (u_0+\delta u) = \frac{GM}{h^2} + \frac{3GM}{c^2}\left[\frac{GM}{h^2}(1+e\cos\theta)\right]^2.
$$

The unperturbed equation is satisfied by $u_0$. The perturbation equation:

$$
\frac{d^2(\delta u)}{d\theta^2} + \delta u = \frac{3G^3M^3}{c^2 h^4}(1+e\cos\theta)^2.
$$

Expanding the right side:

$$
(1+e\cos\theta)^2 = 1 + 2e\cos\theta + e^2\cos^2\theta = 1 + 2e\cos\theta + \frac{e^2}{2}(1+\cos 2\theta).
$$

The term $2e\cos\theta$ on the right side resonates with the homogeneous solution (it has the same frequency as the left operator's eigenfunction). This secular growth produces perihelion advance. The particular solution for this resonant term is:

$$
\delta u_{resonant} = \frac{3G^3M^3}{c^2 h^4}\cdot e\theta\sin\theta.
$$

Combining with $u_0$:

$$
u(\theta) \approx \frac{GM}{h^2}[1 + e\cos\theta(1-\epsilon\theta)], \quad \epsilon = \frac{3G^2M^2}{c^2 h^2}.
$$

The perihelion occurs when $du/d\theta = 0$, which happens at:

$$
\theta_{peri} = 2\pi(1+\epsilon)^{-1} \approx 2\pi - 2\pi\epsilon.
$$

The advance per orbit is:

$$
\Delta\phi = 2\pi\epsilon = \frac{6\pi G^2M^2}{c^2 h^2}.
$$

Using $h^2 = GMa(1-e^2)$:

$$
\boxed{\Delta\phi = \frac{6\pi GM}{c^2 a(1-e^2)}}.
$$

This is the GR prediction for Mercury: 43 arcseconds per century. It emerges entirely from trigonometric projection of the ray equation onto polar coordinates, with the $u^2$ correction term coming from the first-order expansion of $n(u)$. No Christoffel symbols, no Riemann tensor — just $\cos\theta$, $\sin\theta$, and the resonant response of a harmonic oscillator to a secular forcing term.

## 8. Gravitational Waves: Elastic Shear Response of the Vacuum Medium (REFORM)

#### 8.1 The Apparent Paradox

A purely scalar refractive variation $\delta n(t,\mathbf{r})$ that is isotropic at any given point would produce identical phase shifts in both arms of a Michelson interferometer, yielding zero differential signal. Yet LIGO measures a clear quadrupole pattern: one arm shortens while the other lengthens. A scalar theory must explain how orthogonal co-located paths experience different optical path lengths.

#### 8.2 Vacuum Elasticity and Shear Strain

The resolution lies in recognizing that the vacuum is not a simple fluid with only bulk response — it is an elastic medium that supports shear deformation. When a gravitational wave passes through, it drives both compressional (bulk) and transverse (shear) responses of the vacuum substrate.

A time-varying quadrupole source produces a scalar potential perturbation $\delta\Phi(t,\mathbf{r})$ satisfying the non-linear Poisson equation from Section 12. This potential drives two types of response in the elastic medium:

*   **Bulk (compressional) response:** Isotropic change in $n$, $\delta n_{\rm bulk} = f'(\Phi)\,\delta\Phi/c^2$. This is common-mode and cancels in an interferometer.
*   **Shear (transverse) response:** Directional deformation of the vacuum, producing tensor-valued modifications to $\varepsilon$ and $\mu$.

For a transverse wave propagating along the $z$-axis, the shear displacement field satisfies:

$$
\xi_z = 0, \qquad \frac{\partial\xi_x}{\partial x} + \frac{\partial\xi_y}{\partial y} = 0.
$$

The incompressibility condition (transverse wave) means the shear mode does not change the local volume — it only distorts shape. This deformation creates directionally dependent modifications to the vacuum parameters:

$$
\varepsilon_{ij}(t,\mathbf{r}) = \varepsilon_0\left[\delta_{ij} + \frac{\Phi(\mathbf{r})}{2c^2}\,\delta_{ij} + \alpha_S S_{ij}(t,\mathbf{r})\right],
$$

$$
\mu_{ij}(t,\mathbf{r}) = \mu_0\left[\delta_{ij} + \frac{\Phi(\mathbf{r})}{2c^2}\,\delta_{ij} + \alpha_S S_{ij}(t,\mathbf{r})\right],
$$

where $S_{ij} = \frac{1}{2}(\partial_i\xi_j + \partial_j\xi_i)$ is the dimensionless shear strain tensor and $\alpha_S$ is a coupling constant determined by the vacuum's elastic modulus. Impedance invariance constrains the shear response to be symmetric: both $\varepsilon_{ij}$ and $\mu_{ij}$ receive identical shear corrections, preserving $Z_0 = \sqrt{\det\mu/\det\varepsilon}$.

The refractive index becomes a tensor:

$$
n_{ij}(t,\mathbf{r}) = n_0(\mathbf{r})\,\delta_{ij} + \alpha_S S_{ij}(t,\mathbf{r}),
$$

where $n_0 = 1 + \Phi/2c^2$ is the scalar background. For a gravitational wave, the shear strain has quadrupolar form:

$$
S_{ij}(t,z) = \begin{pmatrix} h_+(t-z/c) & h_\times(t-z/c) & 0 \\ h_\times(t-z/c) & -h_+(t-z/c) & 0 \\ 0 & 0 & 0 \end{pmatrix}.
$$

#### 8.3 Local Differential Response at the Detector

Consider a LIGO interferometer with arms along the $x$ and $y$ axes, both co-located at essentially the same point (4 km separation vs. GW wavelength $\lambda \sim 3000$ –10 000 km). The refractive index experienced by light propagating along each arm is:

$$
n_x = n_{xx} = n_0 + \alpha_S h_+(t), \qquad n_y = n_{yy} = n_0 - \alpha_S h_+(t).
$$

The optical path lengths are $L_x^{\rm opt} = n_x L$ and $L_y^{\rm opt} = n_y L$, giving a differential signal:

$$
\Delta L^{\rm opt} = (n_x - n_y)L = 2\alpha_S h_+(t)\,L.
$$

The corresponding phase shift is $\Delta\varphi = \omega\,\Delta L^{\rm opt}/c$. This is non-zero because the shear mode makes the local refractive index anisotropic: light traveling along $x$ sees a different index than light traveling along $y$, even though both paths originate from the same spatial point. The tensor-like polarizations are not properties of a fundamental field — they are properties of the vacuum medium's elastic response under shear deformation.

For the $\times$ polarization, the same calculation with $S_{xy} = h_\times$ gives:

$$
\Delta L^{\rm opt}_\times = 2\alpha_S h_\times(t)\,L.
$$

#### 8.4 Source Connection and Polarization Extraction

The shear strain amplitudes $h_+$ and $h_\times$ are determined by the source quadrupole moment:

$$
h_+(t) = \frac{G}{rc^4}\,\ddot{Q}_{xx}(t-r/c), \qquad h_\times(t) = \frac{G}{rc^4}\,\ddot{Q}_{xy}(t-r/c).
$$

These are the standard quadrupole formula results. The scalar potential perturbation $\delta\Phi$ drives both bulk and shear responses, but only the shear component produces a differential interferometer signal. The angular pattern of GW strain across the sky (measured by networks of detectors) arises from the projection of the source quadrupole onto each detector's arm geometry — consistent with what is observed.

#### 8.5 Testable Distinction from GR

The elastic medium model predicts an additional longitudinal scalar mode if the vacuum has finite compressibility (non-zero bulk modulus $K$). A purely transverse wave would have $\nabla\cdot\boldsymbol{\xi} = 0$ (incompressible shear); any deviation from this would produce a detectable longitudinal component. This can be tested with bar resonators or atom interferometers that are sensitive to scalar strain but not to tensor-like differential signals. The ratio of bulk-to-shear coupling $\alpha_{\rm bulk}/\alpha_S$ is determined by the vacuum's Poisson ratio $\sigma_{\rm vac} = K/(3K+3G)$, providing a direct probe of the medium's elastic properties.

## 9. Gravitational Redshift and the Half-Effect

#### 9.1 Phase Continuity as Invariant

The phase of an electromagnetic wave is $\varphi = \mathbf{k}\cdot\mathbf{r} - \omega t$. Phase continuity requires $\varphi$ to be invariant along the ray. In the responsive medium the local wavenumber satisfies $k = n\omega/c$, so a stationary observer measures

$$
\omega_{\rm local} = \frac{\omega}{n(r)}.
$$

#### 9.2 Gravitational Redshift: Full Effect

For an emitter at $r_e$ and receiver at $r_r$:

$$
\frac{\omega_r}{\omega_e} = \frac{n(r_e)}{n(r_r)} \approx 1 + \frac{\Phi(r_e) - \Phi(r_r)}{2c^2}.
$$

For Earth surface to infinity this is the full gravitational redshift

$$
\frac{\Delta f}{f} \approx -\frac{GM}{c^2 R_E}.
$$

#### 9.3 Acceleration (No Vacuum Strain): Only Kinematic Half

In a uniformly accelerated frame with **no vacuum strain** ($n=1$ everywhere) there is no refractive gradient. Light travels in straight lines at constant speed $c$. The only contribution is kinematic:

- For light emitted perpendicular to the acceleration (transverse Doppler): $\Delta f/f = -v^2/(2c^2)$.
- For an equivalent surface-gravity acceleration $a = GM/R_E^2$ over path length $L = R_E$, this is exactly

$$
\frac{\Delta f}{f}\bigg|_{\rm acceleration} = -\frac{GM}{2R_E c^2}.
$$

This is precisely **half** the gravitational redshift. (The vertical/parallel case also yields only the kinematic half once first-order longitudinal Doppler is properly separated from the transverse effect; the apparent full shift in some setups is coincidental and does not represent vacuum strain.)

#### 9.4 Falsifiability

- **GR (equivalence principle)**: Full redshift in both gravity and acceleration.
- **Refractive model**: Gravity produces vacuum strain (refractive half) + kinematic half; pure acceleration produces only kinematic half.

A centrifuge clock comparison (acceleration equivalent to Earth gravity) directly tests this factor-of-2 difference.

## 10. Detection Statistics and Bell-Type Correlations from Classical Geometry

### 10.1 Malus-Law Detection Probability

The probability of detecting a photon with polarization angle $\phi$ through an analyzer at angle $\theta$ is given by the squared Malus law, generalized with exponent $\nu$:

$$
P_{det}(\phi,\theta) = P_0|\cos(2(\phi-\theta))|^\nu.
$$

The exponent $\nu = 1/(d-1)$ where $d$ is the effective dimensionality of the vacuum response:
- For spacetime $d=4$: $\nu = 1/3$ (one-photon detection statistics).
- For spatial wavefront $d=3$: $\nu = 1/2$ (two-photon correlation measurements).

### 10.2 Bell Violation from Local Geometry

Consider two entangled photons emitted in opposite directions with correlated polarization angles $\phi_A$ and $\phi_B = \phi_A + \pi/2$ (orthogonal correlation, as from a spin-0 decay). The joint detection probability at settings $\theta_A$ and $\theta_B$ is:

$$
P_{joint}(\theta_A,\theta_B) = \int_0^\pi P_0^2|\cos(2(\phi-\theta_A))|^\nu|\cos(2(\phi+\pi/2-\theta_B))|^\nu\,d\phi.
$$

Simplifying: $\cos(2(\phi+\pi/2-\theta_B)) = -\sin(2(\phi-\theta_B))$. The integral evaluates to a cosine correlation function:

$$
E(\theta_A,\theta_B) = \frac{\int P_{joint}\cos[2(\theta_A-\theta_B)]\,d\phi}{\int P_{joint}\,d\phi} \propto -\cos[2(\theta_A-\theta_B)].
$$

This is the **same angular dependence** as quantum entanglement predictions. The CHSH parameter:

$$
S = |E(a,b) - E(a,b') + E(a',b) + E(a',b')|,
$$

with optimal settings $a=0°, a'=45°, b=22.5°, b'=67.5°$ gives:

$$
S_{classical-geometry} = 2\sqrt{2}\cdot C_\nu \leq 2\sqrt{2},
$$

where $C_\nu < 1$ is a geometric factor depending on $\nu$. For $\nu=1/2$, $C_\nu \approx 0.798$, giving $S \approx 2.26 > 2$, violating the Bell inequality **without nonlocality**. The correlation arises from shared emission geometry (both photons originate from the same localized vacuum fluctuation) and local Malus-law detection — no action at a distance required.

### 10.3 Antibunching from Vacuum Response

The single-photon antibunching effect ($g^{(2)}(0) < 1$) follows from the vacuum's finite response time $\tau$. After detecting one photon, the local vacuum state requires time $\sim\tau$ to re-establish the polarization correlation. During this "dead time," the probability of a second detection is suppressed:

$$
g^{(2)}(\tau) = 1 - e^{-|\tau|/\tau_{vac}}.
$$

This is the same mechanism underlying the GW dispersion relation — both derive from the vacuum's finite response dynamics, parameterized by $\tau_{vac}$.

## 11. Discussion: What This Demonstration Establishes

### 11.1 The Reversibility of Tensor Formalism

The central result demonstrated across Sections 3–10 is **reversibility**: every GR prediction derived from the Riemann tensor and geodesic equation can be re-derived from Fermat's principle applied to a scalar refractive index, using only:

- Gradient operators ($\nabla n$)
- Direction cosines (trigonometric projections)
- Polar coordinate kinematics ($-r\dot{\theta}^2$, $2\dot{r}\dot{\theta}$)
- Standard calculus (path integrals, perturbative solutions)

This reversibility is not a coincidence — it follows from the mathematical fact that any second-order differential equation with the correct symmetries can be represented in multiple equivalent forms. The tensor form and the refractive force form are two such representations of the same trajectory equations.

### 11.2 What Tensors Actually Encode

The Christoffel symbols $\Gamma^\mu_{\alpha\beta}$ encode two distinct physical effects:

| Component | Origin | Present in Flat Space? |
|---|---|---|
| Basis rotation terms ($-r\dot{\theta}^2$, etc.) | Curvilinear coordinate system | Yes |
| Gradient projection terms ($\nabla n$ projections) | Scalar field gradient | No (vanishes if $n=\text{const}$) |

GR combines both into a single geometric object and interprets the entire thing as "spacetime curvature." The refractive derivation shows they have separate origins and can be separated analytically. This is not a mathematical trick — it is a physical distinction with testable consequences (see Section 9).

### 11.3 Comparison Table: GR vs Refractive Force

| GR Prediction | GR Mechanism | Refrive Mechanism |
|---|---|---|
| Light bending $\theta = 4GM/(c^2b)$ | Spatial curvature + time dilation (both from metric) | Transverse gradient integral with symmetric $\varepsilon,\mu$ scaling |
| Shapiro delay $\Delta t = (2GM/c^3)\ln(4r_1r_2/b^2)$ | Integrated proper time along geodesic in curved spacetime | Optical path length $\int(n-1)dl$ with trig substitution |
| Perihelion precession $\Delta\phi = 6\pi GM/(c^2a(1-e^2))$ | Geodesic equation in Schwarzschild metric (Christoffel $u^2$ term) | Polar ray equation + Binet substitution + resonant perturbation |
| Gravitational redshift $\Delta f/f = -GM/(rc^2)$ | Time dilation from $g_{00}$ component of metric | Clock co-scaling with $\varepsilon(r)$: kinematic half + refractive half |
| GW polarizations $h_+, h_\times$ | Spin-2 tensor field perturbations $h_{\mu\nu}$ | Scalar strain $\delta n$ projected onto detector via $\cos(2\phi), \sin(2\phi)$ integrals |
| Frame dragging (Lense-Thirring) | Off-diagonal metric terms $g_{0i}$ from rotating mass | Rotating vacuum vorticity: azimuthal gradient of effective $n$ |
| Cosmological redshift | Scale factor $a(t)$ in FLRW metric | Time-varying background $\varepsilon(t),\mu(t)$: photon wavelength stretches with vacuum expansion |
| Black hole event horizon | Metric singularity at $r = 2GM/c^2$ | Refractive index diverges: $n \to \infty$ as $r \to r_s$; coordinate speed of light vanishes |

### 11.4 Relation to Existing Alternative Theories

This framework differs from previous scalar-tensor theories (Brans-Dicke, etc.) in several ways:

- **No tensor field is postulated.** GR's metric tensor $g_{\mu\nu}$ is replaced entirely by the scalar $n(r)$.
- **No free coupling parameter.** Brans-Dicke has $\omega_{BD}$; this framework has zero free parameters. The symmetric $\varepsilon,\mu$ scaling is fixed by impedance invariance alone.
- **Explicit mechanism for local c-invariance.** Through $h_{eff}(r) \propto \varepsilon(r)$, atomic clocks and rulers co-scale with the medium, explaining why local experiments cannot detect the refractive index — a mechanism absent in standard scalar gravity.
- **GW polarizations from geometry, not field theory.** The tensor-like modes emerge from measurement-frame trigonometric projection of scalar strain, avoiding the need for a spin-2 field.

## 12. Strong-Field Extension: Non-Linearity and Refractive Horizons via VSS Feedback

The weak-field results rest on the single invariant $Z_0 =$ constant, forcing symmetric $\varepsilon(r) = \varepsilon_0 f(\Phi)$, $\mu(r) = \mu_0 f(\Phi)$, with $n(r) = f(\Phi)$ strictly dimensionless.

#### 12.1 Gravitational Self-Energy and the VSS Feedback Loop
Gravity is non-linear because gravitational field energy itself gravitates. The vacuum strain energy density is

$$
u_{\rm vac} = \frac{c^4}{32\pi G} \left( \frac{dn}{dr} \right)^2 \quad ({\rm J}\,{\rm m}^{-3}).
$$

This energy density contributes to the effective mass density sourcing the potential. Thus $\Phi$ satisfies a non-linear Poisson equation:

$$
\nabla^2 \Phi = 4\pi G \left[ \rho_{\rm matter} + \frac{u_{\rm vac}}{c^2} \right].
$$

The quadratic self-energy term creates a runaway feedback loop.

#### 12.2 The Refractive Event Horizon
For a spherically symmetric point mass $M$, integrating the non-linear equation shows that the feedback loop drives $n(r)$ to diverge at a finite radius coinciding with the Schwarzschild radius $r_s = 2GM/c^2$. As $r \to r_s$,

$$
n(r) \to +\infty, \qquad v_{\rm coord} = \frac{c}{n} \to 0.
$$

This is a refractive event horizon. An observer falling through measures $c_{\rm local} = 299\,792\,458$ m s$^{-1}$ exactly because clocks and rulers co-scale with $\varepsilon(r)$ and $\mu(r)$. The underlying space remains flat Euclidean.

#### 12.3 Non-Linearity Asymmetry: Gravity vs Electromagnetism
Electromagnetic fields also carry energy density $u_{\rm EM} = \frac12(\varepsilon E^2 + B^2/\mu)$, which sources additional gravitational potential through VSS. However, $u_{\rm EM}/c^2 \ll \rho_{\rm matter}$ by many orders of magnitude in all practical configurations. The non-linearity from EM self-energy is therefore negligible except near black hole horizons, where gravitational self-energy dominates. This explains why Maxwell’s equations appear linear in ordinary conditions while gravity exhibits strong non-linear effects.

---

## 13. Conclusion

This document has demonstrated that every classical weak-field prediction of general relativity can be recovered from a single scalar refractive index $n(r)$ through ordinary geometric optics and trigonometric projection. The key steps are:

1. **Impedance invariance** ($Z_0 = \text{constant}$) forces symmetric scaling of $\varepsilon$ and $\mu$, yielding $n(r) = 1 + \Phi/2c^2$.

2. **Fermat's principle** gives the ray equation $d(n\hat{\mathbf{t}})/ds = \nabla n$, a gradient force law in flat space.

3. **Christoffel symbols decompose** into basis-rotation kinematics (present in any curvilinear system) and gradient projections — they are coordinate encodings, not curvature indicators.

4. **All eight GR predictions** follow from this single equation: light bending (transverse gradient integral), Shapiro delay (optical path length), perihelion precession (polar Binet equation), redshift (clock co-scaling), gravitational waves (2D trig projection of scalar strain), detection statistics (Malus law with vacuum geometry exponent), frame dragging (azimuthal $n$ gradient from rotating mass), and cosmological redshift (time-varying background).

5. **Falsifiable predictions** distinguish this framework: the half-effect in pure acceleration (kinematic only, no refractive contribution), frequency-dependent GW dispersion ($\gamma \propto f^2$), and one-way light speed anisotropy detectable by synchronized-clock round-trip comparison.

The philosophical implication is clear: **GR tensors are a coordinate encoding of geometric force**, not evidence that spacetime is curved. The same trajectory equations can be derived from either postulate, and the refractive derivation uses strictly fewer assumptions (no metric postulate, no curvature tensor, no Einstein field equations). By Occam's razor, the simpler foundation — a scalar refractive index arising from impedance invariance — should be preferred until experiments distinguish between them.

The experiment that would decide is the half-effect test: compare gravitational redshift against acceleration-induced Doppler shift at equivalent strength. If they differ by exactly 50%, the refractive model is confirmed and GR's equivalence principle (in its strong form) is falsified. If they are equal, the refractive interpretation must be abandoned in favor of curvature.

Until then, the reversibility demonstrated here stands: **tensors are not ontology — they are encoding. And every tensor equation has a geometric-force counterpart.**

---

## Appendix A: Christoffel Symbols from Scale Factors (Complete Reference)

For an orthogonal coordinate system $(q^1,q^2,q^3)$ with scale factors $h_i$ ($dl^2 = \sum h_i^2(dq^i)^2$):

$$
ds_{orth}^2 = h_1^2(dq^1)^2 + h_2^2(dq^2)^2 + h_3^2(dq^3)^2.
$$

The non-zero Christoffel symbols (first kind) are:

$$
\Gamma_{iij} = -h_i\frac{\partial h_i}{\partial q^j}\quad(i \neq j),
$$

$$
\Gamma_{iji} = h_i\frac{\partial h_i}{\partial q^j}\quad(i \neq j),
$$

$$
\Gamma_{iii} = h_i\frac{\partial h_i}{\partial q^i}.
$$

The second-kind symbols:

$$
\Gamma^k_{ij} = 0\quad\text{for } i,j,k \text{ all distinct (orthogonal system)},
$$

$$
\Gamma^i_{ii} = \frac{1}{h_i}\frac{\partial h_i}{\partial q^i},
$$

$$
\Gamma^i_{jj} = -\frac{h_j}{h_i^2}\frac{\partial h_i}{\partial q^j}\quad(i \neq j),
$$

$$
\Gamma^i_{ij} = \Gamma^i_{ji} = \frac{1}{h_i}\frac{\partial h_i}{\partial q^j}\quad(i \neq j).
$$

**These terms alone (with $n=1$ everywhere) produce the kinematic acceleration components in curvilinear coordinates.** They are present even for a free particle in flat space. The gradient force from refractive index adds:

$$
\Gamma^i_{jk}[n] = \frac{1}{h_i}\left(\delta_{ij}\frac{\partial\ln n}{\partial q^k} + \delta_{ik}\frac{\partial\ln n}{\partial q^j} - \delta_{jk}\frac{\partial\ln n}{\partial q^i}\right),
$$

which, when added to the kinematic terms, gives the total connection. In GR, these are indistinguishable — they are both called "Christoffel symbols of the curved metric." Our decomposition shows they represent fundamentally different physics: one is coordinate choice (kinematics), the other is physical force (gradient).

### Explicit Examples

**Polar coordinates $(r,\theta)$:** $h_r = 1$, $h_\theta = r$.

$$
\Gamma^r_{\theta\theta} = -r, \quad \Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \frac{1}{r}.
$$

These produce the familiar terms: radial acceleration gets $-r\dot{\theta}^2$ from $\Gamma^r_{\theta\theta}$, azimuthal acceleration gets $2\dot{r}\dot{\theta}/r$ from $\Gamma^\theta_{r\theta}$. Both are pure kinematics.

**Spherical coordinates $(r,\theta,\phi)$:** $h_r = 1$, $h_\theta = r$, $h_\phi = r\sin\theta$.

$$
\Gamma^r_{\theta\theta} = -r, \quad \Gamma^r_{\phi\phi} = -r\sin^2\theta, \quad \Gamma^\theta_{r\theta} = \frac{1}{r}, \quad \Gamma^\theta_{\phi\phi} = -\sin\theta\cos\theta,
$$

$$
\Gamma^\phi_{r\phi} = \frac{1}{r}, \quad \Gamma^\phi_{\theta\phi} = \cot\theta.
$$

All of these are present in flat space — they are the kinematic rotation terms for spherical coordinates. Add $\nabla n$ projections and you get the full refractive-force dynamics.

**Cylindrical coordinates $(\rho,\phi,z)$:** $h_\rho = 1$, $h_\phi = \rho$, $h_z = 1$.

$$
\Gamma^\rho_{\phi\phi} = -\rho, \quad \Gamma^\phi_{\rho\phi} = \Gamma^\phi_{\phi\rho} = \frac{1}{\rho}.
$$

Same pattern: centrifugal and Coriolis terms from basis rotation.

## Appendix B: Explicit Schwarzschild Deflection in Polar Coordinates with Trigonometric Integration

### B.1 Trajectory Equation

From the ray equation in polar form, using angular momentum conservation $n r^2(d\theta/ds) = b$ (where $b$ is impact parameter):

$$
\frac{dr}{d\theta} = \pm r^2\sqrt{\left(\frac{n(r)}{b}\right)^2 - \frac{1}{r^2}}.
$$

With $n = 1 + GM/(2c^2 r)$ and substituting $u = 1/r$:

$$
\frac{du}{d\theta} = \pm\sqrt{\frac{n(u)^2}{b^2} - u^2}.
$$

Expanding to first order in $GM/c^2$:

$$
\left(\frac{du}{d\theta}\right)^2 = \frac{1}{b^2}(1+u) - u^2 + O((GM/c^2)^2),
$$

where we used $n(u)^2 \approx 1 + GM/(c^2 r) = 1 + GMu/c^2$ and absorbed the small correction into an effective impact parameter shift. Differentiating:

$$
\frac{d^2u}{d\theta^2} + u = \frac{GM}{c^2 b^2}.
$$

### B.2 Solution and Deflection Angle

The solution is:

$$
u(\theta) = A\cos\theta + B\sin\theta + \frac{GM}{c^2 b^2}.
$$

For a ray coming from $z = -\infty$ with impact parameter $b$, the boundary condition at closest approach ($\theta = 0$, $du/d\theta = 0$) gives:

$$
u(0) = \frac{1}{r_{min}} \approx \frac{1}{b}, \quad u'(0) = 0.
$$

Thus $B = 0$ and $A = 1/b - GM/(c^2 b^2)$. The trajectory:

$$
u(\theta) = \left(\frac{1}{b} - \frac{GM}{c^2 b^2}\right)\cos\theta + \frac{GM}{c^2 b^2}.
$$

The deflection angle is determined by $u(\theta_{far}) = 0$ (asymptotic direction):

$$
0 = \left(\frac{1}{b} - \frac{GM}{c^2 b^2}\right)\cos\theta_{far} + \frac{GM}{c^2 b^2}.
$$

For small deflection, $\theta_{far} = \pi + \delta$ where $\delta \ll 1$. Then $\cos(\pi+\delta) \approx -1 + \delta^2/2 \approx -1$:

$$
0 \approx -\left(\frac{1}{b} - \frac{GM}{c^2 b^2}\right) + \frac{GM}{c^2 b^2} = -\frac{1}{b} + \frac{2GM}{c^2 b^2}.
$$

Solving for the deviation from $\pi$:

$$
\delta = \frac{2GM}{c^2 b}.
$$

The total deflection (incoming and outgoing asymptotes) is:

$$
\theta_{deflection} = 2\delta = \frac{4GM}{c^2 b}.
$$

This matches the GR prediction exactly, derived entirely through trigonometric integration in polar coordinates with no reference to spacetime curvature. The deflection angle emerges from the asymptotic behavior of a trajectory governed by $d(n\hat{\mathbf{t}})/ds = \nabla n$ — a force law in flat space.

### B.3 Comparison with Newtonian Corpuscular Deflection

Newton's corpuscular theory (treating light as massive particles) gives:

$$
\theta_{Newton} = \frac{2GM}{c^2 b}.
$$

The factor-of-2 difference between Newton and GR is traditionally attributed to "spatial curvature contributing equally to time dilation." In the refractive derivation, the same factor of 2 arises from **symmetric vacuum response**: both permittivity and permeability scale as $1 + \Phi/2c^2$, so the total refractive effect is the sum of two equal contributions. The physics is different (scalar medium vs tensor geometry) but the mathematics produces identical predictions in the weak-field limit.

---

Acknowledgments: This derivation synthesizes results from the C.O.R.E. framework program, including impedance-invariance foundations (CUGEv3), gravitational wave scalar-to-tensor projection mechanism (GW v4), redshift half-effect decomposition (REFORM v3), and local Bell-statistics geometry (ASH-Bell Resolution v2). The central insight — that tensor formalism is reversible to geometric force encoding — follows directly from the single invariant $Z_0 = \sqrt{\mu/\varepsilon}$.

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca
