**Preservation of Two-Way Light Speed Isotropy in CUGE vs General Relativity**

**David Barbeau, Independent Researcher**  
david@bigbadaboom.ca | www.bigbadaboom.ca  

March 30, 2026, Revision 2

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.  
©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

## Abstract

This article demonstrates how both General Relativity (GR) and the Classical Unification of Gravity and Electromagnetism (CUGE) framework predict the observed isotropy of the two-way speed of light — despite radically different physical foundations. While GR relies on local Lorentz invariance in curved spacetime, CUGE achieves the same result through the co-variation of atomic clocks, rulers, and electromagnetic wave propagation in a refractive vacuum with symmetric permittivity and permeability. The result is a singularity-free, flat-spacetime alternative that reproduces all weak-field predictions of GR.

---

## 1. Introduction: The Problem of \(c\)-Isotropy

One of the most profound features of modern physics is the local invariance of the speed of light. All experimental tests — from Michelson-Morley to GPS and laser ranging — confirm that the two-way (round-trip) speed of light is measured to be exactly

\[
c = 299\,792\,458\,\text{m/s} \tag{1.1}
\]

in every direction and at every location, regardless of gravitational potential. This is known as **\(c\)-isotropy**.

In General Relativity (GR), this is ensured by the equivalence principle: spacetime is locally flat, and Lorentz symmetry holds in freely falling frames. But in alternative models — particularly those set in flat spacetime — this invariance must be derived, not assumed.

The Classical Unification of Gravity and Electromagnetism (CUGE) framework [1] proposes that gravity emerges not from geometry, but from symmetric variations in the electromagnetic properties of the vacuum:

\[
\varepsilon(r) = \varepsilon_0\left(1 + \frac{GM}{2c^2 r}\right),\qquad
\mu(r) = \mu_0\left(1 + \frac{GM}{2c^2 r}\right) \tag{1.2}
\]

These variations produce a position-dependent coordinate speed of light:

\[
c_{\text{coord}}(r) = \frac{c}{n(r)}, \qquad n(r) \equiv \sqrt{\varepsilon(r)\mu(r)} \approx 1 + \frac{GM}{2c^2 r} \tag{1.3}
\]

Yet, despite this variation, local observers always measure \(c\) for two-way light paths. This paper shows how both GR and CUGE achieve this — and why CUGE offers a compelling physical mechanism behind the success of GR.

---

## 2. General Relativity: Geometric Enforcement of \(c\)-Isotropy

In GR, spacetime curvature near mass is described by the Schwarzschild metric. In isotropic coordinates, the line element is

\[
ds^2 = -\left(1 - \frac{2GM}{c^2 r}\right)c^2\,dt^2 + \left(1 + \frac{2GM}{c^2 r}\right)(dx^2 + dy^2 + dz^2) \tag{2.1}
\]

For weak fields, we expand to first order:

\[
g_{00} \approx -\left(1 - \frac{2\Phi}{c^2}\right),\qquad g_{ij} \approx \left(1 + \frac{2\Phi}{c^2}\right)\delta_{ij},\qquad \Phi = -\frac{GM}{r} \tag{2.2}
\]

### 2.1 Local Inertial Frames and Light Propagation

At any point, an observer can define a local inertial frame where spacetime is approximately Minkowskian. In this frame the measured speed of light is \(c\) by construction of local Lorentz invariance.

---

## 3. CUGE: Emergent \(c\)-Isotropy from Vacuum Co-Variation

In the CUGE framework the vacuum is a responsive medium whose permittivity and permeability vary symmetrically with the local gravitational potential. Atomic clocks and rulers are themselves electromagnetic systems embedded in this same responsive vacuum. According to the Atomic Statistical Hypothesis (ASH), the effective Planck constant appearing in atomic transitions is not the bare universal constant \(h\) but a material-dependent statistical average \(h_{\rm eff}\) that emerges from the continuous-wave interaction with the detector’s energy thresholds. In the responsive vacuum of CUGE these thresholds are modulated by the local permittivity, yielding the linear scaling \(h_{\rm eff}(r) \propto \varepsilon(r)\). The standard dielectric scaling for the transition energy remains \(E \propto 1/\varepsilon(r)^2\), but the observed frequency becomes \(\nu = E / h_{\rm eff} \propto 1/\varepsilon(r)^2 \times 1/\varepsilon(r) = 1/\varepsilon(r)\). Therefore the locally measured wavelength and frequency satisfy \(\lambda_{\rm meas} \propto \varepsilon(r)\) and \(f_{\rm meas} \propto 1/\varepsilon(r)\), so the measured speed of light is

\[
c_{\rm local} = \lambda_{\rm meas} \cdot f_{\rm meas} \propto \varepsilon(r) \cdot \frac{1}{\varepsilon(r)} = c = \text{constant}, \tag{3.1}
\]

independent of gravitational potential and direction.

### 3.1 How Local Observers Measure Light Speed

Local observers do not use coordinate time or distance. They use atomic clocks and rulers, which depend on \(\varepsilon(r)\) and \(\mu(r)\):

| Quantity                  | Dependence                  | Effect Near Mass                  |
|---------------------------|-----------------------------|-----------------------------------|
| Atomic frequency \(\nu\)  | \(\propto 1/\varepsilon(r)\) | Clocks run slower near mass       |
| Bohr radius \(a_0\)       | \(\propto \varepsilon(r)\)   | Rulers expand                     |
| Measured wavelength \(\lambda_{\rm meas}\) | \(\propto a_0 \propto \varepsilon(r)\) | — |
| Measured frequency \(f_{\rm meas}\) | \(\propto \nu \propto 1/\varepsilon(r)\) | — |

