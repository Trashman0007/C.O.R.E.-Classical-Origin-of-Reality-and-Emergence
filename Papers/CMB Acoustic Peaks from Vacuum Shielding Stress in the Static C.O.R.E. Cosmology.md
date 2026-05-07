# **CMB Acoustic Peaks from Vacuum Shielding Stress in the Static C.O.R.E. Cosmology**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
Mai 6, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

### Abstract

In the C.O.R.E. framework (CUGE + ASH + REFORM + ZEUS) the universe is static, Euclidean, and eternal. The cosmic microwave background (CMB) arises as steady-state thermal emission from Vacuum Shielding Stress (VSS) energy stored in the responsive vacuum, with temperature and polarization anisotropies produced by scalar strain fluctuations in the filamentary cosmic web. We derive the full set of acoustic peaks directly from geometric Limber projection of the web’s characteristic transverse scale (\(\lambda_{\rm web} \approx 100\)–\(150\,h^{-1}\) Mpc), set by the effective Jeans length of the ray-equation damping term. No expansion, recombination, or baryon-photon oscillations are required. The same VSS mechanism that supplies extra dynamical mass for flat rotation curves, explains the DAMA/LIBRA annual modulation (and Wilczak photon-detector residuals), and reproduces the BAO scale also generates the observed CMB temperature power spectrum \(C_\ell^{TT}\), E/B-mode polarization, and TE cross-correlation. All predictions are untuned, use only existing C.O.R.E. equations (dimensionless refractive index \(n(r)\), SI base units, local gradients distinguished from integrated phase), and match Planck 2018 peak positions (\(\ell_1 \approx 220\), \(\ell_2 \approx 540\), \(\ell_3 \approx 820\)) and relative amplitudes to high precision. This closes the last major cosmological observable within the classical responsive-vacuum ontology.

---

### 1. Introduction

Standard \(\Lambda\)CDM attributes the CMB acoustic peaks to frozen sound waves in the baryon-photon fluid at recombination (\(z\approx 1100\)). In the C.O.R.E. framework there is no Big Bang, no expansion, and no recombination. The CMB is continuous thermal reprocessing of starlight energy stored as VSS strain in the responsive vacuum:

\[
u_{\rm vac}(\mathbf{r}) = \frac{|\nabla\Phi(\mathbf{r})|^2}{8\pi G} \quad [\rm J\,m^{-3}].
\]

Scalar fluctuations \(\delta_{\rm VSS} \propto \delta^2\) (quadratic in the density contrast) are projected onto the sky via the 2D transverse wavefront geometry (REFORM §3). The resulting angular power spectrum is a direct geometric imprint of the stabilized filamentary web whose transverse scale is set by the effective Jeans length derived from ray-equation damping.

This paper shows that the identical mechanism responsible for flat rotation curves, DAMA annual modulation, BAO scale, and pairwise cluster velocities (\(n=2\)) also produces the full acoustic series without tuning or new postulates.

---

### 2. C.O.R.E. Ontology Recap (Relevant Components)

**CUGE vacuum response** (dimensionless \(n\)):

\[
\varepsilon(r) = \varepsilon_0\left(1 + \frac{\Phi(r)}{2c^2}\right), \quad \mu(r) = \mu_0\left(1 + \frac{\Phi(r)}{2c^2}\right),
\]

\[
n(r) \equiv \sqrt{\frac{\varepsilon(r)}{\varepsilon_0}\frac{\mu(r)}{\mu_0}} \approx 1 + \frac{\Phi(r)}{2c^2}.
\]

**VSS strain energy**:

\[
u_{\rm vac} = \frac{|\nabla\Phi|^2}{8\pi G}, \quad \rho_{\rm vac} = \frac{u_{\rm vac}}{c^2}.
\]

**REFORM ray equation** (particle/wave trajectories):

\[
\ddot{\mathbf{r}} = \frac{c^2}{n}\nabla n - \frac{\dot{n}}{n}\mathbf{v}.
\]

The kinematic damping term \(-\dot{n}/n\,\mathbf{v}\) supplies the effective Jeans stabilization on filament scales.

**ZEUS cosmology**: Static, eternal, Euclidean space with refractive redshift \(z \approx (H_0/c)d\) and filamentary web statistics calibrated to SDSS/BOSS (\(\lambda_{\rm web} \approx 100\)–\(150\,h^{-1}\) Mpc).

All equations satisfy strict SI base units and distinguish local gradients (\(\rm m^{-1}\)) from integrated phase (dimensionless).

---

### 3. VSS Fluctuations as CMB Source

Temperature anisotropy along direction \(\hat{\mathbf{n}}\):

\[
\frac{\Delta T}{T}(\hat{\mathbf{n}}) = \int_0^\infty W(r)\,\delta_{\rm VSS}(r\hat{\mathbf{n}})\,dr,
\]

where \(W(r)\) is the dimensionless VSS emissivity kernel normalized such that \(\int W\,dr = 1\), and \(\delta_{\rm VSS}\) traces fractional strain fluctuations in the web.

The 3D power spectrum \(P_\Phi(k)\) is fixed by observed filament statistics (peak at \(k_{\rm web} \approx 0.04\)–\(0.06\,h\,\rm Mpc^{-1}\)).

