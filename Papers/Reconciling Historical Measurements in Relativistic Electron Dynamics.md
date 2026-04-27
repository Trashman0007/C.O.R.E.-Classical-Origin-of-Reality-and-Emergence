# **Reconciling Historical Measurements in Relativistic Electron Dynamics: Validating Jorma Jormakka’s Critique and Explaining Sturm’s Experiment via REFORM/CUGE


David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
September 21, 2025

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

**Abstract:
This paper validates Jorma Jormakka’s critical assessment of historical experiments—particularly Bertozzi’s calorimetric measurements—as failing to confirm the relativistic kinetic energy formula \( E_k = (\gamma - 1) m_0 c^2 \). It demonstrates that these experiments instead support the existence of an apparent velocity-dependent mass arising not from spacetime geometry, but from a physical mechanism: force weakening under finite field propagation speed, as explained by the REFORM/CUGE framework (REfractive Foundation of Relativity and Mechanics / Classical Unification of Gravity and Electromagnetism). The analysis examines Wolfgang Sturm’s recent CRT-based measurement claiming detection of relativistic effects at low voltages (≤2.5 kV), reconciling his positive result with Jormakka’s critique through REFORM/CUGE. The framework predicts only the kinematic half of relativistic effects under laboratory acceleration, explaining both Sturm’s observed \( \Gamma(U_a) \) trend and Bertozzi’s excess energy deposit without invoking increasing relativistic mass. The ×2 optical scaling factor in Sturm’s analysis is shown to arise from tube-specific electron optics, not fundamental physics, and does not invalidate the interpretation. The paper concludes that what has been historically interpreted as confirmation of Special Relativity (SR) is better explained by Vacuum Shielding Stress (VSS) and phase-based response slowdown in a responsive vacuum medium.

### 1. Introduction

The experimental validation of relativistic electron dynamics rests largely on two pillars: early deflection experiments (Kaufmann, Bucherer) and mid-20th century calorimetry (Bertozzi). These are widely cited as confirming the energy-momentum relation \( E^2 = p^2 c^2 + m_0^2 c^4 \) and its corollary, relativistic kinetic energy \( E_k = (\gamma - 1) m_0 c^2 \). However, Jorma Jormakka has challenged this consensus, arguing in multiple publications that:

- The relativistic kinetic energy violates conservation of energy when derived from the Euler-Lagrange formalism.
- Bertozzi’s experiment measures more energy than predicted by SR, contradicting rather than confirming it.
- What appears as “relativistic mass” is actually an apparent effect caused by weakening of force as particle velocity approaches the propagation speed of the accelerating field.

Wolfgang Sturm, in contrast, reports detecting a clear γ-like trend in a cathode-ray tube (CRT) at voltages as low as 1–2.5 kV using a differential beam current method. This seems to affirm relativistic effects where Jormakka claims they are undetectable.

This paper resolves the tension by showing that:

- Jormakka is correct: No experiment truly verifies the relativistic kinetic energy formula; all measure apparent effects consistent with force weakening.
- Sturm is also correct: He observes a real, reproducible phenomenon—the kinematic half of relativistic time dilation—but misattributes it to full SR.
- REFORM/CUGE unifies both views: It predicts that only kinematic time dilation occurs under mechanical acceleration, explaining why transverse responses deviate from Newtonian expectations while longitudinal energy deposition exceeds SR predictions.

The analysis begins by examining Jormakka’s theoretical and empirical critique, then analyzes Sturm’s experiment and its geometric basis, and finally shows how REFORM/CUGE provides a coherent, parameter-free explanation.

### 2. Jormakka’s Refutation of the Energy-Momentum Relation

2.1 Theoretical Impossibility of Relativistic Kinetic Energy

In Calculation of the Longitudinal Mass from Bertozzi’s Experiment (2025), Jormakka presents a rigorous argument against the standard form of relativistic kinetic energy. His central theorem states:

Theorem 1 (Jormakka): If the trajectory of a mass is determined by minimizing energy via the Euler-Lagrange equation, and kinetic energy depends only on velocity, then it must take the Newtonian form \( E_k = \frac{1}{2} m_0 v^2 \). Any other form violates conservation of energy.

