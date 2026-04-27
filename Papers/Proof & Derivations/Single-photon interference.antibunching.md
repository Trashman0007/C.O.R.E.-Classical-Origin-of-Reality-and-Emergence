# **Single-photon interference / antibunching**  

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
April 22, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

ASH models light as a continuous electromagnetic wave  
\[
E(t) = E_0 \cos(2\pi\nu t + \psi), \qquad I \propto E_0^2,
\]  
with energy flux conserved spherically (\(I \propto 1/r^2\)). Detection is a nonlinear, material-dependent threshold process. The local detection probability at a detector with analyzer angle \(\theta\) is  
\[
P_{\rm det}(\phi,\theta) = \frac{|\cos(2(\phi-\theta))|^\nu}{Z}, \qquad \nu = \frac{1}{d-1} \ge \frac13,
\]  
where \(\phi\) is the shared wave phase/polarization angle (\(\phi\sim{\rm Uniform}[0,2\pi)\)), \(\nu\) arises from vacuum-cloud geometry (CUGE), and \(Z\) normalizes \(\int_0^{2\pi} P_{\rm det}\,d\phi = 1\). All quantities are dimensionless; \(P_{\rm det}\) is a probability density.

**Single-photon interference.**  
A continuous wave packet of total integrated intensity normalized to \(\langle N\rangle\approx 1\) (one “quantum” worth of energy) is sent through a double-slit or interferometer. The wave interferes classically: intensity at detector position \(x\) follows the standard pattern \(I(x)\propto|\psi_1(x)+\psi_2(x)|^2\). Each detector samples locally via the threshold \(P_{\rm det}\propto I(x)^\nu\) (\(\nu>0\)). Post-selection on rare detection events (low-\(E_0\) regime) reproduces the classical interference fringes statistically, exactly as in Sturm’s double-slit and Jamin-interferometer analogs. No discrete photons are required; detections are sparse threshold crossings of the continuous field.

**Antibunching (Hong–Ou–Mandel / HBT type).**  
Consider a 50/50 beam splitter with two output ports feeding detectors D1 and D2. For a single low-amplitude wave packet (total energy \(\approx h_{\rm eff}\nu\)), the fields at the outputs are correlated:  
\[
E_1(t) = \frac{E_0}{\sqrt{2}} \bigl(A(t) + B(t)\bigr), \qquad E_2(t) = \frac{E_0}{\sqrt{2}} \bigl(A(t) - B(t)\bigr),
\]  
where \(A(t)\) and \(B(t)\) are the input-mode amplitudes (identical for indistinguishable “single-photon” input). For perfect destructive interference in the coincidence channel (phase-matched inputs), the instantaneous local intensities satisfy \(I_1(t) + I_2(t) = E_0^2 |A(t)|^2\) (energy conservation), but the product \(I_1(t)I_2(t)\) is suppressed when the wave amplitude is concentrated in one port.

The coincident detection probability in a small time bin \(\Delta t\) (dimensionless) is the expectation over the shared phase \(\phi\):  
\[
P_{\rm coin} = \int_0^{2\pi} \frac{d\phi}{2\pi} \, P_{\rm det}^{(1)}(\phi) \, P_{\rm det}^{(2)}(\phi),
\]  
with  
\[
P_{\rm det}^{(i)}(\phi) = \frac{|\cos(2(\phi - \theta_i))|^\nu}{Z}.
\]  
For HOM geometry (\(\theta_1 = \theta_2 + \pi/2\)), the product \(|\cos(2\phi)|^\nu \,|\sin(2\phi)|^\nu \propto |\sin(4\phi)|^\nu\) averages to a value suppressed by the nonlinearity \(\nu > 0\). In the low-intensity limit (\(E_0\) small, mean detections \(\langle n\rangle\ll 1\)), the single-detection rates are  
\[
P_i \propto \int_0^{2\pi} \frac{d\phi}{2\pi} \, |\cos(2(\phi - \theta_i))|^\nu,
\]  
while the coincidence rate scales as \(\sim E_0^{2\nu}\) (higher power because both thresholds must be crossed simultaneously by the shared wave packet). The normalized second-order correlation function is therefore  
\[
g^{(2)}(0) = \frac{P_{\rm coin}}{P_1 P_2} \propto \frac{\langle |\cos(2\phi)|^\nu |\sin(2\phi)|^\nu \rangle}{\langle |\cos(2\phi)|^\nu \rangle \langle |\sin(2\phi)|^\nu \rangle} < 1,
\]  
and approaches 0 for \(\nu \to \infty\) (sharp threshold) or perfect destructive interference. This reproduces antibunching purely from continuous-wave interference + nonlinear threshold detection (no discrete photons).

**Dimensional verification.**  
All \(P_{\rm det}\) and \(g^{(2)}(0)\) are dimensionless probabilities. The wave amplitude \(E_0\) cancels in ratios; only relative phases and thresholds (dimensionless after normalization) enter.

**Connection to experiments.**  
Sturm’s classical analogs (double-slit deficit, hidden energy, Bell/CHSH with multipliers) already demonstrate the same mechanism: shared continuous fields + nonlinear post-selection produce quantum-like statistics. The above calculation closes the gap for antibunching/HOM without invoking photons or non-locality.

This derivation uses only the existing ASH power-law detection probability and shared hidden variable \(\phi\), preserving continuity, locality, and all prior C.O.R.E. results. The open question is now resolved analytically.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---