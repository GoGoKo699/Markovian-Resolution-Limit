# From a decay curve to an intervention law

A quantum system can lose an excitation while interacting with a larger,
closed system. Looking only at the smaller system can make that reversible
interaction resemble irreversible noise. The question in this project is
how often an experimenter must act on the smaller system to expose a
difference between those two descriptions when the microscopic interaction
has a known strength bound.

The single common educational anchor for both sister projects is Rivas and
Huelga's *Open Quantum Systems: An Introduction*, [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2).
The [anchor bridge](ANCHOR.md) identifies the source
version, relevant sections, and notation. This tutorial connects those
foundations to the project's argument; the [30-milestone map](MILESTONES.md)
gives the complete conceptual route. Exact assumptions and proofs belong to
the linked pages under `science/`.

## Route through the explanation

| Part | Milestones | Connection |
|---|---|---|
| [States, maps and records](#states-maps-and-records) | [M01–M04](MILESTONES.md#m01) | A physical experiment becomes a probability distribution. |
| [Two descriptions of the same decay](#two-descriptions-of-the-same-decay) | [M05–M11](MILESTONES.md#m05) | A reduced unitary evolution can match a Markov channel at a specified time. |
| [A complete one-pulse example](#a-complete-one-pulse-example) | [M12–M13](MILESTONES.md#m12), [M17](MILESTONES.md#m17) | An interior operation distinguishes controlled processes with equal endpoints. |
| [A test that works without identifying the bath](#a-test-that-works-without-identifying-the-bath) | [M14–M16](MILESTONES.md#m14) | Short-time loss and a retained survival record give a universal witness. |
| [A model that hides from every permitted tester](#a-model-that-hides-from-every-permitted-tester) | [M17–M22](MILESTONES.md#m17) | Exact cells, parity and adaptive composition give the converse. |
| [The complete law and its scope](#the-complete-law-and-its-scope) | [M23](MILESTONES.md#m23) | The two bounds determine the contact scale and coupling cost. |
| [Temporal access changes global sensing precision](#temporal-access-changes-global-sensing-precision) | [M24–M29](MILESTONES.md#m24) | An explicit collision sensor gives a global contact law and a timing limitation. |

The one-pulse example can be read before the formal rate construction. It
illustrates one particular microscopic model. The universal result requires
the two proof directions developed afterward.

## States, maps and records

Let $`S`$ denote the observed system. Its state is a positive matrix
$`\rho`$ with trace one. A measurement outcome has a positive effect
$`F`$ with $`0\le F\le I`$, and its probability is
$`\mathrm{Tr}(F\rho)`$. For a two-level system, the pure states
$`|0\rangle`$ and $`|1\rangle`$ can represent the ground and excited
states. The projector $`P=|1\rangle\langle1|`$ asks whether the excitation
is present.

A quantum channel $`\Phi`$ transforms input states into output states. It
must also work on a system entangled with an otherwise untouched reference
$`R`$: the enlarged transformation is $`\Phi\otimes\mathrm{id}_R`$.
Complete positivity is the condition ensuring positivity for these enlarged
inputs. A Kraus representation writes a channel as

```math
\Phi(\rho)=\sum_a A_a\rho A_a^\dagger,
\qquad \sum_a A_a^\dagger A_a=I.
```

The sum describes an output with the Kraus label ignored. An **instrument**
instead specifies both the state change and a recorded outcome. This
distinction matters because the experimenter can select later operations
from the accumulated record. The repository always retains outcomes before
forming its final binary decision.

Two output states have trace distance

```math
d(\rho,\sigma)=\frac12\|\rho-\sigma\|_1.
```

Here $`\|X\|_1`$ is the sum of the singular values of $`X`$. The distance
is the largest difference in the probability of one measurement event.
Subsequent common physical processing cannot increase it. For two channels,
the corresponding reference-assisted distance is
$`\tfrac12\|\Phi-\Psi\|_\diamond`$.
That norm allows an input entangled with a reference, so a bound stated in
it remains valid when the channel is part of a larger experiment. These
notions enter the [controlled-interval proofs](../science/intervention_bounds.md).

## Two descriptions of the same decay

Consider a Markov amplitude-damping law with decay rate $`\gamma>0`$.
If the system starts excited, the probability of still being excited at
time $`t`$ is

```math
p_{\mathrm M}(t)=e^{-\gamma t}.
```

The target channel is $`e^{t\mathcal L_\gamma}`$, where

```math
\mathcal L_\gamma(\rho)
=\gamma\left(\sigma_-\rho\sigma_+
-\frac12\{P,\rho\}\right),
\qquad \sigma_-=|0\rangle\langle1|.
```

The notation $`\{A,B\}=AB+BA`$ denotes an anticommutator. Exponentiating
the generator gives a family of channels satisfying the semigroup rule:
evolving for $`s`$ and then $`t`$ gives the same uninterrupted channel as
evolving for $`s+t`$. The target **process** additionally prescribes using
these channels between interventions, with no bath memory linking those
intervals. The anchor supplies the map and semigroup foundations;
the [operational model](../science/model.md) specifies this controlled use.

Now introduce one environmental qubit $`E`$, initially in $`|0\rangle`$,
and an exchange Hamiltonian

```math
K=g\left(\sigma_+\otimes\sigma_-
+\sigma_-\otimes\sigma_+\right).
```

An excitation oscillates between system and environment. Over an interval
of length $`h`$, write $`\theta=gh`$. Joint unitary evolution gives

```math
|1\rangle_S|0\rangle_E
\longmapsto
\cos\theta\,|1\rangle_S|0\rangle_E
-i\sin\theta\,|0\rangle_S|1\rangle_E.
```

Ignoring the environment gives Kraus operators

```math
A_0=|0\rangle\langle0|+\cos\theta\,|1\rangle\langle1|,
\qquad
A_1=-i\sin\theta\,|0\rangle\langle1|.
```

Choosing $`\cos\theta=e^{-\gamma h/2}`$ makes this channel equal to
the Markov channel at time $`h`$. It matches coherences as well as the
excited-state population, and it works on entangled inputs. It need not
match the target at intermediate times or after an intervention.

This is the first connection to the anchor's microscopic description:
tracing out an environment gives a map, while correlations left inside the
joint system influence later controlled evolution. The
[exact endpoint calculation](../science/amplitude_damping.md#exact-endpoint-channel)
shows the equality directly.

## A complete one-pulse example

Take one lifetime $`T=1/\gamma`$ and choose the strength bound
$`\Lambda=\gamma`$. Use the preceding single collision for the whole
run, with

```math
\theta=\arccos(e^{-1/2}),\qquad g=\gamma\theta\le\gamma.
```

The strength condition holds because $`\theta^2\le1`$, as shown in the
[strength-bound proof](../science/amplitude_damping.md#strength-bound).
The tester prepares $`|1\rangle_S`$; the specified microscopic device
initializes its inaccessible bath in $`|0\rangle_E`$. Read the system
excitation at the fixed final time $`T`$. With no interior operation, both models give
probability $`e^{-1}`$.

For a second experiment, apply one phase flip
$`Z=|0\rangle\langle0|-|1\rangle\langle1|`$ to the system at
$`T/2`$. This is one counted contact. The exchange interaction changes
sign under that phase flip, so with $`U(t)=e^{-itK}`$,

```math
U(T/2)(Z\otimes I)U(T/2)=Z\otimes I.
```

The second half of the collision reverses the excitation transfer from the
first half. The microscopic system ends excited with certainty. Under the
Markov law, the phase flip leaves populations unchanged and the decay
continues, so the final excited-state probability remains $`e^{-1}`$.

| Experiment over the same fixed lifetime | Interior contacts | Microscopic excited probability | Markov excited probability |
|---|---:|---:|---:|
| Prepare, wait, read | 0 | $`e^{-1}`$ | $`e^{-1}`$ |
| Prepare, phase flip halfway, read | 1 | $`1`$ | $`e^{-1}`$ |

If the two hypotheses are equally likely and outcome “excited” selects the
microscopic model, this second experiment succeeds with probability
$`1-e^{-1}/2`$. The experiment remains uncertain under the Markov
hypothesis; observing one outcome does not identify an arbitrary bath.

The example concerns a specified microscopic realization. The full theorem
must also address two different questions: a tester optimized for each
fixed realization, and one tester that works for every allowed realization.
The [optimization order](../science/model.md#two-different-orders-of-optimization)
distinguishes them as $`\Delta_N`$ and $`\Gamma_N`$, respectively.

## A test that works without identifying the bath

The microscopic class allows any finite bath, including a mixed bath and
arbitrary retained memory. Its Hamiltonian is

```math
H_{SE}(t)=I_S\otimes H_E(t)+K(t),
\qquad \|K(t)\|_\infty\le\Lambda.
```

The norm $`\|K\|_\infty`$ is the largest singular value of the complete
system-affecting Hamiltonian. Bath-only motion can be removed by a change
of interaction picture. System-local drives remain charged to the bound.
The initial bath is independent of the prepared system and reference.

For amplitude damping, repeatedly ask whether the system is still excited.
For a general target in the theorem, use a pure system-reference projector
$`P_*`$ chosen to maximize the initial survival loss. If every previous
measurement succeeded, the observed state has returned to the same
rank-one projector. The conditional bath may have changed, but the
[survival estimate](../science/intervention_bounds.md#survival-under-a-bounded-retained-interaction)
still gives

```math
p_{\mathrm{fail,mic}}(\tau)\le\Lambda^2\tau^2.
```

A bounded Hamiltonian first creates a small transition amplitude; the
probability is its square. The target dissipator instead has a linear
short-time loss,

```math
p_{\mathrm{fail,M}}(\tau)=\nu\tau+O(\nu^2\tau^2).
```

For amplitude damping, $`\nu=\gamma`$. In the general theorem,
$`\nu`$ is the maximum initial entanglement-infidelity rate. Its
[definition](../science/dissipators.md#1-generator-intrinsic-rate-and-scope)
uses a possibly mixed system state and its purification. The pure
system-reference probe can therefore outperform every pure system-only
probe for this rate.

Choosing $`\tau`$ proportional to $`\nu/\Lambda^2`$ makes the linear
loss reliably larger than the quadratic bound. The experiment records
whether all its survival measurements succeeded and reports that bit at
$`T=1/\nu`$. It retains failures in the outcome statistics. No discarded
failure ensemble or bath reset is used.

The [universal witness proof](../science/dissipators.md#3-a-universal-survival-witness)
fixes $`\tau=\nu/(8\Lambda^2)`$ and uses at most
$`\min\{N,\lfloor(\Lambda/\nu)^2\rfloor\}`$ contacts. It produces a
positive signed gap, with the same meaning of outcome one, for every
microscopic alternative. This proves a lower bound on $`\Gamma_N`$.

The target class is part of this claim. Its Lindblad jumps must have an
optimally centered representation with no coherent Hamiltonian in that
representation. Centering arbitrary jumps can induce a Hamiltonian term;
the theorem does not remove that physical drift at no cost. The
[scope example](../science/dissipators.md#8-why-centering-does-not-remove-a-hamiltonian-for-free)
exhibits the issue explicitly.

## A model that hides from every permitted tester

The converse requires one microscopic realization with a fixed schedule
that works against every allowed input, reference, instrument and
classically adaptive contact time. Showing that a selected pulse has a
small effect would not establish this quantifier order.

Assume $`\Lambda\ge\nu>0`$ and divide the lifetime into

```math
m=\lfloor(\Lambda/\nu)^2\rfloor,
\qquad h=\frac{1}{\nu m}
```

cells. All bath cells are prepared at time zero. Each interacts once and
is then retained without further coupling. The exact construction uses at
most $`d^2+1`$ bath levels per cell for a system of dimension $`d`$.

For the general dissipator, the distinguished no-jump Kraus operator is
$`A_0=e^{-hQ/2}`$, where $`Q`$ is the sum of the centered jumps'
$`M_a^\dagger M_a`$. The remaining completely positive map supplies the
other Kraus operators. A unitary completion then realizes the **entire**
target cell channel with

```math
\|K_h\|_\infty
=\frac{\arccos(e^{-\nu h/2})}{h}
\le\sqrt{\frac\nu h}\le\Lambda.
```

The [exact-cell proof](../science/dissipators.md#4-exact-cells-with-bounded-hamiltonian-action)
attributes the underlying channel-completion ingredients. An uninterrupted
cell incurs no channel error.

Three further facts turn this endpoint construction into a controlled
process bound.

1. **Bath parity removes first-order errors.** Flipping the sign of the
   cell Hamiltonian can be implemented by a bath parity operation. It
   preserves the initial bath state, commutes with every tester operation,
   and disappears when the bath is traced out. Consequently all odd orders
   in the controlled channel's Dyson expansion vanish. The discrepancy is
   quadratic in the cell's action, even with retained adaptive records.
2. **Only cells with an interior contact contribute.** A cell containing
   only memory operations still has the exact target endpoint map. The
   memory operations commute branch by branch with system-bath evolution,
   including for entangled states. Their record can specify at cell
   entrance whether the first system contact will occur inside that cell.
3. **The adaptive sum uses one probability distribution.** The hybrid
   argument replaces a cell between a microscopic prefix and a Markov
   suffix. All activity probabilities therefore come from the same
   microscopic execution. Each realized branch activates at most $`N`$
   cells, even if different branches contact different cells.

These are the [controlled-interval lemmas](../science/intervention_bounds.md).
They give a cell error at most $`\cosh^2(1)/m`$ and a total error at most
$`N\cosh^2(1)/m`$. The bound applies to complete records and arbitrary
protected references. Many contacts inside one cell do not multiply its
uniform error bound.

## The complete law and its scope

Put $`q=(\nu/\Lambda)^2`$, take $`\Lambda\ge\nu>0`$, and observe one
run over $`T=1/\nu`$. The universal survival test and the single hiding
construction give

```math
\frac1{64}\min\{1,Nq\}
\le\Gamma_N\le\Delta_N
\le\min\{1,2\cosh^2(1)Nq\}.
```

Thus a sufficiently small fixed positive distinguishing gap has contact cost of order
$`(\Lambda/\nu)^2`$. For example, in the asymptotic scaling regime,
doubling the permitted microscopic strength at fixed target rate multiplies
this contact scale by four. The constants in the theorem are not an exact
critical threshold.

At $`N=0`$, both quantities are exactly zero: the hiding construction
matches the fixed terminal channel on every input. An earlier system
measurement is an interior contact, even if its result is saved until the
end. The zero-contact statement depends on that fixed terminal convention.

Solving the same bounds for the strength needed to attain worst-case
accuracy $`\epsilon`$ gives

```math
\Lambda_{\min}(N,\epsilon)
=\Theta\!\left(\nu\sqrt{N/\epsilon}\right),
\qquad N\ge1,\quad 0<\epsilon<1/64.
```

The [interpretation page](../science/interpretation.md) derives the explicit
constants and two robustness statements: a factor-two window of waiting
intervals preserves the survival witness's scaling, and instrument errors
bounded by $`\eta_j`$ in half diamond norm reduce its signed gap by at most
$`2\sum_j\eta_j`$.

The theorem charges coupling strength and system contacts. Its hiding
construction can use an exponentially large finite bath and an externally
prescribed switching schedule. It assumes calibrated $`\nu`$ and
$`\Lambda`$, ideal instantaneous contacts, and one process use. A constant
gap gives statistical evidence; unlimited independent runs, a physical
clock, finite-duration controls and efficient bath preparation require
additional resource accounts.

The [related-work account](../references/RELATED_WORK.md) separates the
established Zeno scale, collision framework, rate normalization and channel
completion tools from the matching controlled-process law studied here.
The [finite checks](../verification/README.md) reproduce the explicit qubit
echo and a general qutrit construction. They check particular constructions;
the uniform claims follow from the linked analytical proofs.

## Temporal access changes global sensing precision

The resolution law concerns discrimination from a fixed dissipator. A
separate sensing experiment asks how well an initially unknown frequency
can be estimated when the same number of contacts can be placed inside
microscopic interactions. To answer it, we need a specified signal-bearing
device, an estimator and a statistical converse. Neither a distinguishability
gap nor the reciprocal of local information supplies that conclusion.

### A fixed collision instrument

Use one sensor, a protected ancillary qubit and a sequence of inaccessible
bath qubits. All bath qubits start in $`|0\rangle`$ at time zero; each
interacts once and is retained afterward. For a cell of fixed duration
$`h`$, the simultaneous signal and coupling are

```math
H=\frac{\epsilon}{2}Z_S\otimes I_E+gN_\phi\otimes X_E,
\qquad \epsilon=\omega-\omega_0,
\qquad N_\phi=\cos\phi\,X_S+\sin\phi\,Y_S.
```

The positive coupling $`g`$, clock $`h`$ and nominal compensation
$`\omega_0`$ stay fixed. The arbitrary unknown angle $`\phi`$ is shared
across all trials. Set $`\chi=gh\in(0,\pi/4)`$ and
$`R=\sqrt{g^2+\epsilon^2/4}`$. A plain cell has Kraus operators

```math
K_{0,p}=\cos(Rh)I-i\frac{\epsilon}{2R}\sin(Rh)Z_S,
\qquad K_{1,p}=-i\frac{g}{R}\sin(Rh)N_\phi.
```

Encoding the logical state in the even-parity span of $`|00\rangle`$ and
$`|11\rangle`$ makes the flip branch change parity. A system–ancilla parity
measurement identifies whether a flip occurred without reading the logical
phase or measuring the bath. Each branch is proportional to a unitary, but
its probability depends on the unknown frequency.

With one fixed coupling and boundary-only access, the companion's
[global converse](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md#the-fixed-coupling-nuisance-curve)
gives inverse-linear worst-case error on a suitable fixed band. This is a
limitation against all permitted adaptive boundary controllers, not a
failure of one recovery circuit. The companion removes it by selecting two
couplings. Here the coupling remains fixed and the additional resource is
access inside cells.

### A temporal menu and retained phases

The two settings are an untouched cell and a cell with one midpoint
$`Z_S`$ pulse. The latter reverses the transverse interaction while preserving
the signal term. Include a known endpoint frame correction in the boundary
instrument. If the echoed cell reports an odd parity, include an additional
conditional $`Z_S`$ in that same instrument. The
[exact calculation](../science/global_contact_precision.md#two-temporal-settings-at-one-coupling)
then makes both settings' flip operators proportional to the same
$`N_\phi`$. These corrections are part of a paid boundary contact.

Use an echoed cell after an even result and a plain cell after an odd result.
Two flips cancel the unknown axis because $`N_\phi^2=I`$, while
$`N_\phi Z_SN_\phi=-Z_S`$ determines the intervening signal's sign.
Every even-ending parity record therefore specifies a known nonlinear phase
function $`\Phi_{\mathcal R}(\epsilon)`$ and a pure logical output
$`e^{-i\Phi_{\mathcal R}(\epsilon)Z_L/2}|+_L\rangle`$ independent of
$`\phi`$. This is exact away from compensation too; it does not make the
record probabilities frequency independent.

Cancellation alone is insufficient. Long phases can wrap around many times,
and some records have poor sensitivity. On one fixed sufficiently small
band, a parameter-independent gate accepts records with probability bounded
away from zero and guarantees that each accepted phase has derivative of
order the block length throughout that band. The
[shared estimator](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/recorded_phase_estimation.md)
first pays for coarse localization, then uses successively longer blocks.
At each stage it measures relative to the phase predicted at the current
interval center and inverts the actual accepted phase functions. Nested
intervals resolve ambiguity, while tapered repetitions control the risk of
an incorrect refinement without a logarithmic cost in the final scaling.
The concentration argument is conditional on the actual records; averaging
then uses their true frequency-dependent law. Rejected blocks still consume
their full duration.

The updated classical estimate selects a readout basis. It never changes
$`\omega_0`$ or physically retunes the device. The pure phase records,
uniform acceptance and estimator are the missing links between a local
echo calculation and a global frequency-error guarantee.

### The full contact budget

Now let $`n`$ count physical sensing cells and $`m`$ count allowed inside-cell
contacts; these are the sensing experiment's resources, distinct from the
contact count $`N`$ and natural lifetime of the discrimination theorem.
The hard deadline is $`T=nh`$, with at most $`n-1`$ total nonterminal
system contacts and at most $`m`$ of them inside cells. Initial preparation
and readout at $`T`$ are free. Every earlier readout counts.

For $`n\ge3`$ and $`m\ge1`$, use the entire temporal-menu estimator,
including calibration and repetitions, within

```math
Q=\min\!\left\{m,\left\lfloor\frac{n-1}{2}\right\rfloor\right\}
```

cells, when $`Q`$ is sufficiently large for that construction. For smaller
$`Q`$, use the plain-cell calibration design described below. The temporal
construction uses at most $`Q`$ interior pulses and $`Q`$ boundary instruments,
including its final early readout. Each boundary instrument combines frame
correction, parity measurement, any conditional correction, readout and reset
as needed. Thus the protocol fits both budgets on every history. Store the
estimate during the remaining charged cells. Since $`Q\ge m/3`$, this gives
error of order $`1/(h^2m^2)`$. A separate design uses all $`n`$ plain cells
for calibration and gives order $`1/(h^2n)`$; choose the better design from
the known budgets. These are alternatives, not two allocations of the same
cells. The plain design also covers zero inside-cell allowance and small
budgets.

For the converse, one smooth nuisance curve cancels coherent parameter
accumulation in untouched cells. A cell with interior controls can contribute
a bounded coherent derivative. The
[hard-activity bound](../science/intervention_bounds.md#a-derivative-bound-with-a-hard-activity-budget)
combines the two contributions: untouched cells give a derivative norm of
order $`\sqrt n`$, while at most $`m`$ active cells give order $`m`$.
A fixed smooth prior converts the uniform information bound into a lower
bound for biased as well as unbiased estimators. The resulting
[global contact law](../science/global_contact_precision.md) is

```math
R^*_{n,m}
=\Theta_{\chi,Eh}\!\left(\frac{1}{h^2(n+m^2)}\right),
\qquad 0\le m\le n-1,
```

uniformly over the shared direction on one fixed band of half-width $`E`$.
The contact budget is structural on every possible history, including rare
branches; an expected contact count would be a different model.

### What the timing record reveals

A known fixed displacement $`\delta`$ of the pulse from the midpoint, with
$`0<|\delta|<h/2`$, and hidden random jitter do not supply the same channel.
The midpoint case $`\delta=0`$ is covered by the ideal contact theorem above.
For a fixed displacement, each parity
branch remains proportional to a unitary. Its axis shift is a known function
of frequency, so the retained record still specifies a known phase function to which the
record-selection and estimation argument applies. A plain/pulsed-cell menu preserves quadratic global precision on a suitable
band when the interior-contact allowance is linear in $`n`$. Here the fixed
displacement is supplied as known device information. Learning an unknown
offset would require an additional model and charged calibration; this
claim does not provide that procedure.

For the [hidden-jitter model](../science/timing_precision.md), every pulsed
cell instead has displacement $`+d`$ or $`-d`$ with equal probabilities,
independently, with $`0<d<h/2`$ known and the realized signs unobserved.
Away from compensation, the odd-parity branch generally mixes two different
operations. Parity does not reveal which one occurred, so it cannot be used
as a pure labelled trajectory.
For the permitted menu of plain cells and one such pulse per pulsed cell,
fixed nonzero jitter gives optimal fixed-band worst-case error
$`\Theta(n^{-1})`$ at fixed hardware. Additional interior pulses, selectable
couplings and retuned compensation lie outside this converse.

With $`m=\Theta(n)`$, at exact compensation the same menu can retain
quadratic pointwise classical Fisher information. This does not contradict the global limitation: a prior
on a fixed subinterval away from compensation supplies the minimax lower
bound. It does not bound risk at every individual frequency. If jitter
shrinks with the experiment and $`m=\Theta(n)`$, the proved necessary
condition for quadratic global precision is

```math
d=O(h/\sqrt n).
```

Sufficiency of this accuracy scale is not proved. The distinction is about
the controller's available timing information and its precise control menu,
not a universal law for all imperfect pulse sequences. These sensing results
have their own device assumptions; they neither extend the centered-generator
resolution theorem to arbitrary signals nor replace its proof.

Return to the [milestone map](MILESTONES.md), the
[anchor bridge](ANCHOR.md), or the [main reading routes](../README.md).