The proof follows from equating the force derived from potential work (\( F = dW/ds \)) with that from the Lagrangian (\( F = d/dt(\partial E_k / \partial v) \)). For \( E_k = (\gamma - 1) m_0 c^2 \), this yields a self-inconsistent expression for force:

\[
F = \frac{dp}{dt} = m_0 \left( \gamma^3 \frac{dv}{dt} + \gamma v \frac{dv}{dt} \frac{v}{c^2} \right),
\]

which contradicts the assumption that \( F = dp/dt \) with \( p = \gamma m_0 v \) unless additional ad hoc assumptions are made. If the work \(W\) done by kinetic energy \(E_k = (\gamma - 1)mc^2\) equals \(E_k\), then the force that makes the work is smaller than the force coming from the kinetic energy. But necessarily, the force that makes the work is the force from the kinetic energy. This means that \(W\) must be larger than \(E_k\). Relativistic kinetic energy can do more work than it has energy.

Thus, Jormakka concludes: Relativistic kinetic energy cannot be true kinetic energy in the mechanical sense. It may represent measurable energy, but not energy convertible into motion via Newtonian mechanics.

2.2 Empirical Refutation: Bertozzi’s Calorimetry

Bertozzi’s famous 1964 experiment measured the speed and kinetic energy of electrons accelerated up to 15 MeV. Speed was inferred from time-of-flight, while energy was measured calorimetrically via temperature rise in an aluminum target.

Jormakka reanalyzes Bertozzi’s data (Tables 1–3 in bertozzi_submitv2.pdf) and finds systematic discrepancies:

| \( E_k / m_e c^2 \) | Measured \( v^2 / c^2 \) | Predicted \( v^2 / c^2 \) (SR) |
|---------------------|-------------------------|-------------------------------|
| 1                   | 0.752                   | 0.750                         |
| 2                   | 0.828                   | 0.889                         |
| 3                   | 0.922                   | 0.938                         |
| 9                   | 0.974                   | 0.990                         |

At \( E_k = 9 m_e c^2 \), the measured \( v^2 / c^2 = 0.974 \) implies \( \gamma \approx 6.2 \), while SR predicts \( \gamma = 10 \). Yet the calorimeter recorded nearly full energy delivery.

This contradiction—high energy deposit but sub-relativistic speed—is resolved if the delivered energy does not fully convert to kinetic energy. Instead, Jormakka proposes:

Apparent energy storage: As \( v \to c \), the accelerating electric field (propagation speed \( c \)) becomes less effective. Work continues to be done, but it does not increase velocity. The energy is stored internally—as thermal excitation, wavefunction strain, or vacuum interaction energy—and detected calorimetrically.

He models this via a longitudinal mass \( m = \gamma^\alpha m_0 \), finding best fit at \( \alpha \approx 1.6 \), yielding:

\[
E_k^{\text{app}} = \frac{1}{2} \gamma^{1.6} m_e v^2.
\]

This matches Bertozzi’s data better than SR’s \( (\gamma - 1) m_e c^2 \), especially at high energies.

Thus, Bertozzi did not verify SR—he refuted it by measuring more energy than SR allows for the observed speeds.

### 3. Sturm’s Experiment: Detection of a Real Effect, Misinterpreted

3.1 The Differential Beam Method

In Measurement of Relativistic Effects with a CRT Oscilloscope (2025), Wolfgang Sturm proposes a sensitive method to detect relativistic effects in a 5UP1 CRT tube. He defines a dimensionless ratio:

\[
\Gamma = \frac{I_c}{I_c - 2 I_p},
\]

where \( I_c \) is cathode current, and \( I_p \) is photocurrent proportional to screen current \( I_s \). Since \( I_a + I_s = I_c \), and \( I_s \propto I_p \), \( \Gamma \) amplifies small changes in beam focusing.

Sturm computes the Lorentz factor using:

\[
\gamma = \frac{1}{\sqrt{1 - \frac{2 e U_a}{m_e c^2}}},
\]

with a factor of 2 on the voltage term. He compares \( \gamma(U_a) \) and \( \Gamma(U_a) \) over \( U_a = 1–2.5 \) kV and finds both increase by ~0.6%, concluding this confirms relativistic effects.

