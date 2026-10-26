# Timing information and global microscopic precision

[Controlled sensing](sensing_bridge.md) · [Ideal contact law](global_contact_precision.md) · [Companion global sensing proof](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md)

A timing error is not specified by its magnitude alone. A fixed pulse displacement gives a definite conditional quantum operation; unobserved independent timing fluctuations mix different operations. This page separates those experiments and proves a global limitation for one precisely defined timing menu. The controller may select plain cells or cells containing one imperfect echo, but may not insert further pulses inside a cell.

## Timing model and counted resources

Fix $`g,h>0`$, $`\chi=gh\in(0,\pi/4)`$, nominal compensation $`\omega_0`$, and one shared unknown angle $`\phi`$. Write $`\epsilon=\omega-\omega_0`$ and $`N'_\phi=\partial_\phi N_\phi`$. A cell uses the Hamiltonian

```math
H_\pm=\frac{\epsilon}{2}Z_S\otimes I_E
\pm gN_\phi\otimes X_E,
\qquad R=\sqrt{g^2+\epsilon^2/4}.
```

A physical $`Z_S`$ pulse at time $`h/2+\delta`$ gives, after removing the known accumulated pulse frame,

```math
V_\delta=e^{-iH_-(h/2-\delta)}e^{-iH_+(h/2+\delta)}.
```

The frame depends on the number of pulses, not their displacement, and is absorbed into later boundary instruments or terminal readout. In the constructions below, its known correction is composed with the already counted endpoint instrument; it is never an additional free physical pulse. Every bath qubit is prepared at time zero, interacts once, and is retained afterward without access or reuse.

A **systematic displacement** is one fixed $`\delta`$ throughout the experiment. If it is known and the commanded pulse position can be adjusted, moving the command by $`-\delta`$ restores the midpoint with the same one-pulse contact count. This uses a calibrated timing setting. An unknown systematic displacement requires a specified calibration model; knowing an estimate does not supply an exact timing correction for free.

The **hidden-jitter model** below instead has $`\delta=+d`$ or $`-d`$ with equal probabilities, independently in each pulsed cell, where $`0<d<h/2`$ is known. The realized signs are never available to the controller, and the fluctuations are independent of the unknown parameters, controls and earlier records. A pulsed cell always contains exactly one $`Z_S`$ pulse. There is no further contact within that cell, no adjustable pulse-position menu, and no physical retuning of the compensation.

At each cell entrance, a classical controller may choose a plain cell or this jittered-echo cell using its available record. Boundary operations on the sensor and protected memory may be adaptive, and all measurement outcomes are retained. For $`n`$ cells, the original contact accounting permits at most $`n-1`$ total nonterminal system contacts, of which at most $`m`$ are jittered interior pulses. Each nonterminal boundary instrument also counts. Initial preparation and terminal readout at $`T=nh`$ are free. The converse will relax the boundary-contact budget, which only strengthens it.

## Exact displaced and averaged instruments

Define real coefficients

```math
D=\cos(2R\delta)-\cos(Rh),\qquad
u=\cos(Rh)+\frac{g^2}{R^2}D,\qquad
v=\frac{\epsilon}{2R}\sin(Rh),
```

```math
w=\frac gR\sin(2R\delta),\qquad
x=\frac{\epsilon g}{2R^2}D.
```

Direct multiplication of the two joint propagators gives the bath-input Kraus operators

```math
K_0=uI-ivZ_S,\qquad
K_1=-i(wN_\phi+xN'_\phi).
```

In particular $`u^2+v^2+w^2+x^2=1`$. Because $`N_\phi`$ and $`N'_\phi`$ anticommute, each parity branch of this fixed-displacement experiment is proportional to a unitary. The flip axis has a known frequency-dependent displacement relative to $`\phi`$.

For hidden symmetric jitter, evaluate the coefficients at $`\delta=d`$. Only $`w`$ changes sign when the timing sign changes. Averaging the two physical channels therefore gives the exact three-Kraus representation

```math
L_0=uI-ivZ_S,\qquad
L_1=-iwN_\phi,\qquad
L_2=-ixN'_\phi.
```

A parity measurement distinguishes $`L_0`$ from the combined odd branch, but does not identify $`L_1`$ versus $`L_2`$. That missing label cannot be treated as an observed trajectory. The coefficients, including their frequency dependence, come from the same fixed Hamiltonian and clock; this is not a subdivision of a Markov endpoint channel.

