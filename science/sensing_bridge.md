# A controlled-noise sensing experiment as a resolution test

[Operational model](model.md) · [Controlled-interval estimates](intervention_bounds.md) · [Companion sensing analysis](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_sensing.md)

The companion [Noise-Rate-Activated-Sensing project](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing) asks how access to two incoherent noise rates changes frequency estimation when the transverse error direction is unknown. Its retained parity record also supplies a concrete test of the assumed noise law. This page gives a discrepancy certificate valid for every bounded microscopic alternative and a uniform approximation guarantee for one explicit two-rate collision device. A midpoint-pulse calculation and a matching contact-budget bound then quantify how access inside collisions turns this device's microscopic memory into a local sensing resource.

These statements use a **controlled device with a classical rate-input port**; the midpoint experiment holds that port fixed. They do not substitute a sensing contact count into the headline theorem for a fixed, centered, drift-free dissipator over one intrinsic lifetime. The device family and its response to each allowed command are fixed before choosing the sensing protocol. A classical command can select a rate; it does not expose the bath or coherently apply the unknown error operator.

## The common experiment and its resources

Let the sensor and protected ancilla be qubits, and put

```math
N_\phi=\cos\phi\,X_S+\sin\phi\,Y_S,
\qquad
\Pi=\frac{I+Z_SZ_A}{2}.
```

The unknown angle is shared by both settings and all trials. The Markov prediction at selected rate $`\gamma\in\{a,b\}`$, with $`0<a<b`$, is

```math
\mathcal L_{\eta,\phi,\gamma}(\rho)
=-i\frac{\eta}{2}[Z_S,\rho]
+\gamma(N_\phi\rho N_\phi-\rho).
```

Here $`\eta=\omega-\omega_0`$ is the residual frequency after a specified, parameter-independent nominal compensation. The setting $`\omega_0`$ is held fixed throughout the comparison; estimating or calibrating it is not an uncharged preliminary step. The signal preserves the two parity sectors, while each transverse error exchanges them.

Start in the code sector $`\Pi`$, measure parity at intervals $`\Delta`$, retain every outcome, and select rate $`a`$ after an even result and rate $`b`$ after an odd result. No recovery pulse is applied in this protocol. The final logical measurement and any deadline failure are also retained. Preparation, measurements, classical decisions and ancillary storage remain ideal. Their finite duration, work cost and noise are not quantified here.

For $`T=n\Delta`$, there are $`n-1`$ interior parity contacts; the parity measurement at $`T`$ can be included in the final readout under this repository's counting convention. There can additionally be up to $`n-1`$ changes of the rate command. Those commands are declared inputs to this controlled device, not automatically instruments in the fixed-generator theorem. The microscopic collision clock introduced below is another explicit resource.

## A parity-record discrepancy certificate

Let $`E_n`$ denote the event that every one of the $`n`$ measured parity results is even. It includes trajectories with hidden pairs of jumps; it is not the no-jump event. On this branch the selected rate remains $`a`$. For every signal frequency, common axis and initial logical state,

```math
\Pr_{\mathrm M}(E_n)
=\left(\frac{1+e^{-2a\Delta}}2\right)^n.
```

Indeed, the jump rate is state independent because $`L^\dagger L=aI`$, and the Hamiltonian preserves parity. Conditional on the preceding even results, an even Poisson jump count in the next interval has the displayed one-step probability. Logical evolution within the sector does not change it.

Consider instead any microscopic device whose conditional Hamiltonian between checks can be written as a parity-preserving part plus a remainder,

```math
H(t)=H_{\mathrm{diag}}(t)+K(t),
\qquad
[H_{\mathrm{diag}}(t),\Pi\otimes I_E]=0,
\qquad
\|K(t)\|_\infty\leq\Lambda_\perp.
```

