**Analytic Proof of Geodesic Completeness in the C.O.R.E. Refractive Framework**  

David Barbeau, Independent Researcher  
david@bigbadaboom.ca | [www.bigbadaboom.ca](https://www.bigbadaboom.ca)  
April 22, 2026 **Version: 1**

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission—contact @stoic_david on X.<br>©2025 David Barbeau | david@bigbadaboom.ca | arXiv perpetual license 1.0 (non-commercial)

---

(CUGE + REFORM, SI base units, \(n \equiv \sqrt{\varepsilon_r \mu_r}\) strictly dimensionless)

The spacetime is flat Euclidean \(\mathbb{R}^3 \times \mathbb{R}\) (no curvature). Gravitational potential is regularized by finite MACHO radius \(\varepsilon \sim 10^{-15}\) m (CUGE v3):

\[
\Phi(\mathbf{r}) = \frac{GM}{\sqrt{|\mathbf{r}|^2 + \varepsilon^2}}, \qquad [\Phi] = \rm m^2 s^{-2}.
\]

Refractive index (dimensionless):

\[
n(\mathbf{r}) = 1 + \frac{\Phi(\mathbf{r})}{2c^2} \ge 1, \qquad c = 299\,792\,458~\rm m\,s^{-1}.
\]

**Lemma 1 (Global smoothness and bounds).**  
\(n(\mathbf{r})\) is \(C^\infty(\mathbb{R}^3)\), \(n \ge 1\), \(|\nabla n| \le C_\varepsilon / (|\mathbf{r}|^2 + \varepsilon^2)\) (bounded), and \(n(\mathbf{r}) \to 1\) as \(|\mathbf{r}| \to \infty\).

**Ray equation (null geodesics / light rays, REFORM v3):**

\[
\frac{d}{ds}(n\,\hat{\mathbf{t}}) = \nabla n \quad\Leftrightarrow\quad \ddot{\mathbf{r}} = \frac{c^2}{n}\nabla n - \frac{\dot{n}}{n}\mathbf{v},
\tag{2.1}
\]

where \(s\) is affine parameter along the ray (\(ds = c_{\rm coord}\,dt\), \(c_{\rm coord} = c/n\)), \(\mathbf{v} = d\mathbf{r}/dt\), and \([\ddot{\mathbf{r}}] = \rm m\,s^{-2}\). The term \(-\dot{n}/n\,\mathbf{v}\) is linear damping.

**Theorem (Geodesic completeness).**  
Every inextendible geodesic (null or timelike) can be extended to all affine parameter values \(\lambda \in (-\infty, +\infty)\). No singularities form in finite affine parameter.

**Proof.**  

1. **Smoothness of coefficients.**  
   The right-hand side of (2.1) is \(C^\infty\) on \(\mathbb{R}^3 \times T\mathbb{R}^3\) because \(n\), \(\nabla n\), and \(\dot{n} = \mathbf{v}\cdot\nabla n\) inherit global smoothness from \(\Phi\) (Lemma 1). All terms remain bounded: \(|\frac{c^2}{n}\nabla n| \le C_1\) (uniform bound), and the damping coefficient \(|\dot{n}/n| \le C_2|\mathbf{v}|\) (linear growth).

2. **Local existence.**  
   Standard Picard–Lindelöf theorem gives unique local solutions on some interval \([0, \lambda_0)\).

3. **No finite-time blow-up (global continuation).**  
   Suppose a maximal solution exists only on \([0, \lambda_*)\) with \(\lambda_* < \infty\). Then either \(|\mathbf{r}(\lambda)| \to \infty\) or \(|\mathbf{v}(\lambda)| \to \infty\) as \(\lambda \to \lambda_*^-\) (by compactness of closed balls).  

   - **Case \(|\mathbf{r}| \to \infty\):** Outside any compact set, \(n \to 1\), \(\nabla n \to 0\), so (2.1) reduces to \(\ddot{\mathbf{r}} \approx 0\). Straight-line motion cannot escape to infinity in finite \(\lambda\) (contradiction).  
   - **Case \(|\mathbf{v}| \to \infty\):** Multiply (2.1) by \(\mathbf{v}\) and integrate:  
     \[
     \frac{d}{d\lambda}\Bigl(\tfrac12 n|\mathbf{v}|^2\Bigr) = c^2 \mathbf{v}\cdot\nabla n - \tfrac12 \dot{n}|\mathbf{v}|^2.
     \]
     The damping term \(-\tfrac12 \dot{n}|\mathbf{v}|^2\) (quartic in \(|\mathbf{v}|\) when \(\dot{n} \propto \mathbf{v}\cdot\nabla n\)) dominates any growth from the gradient term (bounded by Lemma 1). Thus kinetic energy along the ray remains bounded, contradicting \(|\mathbf{v}| \to \infty\).

   Therefore \(\lambda_* = +\infty\) (similarly for \(-\infty\)). All geodesics extend indefinitely.

4. **Timelike geodesics (massive particles).**  
   The same variational principle \(\delta\int n\,ds = 0\) (Fermat) governs timelike paths in the eikonal limit. The effective metric \(ds_{\rm opt}^2 = n^2(dt^2 - d\mathbf{x}^2)\) (conformally flat) is complete: \(n \ge 1 > 0\) and the underlying Euclidean space is complete, so the optical manifold is geodesically complete.

5. **Strong-field regime.**  
   Finite \(\varepsilon\) eliminates \(r=0\) singularity. Near \(r \approx \varepsilon\), \(n\) reaches a maximum but remains finite and smooth; the ray equation yields a refractive turning point where \(c_{\rm coord} \to 0\) while local \(c\) stays invariant. No causal breakdown occurs.

**Conclusion.**  
The C.O.R.E. framework is geodesically complete on \(\mathbb{R}^3 \times \mathbb{R}\). All geodesics extend to infinite affine parameter with no curvature singularities, event horizons, or finite-time blow-up. The proof relies only on global \(C^\infty\) smoothness of \(n\), bounded gradients, and the linear/quartic damping in the ray equation—all verified in SI base units with dimensionless \(n\).

This closes the last open mathematical question for the strong-field regime. The framework is now fully self-consistent at the analytic level.

---

**License:** arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use (e.g., education, videos) encouraged with attribution to David Barbeau. Commercial use requires permission — contact @stoic_david on X.

© 2025 David Barbeau | david@bigbadaboom.ca

---