## Calibrated systematic displacement

For each fixed known $`0<|\delta|<h/2`$, a menu of plain cells and cells pulsed at $`h/2+\delta`$ retains quadratic **global** precision on some fixed sufficiently small band around compensation. The known displacement is supplied as part of the device specification; this is not a theorem for learning an unknown displacement. Retiming is not needed for this assertion. The signal-generator bound supplies the matching inverse-quadratic risk lower order.

Write $`z=2g\delta`$. Near $`\epsilon=0`$, $`w`$ has a fixed nonzero sign. Absorb that sign into the flip branch's scalar phase and define smooth known functions

```math
\theta_{\rm e}(\epsilon)=2\arctan(v/u),
\qquad
\zeta_{\rm e}(\epsilon)=\arctan(x/w).
```

The pulsed cell's normalized flip is $`N_{\phi+\zeta_{\rm e}}`$. The plain cell has its usual no-flip phase $`\theta_0`$ and $`\zeta_0=0`$. At compensation, set $`p_{\rm e}=\sin^2 z`$, $`p_0=\sin^2\chi`$, and

```math
d_{\rm e}=\theta'_{\rm e}(0)=\frac{\sin\chi}{g\cos z},
\qquad
z_{\rm e}=\zeta'_{\rm e}(0)
=\frac{\cos z-\cos\chi}{2g\sin z},
\qquad
d_0=\frac{\tan\chi}{g}.
```

The transition rewards must include the flip-axis phase. Define $`f_{\rm e}=(1-p_{\rm e})d_{\rm e}-2p_{\rm e}z_{\rm e}`$ and $`f_0=(1-p_0)d_0`$. Their exact contrast is

```math
\frac{f_{\rm e}}{p_{\rm e}}-\frac{f_0}{p_0}
=
\frac{(\sin\chi-\sin z)\sin(\chi+z)}
{g\sin\chi\,\sin^2z}>0
\qquad (0\lt |z|\lt \chi).
```

Use the pulsed setting in the even sector and the plain setting in the odd sector, measuring parity at boundaries. With $`\sigma_{i-1}`$ the preceding parity sign, every retained record ending even has the exact nuisance-independent phase

```math
\Phi_R(\epsilon)
=\sum_i\sigma_{i-1}
\left[
\mathbf1_{\rm stay}\theta_{j_i}(\epsilon)
-2\mathbf1_{\rm flip}\zeta_{j_i}(\epsilon)
\right].
```

This follows by commuting the known $`Z`$ rotations past successive flips; the shared $`N_\phi`$ factors cancel in pairs. The stationary phase-derivative drift at zero is

```math
\mu_0=\frac{p_0f_{\rm e}-p_{\rm e}f_0}{p_{\rm e}+p_0}>0.
```

For completeness, a parameter-independent acceptance event can be certified as follows. Freeze each transition reward at zero and let $`D_R^0`$ be its sum over $`L`$ cells. By continuity, shrink the frequency band, independently of $`L`$, so that the two-state parity chain has $`p_{\rm e}<p_0<1/2`$, the stationary mean of this frozen reward is at least $`3\mu_0/4`$, and its even-minus-odd conditional mean is positive. Its mean starting even is then at least $`3\mu_0L/4`$, including the nonnegative transient term.

The frozen transition reward is uniformly bounded by a constant $`M`$. If $`\rho<1`$ bounds the chain's nontrivial eigenvalue uniformly on the band, conditioning across the intervening transitions bounds its covariance sum by $`VL`$, where one may take $`V=M^2[1+2/(1-\rho)]`$. Thus Chebyshev's inequality and the final-even probability of at least $`1/2`$ imply

```math
\Pr\{\text{final even and }D_R^0\ge\mu_0L/2\}
\ge\frac14
\qquad \left(L\ge\frac{64V}{\mu_0^2}\right).
```

Shrink the same fixed band further so every actual derivative reward differs from its frozen value by at most $`\mu_0/4`$. Every accepted record then obeys $`\mu_0L/4\le\Phi'_R(\epsilon)\le\beta L`$ throughout the band, for a fixed finite $`\beta`$. The [recorded-phase estimation theorem](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/recorded_phase_estimation.md) applies directly to these known record-dependent phase functions, giving $`O(B^{-2})`$ worst-case risk with a hard budget of $`B`$ active cells. Its repetitions, rejected records and multiscale ambiguity resolution are all included in that budget.

