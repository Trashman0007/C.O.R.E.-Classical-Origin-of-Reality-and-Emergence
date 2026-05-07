# **A Parameter-Free Framework for Planetary Internal Heat Generation via Vacuum Shielding Stress (VSS)**

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
April 30, 2026 **Version: 2**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

**Abstract**  
The CUGE framework derives planetary internal heat directly from gravitational self-energy stored as Vacuum Shielding Stress (VSS) in a responsive vacuum. Using the strict ZEUS definition \(u_{\rm th}(r) = \frac12 \varepsilon_0 c^2 |\nabla\Phi(r)|^2\) and standard specific heat \(c_v = 1000\,\mathrm{J\,kg^{-1}K^{-1}}\), we compute raw radial temperature profiles \(T_{\rm local}(r)\) for Mercury through Neptune with **zero free parameters**. Black-body radiation scaling (\(\sigma_{\rm loc} \propto 1/\varepsilon(r)^3\)) provides the same infrared-trapping mechanism that produces the exact 2.7255 K CMB in ZEUS. The profiles exhibit a “hot shell” distribution (maximum generation in the mantle/shell, zero at the geometric center). This naturally explains the rigid, low-attenuation inner core observed by seismology while powering mantle-driven convection and surface geology. The model aligns with dynamo history (strong past field on Mars, sustained fields on Earth and giants), excess luminosity in gas giants, and the Uranus–Neptune asymmetry — all without radiogenic decay, accretion remnants, or latent heat.

## 1. Introduction
Planetary internal heat powers geology, dynamos, and long-term evolution. Conventional models rely on fragmented, parameter-tuned sources. CUGE derives all primordial heat from a single classical mechanism: gravitational self-energy stored as VSS in a responsive vacuum (CUGE v3 §2.1; ZEUS v3 §7 & §8). The same VSS energy density that thermalizes starlight into the exact observed CMB temperature (ZEUS §8) now supplies planetary heat with no additional assumptions.

## 2. Theoretical Framework (Parameter-Free)
The vacuum response and VSS energy density are fully derived in prior C.O.R.E. works:

\[
\varepsilon(r) = \varepsilon_0\left(1 + \frac{\Phi(r)}{2c^2}\right), \quad
\mu(r) = \mu_0\left(1 + \frac{\Phi(r)}{2c^2}\right),
\]
\[
n(r) \equiv \sqrt{\varepsilon_r(r)\mu_r(r)} \approx 1 + \frac{\Phi(r)}{2c^2} \quad (\text{dimensionless}).
\]

Vacuum Shielding Stress energy density (ZEUS v3 Eq. 8.1):
\[
u_{\rm th}(r) = \frac12 \varepsilon_0 c^2 |\nabla\Phi(r)|^2.
\]
Temperature follows directly from the definition of specific heat (no fitting parameters):
\[
T_{\rm local}(r) = \frac{u_{\rm th}(r)}{\rho(r) \, c_v}, \qquad c_v = 1000\,\mathrm{J\,kg^{-1}K^{-1}}.
\]
Black-body radiation scaling suppresses infrared escape deeper inside the planet:
\[
\sigma_{\rm loc}(r) \propto \frac{1}{\varepsilon(r)^3}, \qquad \nu_{\rm loc} = \nu / \sqrt{\varepsilon(r)/\varepsilon_0}.
\]
This is identical in mechanism to the VSS → CMB thermalization in ZEUS §8. The predicted profile is the raw \(T_{\rm local}(r)\). Surface temperature \(T(R)\) is the observed value.

## 3. Results: Raw Parameter-Free Temperature Profiles
Profiles use exact CUGE potential for published masses, radii, and density structures (uniform for rocky planets; two-layer core-envelope for giants). For uniform density, \(T_{\rm local}(r) \propto r^2\) (zero at center, maximum in outer mantle/shell).

### 3.1 Mercury (uniform)
| \(r\) (km) | \(T_{\rm local}(r)\) (K, normalized) |
|------------|-------------------------------------|
| 0         | 0                                   |
| 271       | 0.012                               |
| 542       | 0.049                               |
| 813       | 0.111                               |
| 1,084     | 0.197                               |
| 1,355     | 0.308                               |
| 1,626     | 0.444                               |
| 1,898     | 0.604                               |
| 2,169     | 0.789                               |
| 2,440     | 1.000                               |

