# Operational model and the two discrimination quantities

## A noise law is a prediction for controlled experiments

A channel at a single final time does not specify how a system responds when an experimenter acts on it earlier. The object studied here is a process: it supplies the joint probabilities of preparations, interventions, and final measurements. The comparison is between a prescribed Markov process and a microscopic unitary model that may retain environmental memory. This distinction between one-time dynamical maps and controlled multitime statistics is established in the process-tensor framework; see [Pollock et al.](../references/RELATED_WORK.md#pollock2018) and [Milz and Modi](../references/RELATED_WORK.md#milz2021).

Fix a finite-dimensional system $`S`$, an observation horizon $`T>0`$, and a target Markov generator $`\mathcal L`$. The target process $`\mathcal M`$ applies $`e^{(t-s)\mathcal L}`$ between consecutive system contacts. These propagators compose independently of earlier contacts, while the tester is free to retain its own quantum memory.

The qubit example uses

```math
\mathcal L_\gamma(X)
=\gamma\left(\sigma_-X\sigma_+
-\frac12\{P,X\}\right),
\qquad
P=|1\rangle\langle1|,
\qquad
\sigma_-=|0\rangle\langle1|.
```

Its horizon is one decay lifetime, $`T=1/\gamma`$. The rate $`\gamma>0`$ is a specified, calibrated target parameter. The theorem does not estimate that rate from data.

## Microscopic alternatives

Let $`\mathfrak D_\Lambda(T)`$ be the following class of microscopic models. A member $`\mathcal D`$ specifies:

1. A finite-dimensional environment $`E`$, with no common dimension bound across the class.
2. An initial environment state $`\eta_E`$, independent of the tester's initial system and reference state.
3. Predetermined Hamiltonian functions

   ```math
   H_{SE}(t)=I_S\otimes H_E(t)+K(t),
   \qquad
   \|K(t)\|_\infty\leq\Lambda
   ```

   for almost every $`t\in[0,T]`$.

We set $`\hbar=1`$. The Hamiltonians are measurable and integrable enough to define their unitary propagators. For example, piecewise continuous functions satisfy this requirement. The environment Hamiltonian $`H_E(t)`$ can have an arbitrarily large norm: bath-only motion is not charged to $`\Lambda`$. Passing to its interaction picture preserves $`\|K(t)\|_\infty`$ and does not affect any tester operation.

All dynamics that act nontrivially on $`S`$ are included in $`K`$. In particular, an unknown fast transverse system drive is not a free resource. The bound is on the complete retained interaction-picture generator, rather than separately on each of many terms whose sum might have a larger norm.

For an initial tester state $`\rho_{SR}`$, the joint initial condition is $`\rho_{SR}\otimes\eta_E`$. Between contacts, the Hamiltonian acts on $`SE`$ and as the identity on the protected tester memory $`R`$. The tester has no access to $`E`$.

A device is fixed before the tester chooses a protocol. Its environment state and Hamiltonian schedule cannot depend on the tester's input, instrument choices, or realized outcomes. Ordinary unitary backaction through $`S`$ is allowed. No environment reset, environmental discard, or new environmental subsystem is supplied after time zero. The constructive model initializes all of its future collision partners at time zero and retains spent partners without coupling to them again.

The class permits externally prescribed time dependence. It does not require an autonomous Hamiltonian, and the cost of a quantum clock implementing the switching schedule is not part of the result. Environment dimension, initial bath purity, and the prescribed schedule are explicit resources of the construction, although they are not the variables optimized by the theorem.

## What the tester may do

An $`N`$-contact tester has an arbitrary finite-dimensional protected memory $`R`$ and a classical record. It may:

- Prepare an arbitrary state $`\rho_{SR}`$ at time zero.
- Apply at most $`N`$ instantaneous instruments that act on $`S`$ and possibly $`R`$, at times strictly between $`0`$ and $`T`$.
- Choose each instrument and its contact time from the previous classical record.
- Perform arbitrary operations on $`R`$ alone between system contacts.
- Make an arbitrary final measurement on $`SR`$ and its records at the fixed time $`T`$.

The final declared output is a bit $`X\in\{0,1\}`$. A tester can retain more detailed records internally and apply any classical decision rule before producing this bit.

Initial preparation and the final readout are not counted in $`N`$. An intermediate readout of $`S`$ is counted even if the tester then stores its result until $`T`$. A swap into a protected memory, a reset of $`S`$, and a unitary pulse on $`S`$ each count as a system contact. Several zero-time operations at the same time may be composed into one instrument; allowing them to count separately cannot improve an upper bound for an at-most-$`N`$ budget.

The contact times may be arbitrary real numbers and may be classically adaptive. No minimum spacing is imposed. There is no continuous uncounted coupling or monitoring of $`S`$ between contacts. The model does not permit coherent superpositions of contact times. The controls and readout are ideal; their finite duration, noise, work cost, and energy cost are not included in the contact count.

For a direct finite-dimensional formulation, first take finite-outcome instruments and finite classical protocol trees, with arbitrarily large finite memory and arbitrarily many finite branches. Also allow their classical mixtures and their operational limits: a limiting tester is admissible when its output probabilities converge for the target and each microscopic alternative. The bounds below are uniform over the finite protocols and therefore extend to this specified closure. No result is asserted about a controller outside this class.

Free memory-only measurements do not create an uncounted observation channel into the evolving system. Even when $`R`$ is entangled with $`SE`$, a map on $`R`$ commutes, branch by branch, with evolution on $`SE`$. The [controller normal form](intervention_bounds.md#memory-only-controller-normal-form) makes this statement precise and includes conditional steering.

## Two different orders of optimization

For a tester $`\mathsf T`$, write

```math
p_{\mathcal P}^{\mathsf T}
=\Pr_{\mathcal P,\mathsf T}\{X=1\}.
```

The distance to the closest microscopic alternative is

```math
\Delta_N(\mathcal M;\Lambda,T)
=\inf_{\mathcal D\in\mathfrak D_\Lambda(T)}
\sup_{\mathsf T\in\mathfrak T_N(T)}
\left|p_{\mathcal D}^{\mathsf T}-p_{\mathcal M}^{\mathsf T}\right|.
```

Here a microscopic device is fixed first, and the inner supremum allows a tester chosen for that device. For fixed $`\mathcal D`$, this supremum is equivalently the largest total-variation distance of complete classical output records: any record can be mapped to the event that attains its total variation, and that binary decision is an allowed tester. A quantum final output can likewise be measured optimally because the final measurement is unrestricted.

The strength of one universally oriented test is a different quantity:

```math
\Gamma_N(\mathcal M;\Lambda,T)
=\sup_{\mathsf T\in\mathfrak T_N(T)}
\inf_{\mathcal D\in\mathfrak D_\Lambda(T)}
\left(p_{\mathcal D}^{\mathsf T}-p_{\mathcal M}^{\mathsf T}\right).
```

Outcome $`1`$ is interpreted as evidence for the microscopic alternative. The same tester and the same decision orientation must work for every $`\mathcal D`$. In an equal-prior binary experiment, a signed probability gap $`b`$ gives success probability $`(1+b)/2`$ under that decision rule.

The elementary comparison is

```math
0\leq\Gamma_N(\mathcal M;\Lambda,T)
\leq\Delta_N(\mathcal M;\Lambda,T)
\leq1.
```

The first inequality follows by choosing a constant-output tester. For every fixed tester and every device, its signed gap is at most that device's best absolute gap. Taking the indicated extrema proves the middle inequality. A saddle point or equality of the two optimization orders is not assumed.

The proofs establish both sides with explicit objects: one survival tester has a positive signed gap for every microscopic model, and one collision model has a small absolute gap for every tester. These are stronger quantifier statements than checking a selected measurement on a selected bath.

## The general intervention law

The main theorem concerns finite-dimensional dissipators that admit an optimally centered jump representation with no coherent term:

```math
\mathcal L(X)=\sum_a\left(M_aXM_a^\dagger
-\frac12\{M_a^\dagger M_a,X\}\right),
\qquad Q=\sum_a M_a^\dagger M_a.
```

The centering condition is

```math
\nu:=\|Q\|_\infty
=\max_{\rho\in\mathsf D(S)}
\sum_a\left(\mathrm{Tr}(\rho M_a^\dagger M_a)
-|\mathrm{Tr}(\rho M_a)|^2\right)>0.
```

The absence of a coherent term is required in this centered representation. Centering an arbitrary Lindblad representation can induce such a term, so this hypothesis is a substantive restriction or an explicit assumption of compensated drift. The [general dissipator theorem](dissipators.md) explains the normalization, proves $`\|\mathcal L\|_\diamond=2\nu`$, and identifies a system-reference state with instantaneous survival loss $`\nu`$.

For a calibrated target rate $`\nu>0`$, set

```math
T=\frac1\nu,
\qquad q=\left(\frac{\nu}{\Lambda}\right)^2.
```

For $`\Lambda\geq\nu`$ and every integer $`N\geq0`$, the theorem gives

```math
\frac1{64}\min\{1,Nq\}
\leq\Gamma_N
\leq\Delta_N
\leq\min\{1,2\cosh^2(1)Nq\}.
```

The constants are independent of system dimension and the number of jumps. The lower bound uses one survival test that does not depend on the microscopic device. The upper bound uses one externally scheduled collision model that is fixed independently of both the tester and its contact budget. Its channel is exactly the target channel at every collision boundary.

## Amplitude damping and the sharper constant

For amplitude damping, put

```math
r=\frac{\Lambda}{\gamma},
\qquad T=\frac1\gamma.
```

For $`r\geq1`$ and every integer $`N\geq0`$, the [amplitude-damping theorem](amplitude_damping.md#matching-bounds) proves

```math
\frac{5}{64}\min\!\left\{1,\frac{N}{r^2}\right\}
\leq\Gamma_N
\leq\Delta_N
\leq
\min\!\left\{1,2\cosh^2(1)\frac{N}{r^2}\right\}.
```

Here $`\nu=\gamma`$, and the exact exponential survival law improves the general lower constant from $`1/64`$ to $`5/64`$.

## Endpoint and single-run conventions

For every target covered by the general theorem, at $`N=0`$ both quantities are exactly zero. This does not mean every microscopic model has the correct endpoint channel. It means that an admissible collision model matches the target channel exactly at the specified final time, including on inputs entangled with $`R`$. Hence terminal-only experiments cannot distinguish that particular model.

The fixed final time matters. A measurement at an earlier time is an interior system contact under this convention. Allowing a freely chosen terminal time changes the zero-contact convention and requires a corresponding statement; it is not silently included here.

The bound concerns one run of duration $`T`$, with probabilities describing repeated executions of that run. It is not a sample-complexity theorem for an uncharged collection of independent runs. Calibration of the target rate $`\nu`$ (equal to $`\gamma`$ for amplitude damping) and certification of the upper bound $`\Lambda`$ are assumptions of the task. Once calibrated, the universal tester uses no knowledge of the bath state, bath dimension, or microscopic Hamiltonian schedule.

## Reading route

The [general dissipator theorem](dissipators.md) supplies the main result, its intrinsic rate, the universal witness, and the exact collision construction. The [controlled-interval bounds](intervention_bounds.md) give the shared survival, parity, and adaptive-controller arguments. The [amplitude-damping example](amplitude_damping.md) provides an explicit exchange Hamiltonian, a sharper lower constant, and an exact single-pulse echo illustrating the local quadratic discrepancy.