The signal and arbitrary bath-only evolution can be included in $`H_{\mathrm{diag}}`$. It suffices to bound the parity-changing block: any remaining diagonal block can also be absorbed into $`H_{\mathrm{diag}}`$. The bath may be retained, correlated with the sensor after earlier checks, and of arbitrary finite dimension. All permitted command responses must be specified as one causal device rule before the experiment; no fresh bath access or adaptive bath reinitialization is granted to the tester.

The [subspace-survival estimate](intervention_bounds.md#survival-under-a-bounded-retained-interaction), applied after each successful projection, gives

```math
\Pr_{\mathrm{mic}}(E_n)
\geq\cos^{2n}(\Lambda_\perp\Delta),
\qquad 0\leq\Lambda_\perp\Delta\leq\frac\pi2.
```

This argument makes no independence assumption about successive microscopic outcomes. Each conditional joint state is supported on $`\Pi\otimes I_E`$, which is all the survival estimate needs. Consequently the total-variation distance of the **complete sensing records** obeys

```math
\mathrm{TV}(P_{\mathrm{mic}},P_{\mathrm M})
\geq
\max\!\left\{0,
\cos^{2n}(\Lambda_\perp\Delta)
-\left(\frac{1+e^{-2a\Delta}}2\right)^n
\right\}.
```

At fixed $`T>0`$ and fixed $`\Lambda_\perp`$, taking $`\Delta=T/n\to0`$ gives a lower certificate tending to $`1-e^{-aT}`$. This is a fixed-horizon, increasingly frequent observation limit. At fixed positive cadence and increasing horizon, the two all-even probabilities can both become exponentially small, so this particular event need not certify a useful long-time discrepancy.

The notation $`\Lambda_\perp`$ does not redefine the headline theorem's strength $`\Lambda`$. A bound on the complete system-affecting generator implies a bound on its off-diagonal block. Conversely, a bound on noise or parity leakage alone need not bound the signal or other diagonal terms. The construction below reports both quantities explicitly.

The discrepancy establishes failure of a statistical model for this retained record. It does not establish failure of a frequency estimator, loss of rate activation, or a bound on Fisher information. A visible change in an ancillary statistic can coexist with unchanged or improved precision.

## One finite-bath device for both rates

Fix a cell duration $`h>0`$ and a horizon $`T=Mh`$. Initialize $`M`$ bath qubits in $`|0\rangle^{\otimes M}`$ at time zero. Cell $`j`$ interacts only with bath qubit $`j`$; spent qubits remain in the environment and are never coupled again. No bath reset or preparation is performed during the run.

Define, for either permitted rate,

```math
p_\gamma(h)=\frac{1-e^{-2\gamma h}}2,
\qquad
\theta_\gamma(h)=\arcsin\sqrt{p_\gamma(h)},
\qquad
g_\gamma(h)=\frac{\theta_\gamma(h)}h.
```

During a complete cell selected at rate $`\gamma`$, the Hamiltonian is

```math
H_{\eta,\phi,\gamma}^{(j)}
=\frac{\eta}{2}Z_S
+g_\gamma(h)N_\phi\otimes X_{E_j}.
```

The cell clock and the two responses $`g_a(h),g_b(h)`$ are fixed independently of the unknown parameters and the tester. The same unknown physical axis appears in every cell. Only the classical amplitude setting changes; the persistent signal has the same coefficient at both settings. The tester cannot manipulate the bath qubits, change an individual collision's duration, or choose a coherent superposition of settings.

Rate commands and system instruments are allowed only at cell boundaries in the approximation statement below. The parity protocol is therefore included whenever $`\Delta=mh`$ for an integer $`m\geq1`$. This restriction is substantive: agreement at boundaries does not license observations inside a cell.

For residual frequencies $`|\eta|\leq W`$, the noise and complete system-affecting strength obey

```math
\Lambda_\perp=g_b(h),
\qquad
\|H_{\eta,\phi,\gamma}^{(j)}\|_\infty
=\sqrt{g_\gamma(h)^2+\eta^2/4}
\leq\sqrt{g_b(h)^2+W^2/4}.
```

The equality uses anticommutation of the two Hamiltonian terms. In particular, a noise-only budget must not be reported as the complete interaction budget. The environment dimension is $`2^M`$, with $`M`$ initially pure qubits and an externally specified collision schedule. These are finite resources at every fixed $`T,h`$; their preparation and clock costs are not claimed to be efficient.

At $`\eta=0`$, tracing a cell qubit gives exactly

```math
\mathcal C_{0,\phi,\gamma,h}
=\cos^2\theta_\gamma\,\mathrm{id}
+\sin^2\theta_\gamma\,\mathcal N_\phi
=e^{\gamma h(\mathcal N_\phi-\mathrm{id})},
\qquad
\mathcal N_\phi(\rho)=N_\phi\rho N_\phi.
```

Thus all boundary-controlled records agree exactly with the compensated Markov model at that parameter value. Their parameter derivatives need not agree. This identity alone is not a Fisher-information comparison; the [companion analysis](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_sensing.md) treats the microscopic sensing response directly.

## Uniform one-cell error with the signal present

Let $`\mathcal C_{\eta,\phi,\gamma,h}`$ be the actual reduced collision channel. For every $`h>0`$, every angle and every residual frequency,

```math
\frac12\left\|
\mathcal C_{\eta,\phi,\gamma,h}
-e^{h\mathcal L_{\eta,\phi,\gamma}}
\right\|_\diamond
\leq
\frac{|\eta|h}{2}
\left[\theta_\gamma\sinh(2\theta_\gamma)+\gamma h\right]
\leq C_0|\eta|\gamma h^2
\leq2|\eta|\gamma h^2,
```

where

```math
C_0=\frac12+\frac{2\sinh(\pi/2)}\pi<2.
```

No small-frequency derivative or unobserved-jump approximation is used.

### Proof by bath parity and the signal interaction picture

Write $`H_0=\eta Z_S/2`$ and move to its interaction picture. Then

```math
K(t)=g_\gamma N_\phi(t)\otimes X_E,
\qquad
N_\phi(t)=e^{iH_0t}N_\phi e^{-iH_0t},
\qquad
\|N_\phi(t)-N_\phi\|_\infty\leq|\eta|t.
```

Compare the reduced interaction-picture channel with that generated by the constant $`K(0)`$. The latter is the exact dissipative channel in the preceding display. The initial bath state is invariant under $`Z_E`$, while each $`K(t)`$ is odd under conjugation by $`Z_E`$. Therefore every odd-order term of either reduced Dyson expansion vanishes after tracing the bath, just as in the [controlled-cell parity argument](intervention_bounds.md#a-controlled-cell-with-odd-bath-parity).

The commutator superoperators at time $`t`$ have diamond norm at most $`2g_\gamma`$, and their difference has norm at most $`2g_\gamma|\eta|t`$. Telescoping a product of $`k`$ factors bounds the integrand difference by

```math
(2g_\gamma)^k|\eta|\sum_{j=1}^k t_j.
```

Over the ordered simplex $`0\leq t_1\leq\cdots\leq t_k\leq h`$, the integral of this sum is $`(kh/2)h^k/k!`$. Initialization and partial trace have diamond norm one. Summing only even $`k\geq2`$ and dividing by two therefore bounds the reduced channel error by

```math
\frac{|\eta|h}{4}
\sum_{\substack{k\geq2\\k\ \mathrm{even}}}
\frac{k(2g_\gamma h)^k}{k!}
=\frac{|\eta|h\theta_\gamma}{2}\sinh(2\theta_\gamma).
```

In the same signal interaction picture, the Markov dissipator is

```math
\mathcal D(t)=\gamma(\mathcal N_{\phi,t}-\mathrm{id}),
\qquad
\|\mathcal D(t)-\mathcal D(0)\|_\diamond
\leq2\gamma|\eta|t.
```

A Duhamel comparison between its time-ordered propagator and $`e^{h\mathcal D(0)}`$ uses only completely positive, trace-preserving propagators on either side of the difference. Its half-diamond error is at most $`\gamma|\eta|h^2/2`$. Combining the two comparisons and restoring the common final signal unitary proves the first bound.

Finally $`0<\theta_\gamma<\pi/4`$ and

```math
\gamma h=-\frac12\log\cos(2\theta_\gamma)
\geq\theta_\gamma^2.
```

The inequality follows by integrating $`\tan x\geq x`$. Since $`\sinh x/x`$ is increasing for positive $`x`$,

```math
\theta_\gamma\sinh(2\theta_\gamma)
\leq\frac{4\sinh(\pi/2)}\pi\theta_\gamma^2
\leq\frac{4\sinh(\pi/2)}\pi\gamma h.
```

This proves the stated universal constant. Bath-parity cancellation is the reason the error has order $`|\eta|\gamma h^2`$ rather than the weaker estimate obtained by directly comparing the two joint unitaries.

## Complete records and bounded-loss estimation

Apply the same parameter-independent boundary instruments, rate decisions, final readout and estimator to the microscopic device and the Markov model. Instruments can use arbitrary protected quantum memory and depend on earlier classical outcomes. Each unused bath qubit remains fresh, while spent qubits can be traced out analytically because they never interact again. Diamond-norm uniformity therefore permits the one-cell estimate to be used on every conditional input, including those entangled with the protected memory.

A channel hybrid over the $`M=T/h`$ cells, keeping all branch labels and failures, gives

```math
\frac12\|\rho_{\mathrm{mic}}^{\mathrm{out}}
-\rho_{\mathrm M}^{\mathrm{out}}\|_1
\leq\varepsilon(T,h),
\qquad
\varepsilon(T,h)=\min\{1,2WbTh\}.
```

The same bound holds for the total-variation distance after any common final measurement. It is uniform over $`|\eta|\leq W`$, the unknown axis, and all protocols in this boundary-restricted class. Adaptive rate selection causes no extra branch-count factor: a record-controlled complete instrument is a channel, and each selected cell has the same uniform upper bound. If a run finishes early, its decoded output and completion flag can be stored through the fixed horizon; unfinished runs keep their failure flag.

For any common loss function with range $`[0,B]`$,

```math
\left|\mathbb E_{\mathrm{mic}}\ell
-\mathbb E_{\mathrm M}\ell\right|
\leq B\varepsilon(T,h).
```

In particular, clip the frequency estimate to the known parameter interval of width $`L`$. Squared loss then lies in $`[0,L^2]`$, and the risk difference for the identical protocol and estimator is at most $`L^2\varepsilon(T,h)`$. Uniformity also implies

```math
\left|R_{\mathrm{mic},\mathcal A}
-R_{\mathrm M,\mathcal A}\right|
\leq L^2\varepsilon(T,h)
```

when both minimax risks optimize over the **same** boundary-restricted strategy class $`\mathcal A`$ and the same parameter domain. It does not compare a restricted microscopic experiment with an unrestricted Markov optimum, or with a microscopic controller granted extra bath or within-cell access. If two such common strategy classes have a certified Markov risk gap greater than $`2L^2\varepsilon(T,h)`$, that gap remains positive in this microscopic realization.

This supplies a finite-horizon transfer criterion. It does not prove the companion project's continuous-timing global bound for a finite-cadence protocol. Total-variation closeness also does not control parameter derivatives or Fisher information; those require a separate calculation.

## The same contact budget at collision midpoints

The [companion microscopic precision analysis](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_precision.md) proves a fixed-rate linear local-information bound when every system contact is restricted to a cell boundary. That timing restriction matters. The same fixed-coupling hardware admits quadratic local information when the same number of contacts can instead be placed inside its cells.

Hold one coupling $`g>0`$ fixed, write $`\chi=gh\in(0,\pi/4)`$, and use $`n`$ physical cells over $`T=nh`$. Here $`h`$ is the collision duration and $`g`$ is a microscopic Hamiltonian strength, not the calibrated Markov rate $`\gamma`$. Prepare

```math
|+_L\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

Apply a known sensor pulse $`Z_S`$ at the midpoint of each of the first $`n-1`$ cells. Make no intermediate parity measurement, apply no pulse in the last cell, and keep the coupling fixed throughout. There are exactly $`n-1`$ interior system contacts, the same count as parity checks at the first $`n-1`$ boundaries. At $`T`$, measure parity and, on an even result, measure the logical $`Y_L`$ observable in the known accumulated pulse frame. An odd result is a retained failure flag with no further information used. The frame adjustment is part of the terminal readout, not an additional interior pulse.

### Reduced response of a refocused cell

In the toggling frame of the preceding pulses, cell $`j\leq n-1`$ has coupling $`s_jg`$ during its first half and $`-s_jg`$ during its second half, with $`s_j=(-1)^{j-1}`$. Its joint propagator in this frame is

```math
V_j=e^{-iH_{-s_j}h/2}e^{-iH_{s_j}h/2},
\qquad
H_s=\frac\eta2Z_S+s gN_\phi\otimes X_{E_j}.
```

At $`\eta=0`$ this propagator is exactly the identity for every $`\phi`$. With $`N'_\phi=\partial_\phi N_\phi`$, its derivative at that point is

```math
\left.\partial_\eta V_j\right|_0
=-\frac i2\left(AZ_S+s_jB N'_\phi\otimes X_{E_j}\right),
\qquad
A=\frac{\sin\chi}{g},
\qquad
B=\frac{1-\cos\chi}{g}.
```

To obtain this expression, the zero-frequency accumulated interaction angle runs from zero to $`s_jgh/2`$ and returns to zero. In the corresponding interaction picture the signal operator is $`Z_S\cos(2gt)+s_jN'_\phi\otimes X_{E_j}\sin(2gt)`$ during the first half; the second half retraces the same angles. Integrating gives $`A`$ and $`s_jB`$.

The bath starts in $`|0\rangle`$, whose $`X_E`$ expectation is zero. Therefore the reduced channel $`\mathcal E_j`$ and its first derivatives obey

```math
\mathcal E_j(0,\phi)=\mathrm{id},
\qquad
\left.\partial_\eta\mathcal E_j\right|_0
=-i\frac A2[Z_S,\,\cdot\,],
\qquad
\left.\partial_\phi\mathcal E_j\right|_0=0.
```

This holds on inputs entangled with the protected ancilla. Different physical cells use different initially prepared bath qubits, and spent cells are never reused. Composing the first $`n-1`$ reduced channels consequently adds their signal derivatives to $`(n-1)A`$. This is a first-derivative statement at compensation; the reduced echoed channel need not remain unitary away from that point.

### Terminal probabilities and efficient information

The last, unrefocused cell has the same no-flip Kraus operator for either sign of its coupling. With

```math
p=\sin^2\chi,
\qquad q=\cos^2\chi,
\qquad d=\frac{\tan\chi}{g},
\qquad D_n=(n-1)A+d,
```

its final even branch has success probability $`q`$ and phase derivative $`D_n`$ at $`\eta=0`$. The known physical frame $`Z_S^{n-1}`$ commutes with parity and is absorbed into the terminal logical observable. The complete marginal readout used here consists of two even-sector outcomes and the odd failure flag. Its probabilities have the expansions

```math
P(\mathrm{even},Y_L=\pm1)
=\frac q2\pm\frac{qD_n}{2}\eta+O(\eta^2),
\qquad
P(\mathrm{odd})=p+O(\eta^2).
```

At the operating point all three probabilities are strictly positive, and they and their first signal derivatives are the same for every unknown axis. Every $`\phi`$ derivative of this marginal likelihood is zero there. The nuisance angle need not be identifiable for efficient information to be defined: minimizing the score variance over nuisance-path slopes leaves this marginal target score unchanged. Its nuisance-adjusted Fisher information therefore equals its target Fisher information:

```math
\mathcal I_\omega^{\mathrm{mid}}(nh)
=qD_n^2
=\frac{\sin^2\chi}{g^2}
\left[1+(n-1)\cos\chi\right]^2.
```

The success probability is included in this expression; failed runs are neither discarded from the likelihood nor removed from the time cost. In particular,

```math
\lim_{n\to\infty}
\frac{\mathcal I_\omega^{\mathrm{mid}}(nh)}{(nh)^2}
=q\left(\frac{\sin\chi}{\chi}\right)^2>0.
```

The finite expression never exceeds $`T^2`$, since its ratio to $`T^2`$ is $`(\sin\chi/\chi)^2[1+(n-1)\cos\chi]^2/n^2\leq1`$. Neither the coupling nor the cell duration needs to change with the horizon. The number of bath cells and the number of pulses grow linearly with $`T`$.

For the target Markov process, the same $`Z_S`$ pulses leave the dissipator unchanged: $`Z_SN_\phi Z_S=-N_\phi`$, and changing a jump operator's sign has no effect on $`N_\phi\rho N_\phi-\rho`$. The signal also commutes with the pulses. The microscopic echo thus exploits coherent evolution within a bath collision that the Markov model does not retain.

This calculation establishes a local sensing benefit from access to collision midpoints. It shows why a boundary-only fixed-rate converse cannot be promoted to an arbitrary-timing converse using contact count alone. It does not establish a global minimax estimation law, optimized local coefficients, or a new bound for the headline fixed-generator minimax problem. The nominal compensation, ideal pulses, known collision clock and protected ancilla remain explicit resources.

## How many contacts must resolve a collision

Keep one coupling $`g`$ and the cell duration $`h`$ fixed, with $`\chi=gh\in(0,\pi/4)`$ and $`T=nh`$. Allow arbitrary adaptive instruments at cell boundaries and at most $`m`$ system contacts strictly inside cells, with the latter budget enforced on every classical history. Several contacts inside one cell still make only one active cell, so the number of active cells is at most $`m`$. All outcomes are retained. This temporarily grants unlimited boundary access for an upper bound; it does not remove boundary contacts from the original resource accounting.

The efficient local frequency information at $`\eta=0`$, with the common unknown angle as nuisance, satisfies

```math
\mathcal I_\omega
\leq\min\left\{n^2h^2,
\left(\frac{\sqrt n}{g}+\frac{mh}{\sin\chi}\right)^2\right\}.
```

To apply the [derivative bound with a hard activity budget](intervention_bounds.md#a-derivative-bound-with-a-hard-activity-budget), take the common nuisance path $`\eta(u)=u`$, $`\phi(u)=\phi_0+ku`$, where

```math
k=\frac{\cot\chi}{2g}.
```

The [exact boundary-channel calculation](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_precision.md#a-common-nuisance-path-removes-coherent-accumulation) gives zero derivative overlap and derivative norm $`a=1/(2g)`$ for an untouched cell. In a cell containing contacts, the full Hamiltonian derivative is

```math
\dot H=\frac{Z_S}{2}+kgN'_\phi\otimes X_E,
\qquad
\|\dot H\|=\sqrt{\frac14+k^2g^2}
=\frac1{2\sin\chi}.
```

The two terms anticommute, which gives the displayed norm. Purify the complete instruments and retain their classical histories. At every common laboratory time their controlled Hamiltonian blocks obey the same derivative bound. A Duhamel integral over the physical cell duration therefore gives

```math
\|\dot V_{\mathrm{active}}\|
\leq L=\frac{h}{2\sin\chi}.
```

This includes adaptive contact times and any number of instruments inside the active cell. Summing branchwise maximum waiting intervals would not justify the same bound; the integral is over one shared interval of length $`h`$. The [memory-only normal form](intervention_bounds.md#memory-only-controller-normal-form) makes the activity decision available at cell entry, and the derivative lemma supplies the claimed information bound. The separate $`T^2`$ cap uses the fixed-angle path and signal derivative $`Z_S/2`$.

For finite controllers and their parameter-independent classical mixtures, the proof is direct. It also extends to the [specified limits with controlled derivatives](intervention_bounds.md#limits-with-controlled-parameter-derivatives). On this nuisance path, $`\|\partial_u H\|\leq1/(2\sin\chi)`$ and $`\|\partial_u^2H\|\leq gk^2`$ uniformly in a neighborhood, so the required event-probability derivative control holds for fixed $`n,m,g,h`$. This extension uses the microscopic Hamiltonian; total-variation closeness by itself still does not transfer Fisher information.

The companion [limited-contact theorem](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_precision.md#limited-access-inside-collision-cells) adds matching lower constructions while imposing at most $`n-1`$ total system contacts, of which at most $`m`$ lie inside cells. The optimal information divided by $`h^2`$ is of order $`n+m^2`$ for fixed $`\chi`$. Consequently, interior-contact budgets of order at most $`\sqrt n`$ preserve linear scaling; a budget proportional to $`n`$ is necessary and sufficient for quadratic scaling. These are local sensing statements for this explicit device, not a substitution into the fixed-generator discrimination law.

## Frequency aliases of the collision clock

The fixed collision clock also limits global frequency identification. Keep one coupling $`g`$, the cell duration $`h`$ and nominal compensation $`\omega_0`$ fixed, and write $`\eta=\omega-\omega_0`$, $`\chi=gh\in(0,\pi/4)`$. The Hamiltonian in a cell is

```math
H(\eta,\phi)=\frac\eta2 Z_S\otimes I_E
+gN_\phi\otimes X_E,
\qquad
R(\eta)=\sqrt{g^2+\eta^2/4}.
```

For every positive integer $`k`$, the two residual frequencies

```math
\eta_k^\pm=\pm\frac2h\sqrt{k^2\pi^2-\chi^2}
```

obey $`R(\eta_k^\pm)h=k\pi`$. The exact joint propagator is therefore

```math
U(\eta_k^\pm,\phi)=(-1)^k I_{SE},
\qquad
K_0=(-1)^kI_S,\qquad K_1=0.
```

The reduced cell channel is the identity, independently of the unknown direction. Its scalar phase is not an accessible output. Only resonances inside the chosen frequency domain are relevant; any imposed bound on the full Hamiltonian must also cover $`R(\eta_k^\pm)=k\pi/h`$.

Suppose two distinct frequencies $`\omega_1,\omega_2`$ in the parameter domain are of the form $`\omega_0+\eta_k^\pm`$. Every parameter-independent controller restricted to cell boundaries has the same complete accessible output at these two frequencies, for every number of cells. To prove this for adaptive controls, start with the same sensor, protected memory and classical record. Each complete collision acts as the identity on their joint state. Applying the same boundary instrument then gives the same outcome probabilities and conditional states on every history. Induction over the cells proves equality of the final classical–quantum outputs; arbitrary terminal measurements, classical randomization and protected-memory processing preserve it. This argument uses the original fresh-cell bath: all bath qubits are prepared at time zero, spent qubits are retained without reuse, and none is accessible to the controller.

Consequently any frequency estimator has the same output law at the two frequencies. With $`d=|\omega_1-\omega_2|`$ and $`\overline\omega=(\omega_1+\omega_2)/2`$, this common law gives

```math
\frac12\left\{
\mathbb E_{\omega_1}[(\widehat\omega-\omega_1)^2]
+\mathbb E_{\omega_2}[(\widehat\omega-\omega_2)^2]
\right\}
=\mathbb E[(\widehat\omega-\overline\omega)^2]+\frac{d^2}{4}
\geq\frac{d^2}{4}.
```

Thus the boundary-only minimax squared error over any domain containing this pair is at least $`d^2/4`$, uniformly in the number of cells. This is an exact indistinguishability statement, not a consequence of small local Fisher information.

A fixed band around compensation admits a positive result. The companion [microscopic identifiability theorem](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_identifiability.md) chooses any fixed $`\chi<r_*<\pi/4`$ and defines

```math
E=\frac2h\sqrt{r_*^2-\chi^2},
\qquad \kappa=h\cos(2r_*)>0.
```

For $`|\omega-\omega_0|\leq E`$, a one-cell Bell-parity and logical-quadrature measurement has an exactly direction-independent likelihood and a strictly increasing mean with derivative at least $`\kappa`$. Repeating this complete experiment $`N`$ times gives an estimator with

```math
\sup_{|\omega-\omega_0|\leq E,\phi}
\mathbb E[(\widehat\omega-\omega)^2]
\leq\frac1{N\kappa^2},
\qquad
\Pr\{|\widehat\omega-\omega|\geq\delta\}
\leq2\exp\!\left(-\frac{N\kappa^2\delta^2}{2}\right).
```

All odd-parity failures are included. These experiments cost $`Nh`$ in physical time and $`N-1`$ boundary measure-and-reprepare contacts, with free initial preparation and final readout. When used as a calibration prefix of a longer experiment, the readout at $`Nh`$ is an additional counted boundary contact, so that prefix costs $`N`$ contacts. This is a sufficient identifiable band, not a maximal-bandwidth claim.

The alias obstruction concerns the fixed-coupling, fixed-duration, fixed-compensation boundary model. Interior-cell contacts, selectable couplings or changes to the compensation are different control allowances. In particular, a paid classical frequency estimate does not itself retune the physical Hamiltonian. The calibration result gives a usable estimation band, while the aliases impose a nonvanishing risk on domains containing them. Neither result turns the local contact-information law into an optimal global-risk law.

## Compatible scales and attribution

For small cells, $`g_b(h)\sim\sqrt{b/h}`$. Choosing a finer cell improves the uniform record approximation while increasing the coupling, the number of preinitialized bath qubits and the clock resolution. More explicitly, $`g_b(h)^2\leq b/h`$, so $`h=b/\Lambda_\perp^2`$ is one sufficient choice for the noise-only coupling budget when the desired observation grid and horizon are integer multiples of that cell. It yields the record bound

```math
\varepsilon(T,h)
\leq\min\!\left\{1,
\frac{2Wb^2T}{\Lambda_\perp^2}\right\}.
```

For an explicit equality case, take $`h=\Delta`$ and $`\eta=0`$. Along the all-even branch the coupling is $`g_a(h)`$, and

```math
\cos^2(g_a(h)\Delta)
=\frac{1+e^{-2a\Delta}}2.
```

The microscopic all-even probability exactly equals the Markov probability, and the survival lower bound is saturated when it uses the actual branch coupling $`g_a(h)`$. Using the larger device-wide bound $`g_b(h)`$ only weakens that certificate. Thus the witness does not force a discrepancy at matched collision boundaries. Finer observations at a fixed physical coupling probe a different regime from recalibrating a new device at a smaller cell size.

Grid alignment is part of this example, not an assumption that every physical bath is synchronized with the measurement clock. The universal parity witness examines increasingly fine observations at a fixed coupling; the construction instead increases its coupling when its cell is made finer. The two statements therefore impose compatible conditions.

The survival mechanism is inherited from [Zeno dynamics and bounded-interaction control](../references/RELATED_WORK.md#misra1977), and the midpoint echo uses established [dynamical-decoupling ideas](../references/RELATED_WORK.md#arenz2015). The repeated-interaction construction, its square-root coupling scale and cancellation of odd bath terms belong to established [collision simulation](../references/RELATED_WORK.md#cattaneo2021). Complete-record comparison uses the [operational multitime viewpoint](../references/RELATED_WORK.md#pollock2018). The role of this bridge is to state and prove their application to one shared unknown-axis sensing device with its signal, control port, contact timing and parameter-uniform error accounted for. No independent novelty or experimental-validation claim follows from this construction.