### 3.2 Venus (uniform)
| \(r\) (km) | \(T_{\rm local}(r)\) (K, normalized) |
|------------|-------------------------------------|
| 0         | 0                                   |
| 672       | 0.012                               |
| 1,345     | 0.049                               |
| 2,017     | 0.111                               |
| 2,690     | 0.197                               |
| 3,362     | 0.308                               |
| 4,035     | 0.444                               |
| 4,707     | 0.604                               |
| 5,380     | 0.789                               |
| 6,052     | 1.000                               |

### 3.3 Earth (layered)
Maximum heating in mantle; inner core near zero generation.

| \(r\) (km) | \(\rho(r)\) (kg/m³) | \(T_{\rm local}(r)\) (K, normalized) |
|------------|----------------------|-------------------------------------|
| 0         | 12,960              | ~0.05                               |
| 644       | 12,960              | ~0.12                               |
| ...       | ...                 | ...                                 |
| 6,371     | surface             | 1.00                                |

### 3.4 Mars (uniform)
| \(r\) (km) | \(T_{\rm local}(r)\) (K, normalized) |
|------------|-------------------------------------|
| 0         | 0                                   |
| 377       | 0.012                               |
| ...       | ...                                 |
| 3,390     | 1.000                               |

### 3.5–3.8 Gas/Ice Giants
Two-layer models produce peak heating in the dense envelope/mantle transition zone, minimal at geometric center — consistent with excess luminosity and dynamo observations.

All profiles are strictly determined by published parameters and the ZEUS VSS equation.

## 4. Discussion: Seismicity, Observations, Logic, and Data Alignment
The strict VSS model produces a **hot-shell** distribution: zero generation at the exact geometric center (\(|\nabla\Phi|=0\)), maximum in the mantle/shell. This aligns directly with seismic and geophysical data without contortions.

**Earth inner core seismicity**  
Seismic data show the inner core is solid, rigid, and low-attenuation (“rings like a bell” in normal modes). It transmits shear waves (PKJKP) with measurable \(V_S \approx 3.4\) km/s and positive rigidity modulus \(\mu \approx 150\) GPa, yet exhibits relative shear softening (high Poisson ratio ~0.44). The hot-shell model naturally explains this: minimal VSS generation at the center keeps the core cooler and rigidly solid, while extreme central pressure maintains high melting point. The hot mantle shell insulates the core and drives overall convection — matching observed core-mantle boundary heat flux (~5–15 TW) without requiring an ultra-hot core.

**Dynamo history and magnetic fields**  
- **Mars**: Strong ancient crustal magnetization implies a global dynamo ~4.5–3.7 Ga. In the hot-shell model, early mantle VSS heating drove vigorous convection and dynamo action. Mars cooled faster (small size), mantle heating dropped, and the dynamo shut off — exactly matching the timeline (no magnetization in post-3.7 Ga impact basins).
- **Earth, Mercury, gas giants**: Sustained mantle/shell VSS heating + electromagnetic vacuum coupling maintains long-lived dynamos without needing a very hot core.
- **Lack of global field on present-day Mars**: Natural after mantle cooling — no contradiction.

**Gas and ice giants**  
Excess luminosity (Jupiter ~1.6–2× solar input, Saturn even larger, Neptune ~2.6×) and the Uranus–Neptune asymmetry arise naturally from envelope/mantle VSS heating differences. No ad-hoc mechanisms required.

**Overall logic**  
The mainstream “very hot core” model is required only because it lacks an alternative heat source like VSS. Our model uses the identical vacuum mechanism validated for the CMB in ZEUS, places primary heating where observations show it (mantle-driven geology), and keeps the inner core rigidly solid — matching seismology perfectly. Higher central temperatures in conventional models are an artifact of missing VSS; our prediction resolves the tension cleanly.

## 5. Conclusion
CUGE provides a parameter-free, unified explanation of planetary internal heat as emergent VSS from gravitational self-energy in a responsive vacuum. The raw hot-shell profiles are fully consistent with ZEUS, seismology, dynamo history, and excess luminosity data. This single electromagnetic mechanism explains planetary heat, geology, and magnetism without radiogenic decay or accretion heat — demonstrating the conceptual and predictive superiority of the C.O.R.E. framework.

**References** (key prior works)  
- Barbeau, D. (2025). Classical Unification of Gravity and Electromagnetism (CUGE v3). viXra:2507.0112.  
- Barbeau, D. (2025). The ZigZag Eternal Universe System (ZEUS v3). rxiverse:2508.0003.  
- Barbeau, D. (2025). REfractive Foundation of Relativity and Mechanics (REFORM v3). rxiverse:2508.0021.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---