An active cell uses at most one interior pulse and one boundary instrument. Taking $`B=\min\{m,\lfloor(n-1)/2\rfloor\}`$ charges the last active readout as an early contact and fits at most $`n-1`$ total contacts over the full horizon $`nh`$; at most $`B\le m`$ are interior pulses. Store the estimate through the remaining physical cells. This proves the quadratic global order when $`m=\Theta(n)`$. It does not authorize ignoring an unknown systematic displacement.


## Global precision with hidden jitter

Use the companion's [fixed identifiable band](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_identifiability.md). Choose fixed $`\chi<r_*<\pi/4`$ and put

```math
E=\frac2h\sqrt{r_*^2-\chi^2},
\qquad
\Omega=[\omega_0-E,\omega_0+E].
```

The full interaction norm is at most $`r_*/h`$ on this nonshrinking interval. Let $`R^*_{n,m}(d;\Omega)`$ be the infimum, over the timing-menu protocols just defined and all estimators, of the worst-case squared frequency error over $`\omega\in\Omega`$ and the shared $`\phi`$.

For every fixed $`0<d<h/2`$,

```math
R^*_{n,m}(d;\Omega)=\Theta(n^{-1}),
\qquad 0\le m\le n-1.
```

The constants may depend on the fixed hardware, band and jitter amplitude, but not on $`n,m`$. The upper bound uses only plain cells: the companion's complete three-outcome calibration experiment has risk at most $`[nh^2\cos^2(2r_*)]^{-1}`$, costs $`nh`$, and uses $`n-1`$ boundary contacts. Thus it fits every value of $`m`$ and includes every failed parity result.

### One nuisance curve and an environment gauge

The lower bound uses a fixed positive residual-frequency interval strictly inside $`(0,E)`$. For a plain cell write

```math
a_0=\cos(Rh),\qquad
b_0=\frac{\epsilon}{2R}\sin(Rh),\qquad
c_0=\frac gR\sin(Rh),
\qquad p_0=c_0^2.
```

Primes on scalar coefficients below denote derivatives with respect to $`\epsilon`$. Define

```math
k(\epsilon)=\frac{a_0b'_0-b_0a'_0}{p_0},
\qquad
\phi'(\epsilon)=k(\epsilon).
```

This is a smooth nuisance curve on the band because $`p_0>0`$. Along it, the plain-cell Kraus derivative overlap vanishes, and its squared derivative norm is a bounded scalar:

```math
\sum_j K_j^\dagger\dot K_j=0,\qquad
\sum_j\dot K_j^\dagger\dot K_j
=\left[(a'_0)^2+(b'_0)^2+(c'_0)^2+p_0k^2\right]I.
```

For the jittered cell set $`p=w^2+x^2`$ and $`a=uv'-vu'`$. In the three-Kraus representation,

```math
\beta=i\sum_jL_j^\dagger\dot L_j=(a-pk)Z_S.
```

For $`\epsilon>0`$ on the chosen interval, $`w,x>0`$: indeed $`0<2Rd<Rh<\pi/4`$ and $`\cos(2Rd)>\cos(Rh)`$. The two odd Kraus operators obey $`L_1^\dagger L_2=iwxZ_S`$. An environment gauge with Hermitian matrix entries

```math
G_{12}=it,\qquad G_{21}=-it,\qquad
t=\frac{a-pk}{2wx},
```

and all other entries zero makes the derivative overlap vanish. In the convention $`\widetilde{\dot L}=\dot L-iGL`$, the gauged derivatives before an irrelevant common environment rotation are

```math
\widetilde{\dot L}_0=u'I-iv'Z_S,
```

```math
\widetilde{\dot L}_1=-i\left[w'N_\phi+(wk+tx)N'_\phi\right],
\qquad
\widetilde{\dot L}_2=-i\left[x'N'_\phi-(xk+tw)N_\phi\right].
```

Consequently

```math
\widetilde\beta=(a-pk-2wxt)Z_S=0,
```

```math
\widetilde\alpha
=\left[(u')^2+(v')^2+(w')^2+(x')^2
+(wk+tx)^2+(xk+tw)^2\right]I.
```

