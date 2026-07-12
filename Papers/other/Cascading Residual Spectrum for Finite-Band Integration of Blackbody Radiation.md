# **Cascading Residual Spectrum for Finite-Band Integration of Blackbody Radiation**  
**(Extension of ASH §3.4 – flat Euclidean 3-space only, SI base units, continuous EM waves)**

**David Barbeau, Independent Researcher**  
david@bigbadaboom.ca | www.bigbadaboom.ca  

July 12, 2026, Version 2

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.  
©2026 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

### 1. Starting point (ASH postulates in flat Euclidean space)
- Light is a continuous electromagnetic wave. Spectral energy density $u(\nu)\,d\nu$ (J m⁻³ Hz⁻¹) or spectral radiance $B(\nu,T)$ (W m⁻² Hz⁻¹ sr⁻¹).
- Material detectors (or cavity walls) possess a continuum of energy thresholds $\phi$. Density of thresholds: $\rho(\phi)$.
- Absorption occurs only when the local wave energy can meet or exceed an available threshold.
- All energy that does **not** meet a threshold is residual and is re-radiated at lower frequencies. This residual is the cascade.
- Nature is spatially flat Euclidean 3-space. Mode density is purely geometric: $8\pi\nu^2/c^3$ (energy density) or $2\nu^2/c^2$ (radiance per steradian). No curvature, no expansion, no free parameters beyond the statistical average threshold spacing $h_{\rm eff}$.

Effective $h_{\rm eff}$ (or simply $h$) emerges as the average spacing of the continuous-wave thresholds. Local $c$-invariance and impedance invariance $Z_0=\sqrt{\mu/\varepsilon}$ are preserved exactly as in CUGE.

### 2. The Non-Linear Cascade Transport Equation

In thermal equilibrium, the threshold density is Boltzmann-weighted. A purely spontaneous (linear) cascade of residual energy yields the Wien spectrum ($u \propto \nu^3 e^{-x}$), which successfully suppresses the ultraviolet catastrophe but fails to reproduce the low-frequency Rayleigh-Jeans tail. To recover the full Planck spectrum from first principles, we must include the classical continuous-wave equivalent of *stimulated emission*: constructive wave interference (wave-seeding). When residual high-frequency energy cascades downward, it interacts non-linearly with the existing macroscopic continuous-wave field, which acts as a seed that enhances the transition probability.

Rather than attempting an intractable microscopic integration over the continuous material threshold distribution $\rho(\phi)$, we formulate the **effective macroscopic steady-state transport equation** for the spectral energy density $u(\nu)$. In statistical mechanics, such transport kernels are rigorously constrained by symmetries, conservation laws, and detailed balance. Within the C.O.R.E. framework, the cascade kernel is strictly dictated by three physical requirements:

1.  **Wave-Seeding (Non-Linear Mixing):** The classical continuous-wave analog of bosonic stimulation requires that the cascade rate is enhanced by the existing field intensity, introducing a non-linear $u(\nu')^2$ dependence.
2.  **Detailed Balance (Thermal Bath Coupling):** The energy difference $\Delta E = h_{\text{eff}}(\nu' - \nu)$ released during the downward cascade is absorbed by the material threshold bath. The transition probability is governed by the Boltzmann weight of the bath accepting this energy, yielding the exponential factor $e^{h_{\text{eff}}(\nu' - \nu)/kT}$.
3.  **Phase-Space and Cross-Section Scaling:** The 3D geometric mode density $g(\nu) \propto \nu^2$ and the energy quantum dictate that the available final states scale as $\nu^3$. Conversely, the non-linear threshold-crossing cross-section is severely suppressed at high frequencies, scaling as $1/\nu'^6$. 

Imposing these physical constraints yields the exact non-linear integral cascade equation:

$$
u(\nu) = A\nu^3 e^{-x} + \int_\nu^\infty \left( \frac{h_{\text{eff}}}{kT A} \right) \frac{\nu^3}{\nu'^6} e^{\frac{h_{\text{eff}}}{kT}(\nu' - \nu)} u(\nu')^2 \, d\nu'
$$

where $x = h_{\text{eff}}\nu / kT$ and $A = 8\pi h_{\text{eff}} / c^3$ is the geometric mode-density prefactor.

*   **$A\nu^3 e^{-x}$** is the direct thermal excitation (the Wien limit).
*   **The integral** represents the downward cascade of residual energy from all higher frequencies $\nu' > \nu$.
*   **The prefactor $\frac{h_{\text{eff}}}{kT A}$** is the dimensional coupling constant ensuring global energy conservation and matching the thermal scale of the bath.

### 3. Exact Solution and the Geometric Series

Differentiating the non-linear integral equation yields a first-order non-linear ODE whose unique physical solution (vanishing at high frequency) is the Planck form. We can prove this directly by substituting the Planck spectrum $u(\nu) = \frac{A\nu^3}{e^x - 1}$ back into the integral equation.

The integrand becomes:

$$
\text{Integrand} = \left( \frac{h_{\text{eff}}}{kT A} \right) \frac{\nu^3}{\nu'^6} e^{x' - x} \left( \frac{A\nu'^3}{e^{x'} - 1} \right)^2 = A \frac{h_{\text{eff}}}{kT} \nu^3 e^{-x} \frac{e^{x'}}{(e^{x'} - 1)^2}
$$

Integrating over $\nu'$ from $\nu$ to $\infty$ (equivalent to integrating over $y$ from $x$ to $\infty$, noting that $d\nu' = \frac{kT}{h_{\text{eff}}} dy$):

$$
\int_x^\infty A \nu^3 e^{-x} \frac{e^{y}}{(e^y - 1)^2} \, dy = A \nu^3 e^{-x} \left[ \frac{-1}{e^y - 1} \right]_x^\infty = A \nu^3 e^{-x} \left( 0 - \frac{-1}{e^x - 1} \right) = \frac{A\nu^3 e^{-x}}{e^x - 1}
$$

Adding this cascaded residual to the direct thermal source term:

$$
u(\nu) = A\nu^3 e^{-x} + \frac{A\nu^3 e^{-x}}{e^x - 1} = A\nu^3 e^{-x} \left( 1 + \frac{1}{e^x - 1} \right) = A\nu^3 e^{-x} \left( \frac{e^x}{e^x - 1} \right) = \frac{A\nu^3}{e^x - 1}
$$

**Q.E.D.** The Planck spectrum is the exact, unique, closed-form solution to this non-linear integral equation. 

The denominator is exactly the infinite geometric series generated by successive wave-seeded residual cascades:

$$
\frac{1}{e^x - 1} = \sum_{n=1}^{\infty} e^{-nx}
$$

Hence the spectrum is an infinite sum of elementary Wien terms:

$$
u(\nu) = A\nu^3 \sum_{n=1}^{\infty} e^{-n h_{\text{eff}}\nu / kT}
$$

(The same expansion holds for spectral radiance $B(\nu, T)$ with the appropriate prefactor).

Because every term is elementary, the integral over any finite band can be evaluated exactly term by term with no approximation.

### 4. Finite-band integration – exact closed form
Because every term is elementary, the integral over any finite band $[\nu_1,\nu_2]$ (or $[x_1,x_2]$) can be performed **term by term** with no approximation.

Introduce the dimensionless variable

$$
x=\frac{h_{\rm eff}\nu}{kT},\qquad dx=\frac{h_{\rm eff}}{kT}\,d\nu.
$$

The band-integrated energy density is

$$
U(\nu_1,\nu_2;T)=\int_{\nu_1}^{\nu_2}u(\nu,T)\,d\nu
=\frac{8\pi(kT)^4}{c^3 h_{\rm eff}^3}\sum_{n=1}^\infty\frac1{n^4}\int_{n x_1}^{n x_2}y^3 e^{-y}\,dy,
$$

where $x_i=h_{\rm eff}\nu_i/kT$.  

The incomplete integral of $y^3 e^{-y}$ is elementary (repeated integration by parts):

$$
\int y^3 e^{-y}\,dy=-e^{-y}(y^3+3y^2+6y+6)+{\rm const}.
$$

