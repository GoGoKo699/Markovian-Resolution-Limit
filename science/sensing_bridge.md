# A controlled-noise sensing experiment as a resolution test

[Operational model](model.md) · [Controlled-interval estimates](intervention_bounds.md) · [Companion sensing analysis](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_sensing.md)

The companion [Noise-Rate-Activated-Sensing project](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing) asks how access to two incoherent noise rates changes frequency estimation when the transverse error direction is unknown. Its retained parity record also supplies a concrete test of the assumed noise law. This page gives two statements about that record: a discrepancy certificate valid for every bounded microscopic alternative, and a uniform approximation guarantee for one explicit two-rate collision device.

These statements use a **controlled device with a classical rate-input port**. They do not substitute a sensing contact count into the headline theorem for a fixed, centered, drift-free dissipator over one intrinsic lifetime. The device family and its response to each allowed command are fixed before choosing the sensing protocol. A classical command can select a rate; it does not expose the bath or coherently apply the unknown error operator.

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

The survival mechanism is inherited from [Zeno dynamics and bounded-interaction control](../references/RELATED_WORK.md#misra1977). The repeated-interaction construction, its square-root coupling scale and cancellation of odd bath terms belong to established [collision simulation](../references/RELATED_WORK.md#cattaneo2021). Complete-record comparison uses the [operational multitime viewpoint](../references/RELATED_WORK.md#pollock2018). The role of this bridge is to state and prove their application to one shared unknown-axis, two-rate sensing device with its signal, control port, clock and parameter-uniform error accounted for. No independent novelty or experimental-validation claim follows from this construction.