All coefficients are bounded on the fixed compact prior interval. The gauge is a valid smooth change of purification: solve $`U'_E=-iU_EG`$ there and replace the Kraus vector by $`U_EL`$. It changes no accessible channel and grants no bath information to the controller.

Both classically selected channel blocks now have zero derivative overlap along the same nuisance curve. Dilating arbitrary boundary instruments and retaining all histories therefore makes derivative contributions from successive cells orthogonal. If $`A_*`$ bounds both scalar derivative norms on the prior interval, the complete output information obeys

```math
F_{\rm out}\le4nA_*.
```

This argument covers adaptive setting choices, arbitrary protected memory and every retained branch. The ordinary [adaptive channel-extension argument](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_precision.md#a-common-nuisance-path-removes-coherent-accumulation) is applied to the explicit gauge above. The [derivative-controlled closure](intervention_bounds.md#limits-with-controlled-parameter-derivatives) preserves the corresponding pointwise classical information bounds. The global risk bound below extends to controlled limits by the separate [bounded-loss argument](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md#global-risk-under-controlled-limits).

Choose a cosine-squared prior of fixed half-width $`\ell>0`$ supported in that positive interval. The scalar van Trees argument used in the [companion global proof](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md) gives, without an unbiasedness assumption,

```math
R^*_{n,m}(d;\Omega)
\ge\frac1{4nA_*+\pi^2/\ell^2}.
```

A prior away from zero is legitimate for worst-case risk over the full band. The fact that the gauge becomes singular as $`\epsilon\to0`$ does not weaken this fixed-prior lower bound. This is a fixed-band minimax obstruction, not a lower bound on risk at every individual frequency.

### A necessary accuracy scale

The same proof gives a bound uniform as jitter shrinks. Fix $`0<d_{\max}<h/2`$ and the positive prior interval above, and write $`\xi=d/h`$. For $`0<d\le d_{\max}`$, $`w`$ is bounded below by a positive constant times $`\xi`$, while $`x`$ is bounded below by a positive constant independent of $`d`$. The other coefficients, their derivatives and the plain-cell nuisance slope are uniformly bounded. Hence the plain-cell derivative norm is at most $`C_0h^2`$ and the gauged jitter-cell norm is at most $`C_1h^2/\xi^2`$, for constants independent of $`n,m,d`$.

The hard bound of $`m`$ jittered cells holds on every controller history, so orthogonality charges their expected number by at most $`m`$. After enlarging a fixed constant $`C`$,

```math
R^*_{n,m}(d;\Omega)
\ge
\max\left\{
\frac1{n^2h^2+\pi^2/\ell^2},
\frac1{Ch^2(n+m/\xi^2)+\pi^2/\ell^2}
\right\}.
```

The first bound uses the fixed-angle signal generator norm $`nh/2`$, with a separate prior if needed. For $`m=\Theta(n)`$, a global $`O(n^{-2})`$ risk would therefore require $`d=O(h/\sqrt n)`$. This is a necessary condition for the stated jittered timing menu. It is not a sufficiency theorem or an optimized joint law in $`n,m,d`$.

## Why the local calculation gives a different answer

At compensation, put

```math
c=\cos(2gd),\quad s=\sin(2gd),\quad
p_{\rm e}=s^2,\quad
A=\frac{\sin\chi}{g},\quad
B=\frac{c-\cos\chi}{g}.
```

The jittered cell has $`L_0=cI`$, $`L_1=-isN_\phi`$, $`L_2=0`$, with frequency derivatives $`-iAZ_S/2`$, $`0`$ and $`-iBN'_\phi/2`$. The last Kraus operator contributes only at second order to the output density. Thus the first-order parity instrument has no-flip phase derivative $`d_{\rm e}=A/c`$. A plain cell has $`p_0=\sin^2\chi`$ and $`d_0=\tan\chi/g`$. The information statements in this section concern pointwise classical score Fisher information at compensation; they assert neither continuity of a rank-changing quantum Fisher metric nor a uniform risk guarantee on a frequency interval.

Choose jittered echoes in the even sector and plain cells in the odd sector, retaining every boundary parity result. The local signed-phase drift is

```math
v_d=\frac{p_0(1-p_{\rm e})d_{\rm e}
-p_{\rm e}(1-p_0)d_0}{h(p_0+p_{\rm e})}
=\frac{A\left[\sin^2\chi\,\cos(2gd)
-\sin^2(2gd)\,\cos\chi\right]}{h(p_0+p_{\rm e})}>0.
```

Positivity follows because $`\sin^2 z/\cos z`$ is strictly increasing on $`(0,\pi/4)`$ and $`2gd<\chi`$. The [retained-even-record local construction](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_sensing.md) therefore supplies $`v_d^2(Nh)^2+o(N^2)`$ information at compensation, with a charged finishing margin and retained failures. Its argument uses the first-order accessible instrument, not an imaginary record of the hidden timing sign.

This protocol uses at most $`N`$ interior pulses and $`N-1`$ boundary measurements, hence at most $`2N-1`$ nonterminal contacts. It does not fit an $`N-1`$ contact budget at the same $`N`$. It can instead run for $`N=\min\{m,\lfloor(n-1)/2\rfloor\}`$ cells of an $`n`$-cell experiment, pay the extra early readout contact, and store its result until the full charged horizon $`nh`$. For $`m=\Theta(n)`$ this still has quadratic local order with at most $`n-1`$ total contacts.

Thus this same timing menu can retain quadratic local information at $`\epsilon=0`$ while its optimal global risk on a fixed band is only of inverse-time order. Away from compensation both hidden odd Kraus operators are present; their unobserved mixing enables the global converse.

### The single repeated primitive

For comparison, restrict every exposed cell to the same jittered-echo primitive and grant arbitrary boundary controls. Let $`\mathcal I^*_{\rm echo}(N,d)`$ denote its optimal efficient local information at compensation. For $`d>0`$,

```math
\frac{N^2A^2}{1+(N-1)p_{\rm e}}
\le\mathcal I^*_{\rm echo}(N,d)
\le\min\left\{N^2h^2,\,
N\left(\frac{A^2}{p_{\rm e}}+B^2\right)\right\}.
```

For the upper bound, the nuisance slope $`k=cA/(2p_{\rm e})`$ cancels the original three-Kraus derivative overlap at zero and gives $`4\alpha=A^2/p_{\rm e}+B^2`$. For the lower bound, perform parity detection and fixed $`X_S`$ recovery after each cell, with a recorded uniformly randomized equatorial terminal readout. The retained flip count is $`K\sim{\rm Binomial}(N,p_{\rm e})`$ at compensation. The conditional phase derivative vector is $`((N-K)A/c,-2K)`$; pooling its full Fisher matrix before eliminating the shared angle gives the displayed lower bound. The physical construction uses $`N`$ interior pulses and $`N-1`$ boundary instruments, exactly $`2N-1`$ contacts.

At $`d=0`$, use the continuous lower-bound value $`N^2A^2`$ and the signal cap $`N^2h^2`$. Since $`A^2+B^2\le h^2`$ and $`p_{\rm e}=\Theta_\chi((d/h)^2)`$,

```math
\mathcal I^*_{\rm echo}(N,d)
=\Theta_\chi\left(
\frac{h^2N^2}{1+N(d/h)^2}
\right).
```

The need for $`d=O(h/\sqrt N)`$ to retain quadratic local order belongs to this single-primitive class. It does not apply to the richer timing menu's local construction above.

## Scope and attribution

The [ideal global contact law](global_contact_precision.md) assumes the prescribed interior timings are implemented exactly. The hidden-jitter theorem concerns the specified plain/jittered-one-pulse menu, with no additional interior controls. It does not bound arbitrary pulse sequences, recorded timing errors, selectable couplings, feedback within a collision, finite-duration controls or physically retuned compensation.

Timing-noise degradation of dynamical decoupling is established prior work. Teixeira, Kapale, Paternostro and Semião, [“Performance of dynamical decoupling in bosonic environments and under pulse-timing fluctuations,” Physical Review A 94, 062322 (2016)](https://doi.org/10.1103/PhysRevA.94.062322), study independent Gaussian pulse-time fluctuations for specified decoupling sequences ([author version](https://arxiv.org/html/1606.08776v2)). Here bounded two-point jitter preserves pulse ordering exactly. The conclusions above follow from the exact collision instrument, its hidden Kraus mixing, and an adaptive global-risk bound; they are not inferred from a sampled coherence decay.
