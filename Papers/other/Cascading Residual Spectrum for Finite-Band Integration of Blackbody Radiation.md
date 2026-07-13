# **Cascading Residual Spectrum for Finite-Band Integration of Blackbody Radiation**  
**(Extension of ASH §3.4 – flat Euclidean 3-space only, SI base units, continuous EM waves)**

**David Barbeau, Independent Researcher**  
david@bigbadaboom.ca | www.bigbadaboom.ca  

July 12, 2026, *Version 3 (july 13 2026)*

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.  
©2026 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

**Abstract**

Max Planck’s 1900 derivation of blackbody radiation introduced energy quanta as a formal mathematical necessity but left the underlying ontology of light unresolved. For over a century, mainstream physics abandoned classical continuous waves in favor of photon statistics to explain quantization and avoid the ultraviolet catastrophe. This paper completes Planck’s original vision by deriving the exact Planck spectrum from first principles within a strictly classical framework: flat Euclidean 3-space, continuous electromagnetic waves, and material oscillators possessing a continuum of energy thresholds $\rho(\phi)$. 

We introduce the concept of **"cascading residuals,"** where wave energy failing to meet a material threshold is re-radiated at lower frequencies, creating a downward spectral cascade. By incorporating a non-linear **"wave-seeding"** mixing term that mimics stimulated emission through constructive interference, we formulate an exact non-linear integral transport equation for spectral energy density. The Planck distribution emerges as the unique steady-state solution to this equation, expressed as an infinite geometric series of elementary Wien terms. This derivation demonstrates that quantization is an emergent property of continuous wave interactions with material thresholds, rather than a fundamental attribute of light. Furthermore, we provide a rapidly converging closed-form analytical series for finite-band integration of blackbody radiation, offering a practical tool for spectrometer calibration and radiative transfer calculations without reliance on numerical quadrature or special functions.

### 1. Starting point (ASH postulates in flat Euclidean space)
- Light is a continuous electromagnetic wave. Spectral energy density $u(\nu)\,d\nu$ (J m⁻³ Hz⁻¹) or spectral radiance $B(\nu,T)$ (W m⁻² Hz⁻¹ sr⁻¹).
- Material detectors (or cavity walls) possess a continuum of energy thresholds $\phi$. Density of thresholds: $\rho(\phi)$.
- Absorption occurs only when the local wave energy can meet or exceed an available threshold.
- All energy that does **not** meet a threshold is residual and is re-radiated at lower frequencies. This residual is the cascade.
- Nature is spatially flat Euclidean 3-space. Mode density is purely geometric: $8\pi\nu^2/c^3$ (energy density) or $2\nu^2/c^2$ (radiance per steradian). No curvature, no expansion, no free parameters beyond the statistical average threshold spacing $h_{\rm eff}$.

Effective $h_{\rm eff}$ (or simply $h$) emerges as the average spacing of the continuous-wave thresholds. Local $c$-invariance and impedance invariance $Z_0=\sqrt{\mu/\varepsilon}$ are preserved exactly as in CUGE.

### §2. The Physical Ontology: Continuous Waves, Vacuum Strain, and Cascading Residuals

To derive the blackbody radiation spectrum from first principles, we must abandon the abstract postulate of indivisible photons and the assumption of an empty geometric void. Under the **Classical Unification of Gravity and Electromagnetism (CUGE)** framework, the vacuum is a responsive, polarizable physical medium characterized by spatially varying permittivity $\varepsilon(r)$ and permeability $\mu(r)$. Because the vacuum is a physical dielectric medium, it inherently supports classical non-linear optical interactions (e.g., wave-wave mixing). 

Simultaneously, the **Atomic Statistical Hypothesis (ASH)** dictates that light propagates strictly as a continuous electromagnetic wave, while the material interacting with this wave (such as the oscillators in a blackbody cavity wall) possesses a continuum of energy thresholds $\rho(\phi)$, rather than artificially discrete "quantum" states.

As the continuous wave field does work on these material oscillators, the interaction is governed by a strict macroscopic energy balance:

$$ E_{\text{incident}} = E_{\text{absorbed}} + E_{\text{residual}} $$

The emergence of apparent "quantization" is driven entirely by two coupled mechanisms:
1. **The Material Choke Point:** An oscillator will only undergo a physical transition (e.g., crossing a work function or bandgap) when the accumulated local continuous-wave energy meets or exceeds its specific material threshold.
2. **The Residual Heat Cascade:** Any incident continuous-wave energy that fails to perfectly meet a threshold is not forbidden from interacting. Driven by the non-linear mixing of the responsive CUGE vacuum, it is continuously shed and re-radiated at lower frequencies as a cascading residual, or dissipated locally into the lattice as heat.