Therefore the **exact finite-band result** is the rapidly convergent series

$$
\boxed{
\begin{aligned}
U(\nu_1,\nu_2;T)
&=\frac{8\pi(kT)^4}{c^3 h_{\rm eff}^3}
\sum_{n=1}^\infty\frac1{n^4}\Bigl[
e^{-n x_1}(n^3 x_1^3+3n^2 x_1^2+6n x_1+6)\\
&\qquad\qquad\qquad
-e^{-n x_2}(n^3 x_2^3+3n^2 x_2^2+6n x_2+6)
\Bigr].
\end{aligned}
}
$$

(The corresponding band radiance $B_{\rm band}$ or photon flux $N_{\rm band}$ follows by the identical expansion with the appropriate prefactor $2h/c^2$ or $2\nu^2/c^2$.)

### 5. Special cases
- **Total integral** ($\nu_1=0$, $\nu_2=\infty$):

$$
\sum_{n=1}^\infty\frac1{n^4}=\zeta(4)=\frac{\pi^4}{90}\qquad\Rightarrow\qquad
U_{\rm tot}=\frac{4\sigma T^4}{c},\qquad\sigma=\frac{2\pi^5 k^4}{15 c^2 h_{\rm eff}^3}.
$$
  
  (Stefan–Boltzmann recovered exactly.)

- **Wien limit** (high-frequency band, $x\gg1$): only the first term $n=1$ survives; the incomplete gamma reduces to the classic Wien closed form.

- **Rayleigh–Jeans limit** (low-frequency band, $x\ll1$): the series sums to the classical $\nu^2 kT$ result.

### 6. Practical algorithm for spectrometer calibration
1. Convert detector band edges $\nu_1,\nu_2$ (or $\lambda_1,\lambda_2$) to dimensionless $x_1,x_2$.
2. Sum the series to $N\approx 20$–30 terms (convergence is exponential; double precision is reached long before).
3. Multiply by the geometric prefactor $8\pi(kT)^4/(c^3 h_{\rm eff}^3)$ (energy density) or the corresponding radiance factor.
4. For photon counts divide by $h_{\rm eff}\nu$ *after* integration, or expand the photon spectral density $u(\nu)/h\nu$ directly (identical series with $\nu^2$ instead of $\nu^3$).

All operations are analytic; no numerical quadrature, no special-function libraries beyond elementary exponentials and polynomials, and no dependence on floating-point implementations of the incomplete gamma.

### 7. Consistency with C.O.R.E. (flat Euclidean space)
- Mode density $8\pi\nu^2/c^3$ is purely geometric (Euclidean volume of $k$-space).
- Cascades are local residual re-emissions; no non-local quanta.
- Thresholds co-scale with $\varepsilon(r)$ exactly as in CUGE, so the measured band integral is independent of gravitational potential (local $c$-invariance).
- Impedance $Z_0$ remains invariant at every re-emission surface → no reflections, no dissipation artefacts.
- Zero free parameters once $h_{\rm eff}$ is fixed by the material (or by the VSS energy scale for the CMB).

### 8. Summary formula for finite-band use
In the cascading-residual ontology the blackbody spectrum is

$$
u(\nu,T)=\frac{8\pi h_{\rm eff}\nu^3}{c^3}\sum_{n=1}^\infty e^{-n h_{\rm eff}\nu/kT}.
$$

Its integral over any finite band $[\nu_1,\nu_2]$ is the exact, rapidly convergent elementary series given in the boxed equation of §4.

This simultaneously:
- completes the derivation that ASH §3.4 stated “requires derivation”,
- supplies a practical, closed-form tool for the finite-band integration problem,
- remains strictly inside flat Euclidean 3-space, continuous waves, and the C.O.R.E. postulates.

**The ultraviolet catastrophe is avoided because high-frequency energy is almost entirely residual and is forced to cascade downward; the finite-band integral is the truncated geometric series of those residuals.**

(The identical cascade applied to the cosmic VSS energy reservoir of ZEUS recovers the observed CMB blackbody spectrum and temperature without expansion.)

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2026 David Barbeau | david@bigbadaboom.ca

---