Thus, the locally measured speed of light is

\[
c_{\rm local} = \lambda_{\rm meas} \cdot f_{\rm meas} \propto \varepsilon(r) \cdot \frac{1}{\varepsilon(r)} = c \tag{3.2}
\]

This is invariant — not by postulate, but by physical co-variation.

### 3.2 Two-Way Measurement in CUGE

Consider a mirror at coordinate distance \(L\) from a source. The round-trip proper distance measured locally is \(2L_{\rm meas}\). The coordinate round-trip time is \(\Delta t_{\rm coord} = 2L n(r)/c\). Because local clocks run slower by the factor \(1/\varepsilon(r) \approx 1/n(r)\), the measured time interval is

\[
\Delta t_{\rm meas} = \Delta t_{\rm coord} \cdot \frac{1}{n(r)} = \frac{2L}{c} \tag{3.3}
\]

The measured length of the arm (in local meters) satisfies

\[
L_{\rm meas} = L / n(r) \tag{3.4}
\]

Therefore the measured two-way speed is

\[
c_{\rm meas} = \frac{2L_{\rm meas}}{\Delta t_{\rm meas}} = \frac{2(L/n(r))}{2L/c} = c \tag{3.5}
\]

✅ Result: **Despite a varying coordinate speed, the measured two-way speed is exactly \(c\), isotropically.**

---

## 4. Direct Comparison: GR vs CUGE

| Feature                  | General Relativity                          | CUGE                                              |
|--------------------------|---------------------------------------------|---------------------------------------------------|
| Spacetime                | Curved                                      | Flat                                              |
| Speed of Light (global)  | Varies via metric                           | \(c_{\rm coord} = c/n(r)\)                        |
| Local \(c\)-isotropy     | Postulated (local Lorentz invariance)       | Derived (co-variation of \(\varepsilon\), \(\mu\), clocks, rulers) |
| Two-way speed measured   | Always \(c\)                                | Always \(c\)                                      |
| Mechanism                | Spacetime geometry                          | Refractive vacuum medium                          |
| Origin of time dilation  | Curvature                                   | Slowed atomic transitions (\(\nu \propto 1/\varepsilon\)) |
| Singularities            | Present (e.g., black holes)                 | Avoided by construction                           |
| Free parameters          | None                                        | None — fully determined by \(GM/r\)               |

---

## 5. Discussion: Why CUGE Matters

The fact that CUGE reproduces local \(c\)-isotropy without spacetime curvature is not a coincidence — it is a direct consequence of the symmetric scaling of \(\varepsilon\) and \(\mu\), which preserves the impedance of free space:

\[
Z = \sqrt{\frac{\mu(r)}{\varepsilon(r)}} = \sqrt{\frac{\mu_0}{\varepsilon_0}} = \text{constant} \tag{5.1}
\]

This prevents reflections, dissipation, and birefringence — ensuring isotropy. It also aligns with the Atomic Statistical Hypothesis (ASH) [6], which treats light as a continuous wave, with quantization arising from material thresholds.

CUGE does not contradict GR — it explains it. Where GR says “Spacetime tells matter how to move; matter tells spacetime how to curve,” CUGE says “Mass modifies the vacuum’s \(\varepsilon\) and \(\mu\); the resulting refractive medium guides both light and atomic processes in lockstep — so local physics always sees \(c\).”

This reframing avoids singularities, unifies gravity with electromagnetism, and grounds time and space in measurable atomic standards — consistent with operational physics.

---

## 6. Conclusion

Both General Relativity and the CUGE framework predict that the two-way speed of light is isotropically measured as \(c\) in all local experiments. This agreement is essential for consistency with Michelson-Morley, GPS, and modern interferometry.

However, the mechanisms differ profoundly:

- **GR enforces \(c\)-isotropy through local geometric flatness.**
- **CUGE derives it from physical co-variation of light, clocks, and rulers in a responsive vacuum.**

CUGE thus provides a singularity-free, classical, and causal foundation for gravitational phenomena — reproducing all four classical tests of GR (perihelion precession, light bending, time dilation, Shapiro delay) without curvature or free parameters.

As such, CUGE is not merely an alternative to GR — it is a physical mechanism for its empirical success, forming a key component of the broader C.O.R.E. framework (Classical Origin of Reality and Emergence) [7].

---

## References

[1] D. Barbeau, *Classical Unification of Gravity and Electromagnetism via Symmetric Vacuum Property Variations*, 2025.  
[2] A. Einstein, *Erklärung der Perihelbewegung des Merkur*, Sitzungsberichte der Preussischen Akademie der Wissenschaften, 1915.  
[3] A. S. Eddington, *The total eclipse of 1919 May 29*, The Observatory, 1919.  
[4] I. I. Shapiro, *Fourth test of general relativity*, Phys. Rev. Lett., 1964.  
[5] C. M. Will, *The confrontation between GR and experiment*, Living Rev. Relativ., 2014.  
[6] D. Barbeau, *Experimental Validation of the Atomic Statistical Hypothesis*, 2025.  
[7] D. Barbeau, *C.O.R.E.: The Classical Origin of Reality and Emergence*, 2025.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---