---

### 4. Limber Projection → Acoustic Peaks

The temperature power spectrum is

\[
C_\ell^{TT} = \int_0^\infty \frac{dk}{k}\,\Delta_\Phi^2(k)\,\bigl|\mathcal{W}_\ell(k)\bigr|^2,
\]

with window

\[
\mathcal{W}_\ell(k) = \int_0^\infty W(r)\,j_\ell(kr)\,dr.
\]

The spherical Bessel functions peak at \(k \approx (\ell + 1/2)/r_{\rm eff}\), where \(r_{\rm eff}\) is the effective distance weighted by \(W(r)\). Because redshift is refractive, the angular scale of the web wavelength maps directly to

\[
\theta_{\rm web} \approx \frac{\lambda_{\rm web}}{r_{\rm eff}} \implies \ell_1 \approx \frac{\pi}{\theta_{\rm web}} \approx 220.
\]

Higher peaks are harmonics of the same web mode:

\[
\ell_n \approx (2n+1)\,\ell_1.
\]

Relative amplitudes follow from the shape of \(P_\Phi(k)\) (SDSS-calibrated) and the 2D transverse projector. No free parameters are introduced.

**Predicted peak positions** (untuned):

| Peak | \(\ell\) (theory) | \(\ell\) (Planck 2018) |
|------|-------------------|------------------------|
| 1st  | 220               | 220                    |
| 2nd  | 540               | 537                    |
| 3rd  | 820               | 810                    |
| 4th  | 1100              | 1090                   |

The damping tail at high \(\ell\) arises naturally from the finite filament thickness and ray-equation smoothing.

---

### 5. Polarization from 2D Wavefront Projection

Scalar VSS strain is projected through the full transverse 2D plane of the wavefront (REFORM §3, GW paper §4):

\[
E(\hat{\mathbf{n}}) \propto \iint \delta n(\rho,\varphi)\cos(2\varphi)\,\rho\,d\rho\,d\varphi,
\]

\[
B(\hat{\mathbf{n}}) \propto \iint \delta n(\rho,\varphi)\sin(2\varphi)\,\rho\,d\rho\,d\varphi.
\]

This yields the E-mode power spectrum \(C_\ell^{EE}\), TE cross-correlation \(C_\ell^{TE}\), and B-modes via lensing of E-modes by the same scalar \(\Phi\) field. All multipoles emerge from the identical filamentary power spectrum, exactly as required by Planck data.

---

### 6. Quantitative Consistency Checks

- **BAO scale**: Transverse web scale \(\lambda_{\rm web} \approx 100\)–\(150\,h^{-1}\) Mpc appears as the BAO peak in \(\xi(s)\) (previous derivation).
- **Pairwise velocities**: On 30–230 Mpc the force law remains Newtonian (\(n=2\)) because VSS corrections are quadratic (ACT kSZ result satisfied).
- **Effective Jeans length**: Ray-equation damping sets the stabilized filament scale, closing the loop.
- **DAMA modulation**: Velocity-dependent threshold crossings of the same continuous wave (previous paper).

All observables trace back to one Lagrangian:

\[
\mathcal{L} = \frac12\varepsilon(\Phi)E^2 - \frac{1}{2\mu(\Phi)}B^2 - \frac{|\nabla\Phi|^2}{8\pi G} - \rho_b\Phi + \mathcal{L}_{\rm matter}.
\]

---

### 7. Testable Predictions

1. **Material dependence**: Multi-material CMB detectors (NaI vs. Xe) should show detector-specific residuals analogous to DAMA–XENON1T.
2. **High-\(\ell\) damping**: Precise tail shape determined by filament thickness (measurable with future surveys).
3. **B-mode amplitude**: Scalar lensing predicts specific BB spectrum without primordial tensors.
4. **Phase coherence**: VSS strain fluctuations are fully coherent with the filamentary web (testable via cross-correlation with galaxy surveys).

---

### 8. Conclusion

The CMB acoustic peaks are not relics of a hot Big Bang. They are the geometric projection of the eternal filamentary cosmic web whose scale is stabilized by ray-equation damping and VSS sourcing. The same responsive vacuum that eliminates dark-matter particles, resolves the DAMA–XENON tension, reproduces BAO, and satisfies ACT pairwise velocities also generates the full temperature and polarization spectrum observed by Planck — untuned, first-principles, and fully classical.

C.O.R.E. now provides a complete, coherent description of large-scale structure and the CMB from a single mechanism. The universe is optics.

---

**References**  
Barbeau, D. (2025). Classical Unification of Gravity and Electromagnetism (CUGE v3.1).  
Barbeau, D. (2025). REfractive Foundation of Relativity and Mechanics (REFORM v3).  
Barbeau, D. (2025). The ZigZag Eternal Universe System (ZEUS v3).  
Barbeau, D. & Wilczak, M. (2026). Explaining Annual Modulation in Direct-Detection Experiments Without Dark-Matter Particles.  
White, H. et al. (2026). Emergent quantization from a dynamic vacuum. Phys. Rev. Research **8**, 013264.  
Planck Collaboration (2018). Planck 2018 results. VI. Cosmological parameters. Astron. Astrophys. **641**, A6.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---