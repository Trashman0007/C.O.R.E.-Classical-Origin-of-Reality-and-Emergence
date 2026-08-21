# Quantitative account of sequential single-site detection under a continuous wave

**David Barbeau, Independent Researcher**  
david@bigbadaboom.ca | www.bigbadaboom.ca  

July 30, 2026, Revision 1

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.  
©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

We work entirely inside ordinary Maxwell electrodynamics plus material response in flat Euclidean 3-space. No ontological photons and no multi-path ontology are required.

### 1. Continuous intensity envelope

The electromagnetic field that reaches the detector is a continuous wave. Its intensity distribution $I(\mathbf{r})$ on the screen is fixed by the classical diffraction integral (Huygens–Fresnel / Kirchhoff). Constructive interference produces maxima; destructive interference produces minima. The field is spatially extended.

### 2. Statistical material thresholds

Each detector site (AgBr grain, APD micro-cell, etc.) is characterised by an energy threshold $\phi$. These thresholds are not identical. They are drawn from a continuous density $\rho(\phi)$ that reflects grain-size variation, lattice defects, impurities and thermal fluctuations — the same continuum of thresholds that appears in the cascading-residual treatment of blackbody radiation.

### 3. Local firing probability

In a short exposure interval $\Delta t$ the energy fluence incident on a site of effective area $a$ located at $\mathbf{r}$ is

$$E(\mathbf{r}) = I(\mathbf{r})\, a\, \Delta t.$$

The probability that the site fires is the probability that its particular threshold lies below the available energy:

$$P_{\text{fire}}(\mathbf{r}) = \int_0^{E(\mathbf{r})} \rho(\phi)\, d\phi.$$

When the mean fluence is far below the mean threshold ($\langle E\rangle \ll \langle\phi\rangle$), this probability is small for every site. Firing events are therefore rare.

### 4. Energy accounting after the first absorption

Suppose a site at $\mathbf{r}_1$ does fire and absorbs energy $\approx\phi_1$. By ordinary energy conservation the continuous field in the immediate neighbourhood of that site is reduced by that amount. The residual energy left in the same local segment of the wavefront is

$$E_{\text{residual}} = E(\mathbf{r}_1) - \phi_1 < 0$$

(or at best a still smaller positive remainder). Consequently the probability that a second, independent site in the same local neighbourhood also crosses its own threshold from the same weak wavefront segment is second-order small:

$$P_{\text{second}} \propto P_{\text{fire}}(\mathbf{r}_1) \times P_{\text{fire}}(\mathbf{r}_2 \approx \mathbf{r}_1) \ll P_{\text{fire}}.$$

No superluminal “steering” or non-local collapse is required. The continuous field simply has a finite energy content in any finite region; once one threshold has been paid, the remainder is even further below the thresholds of neighbouring sites.

### 5. Sequential single-dot statistics

Because the mean number of firings per wavefront segment is $\ll 1$, the detections form a Poisson process whose rate is proportional to the continuous intensity envelope $I(\mathbf{r})$. The first successful threshold crossing on a given weak segment is almost always solitary. Subsequent wavefronts (or later portions of a longer exposure) sample the same envelope independently, gradually building the familiar interference pattern one discrete registration at a time.
This is the direct spatial analogue of the cascading-residual mechanism: a continuous energy distribution interacting with a continuum of material thresholds $\rho(\phi)$ produces discrete, sequential registration events. The “drain dimensions” are simply the local spatial scale over which the continuous field’s energy is shared; once that local budget has paid one threshold, further crossings from the same budget become negligible.
The mathematics is ordinary classical wave propagation plus statistical material response. The path-integral (diffraction-integral) language is used only as a calculational tool for the continuous intensity map; it does not imply that any single entity travels multiple routes at once.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2026 David Barbeau | david@bigbadaboom.ca

---
