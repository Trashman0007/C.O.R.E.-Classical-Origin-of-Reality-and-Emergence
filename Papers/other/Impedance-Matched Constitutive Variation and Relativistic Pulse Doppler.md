# Impedance-Matched Constitutive Variation and Relativistic Pulse Doppler

**A short note on when a variable- $\varepsilon,\mu$ wave equation reproduces Maxwell energy and momentum shifts**

**David Barbeau**  
Independent Researcher  
david@bigbadaboom.ca | www.bigbadaboom.ca  

September 24, 2026 · Version 1

License: arXiv.org perpetual, non-exclusive license 1.0. Non-commercial use encouraged with attribution. Commercial use requires permission — contact @stoic_david on X.  
© 2026 David Barbeau | david@bigbadaboom.ca

---

## Abstract

A vacuum electromagnetic pulse carries energy $U$ and momentum $P=U/c$. Maxwell electrodynamics then implies the relativistic Doppler law for both energy and momentum. A generic mechanical wave equation does not. This note shows the precise constitutive restriction under which a variable-$\varepsilon,\mu$ analog *does* reproduce the Maxwell result: the analog must preserve the two locally measured combinations

$$
Z=\sqrt{\frac{\mu}{\varepsilon}},
\qquad
c=\frac{1}{\sqrt{\varepsilon\mu}}
$$

and must not introduce a preferred rest frame. Observers never measure $\varepsilon$ and $\mu$ separately. They measure $Z=E/H$ and $c=E/B$, then infer

$$
\varepsilon=\frac{1}{Zc},\qquad\mu=\frac{Z}{c}.
$$

Any variation that leaves those two local readings unchanged leaves every observer reporting the same local constants. A filament or sound-like medium with a rest frame is excluded by this criterion, which is why it yields a different Doppler law.

---

## 1. The question

The request is twofold.

1. Show that a mechanical wave equation with varying $\mu$ and $\varepsilon$ in vacuum yields the same Doppler *energy* and *momentum* shifts as Maxwell’s equations, given that an electromagnetic pulse has momentum $U/c$.
2. State how $\mu$ and $\varepsilon$ vary so that different observers measure the same values locally.

The first claim is not automatic. It is true only under a restriction on the variation. The second is an operational statement about what is actually measured.

---

## 2. Maxwell vacuum pulses

In source-free vacuum Maxwell’s equations imply the wave equation

$$
\left(\nabla^2-\frac{1}{c^2}\partial_t^2\right)\mathbf{E}=0,
\qquad
c=\frac{1}{\sqrt{\varepsilon_0\mu_0}},
$$

and the same equation for $\mathbf{B}$. For a locally plane pulse

$$
|\mathbf{B}|=\frac{|\mathbf{E}|}{c},\qquad
\frac{|\mathbf{E}|}{|\mathbf{H}|}=Z_0=\sqrt{\frac{\mu_0}{\varepsilon_0}}.
$$

The field energy and momentum of a unidirectional pulse occupying volume $\mathcal{V}$ are

$$
U=\varepsilon_0 E^2\,\mathcal{V}=\frac{B^2}{\mu_0}\,\mathcal{V},
\qquad
\mathbf{P}=\frac{U}{c}\,\hat{\mathbf{k}}.
$$

That is the content of the remark that an electromagnetic pulse has momentum $e/c$: write $U$ for the pulse energy and

$$
P=\frac{U}{c}.
$$

The vacuum energy–momentum tensor then implies that $(U/c,\mathbf{P})$ transforms as a four-vector. For a pulse receding along its propagation axis at speed $v=\beta c$,