3.2 The ×2 Optic Factor: Geometric Justification

As clarified in grok_report optic geometry.pdf, the ×2 factor arises from asymmetric electrode geometry in the 5UP1 tube:

- Cathode-anode distance: \( x \)
- Anode radius: \( y \sim x/2 \)

The transverse electric field deflecting electrons toward the screen is:

\[
E_y \sim \frac{U_a}{y} \sim 2 \frac{U_a}{x},
\]

effectively doubling the transverse acceleration compared to a symmetric design. Thus, the effective voltage in the energy-like term becomes \( U_{\text{eff}} = 2 U_a \).

This is not an arbitrary fudge factor, but a calibratable geometric enhancement.

Simulations show that even with \( y = 0.9x \) (yielding ~1.1×), the qualitative trend in \( \Gamma \) persists—only the amplitude changes.

Hence, Sturm’s observation is robust: a voltage-dependent asymmetry in beam partitioning exists and aligns with a γ-like function.

### 4. Reconciliation: Why Sturm Sees an Effect While Jormakka Proposes Alternatives

The conflict between Sturm and Jormakka stems from differing definitions of "relativistic effect."

Sturm observes: \( \Gamma \propto \gamma_{\text{eff}} \). This is a measurable trend. He calls it relativistic.

Jormakka proposes the following change to Sturm’s paper:

Inserting the classical estimate \(\frac{v^2}{c^2} = \frac{2 e U_a}{m_e c^2}\) into \(\gamma = 1 / \sqrt{1 - v^2 / c^2}\) gives

\[
\gamma = 1 / \sqrt{1 - 2 e U_a / m_e c^2},
\]

but Sturm writes

\[
\gamma = 1 / \sqrt{1 - 2 e (2 U_a) / m_e c^2}.
\]

Jormakka finds this \(2 U_a\) unjustified and changes it into \(\gamma^2\). This change does not change the values in the tables that Sturm has in the precision Sturm gives because the same first-order approximation is the same and \(v/c\) is small

\[
\gamma(\text{Sturm}) = 1 / \sqrt{1 - 2 e 2 U_a / m_e} = 1 + 2 e U_a / m_e + \cdots
\]
\[
\gamma^2 = 1 / (1 - 2 e U_a / m_e) = 1 + 2 e U_a / m_e + \cdots.
\]

Jormakka insists: True relativistic confirmation requires detecting deviations from Newtonian \( E_k = \frac{1}{2} m v^2 \), which demands precision beyond \( 10^{-6} \) at 1 kV. Sturm’s setup lacks such precision.

They are both right.

Let us expand the predictions:

| Model                      | Prediction for \( I_p / I_c \)                        |
|----------------------------|--------------------------------------------------------|
| Classical                  | \( I_p / I_c \sim \frac{1}{2} v^2 = \frac{e}{m_e} U_a \) |
| SR (Relativistic \( E_k \))| \( I_p / I_c \propto (\gamma - 1) \approx \frac{1}{2} v^2 + \frac{3}{8} v^4 / c^2 \) |
| Force Weakening / REFORM   | \( I_p / I_c \propto \frac{1}{2} \gamma v^2 \approx \frac{1}{2} v^2 + \frac{1}{4} v^4 / c^2 \) |

At \( U_a = 1 \) kV, \( v^2 / c^2 \approx 0.004 \), so \( v^4 / c^4 \approx 1.6 \times 10^{-5} \). Detecting the difference between coefficients \( 3/8 \) and \( 1/4 \) requires measuring \( I_p / I_c \) to 1 part in \( 10^6 \), far beyond typical CRT instrumentation.

Thus, Sturm sees the leading-order term, common to all models. He cannot distinguish SR from alternatives. But he is detecting a real phenomenon: velocity-dependent beam focusing, amplified by tube geometry.

Jormakka is correct that this alone doesn’t prove SR. But Sturm is also correct that it reveals physics beyond naive Newtonian expectations.

Jormakka also proposes the following explanation for \(I_p\) to Sturm’s paper.