Because high-frequency continuous waves are forced to cascade downward as residual heat until they meet a material threshold, the successful transitions merely *appear* to happen in discrete chunks. The effective Planck constant, $h_{\text{eff}}$, is therefore not a fundamental particle property, but the statistical average of these continuous-wave threshold spacings.

It is within this responsive thermal bath of cascading residual heat at temperature $T$ that we define our continuous classical variables:
*   **$n(x)$**: The classical wave occupation number (dimensionless spectral energy density), representing the continuous ambient field, where $x = h_{\text{eff}}\nu / k_B T$.
*   **$N_0$**: The population density of oscillators currently below the required threshold limit.
*   **$N_1$**: The population density of oscillators that have accumulated enough continuous wave energy to cross the threshold.

Because the residual heat bath governs the classical thermal fluctuations of the material, the statistical probability of an oscillator possessing enough energy to breach the continuous threshold dictates that these populations strictly obey the classical **Boltzmann distribution**:

$$ \frac{N_1}{N_0} = e^{-\Delta E / k_B T} = e^{-x} $$

### §3. Classical Detailed Balance and the Emergence of the Planck Spectrum

With the physical ontology established, we define the transition rates between the sub-threshold population $N_0$ and the supra-threshold population $N_1$ using purely classical continuum electrodynamics:

1.  **Classical Absorption (Driven Oscillation):** The continuous ambient electric field does work on the bound electrons in the $N_0$ state, driving them toward the threshold. The rate is proportional to the ambient wave intensity $n(x)$ and the available ground-state oscillators $N_0$:

$$R_{\text{abs}} = \sigma N_0 n(x)$$
	
2.  **Classical Stimulated Emission (Coherent Wave-Mixing):** The ambient continuous wave $n(x)$ phase-locks with the oscillating dipole of an oscillator in the $N_1$ state. This classical resonance stimulates the oscillator to shed its accumulated energy coherently into the field. By classical antenna reciprocity, the coupling cross-section $\sigma$ is identical to absorption:

$$R_{\text{stim}} = \sigma N_1 n(x)$$
	
3.  **The ASH Spontaneous Seed (The Residual Cascade):** An oscillator in the $N_1$ state is continuously subjected to the thermal and electromagnetic fluctuations of the residual heat bath. To maintain thermodynamic equilibrium, it must eventually relax across the threshold, shedding its excess energy as a continuous wave seed (via classical Larmor radiation). Crucially, this relaxation is a local, material-driven imperative that is **independent of the ambient field**. This classical threshold-relaxation is the physical origin of the famous quantum "+1":

$$R_{\text{spont}} = \sigma N_1$$

The kinetic equation for the continuous wave field is the sum of these classical rates, yielding the **ASH-modified collision integral**:

$$\frac{\partial n(x)}{\partial t} = \underbrace{\sigma N_1}_{\text{ASH Seed}} + \underbrace{\sigma N_1 n(x)}_{\text{Stimulated Mixing}} - \underbrace{\sigma N_0 n(x)}_{\text{Absorption}}$$

Factoring out the coupling constant $\sigma$, we obtain the fundamental balance equation:

$$\frac{\partial n(x)}{\partial t} = \sigma \Big[ N_1 \big(1 + n(x)\big) - N_0 n(x) \Big]$$

(Note: In standard quantum mechanics, the $1 + n(x)$ term is inserted via the bosonic creation operator $\hat{a}^\dagger |n\rangle = \sqrt{n+1} |n+1\rangle$. In the ASH framework, the "1" is the classical Larmor seed driven by the residual cascade, and the "$n(x)$" is classical coherent wave-mixing.)

To find the steady-state blackbody spectrum, we require thermal equilibrium (Detailed Balance), meaning the net rate of change of the field must be zero:

$$\frac{\partial n(x)}{\partial t} = 0$$

Setting the collision integral to zero and expanding:

$$N_1 + N_1 n(x) - N_0 n(x) = 0$$

Isolating the terms containing $n(x)$:

$$N_1 = n(x) (N_0 - N_1)$$

Solving for the classical occupation number $n(x)$:

$$ n(x) = \frac{N_1}{N_0 - N_1} = \frac{\frac{N_1}{N_0}}{1 - \frac{N_1}{N_0}} $$

Substituting the classical Boltzmann distribution $\frac{N_1}{N_0} = e^{-x}$:

$$ n(x) = \frac{e^{-x}}{1 - e^{-x}} $$

Multiplying the numerator and denominator by $e^x$ to clear the negative exponent yields the exact classical occupation number:

$$ n(x) = \frac{1}{e^x - 1} $$

Finally, multiplying by the 3D classical density of states $x^3$ and the appropriate physical constants yields the exact **Planck Blackbody Radiation Law**:

$$ u(x) \propto \frac{x^3}{e^x - 1} $$

