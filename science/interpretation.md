# Physical meaning, resource cost and robust readout

The [operational model](model.md) distinguishes a channel observed at one time
from a process interrogated while it runs. The [qubit proof](amplitude_damping.md)
and [general dissipator proof](dissipators.md) give the same scaling in the
second setting. This page explains what that scaling permits an experimenter
to conclude and which physical resources enter it.

## A decay curve does not specify a controlled process

The map at a prescribed final time can be reproduced exactly by a finite
environment with a bounded interaction. The exact-cell construction also
reproduces every complete cell as a channel, including on inputs entangled
with a private reference. Operations made at cell boundaries therefore see
the correct Markov evolution.

Inside a cell, the system and its current environment acquire correlations.
An intervention can act on those correlations through the system. The
microscopic continuation and the Markov continuation can then differ, even
though the uninterrupted endpoint maps agree.

The matching law bounds the largest detectable difference under a budget of
system contacts. The same hiding construction works for every allowed tester;
its coupling schedule is fixed before the tester is selected. Conversely,
the survival tester is chosen without learning the bath Hamiltonian or state.

This does not conflict with the bounded-Hamiltonian obstruction to an exact
nonunitary semigroup. Agreement at finitely many cell endpoints is weaker than
agreement at every time under arbitrary controls. See
[vom Ende](../references/RELATED_WORK.md#vomende2023) and the
[dilation comparisons](../references/RELATED_WORK.md#burgarth2023).

## Why the scale is quadratic

Let $`\nu`$ be the maximum initial entanglement-infidelity rate of the target
dissipator. Starting from its maximizing purification, the Markov failure
probability in a short interval is

```math
p_{\mathrm{fail,M}}(\tau)=\nu\tau+O(\nu^2\tau^2).
```

For any microscopic alternative with bounded system-affecting interaction,
the probability of leaving the same rank-one system-reference subspace is

```math
p_{\mathrm{fail,mic}}(\tau)\le\Lambda^2\tau^2.
```

Repeated successful projections restore that subspace even when the bath has
memory. Linear Markov loss and quadratic microscopic loss become comparable
at $`\tau\asymp\nu/\Lambda^2`$. There are order
$`(\Lambda/\nu)^2`$ such intervals in the natural time $`T=1/\nu`$.

The short-time mechanism and its relation to the quantum jump time are
established physics; [Schulman](../references/RELATED_WORK.md#schulman2001)
and [random dynamical decoupling](../references/RELATED_WORK.md#viola2005)
already explain the sufficient control scale. The operational result adds a
matching converse: below that scale, a single bounded microscopic realization
can remain close to the Markov process for every allowed experiment.

The theorem is a scaling statement with explicit universal constants. It
does not identify an exact critical contact count or optimize those constants.

## One universal decision rule

Write $`q=\nu^2/\Lambda^2`$, with $`\Lambda\ge\nu`$. The ordinary minimax
distance $`\Delta_N`$ permits the best tester for each fixed microscopic
alternative. The guaranteed signed gap $`\Gamma_N`$ requires one binary tester
whose orientation is correct for every alternative. The theorem proves

```math
\frac1{64}\min\{1,Nq\}
\le\Gamma_N\le\Delta_N
\le\min\{1,2\cosh^2(1)Nq\}.
```

The binary output 1 is the recorded event that every survival projection
succeeded. Its probability is larger for every bounded microscopic model
than for the target Markov process. Thus no bath-dependent decision rule is
hidden in the universal lower bound. Equality of the two game values is not
needed or claimed.

For two fixed, equally likely hypotheses, the optimal success probability is
$`(1+d)/2`$, where $`d`$ is their total-variation distinguishability. A constant
gap therefore means a constant advantage over random guessing in one process
use. It does not mean certain identification from one observed outcome.

## Coupling strength required for a controlled approximation

Define $`\Lambda_{\min}(N,\epsilon)`$ as the infimum of admissible strengths
$`\Lambda\ge\nu`$ for which some microscopic realization has worst-case
$`N`$-contact distance at most $`\epsilon`$. Fix $`N\ge1`$ and
$`0<\epsilon<1/64`$. The matching bounds imply

```math
\nu\sqrt{\frac{N}{64\epsilon}}
\le\Lambda_{\min}(N,\epsilon)
\le\nu\sqrt{\frac{2\cosh^2(1)N}{\epsilon}}.
```

For the lower inequality, an error below $`1/64`$ forces
$`N\nu^2/\Lambda^2<1`$, so the unsaturated lower bound applies. For the
upper inequality, choose the explicit exact-cell simulator with the displayed
strength and use its uniform error estimate. Hence

```math
\Lambda_{\min}(N,\epsilon)
=\Theta\!\left(\nu\sqrt{N/\epsilon}\right).
```

This is a coupling-strength requirement for approximating the entire
controlled experiment. It is not a circuit gate count, a bath-size lower
bound, or a claim about the cost of preparing the environment. Earlier
reset-simulator costs and endpoint simulation algorithms use different
resources and accuracy criteria; the comparison is made in
[Related work](../references/RELATED_WORK.md#cleve2017).

## Timing tolerance of the survival witness

The witness does not require every waiting interval to be exactly equal.
The following corollary concerns the instantaneous survival projections
themselves; it does not replace them by finite-duration measurement pulses.

Choose $`m=\min\{N,\lfloor1/q\rfloor\}`$ and allow each actual waiting time
to satisfy

```math
\frac{\nu}{16\Lambda^2}\le\tau_j
\le\frac{\nu}{8\Lambda^2}.
```

Their total duration is at most $`T/8`$. For every conditional bath state,
microscopic survival in one interval is at least $`1-q/64`$. The target
survival obeys the contractive semigroup Taylor estimate

```math
p_{\mathrm M}(\tau)
\le1-\nu\tau+2\nu^2\tau^2
\le1-q/32.
```

The first inequality follows from
$`\|\mathcal L\|_\diamond\le2\nu`$ and

```math
e^{t\mathcal L}-I-t\mathcal L
=\int_0^t(t-s)\mathcal L^2e^{s\mathcal L}\,ds.
```

Therefore the all-success probability gap is at least

```math
(1-q/64)^m-(1-q/32)^m
\ge\frac{31mq}{2048}
\ge\frac{31}{4096}\min\{1,Nq\}
\ge\frac1{256}\min\{1,Nq\}.
```

The first lower estimate uses the difference of powers and
$`(1-q/32)^{m-1}\ge31/32`$. The next uses
$`mq\ge\tfrac12\min\{1,Nq\}`$.

This establishes a finite interval of acceptable spacings, rather than a
requirement for exact equality of times. The interval endpoints scale with
the calibrated dissipative rate and coupling bound. Arbitrary uncertainty
about those parameters is not covered.

## Instrument errors

Suppose the implemented record-preserving instrument at contact $`j`$ differs
from its ideal version by at most $`\eta_j`$ in half diamond norm, uniformly
over its inputs and any private reference. Replacing the instruments one
at a time changes the final outcome probability under either hypothesis by
at most $`\sum_j\eta_j`$. The implemented signed gap is consequently at least

```math
\text{ideal signed gap}-2\sum_j\eta_j.
```

Errors in the initial preparation or final readout can be included as
additional terms in the same sum. This bound follows from contraction of the
complete record-preserving evolution, so microscopic bath memory does not
invalidate it. It is a conservative worst-case guarantee. A finite-duration
laboratory control must first be shown to realize the required instrument
error while accounting for simultaneous system-bath evolution; the present
theorem does not provide that implementation.

## Temporal access as a global sensing resource

The [sensing bridge](sensing_bridge.md) supplies a separate frequency-estimation experiment with one finite-strength collision device. Its [global contact theorem](global_contact_precision.md) fixes the coupling, clock and nominal compensation, and proves

```math
R^*_{n,m}=\Theta_{\chi,Eh}\!\left(\frac1{h^2(n+m^2)}\right)
```

on a fixed sufficient band, uniformly in the common unknown transverse direction. The experiment has $`n`$ cells, at most $`n-1`$ total contacts and at most $`m`$ contacts inside cells. A menu of echoed and untouched cells gives retained records whose exact phase cancels the unknown direction. The companion's [recorded-phase estimator](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/recorded_phase_estimation.md) resolves ambiguity and charges calibration and rejected blocks. A nuisance curve with bounded derivatives gives the matching global converse for every permitted adaptive controller. This supplies both attainability and a uniform risk argument beyond the earlier local information calculation.

The [timing analysis](timing_precision.md) shows why the controller's timing information matters. A known fixed pulse displacement preserves pure conditional records and allows quadratic global precision with a calibrated temporal menu. Independent unobserved two-point jitter mixes two error axes in the same observed parity branch. For the stated plain/one-pulse menu, any fixed positive jitter restores inverse-time global risk, despite quadratic local information at exact compensation. A jitter scale $`d=O(h/\sqrt n)`$ is necessary for global quadratic precision when the inside-cell allowance is linear in $`n`$; sufficiency and stronger timing controls are outside that result.

These sensing statements have their own fixed-band and access assumptions. They complement the controlled-process resolution law rather than extending its fixed-generator quantifiers to arbitrary metrological models.

## Physical resources and scope

| Resource | Assumption and consequence |
|---|---|
| Interaction strength | Every term affecting the system counts in $`\Lambda`$; bath-only evolution may be removed in an interaction picture. The explicit hiding model even has zero free bath Hamiltonian. |
| Tester access | Initial preparation, the final readout at fixed $`T`$, and processing of protected private memory are free. Each interior contact with the system is counted. |
| Timing and feedback | Real-valued contact times and classical adaptation are allowed. The tester class is the operational closure of finite decision trees described in the model. |
| Environment | The lower bound is independent of bath size and conditional bath state. The upper construction uses $`M=\lfloor(\Lambda/\nu)^2\rfloor`$ fresh cells, retained throughout, of dimension at most $`d^2+1`$ each. |
| Switching and preparation | The simulator uses an externally prescribed switching schedule and initially prepared cells. Clock implementation, preparation work and optimal bath dimension are not charged. |
| Coherent drift | The general theorem requires no coherent term in the optimally centered jump representation. Scalar jump shifts can alter that term; they cannot be used to remove it physically for free. |
| Repetitions | The law concerns one process use over $`T=1/\nu`$. Independent experimental repetitions are an additional resource. |

In particular, a decay curve alone cannot determine a finite upper bound on
the microscopic interaction. The experiment needs a separately justified
$`\Lambda`$; this is central to the older
[environmental-versus-intrinsic noise discussion](../references/RELATED_WORK.md#arenz2015).

The physical conclusion is a limit on the control-uniform validity of a
specified Markov model. It does not diagnose whether an unknown bath is
classical or quantum, establish an autonomous implementation, or identify the
microscopic Hamiltonian. Those questions require additional assumptions and
observables.