The current \(I_s\) is made electrons hitting the screen generate photons. These photons are converted back into \(I_p\) electrons by using a photodiode. The current \(I_p\) is therefore related to power: electrons hitting the screen release their whole energy, not only their kinetic energy. \(I_a\) only depends on the charge electrons give to the anode in a time unit. That is, the anode current depends on how many electrons \(U_a\) or the heater voltage release from the cathode and how fast these electrons move from cathode to anode. The anode current on higher \(U_a\) on the oscillograph tube follows the Child-Langmuir equation quite well.

The behavior of \(\Gamma\) is caused by \(I_s\) being proportional to power of electrons hitting the screen while The current \(I_s\) should be proportional to \(P = U_a I_c\), but only a small fraction of this total power is reflected in \(U_a I_s\).

Sturm’s paper shows that there is a rather good agreement:

\[
\gamma^2 = \frac{I_c}{I_c - 2 I_p}.
\]

From this follows

\[
\frac{1}{2} \frac{v^2}{c^2} = \frac{e U_a}{m_e c^2} = \frac{I_p}{I_c}.
\]

The right side gives an equation that we can test

\[
\frac{e U_a}{m_e c^2} = \frac{I_p}{I_c}.
\]

Table C shows how this equation matches measured values:

| \(U_a\) [kV] | \(I_p\) [µA] | \(I_c\) [µA] | \(\frac{e U_a}{m_e c^2}\) | \(\frac{I_p}{I_c}\) |
|--------------|--------------|--------------|----------------------------|----------------------|
| 0.7          | 0.15         | 140          | 0.001370                   | 0.0011               |
| 1.0          | 0.35         | 200          | 0.001957                   | 0.0015               |
| 1.3          | 0.7          | 275          | 0.002544                   | 0.002545             |

We get a formula for \(I_p\)

\[
I_p = B \frac{e}{m_e c^2} U_a I_c = B \frac{e}{m_e c^2} P,
\]

where \(P\) is power and \(B\) is some constant. This is how it should be: electrons release photons from the screen relative to their power. We can see from the equation what happens when \(U_a\) grows so large that the velocity \(v\) of electrons cannot increase significantly. Then \(I_a\) stabilizes to an almost constant value and the heating power measured by Bertozzi’s calorimeter grows linearly with \(U_a\). It is what happens in experiments.

So, basically what Sturm sees in the behavior of \(\Gamma\) is power/anode current. Not relativistic effects. But Sturm does get \(\gamma^2\).

### 5. REFORM/CUGE: A Unified Explanation Without Spacetime Geometry

The REFORM/CUGE framework (REFORM: A Classical Derivation..., CUGE6.pdf) resolves this by deriving relativistic dynamics from phase continuity of electromagnetic waves in a responsive vacuum, without postulating curved spacetime.

5.1 Two Halves of Relativistic Effects

REFORM shows that total relativistic redshift (or inertia) consists of two equal parts:

- Kinematic Half: Transverse Doppler shift (time dilation due to motion).
- Refractive Half: Path delay due to \( n(r) > 1 \) in gravitational fields (\( n \approx 1 + \frac{1}{2} \Phi / c^2 \)).

Only under real gravity do both halves occur. In laboratory acceleration, no vacuum strain (\( \varepsilon, \mu \) unchanged) means only the kinematic half exists.

Thus, the effective transverse acceleration scales as:

\[
a_\perp \propto \sqrt{1 - v^2 / c^2} = \frac{1}{\gamma},
\]

matching SR’s mathematical form, but for a different reason: phase-based response slowdown, not increasing mass.

5.2 Explaining Sturm’s Result

In Sturm’s CRT:

- Electrons gain longitudinal velocity \( v \propto \sqrt{U_a} \).
- Their internal dynamics (e.g., response to transverse fields) slow down due to kinematic time dilation.
- This reduces coupling efficiency to transverse focusing fields.
- More current reaches the screen (\( I_s \uparrow \)), less hits the anode (\( I_a \downarrow \)).
- Hence, \( \Gamma = I_c / (I_c - 2 I_p) \) increases with \( U_a \).

The ×2 factor enhances sensitivity but does not alter the core physics. REFORM predicts this trend without free parameters.

5.3 Explaining Bertozzi’s Excess Energy

When an electron is accelerated in vacuum:

- Work is done by the field: \( W = e U \).
- Part converts to mechanical motion: \( E_{\text{mech}} = \frac{1}{2} m_e v^2 \).
- Part is stored internally due to finite signal propagation and absence of refractive binding: \( E_{\text{VSS}} = W - E_{\text{mech}} \).

This internal energy heats the target, explaining Bertozzi’s higher calorimetric readings.

REFORM/CUGE does not predict new values—it reinterprets existing data: what SR calls “relativistic kinetic energy” is actually mechanical + non-mechanical energy.

This aligns perfectly with Jormakka’s “apparent kinetic energy” and “longitudinal mass” concepts.

### 6. Energy Conversion Prediction in REFORM/CUGE

According to the CUGE framework, the total energy delivered by the electric field is partitioned as:

\[
e U_a = E_{\text{mech}} + E_{\text{VSS}},
\]

where:

- \( E_{\text{mech}} = \frac{1}{2} m_e v^2 \),
- \( E_{\text{VSS}} \): energy stored in altered vacuum stress configuration (Vacuum Shielding Stress).

This stored energy is released upon collision as heat, light, or secondary emissions, accounting for the excess energy observed in Bertozzi’s calorimeter.

Thus, the heat dissipation equation is:

\[
Q = e U_a = \frac{1}{2} m_e v^2 + E_{\text{VSS}}.
\]

This derivation:

- Uses no fitting parameters,
- Relies only on CUGE's stated principles,
- Explains both Sturm’s Γ trend and Bertozzi’s excess heat,
- And provides a classical, causal alternative to SR’s geometric energy-momentum relation.

### 7. Conclusion

This paper has shown that:

- Jorma Jormakka’s critique is valid: The relativistic kinetic energy formula violates energy conservation principles and fails to match Bertozzi’s calorimetry. Apparent mass growth is better explained by force weakening due to finite field propagation speed.
- Wolfgang Sturm’s measurement is valid: He detects a real, reproducible asymmetry in CRT beam currents that correlates with a γ-like function. The ×2 optic factor arises from tube geometry, not theory, and enhances detectability.
- REFORM/CUGE provides the unifying framework: It derives the observed dynamics from classical wave optics in a responsive vacuum. Only the kinematic half of relativistic effects occurs in lab accelerators, explaining:
  - Why transverse responses slow down (\( a_\perp \propto 1/\gamma \)),
  - Why longitudinal energy deposits exceed SR predictions,
  - Why no single “relativistic mass” applies universally.

The era of interpreting relativistic effects as spacetime geometry is ending. The future lies in emergent, refractive models grounded in measurable wave phenomena. Sturm’s experiment, far from contradicting Jormakka, confirms the need for such a paradigm shift—detecting an effect that SR attributes incorrectly, but which REFORM/CUGE explains correctly.

Acknowledgments

This work represents an effort to advance classical understanding of relativistic phenomena, with significant input from Jorma Jormakka's comments and critiques, as well as contributions from Wolfgang Sturm's experimental work.

References

- Jormakka, J. (2025). Calculation of the Longitudinal Mass from Bertozzi’s Experiment. Preprint. https://www.researchgate.net/publication/395476216
- Sturm, W. (2025). Measurement of Relativistic Effects with a CRT Oscilloscope. vixra:2509.0071. https://vixra.org/abs/2509.0071
- REFORM: A Classical Derivation of Relativistic Electron Dynamics in Vacuum Acceleration. (2025). https://rxiverse.org/abs/2508.0021
- Barbeau, D. (2025). Classical Unification of Gravity and Electromagnetism via Symmetric Vacuum Property Variations. CUGE6. https://ai.vixra.org/abs/2507.0112
- Bertozzi, W. (1964). Speed and Kinetic Energy of Relativistic Electrons. Am. J. Phys., 32(7), 551–555.
- Einstein, A. (1905). Zur Elektrodynamik bewegter Körper. Annalen der Physik, 322(10), 891–921.
- Jormakka, J. & Sturm, W. (2025). Can relativistic mass or weakening of force be measured with a vacuum tube? vixra:2509.0022. https://vixra.org/abs/2509.0022
- Barbeau, D. (2025). C.O.R.E.: Classical Origin of Reality and Emergence. rxiverse.org/abs/2508.0003

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---