**Conclusion:** The Planck spectrum is not the exclusive domain of quantized light. It is the unique, mathematically rigorous steady-state solution of continuous classical waves interacting with material energy thresholds. The density matrix and the "photon" are therefore revealed to be highly effective, emergent statistical bookkeeping tools that perfectly map onto the macroscopic outcomes of this deeper, purely classical reality.

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
- supplies a practical, closed-form tool for the finite-band integration problem posed on the physicsdiscussionforum,
- remains strictly inside flat Euclidean 3-space, continuous waves, and the C.O.R.E. postulates.

**The ultraviolet catastrophe is avoided because high-frequency energy is almost entirely residual and is forced to cascade downward; the finite-band integral is the truncated geometric series of those residuals.**

(The identical cascade applied to the cosmic VSS energy reservoir of ZEUS recovers the observed CMB blackbody spectrum and temperature without expansion.)

### 9. Historical Context and Completion of Planck’s Work

Max Planck’s derivation of blackbody radiation in 1900 is widely regarded as the birth of quantum mechanics, yet it was born from a deep ontological conflict that Planck himself struggled to resolve for over a decade. In his famous paper, Planck arrived at the correct spectral formula by mathematically interpolating between Wien’s law (valid at high frequencies) and the Rayleigh-Jeans law (valid at low frequencies). To make this work formally, he introduced the radical assumption that material oscillators could only exchange energy in discrete units of $E = nh\nu$. 

However, Planck did not believe light itself was quantized. He viewed electromagnetic radiation as a continuous classical wave and assumed that "quantization" applied strictly to the matter (the cavity walls). For years following 1900, Planck actively resisted Albert Einstein’s 1905 proposal of light quanta (photons), spending considerable effort attempting to derive his own formula using purely classical physics. His failure was not due to a lack of mathematical skill, but because he lacked the necessary dynamical mechanism: he assumed material oscillators were simple harmonic resonators subject to equipartition, rather than possessing a continuum of energy thresholds interacting with continuous waves via cascading residuals.

The C.O.R.E. framework now completes Planck’s original vision by providing exactly this missing physical mechanism. By shifting the ontology to one where **light remains a continuous wave** and quantization emerges from **material detectors/oscillators possessing a continuum of thresholds $\rho(\phi)$**, we can derive the exact Planck spectrum without ever invoking fundamental photons. 

In this framework:
*   The static mathematical rule $E = nh\nu$ is replaced by a dynamic process: continuous waves encounter material thresholds, and "residual" energy that fails to meet a threshold cascades downward in frequency until it does. 
*   The integer $n$ in the resulting geometric series $\sum e^{-nx}$ no longer represents a count of fundamental particles, but rather successive steps of wave-seeded residual emission down through the energy spectrum.
*   The ultraviolet catastrophe is avoided not because high-frequency photons are statistically unlikely to exist (as in standard quantum statistics), but because high-frequency continuous waves become residual and are forced to cascade downward until they meet a material threshold.

By introducing the non-linear "wave-seeding" mixing term, this work finally provides the classical dynamical equivalent of stimulated emission that Planck sought for decades. It transforms Planck’s formal mathematical interpolation into a complete, dynamical theory where quantization is an emergent property of continuous waves interacting with matter—fulfilling Planck's own long-held hope that the blackbody spectrum could be derived without abandoning the classical concept of continuous electromagnetic fields.

### Addendum: Clarification on the $h_{\text{eff}}$ Scaling Paradox

A rigorous application of the C.O.R.E. framework requires distinguishing between *internal* atomic standards and *external* threshold interactions. In **REFORM §7**, the scaling $h_{\text{eff}}(r) \propto \varepsilon(r)$ is discussed in the context of general phase continuity and internal atomic coherence. However, as detailed in **CUGE Appendix A.2**, the effective Planck constant governing *external* threshold processes (such as the photoelectric effect, Bell/ASH correlations, and blackbody cavity wall absorption) is derived from the material work function $\phi(r) \propto 1/\varepsilon(r)^2$ and the local field energy gain per cycle. 

For external detection and threshold crossing, the correct scaling is:

$$ h_{\text{eff}}(r) \propto \frac{1}{\varepsilon(r)} $$

Because the blackbody spectrum is established by the continuous waves interacting with the *external* material thresholds of the cavity walls (the ASH choke points), the dimensionless frequency $x = h_{\text{eff}}\nu / k_B T$ correctly utilizes the external threshold scaling. This material-dependent scaling ensures energy conservation across the vacuum-matter interface without requiring a universal, fundamental quantum of action, and leaves the local invariance of $c$ (governed by internal clocks and rulers) perfectly intact.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X. © 2026 David Barbeau | david@bigbadaboom.ca

---
