# From a decay curve to an intervention law

A quantum system can lose an excitation while interacting with a larger,
closed system. Looking only at the smaller system can make that reversible
interaction resemble irreversible noise. The question in this project is
how often an experimenter must act on the smaller system to expose a
difference between those two descriptions when the microscopic interaction
has a known strength bound.

The single educational anchor is Rivas and Huelga's *Open Quantum Systems:
An Introduction*. The [anchor bridge](ANCHOR.md) identifies the exact source
version, relevant sections, and notation. This tutorial connects those
foundations to the project's argument; the [30-milestone map](MILESTONES.md)
gives the complete conceptual route. Exact assumptions and proofs belong to
the linked pages under `science/`.

## Route through the explanation

| Part | Milestones | Connection |
|---|---|---|
| [States, maps and records](#states-maps-and-records) | [M01–M04](MILESTONES.md#m01) | A physical experiment becomes a probability distribution. |
| [Two descriptions of the same decay](#two-descriptions-of-the-same-decay) | [M05–M11](MILESTONES.md#m05) | A reduced unitary evolution can match a Markov channel at a specified time. |
| [A complete one-pulse example](#a-complete-one-pulse-example) | [M12–M13](MILESTONES.md#m12), [M18–M19](MILESTONES.md#m18) | An interior operation distinguishes controlled processes with equal endpoints. |
| [A test that works without identifying the bath](#a-test-that-works-without-identifying-the-bath) | [M14–M17](MILESTONES.md#m14) | Short-time loss and a retained survival record give a universal witness. |
| [A model that hides from every permitted tester](#a-model-that-hides-from-every-permitted-tester) | [M20–M25](MILESTONES.md#m20) | Exact cells, parity and adaptive composition give the converse. |
| [The complete law and its scope](#the-complete-law-and-its-scope) | [M26–M30](MILESTONES.md#m26) | The two bounds determine the contact scale and coupling cost. |

The one-pulse example can be read before the formal rate construction. It
illustrates one particular microscopic model. The universal result requires
the two proof directions developed afterward.

## States, maps and records

Let $`S`$ denote the observed system. Its state is a positive matrix
$`\rho`$ with trace one. A measurement outcome has a positive effect
$`F`$ with $`0\le F\le I`$, and its probability is
$`\operatorname{Tr}(F\rho)`$. For a two-level system, the pure states
$`|0\rangle`$ and $`|1\rangle`$ can represent the ground and excited
states. The projector $`P=|1\rangle\langle1|`$ asks whether the excitation
is present.

A quantum channel $`\Phi`$ transforms input states into output states. It
must also work on a system entangled with an otherwise untouched reference
$`R`$: the enlarged transformation is $`\Phi\otimes\operatorname{id}_R`$.
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

Return to the [milestone map](MILESTONES.md), the
[anchor bridge](ANCHOR.md), or the [main reading routes](../README.md).