$$
\frac{U'}{U}=\frac{P'}{P}=\frac{f'}{f}=\sqrt{\frac{1-\beta}{1+\beta}}.
$$

Approaching, the sign of $\beta$ flips. The same factor follows from the Lorentz transformation of the wave four-vector $K^\mu=(\omega/c,\mathbf{k})$ with $\omega=ck$.

This is the Maxwell target. Any analog must reproduce $P=U/c$ *and* this factor.

---

## 3. What counts as a mechanical analog

A transverse string or elastic filament with a rest frame is *not* the analog of vacuum electromagnetism. Its wave equation

$$
\partial_{xx}u=\frac{1}{v^2}\partial_{tt}u
$$

has a distinguished frame in which the medium is at rest. Source and observer motion relative to that frame produce the Galilean factor

$$
f'=f\,\frac{v\pm v_{\rm obs}}{v\pm v_{\rm src}},
$$

and the wave’s momentum is not forced to equal $U/v$ in every inertial frame. That is the mismatch already noted in the thread.

The correct one-dimensional analog of Maxwell is the lossless telegrapher system, which is Maxwell reduced to a transmission line:

$$
\partial_x V=-\partial_t(\mu I),
\qquad
\partial_x I=-\partial_t(\varepsilon V).
$$

Eliminating $I$ gives

$$
\partial_x\left(\frac{1}{\mu}\partial_x V\right)=\partial_t(\varepsilon\,\partial_t V).
$$

Here $\varepsilon$ plays the role of capacitance per length and $\mu$ the role of inductance per length. The local wave impedance and phase speed are

$$
Z=\frac{V}{I}=\sqrt{\frac{\mu}{\varepsilon}},
\qquad
c=\frac{1}{\sqrt{\varepsilon\mu}}.
$$

If $\varepsilon$ and $\mu$ are constants, this *is* one-dimensional vacuum Maxwell. Power and momentum densities are

$$
S=VI=\frac{V^2}{Z},
\qquad
g=\frac{S}{c^2},
$$

so a unidirectional pulse again satisfies $P=U/c$.

The analog therefore starts already on the Maxwell side, not on the filament side. The only remaining question is which variations of $\varepsilon$ and $\mu$ preserve that fact.

---

## 4. Two variations, only one of which is vacuum

Write a local rescaling

$$
\varepsilon\to\lambda\,\varepsilon,\qquad\mu\to\sigma\,\mu.
$$

Then

$$
Z\to Z\sqrt{\frac{\sigma}{\lambda}},
\qquad
c\to\frac{c}{\sqrt{\lambda\sigma}}.
$$

- **Impedance-preserving, speed-changing.** $\sigma=\lambda$. Then $Z$ is fixed and $c$ changes. This is a refractive medium, not vacuum.
- **Speed-preserving, impedance-changing.** $\sigma=\lambda^{-1}$. Then $c$ is fixed and $Z$ changes. Local field ratios $E/H$ change. That is not the measured vacuum.
- **Vacuum redundancy.** $\lambda\sigma=1$ *and* $\sigma/\lambda=1$, hence $\lambda=\sigma=1$, or more generally any pair of transformations that is equivalent to a change of units. The only local invariants are $Z$ and $c$.

Vacuum phenomenology is the third case: both measured combinations stay fixed at each event,

$$
Z(x)=Z_0,\qquad c(x)=c.
$$

That still allows a *coordinate* description in which $\varepsilon$ and $\mu$ look as if they vary, provided they vary together so that

$$
\mu(x)=\frac{Z_0}{c},\qquad\varepsilon(x)=\frac{1}{Z_0 c}
$$

remain the same local numbers. It does *not* allow a medium rest frame, a preferred direction, or a refractive index different from $1$.

If those conditions are dropped, the analog leaves vacuum electrodynamics and the Doppler law changes.

---

## 5. Doppler from the analog

Assume the restriction of §4. Then the analog wave equation is locally

$$
\partial_{xx}V-\frac{1}{c^2}\partial_{tt}V=0
$$

with the same $c$ in every inertial frame, and the pulse still satisfies $P=U/c$.

Phase continuity on a null characteristic $x\pm ct=\text{const}$ is frame-independent once $c$ is. Boosting along the propagation axis therefore maps the wave four-vector exactly as in Maxwell theory,

$$
\omega'=\omega\,\gamma(1-\beta),\qquad
k'=\frac{\omega'}{c},
$$

which is

