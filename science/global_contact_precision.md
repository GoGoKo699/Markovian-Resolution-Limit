# Global precision from a limited number of resolved collisions

[Sensing bridge](sensing_bridge.md) · [Adaptive activity bound](intervention_bounds.md#a-derivative-bound-with-a-hard-activity-budget) · [Companion global estimation method](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/recorded_phase_estimation.md)

For the explicit finite-strength collision sensor, access inside a limited number of collisions changes global estimation precision as well as local information. The attaining protocol chooses between an echoed and an untouched cell at one fixed coupling. Its retained parity record specifies an exact phase, so a global estimator can resolve frequency ambiguity without retuning the Hamiltonian. A uniform nuisance-curve argument supplies the matching limitation for every allowed adaptive controller.

## Statistical task and resource model

Fix one coupling $`g>0`$, cell duration $`h>0`$ and nominal compensation $`\omega_0`$, with $`\chi=gh\in(0,\pi/4)`$. Write $`\epsilon=\omega-\omega_0`$. During each cell the sensor and its assigned bath qubit evolve under

```math
H(\epsilon,\phi)=\frac\epsilon2Z_S\otimes I_E
+gN_\phi\otimes X_E,
\qquad N_\phi=\cos\phi\,X_S+\sin\phi\,Y_S.
```

The unknown angle is shared across the entire experiment. All bath qubits are initialized in $`|0\rangle`$ at time zero, used once and retained afterward without access or reuse. Protected ancillary memory is available. The hardware, collision clock and nominal compensation are fixed independently of the experimental budget.

Observe $`n\ge1`$ cells over the hard horizon $`T=nh`$. At most $`n-1`$ instantaneous system–memory contacts are allowed strictly between time zero and $`T`$; at most $`m`$ of them lie strictly inside collision cells, where $`0\le m\le n-1`$. Every budget holds on every classical history. Initial preparation and final readout at $`T`$ are free. An early readout is counted, and the remaining observation time is still charged. Operations at one boundary may be combined into one instrument. Controls can use classical feedback and arbitrary protected memory, but cannot access the bath, change the cell duration, add signal exposure or retune the compensation.

For a fixed nonshrinking frequency interval $`\Omega=[\omega_0-E,\omega_0+E]`$, define

```math
R_{n,m}^*(\Omega)
=\inf_{\mathcal P,\widehat\omega}
\sup_{\omega\in\Omega,\phi}
\mathbb E_{\omega,\phi}^{\mathcal P}
[(\widehat\omega-\omega)^2].
```

The infimum includes biased estimators, retained failure records, adaptive contact times and repetitions charged to the same horizon. The controller class consists of finite adaptive instruments, parameter-independent mixtures and the [controlled operational limits](intervention_bounds.md#limits-with-controlled-parameter-derivatives) specified by event-probability convergence on an open parameter neighborhood with the same structural budgets.

## Global contact theorem

There is an $`E>0`$, depending only on the fixed hardware, such that

```math
\boxed{
R_{n,m}^*(\Omega)
=\Theta_{\chi,Eh}\!\left(\frac1{h^2(n+m^2)}\right)
\qquad(n\ge1,\ 0\le m\le n-1).
}
```

The constants are uniform over the displayed budgets and over the unknown direction. The sufficient frequency band is specified below and is held fixed as the budget grows. The theorem does not identify optimal global constants or a maximal bandwidth. It concerns this collision device with ideal instantaneous contacts; it is separate from the headline fixed-generator discrimination law.

## Two temporal settings at one coupling

Let $`R=\sqrt{g^2+\epsilon^2/4}`$ and $`r=Rh`$. An untouched cell has the parity-resolved Kraus operators

```math
K_{0,p}=\cos r\,I-i\frac\epsilon{2R}\sin r\,Z_S,
\qquad
K_{1,p}=-i\frac gR\sin r\,N_\phi.
```

For an echoed cell, apply one sensor $`Z_S`$ pulse at its midpoint. If $`U_{1/2}=\exp[-iHh/2]`$, its physical propagator is $`U_{1/2}Z_SU_{1/2}`$. Include the known final $`Z_S`$ frame correction in the endpoint boundary instrument. The corrected propagator is

```math
V=Z_SU_{1/2}Z_SU_{1/2}
=e^{-iH_-h/2}e^{-iH_+h/2},
\qquad
H_\pm=\frac\epsilon2 Z_S\otimes I_E
\pm gN_\phi\otimes X_E.
```

Thus there is one inside-cell pulse, and the boundary frame correction is included in the separately counted boundary contact. Multiplying the two exact half-cell propagators gives

```math
V=(uI-ivZ_S)\otimes I_E-i xN'_\phi\otimes X_E,
\qquad N'_\phi=\partial_\phi N_\phi,
```

```math
u=\cos r+\frac{g^2}{R^2}(1-\cos r),
\qquad
v=\frac\epsilon{2R}\sin r,
\qquad
x=\frac{\epsilon g}{2R^2}(1-\cos r).
```

In particular, $`u^2+v^2+x^2=1`$. Parity identifies the Kraus branches $`K_{0,e}=uI-ivZ_S`$ and $`K_{1,e}=-ixN'_\phi`$. On an odd result of an echoed cell, apply one additional known $`Z_S`$ within that same boundary instrument. The identity $`Z_SN'_\phi=-iN_\phi`$ turns its flip Kraus operator into $`-xN_\phi`$. The frame correction, parity measurement and this conditional correction form one instrument; they do not require another contact. The correction preserves parity.

Both temporal settings now have the same unknown flip operator $`N_\phi`$, up to scalar amplitudes, and the no-flip operators are known rotations about $`Z_S`$. On a small band with $`r<\pi/4`$, write

```math
p_e=x^2,\qquad p_p=\frac{g^2}{R^2}\sin^2r,
\qquad q_j=1-p_j,
```

```math
\theta_e(\epsilon)=2\arctan(v/u),
\qquad
\theta_p(\epsilon)=2\arctan\!\left(
\frac\epsilon{2R}\tan r\right),
\qquad
K_{0,j}=\sqrt{q_j}\,e^{-i\theta_jZ_S/2}.
```

The real phase branches are smooth because $`u>0`$ and $`\cos r>0`$. At compensation,

```math
p_e(0)=0,\qquad p_p(0)=\sin^2\chi,
\qquad
d_e=\theta_e'(0)=A=\frac{\sin\chi}{g},
\qquad
d_p=\theta_p'(0)=d=\frac{\tan\chi}{g}.
```

The absence of an echo flip at zero does not assert that the echoed cell is noiseless off compensation: $`p_e(\epsilon)=x^2`$ is generally positive. When $`x`$ changes sign, its sign is a scalar phase on the flip branch and does not change the conditional logical state.

## Attainability by recorded phases

Prepare $`|+_L\rangle=(|00\rangle+|11\rangle)/\sqrt2`$ in even parity. After an even result use an echoed cell; after an odd result use an untouched cell. Measure parity at each boundary, retaining every result. Use the echoed-cell conditional correction just described, without returning an odd state to even parity.

For an even terminal record $`\mathcal R=(\sigma_0,\ldots,\sigma_L)`$, with $`\sigma_0=\sigma_L=+1`$, the normalized logical output is exactly

```math
e^{-i\Phi_{\mathcal R}(\epsilon)Z_L/2}|+_L\rangle,
\qquad
\Phi_{\mathcal R}(\epsilon)
=\sum_{i=1}^L\sigma_{i-1}
\mathbf1_{\{\sigma_i=\sigma_{i-1}\}}
\theta_{j(\sigma_{i-1})}(\epsilon),
```

where $`j(+1)=e`$ and $`j(-1)=p`$. Indeed, the normalized flips are all $`N_\phi`$, and $`N_\phi^2=I`$, $`N_\phi Z_SN_\phi=-Z_S`$. Moving the no-flip rotations through the earlier flips gives the displayed signed phase; an even number of flips cancels the unknown direction. The endpoint instrument implements the chosen logical readout after its parity and frame corrections. This remains a single counted boundary contact if the endpoint precedes the hard deadline.

### A sufficient fixed band

Choose $`E>0`$ sufficiently small that $`r_*:=\sqrt{\chi^2+(Eh/2)^2}<\pi/4`$ and, throughout $`|\epsilon|\le E`$,

```math
0\le p_e(\epsilon)\lt p_p(\epsilon)\lt \frac12,
\qquad
\mu^0(\epsilon)
=\frac{p_pq_eA-p_eq_pd}{p_e+p_p}
\ge\frac{3A}{4},
```

```math
\max\{|\theta'_e(\epsilon)-A|,
|\theta'_p(\epsilon)-d|\}\le\frac A4.
```

Such an interval exists: $`p_p(0)>0`$, $`p_e(0)=0`$, the phase derivatives are smooth, and $`\mu^0(0)=A>0`$. Fix the interval independently of $`n,m`$. The full interaction norm throughout it is at most $`r_*/h`$, which any imposed hardware strength limit must cover. Compactness also gives

```math
\lambda(\epsilon)=1-p_e(\epsilon)-p_p(\epsilon)
\le\rho\lt 1.
```

The [two-state parity gate](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/recorded_phase_estimation.md#a-two-state-parity-gate) applies with frozen rewards $`d_e=A`$, $`d_p=d`$ and positive drift $`\mu_0=A`$. For all sufficiently large fixed block lengths $`L`$, retain a record as usable precisely when it ends even and its frozen derivative reward obeys $`D_L^0\ge AL/2`$. Its acceptance probability is at least $`1/4`$, uniformly in the band and the nuisance. Every usable record satisfies

```math
\frac{AL}{4}\le\Phi'_{\mathcal R}(v)\le\beta L
\quad\text{for all }|v|\le E,
\qquad
\beta=\max_{j\in\{e,p\}}\sup_{|v|\le E}|\theta'_j(v)|.
```

The gate argument uses the uniform gap in $`p_e+p_p`$, not a positive lower bound on $`p_e`$. It therefore includes compensation, where the initial even state is absorbing. Records with zero probability at a particular frequency need no conditional output there; the accepted-phase functions have the same smooth continuation.

Untouched one-cell trials supply the [paid coarse estimator](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_identifiability.md) on this band with $`\kappa=h\cos(2r_*)>0`$. The [recorded-phase estimation lemma](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/recorded_phase_estimation.md#recorded-phase-estimation-lemma) then gives worst-case error at most $`C_1/(h^2Q^2)`$ within $`Q`$ cells, including all calibration and all rejected blocks. It chooses final measurement bases using the recorded phase and earlier estimates; it never changes the physical compensation. Rescaling the target to $`h\epsilon`$ makes $`C_1`$ depend only on $`\chi,Eh`$. A fixed estimate on the band covers small $`Q`$ after increasing this constant.

### Fit the full contact budget

For $`n\ge3`$ and $`m\ge1`$, set

```math
Q=\min\!\left\{m,\left\lfloor\frac{n-1}{2}\right\rfloor\right\}.
```

Run the complete temporal-menu estimator, including its coarse stage and repeated blocks, using at most $`Q`$ physical cells. There is at most one midpoint pulse per used cell. Every cell-end frame correction, parity readout, optional conditional correction, terminal block readout and next preparation is included in its one boundary instrument. Because the estimator finishes before $`nh`$, count its last readout too. Hence there are at most $`Q`$ inside-cell contacts and $`Q`$ boundary contacts, so

```math
\text{inside-cell contacts}\le Q\le m,
\qquad
\text{total contacts}\le2Q\le n-1.
```

Store the classical estimate through the remaining charged cells without further system contacts. No branch obtains a shorter charged horizon or a free retry. For $`n\ge3`$ and $`1\le m\le n-1`$, $`Q\ge m/3`$, so this design gives risk at most $`9C_1/(h^2m^2)`$.

Independently, use all $`n`$ cells for the untouched-cell calibration experiment. It uses exactly $`n-1`$ boundary contacts and no inside-cell contacts, with risk at most $`C_0/(h^2n)`$, where $`C_0=1/\cos^2(2r_*)`$. Choose the better of these two designs from the known budgets. Since

```math
\min\!\left\{\frac{C_0}{n},\frac{9C_1}{m^2}\right\}
\le\frac{C_0+9C_1}{n+m^2},
```

this proves the attaining order. The cases $`m=0`$ and $`n=1,2`$ use the untouched-cell estimator and are covered by a fixed enlargement of the constant. No simultaneous allocation of $`n`$ calibration cells and additional uncharged sensing cells is used.

## Uniform converse for arbitrary adaptive contacts

Use the untouched-cell [fixed-coupling nuisance curve](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md#the-fixed-coupling-nuisance-curve). It has target derivative one and a smooth angle $`\phi(\epsilon)`$ satisfying $`\phi'=q_p\theta'_p/(2p_p)`$. This curve is a comparison subfamily for the worst-case risk, not a restriction on the unknown parameters given to the controller.

Let

```math
p_{\min}=\chi^2\left(\frac{\sin r_*}{r_*}\right)^2,
\qquad
K=\sup_{|\epsilon|\le E}|\phi'(\epsilon)|,
\qquad
a_0=\frac h{2\sqrt{p_{\min}}},
\qquad
b_0=h\sqrt{\frac14+g^2K^2}.
```

For an untouched cell, its Kraus isometry obeys $`V^\dagger\dot V=0`$ throughout the band and $`\|\dot V\|\le a_0`$. In a cell containing arbitrary contacts, the full Hamiltonian derivative along the same curve is

```math
\dot H=\frac12Z_S\otimes I_E
+g\phi'(\epsilon)N'_\phi\otimes X_E,
\qquad
\|\dot H\|=\sqrt{\frac14+g^2\phi'(\epsilon)^2}.
```

The two terms anticommute. The common-laboratory-time Duhamel argument bounds the derivative norm of any active-cell isometry by $`b_0`$, including adaptive instruments and times inside that cell. At most $`m`$ cells can be active on any complete history. The [hard-activity derivative bound](intervention_bounds.md#a-derivative-bound-with-a-hard-activity-budget) therefore gives, uniformly throughout the band,

```math
J_\epsilon
\le4(a_0\sqrt n+b_0m)^2
\le4(a_0^2+b_0^2)(n+m^2).
```

This argument grants unlimited boundary instruments only as a relaxation for the converse. The structural inside-cell budget remains enforced on every history, including zero-probability histories. It does not substitute an expected contact count for the hard budget.

Apply the cosine prior on $`[-E,E]`$, whose Fisher information is $`\pi^2/E^2`$, along this nuisance curve. The [global van Trees argument](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md#from-uniform-information-bounds-to-risk-bounds) yields

```math
R_{n,m}^*(\Omega)
\ge\frac1{4(a_0^2+b_0^2)(n+m^2)+\pi^2/E^2}.
```

This lower bound applies to biased estimators and to the complete accessible output. For the stated operational limits, use the companion's [direct bounded-loss argument](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md#global-risk-under-controlled-limits): clip and finitely quantize the estimator, pass its Bayes risk through event-probability convergence under the same fixed prior, then refine the quantization. This transfers the global lower bound without continuity of Fisher information or any enlargement of the controller class.

Separately, the curve has bounded first and second derivatives on a slightly larger band with $`p_p>0`$, so the [controlled-derivative limit argument](intervention_bounds.md#limits-with-controlled-parameter-derivatives) retains the information bound itself for local-precision uses. In particular, $`\|\partial_\epsilon^2H\|\le g(|\phi''|+|\phi'|^2)`$ is uniformly bounded independently of the controller.

Because $`a_0/h`$, $`b_0/h`$ and $`Eh`$ are fixed dimensionless quantities, this is the required lower order $`1/[h^2(n+m^2)]`$. Together with the two attaining designs it proves the global contact theorem.

## What temporal access supplies

The attaining resource is a selectable temporal setting inside a collision, combined with its retained syndrome record. Echoing every cell with one unchanged primitive is a different construction; its local sensitivity alone does not establish global quadratic precision. The [timing-error analysis](timing_precision.md#global-precision-with-hidden-jitter) distinguishes fixed systematic offsets from unobserved random jitter and analyzes the effect of hidden timing fluctuations on global estimation.

The global contact theorem assumes exact midpoint pulses for its attaining temporal menu. It does not claim the same upper bound for an imperfect timing record, finite-duration pulses or hidden jitter. The converse remains an ideal-control limitation. This is a theorem for the explicit sensing device, with its own estimator and uniform converse; it is not a logical corollary of the headline fixed-generator discrimination law.