$$
\frac{\omega'}{\omega}=\sqrt{\frac{1-\beta}{1+\beta}}
$$

for a receding source. Because $U=\hbar\omega$ for a monochromatic component, or more classically $U\propto\omega$ for a fixed-cycle pulse, and because $P=U/c$,

$$
\frac{U'}{U}=\frac{P'}{P}=\frac{\omega'}{\omega}.
$$

That is the Maxwell energy and momentum shift.

The same calculation on a filament fails at the first step: the characteristics are $x\pm vt=\text{const}$ only in the medium frame, so the boosted frequency is Galilean and $P=U/v$ does not hold in the observer frame.

Thus:

> A variable- $\varepsilon,\mu$ wave equation reproduces Maxwell Doppler energy and momentum shifts if and only if it is the impedance-matched, constant- $c$ , rest-frame-free analog of §3–4. A mechanical filament is not that analog.

---

## 6. What observers actually measure

No inertial observer extracts $\varepsilon$ or $\mu$ by a standalone experiment in vacuum. The operational chain is:

1. Measure the travel time of a pulse over a local rod; this is $c_{\rm loc}$.
2. Measure the ratio of the transverse fields on the pulse; this is $Z_{\rm loc}=E/H=E/(cB)$.
3. Infer

$$
\varepsilon_{\rm loc}=\frac{1}{Z_{\rm loc}\,c_{\rm loc}},
\qquad
\mu_{\rm loc}=\frac{Z_{\rm loc}}{c_{\rm loc}}.
$$

Equivalently,

$$
c_{\rm loc}=\frac{1}{\sqrt{\varepsilon\mu}},
\qquad
Z_{\rm loc}=\sqrt{\frac{\mu}{\varepsilon}}.
$$

Experiments constrain the pair $(Z,c)$, not $\varepsilon$ and $\mu$ independently. That is why SI can treat $c$ as defined and absorb the remaining conventional freedom into the unit system: after the 2019 redefinition one measures the fine-structure constant and *assigns* $\mu_0=2\alpha h/(e^2 c)$, $\varepsilon_0=1/(\mu_0 c^2)$. The physics resides in the two combinations, not in two independent vacuum substances.

Consequently, different observers report the same local $\varepsilon$ and $\mu$ exactly when they report the same local $Z$ and the same local $c$. Under a Lorentz boost of a vacuum pulse those ratios are preserved: a boosted plane wave still satisfies $E'/H'=Z_0$ and $E'/B'=c$. The inferred constitutive pair is therefore the same in every inertial frame.

---

## 7. How $\varepsilon$ and $\mu$ are allowed to “vary”

Collecting the restriction:

$$
\boxed{
\mu(x)=\frac{Z_0}{c},\qquad
\varepsilon(x)=\frac{1}{Z_0 c}
}
$$

at every event, in every inertial frame, with the same numbers $Z_0$ and $c$. The only admissible “variation” is a joint rescaling that is cancelled by the way fields, charges, and units are defined, leaving $Z_0$ and $c$ untouched.

Two discarded options:

- Let $\varepsilon$ and $\mu$ scale by the same factor, keeping $Z$ but changing $c$. Local observers would then disagree about $c$, or one would have to rescale clocks and rods with them. That is a refractive medium, not vacuum.
- Let $\varepsilon$ and $\mu$ define a medium rest frame. Then the Doppler law becomes mechanical and conflicts with the measured electromagnetic shift.

So the answer to “how do they vary so that different observers measure the same values locally?” is: they do not vary as independent fields in vacuum. They co-vary, if they co-vary at all, so that every observer’s local instruments still read the same $Z_0$ and the same $c$, and therefore the same

$$
\varepsilon=\frac{1}{Z_0 c},\qquad\mu=\frac{Z_0}{c}.
$$

---

## 8. What this does not claim

This note does not derive Maxwell’s equations, assign numerical values to $c$ or $Z_0$, or treat gravity. Position-dependent $\varepsilon(\mathbf{x}),\mu(\mathbf{x})$ with only $Z=Z_0$ held fixed changes the coordinate phase speed and is a refractive model. That may be a separate theory; it is not required to answer the vacuum Doppler question, and it is not assumed here.

The only claim is the biconditional of §5 plus the operational identification of §6.

---

## 9. Conclusion

A variable-$\varepsilon,\mu$ wave equation reproduces the Maxwell Doppler law for pulse energy and momentum only when it is the impedance-matched analog of one-dimensional electrodynamics and introduces no medium rest frame. Under the restrictions

$$
Z=\sqrt{\frac{\mu}{\varepsilon}}=Z_0,\qquad
c=\frac{1}{\sqrt{\varepsilon\mu}},
$$

a unidirectional vacuum pulse still satisfies $P=U/c$, and a boost along the propagation axis yields

$$
\frac{U'}{U}=\frac{P'}{P}=\frac{f'}{f}=\sqrt{\frac{1-\beta}{1+\beta}}.
$$

A filament or other mechanical medium with a preferred frame does not satisfy these conditions and therefore does not yield the same shifts.

Local measurements never determine $\varepsilon$ and $\mu$ independently. An observer extracts $Z=E/H$ and $c=E/B$ from the pulse fields and travel time, then infers

$$
\varepsilon=\frac{1}{Zc},\qquad\mu=\frac{Z}{c}.
$$

Any constitutive variation that preserves those two local readings leaves every inertial observer with the same reported values of $\varepsilon$ and $\mu$.
