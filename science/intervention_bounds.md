# Bounds for controlled intervals

This page supplies the common estimates used by the collision constructions and survival tests. The operational definitions and counting convention are in [the model](model.md).

## Memory-only controller normal form

Consider an interval with fixed boundaries $`b<e`$, after any common operations assigned to $`b`$. Before the first contact with $`S`$ in this interval, the tester may manipulate and measure its protected memory $`R`$, and use those outcomes to choose when that contact will occur. Stop collecting these memory-only operations at the first system contact or at $`e`$, whichever comes first. The collected controller can be represented by a single instrument on $`R`$ at time $`b`$, whose classical outcome specifies the first contact time and the accumulated local record. Include an outcome for no contact in the open interval $`(b,e)`$. No operation beyond $`e`$ is moved to $`b`$.

To prove this for a finite protocol tree, fix a branch of its memory-only operations. Each map on that branch acts on $`R`$ alone. For any joint $`SE`$ propagator and any branch map $`\mathcal A_R`$,

```math
(\mathcal U_{SE}\otimes\operatorname{id}_R)
\circ(\operatorname{id}_{SE}\otimes\mathcal A_R)
=
(\operatorname{id}_{SE}\otimes\mathcal A_R)
\circ(\mathcal U_{SE}\otimes\operatorname{id}_R).
```

Move the collected branch maps to $`b`$, retaining the originally selected contact time. This yields the same subnormalized joint state at that contact, or at $`e`$ on a no-contact branch. Sum the branch maps with the same declared outcome to obtain the required instrument. The equality also holds for the target Markov propagators, because they act on $`S`$ alone.

This is a branchwise identity even for entangled $`RSE`$ inputs. It preserves conditional steering and is not an appeal to independence of the joint state. Therefore a flag recording whether the interval will contain a system contact can be made classical at its entrance. Subsequent contacts within an active interval may remain fully adaptive.

The construction extends to the operational limits included in the tester class. It does not move a system contact for free or convert continuous system monitoring into a memory-only operation.

## Survival under a bounded retained interaction

Let $`\Pi`$ be a projector on the observed system and any protected reference. Assume that the free environment Hamiltonian acts trivially on that observed space, and the remaining generator has norm at most $`\Lambda`$. If the initial joint state is supported on $`\Pi\otimes I_E`$, then after a duration $`s`$ with no contacts,

```math
\Pr\{\Pi\}\geq\cos^2(\Lambda s),
\qquad 0\leq\Lambda s\leq\frac\pi2.
```

First pass to the interaction picture of the free bath motion. Its propagator commutes with $`\Pi\otimes I_E`$ and preserves the norm bound. Purify the initial state if necessary and write $`q(s)`$ for the probability outside the projector. For almost every time,

```math
\left|\frac{dq}{ds}\right|
\leq2\Lambda\sqrt{q(s)(1-q(s))}.
```

Indeed, only the off-diagonal Hamiltonian block between the two projector subspaces contributes, and its norm is at most $`\Lambda`$. Integrating the scalar comparison from $`q(0)=0`$ bounds the angle $`\arcsin\sqrt{q(s)}`$ by $`\Lambda s`$. The result follows.

After a successful projective measurement, the normalized conditional state is again supported on the same projector. Thus, for successive waiting times $`s_1,\ldots,s_n`$ satisfying the same restriction,

```math
\Pr\{\text{every measurement succeeds}\}
\geq\prod_{j=1}^n\cos^2(\Lambda s_j).
```

The environment can change and become correlated after every contact. No environment reset, fixed conditional bath state, or independence between the outcomes is assumed.

The lemma also holds with a free Hamiltonian that is block diagonal in $`\Pi`$ and a bounded remainder: its interaction picture preserves $`\Pi`$ and the norm. The canonical model only requires bath-only free motion, so this stronger observation is not needed for the headline theorem.

## A controlled cell with odd bath parity

Let a cell of duration $`h`$ start with a fresh environmental subsystem in a state $`\eta`$ invariant under a Hermitian unitary $`Z_E`$. Suppose that the cell Hamiltonian satisfies

```math
Z_EH(t)Z_E=-H(t),
\qquad
a=\int_0^h\|H(t)\|_\infty\,dt.
```

The tester may apply any permitted subroutine during this cell, including quantum references, instruments, record-dependent choices, and classically adaptive contact times. Let $`\mathcal F_H`$ be the resulting channel from the input tester state to its full output state and records after tracing the cell environment. Let $`\mathcal F_0`$ use the same tester subroutine with the cell Hamiltonian removed. Then

```math
\frac12\|\mathcal F_H-\mathcal F_0\|_\diamond
\leq\sinh^2(a).
```

### Proof

For a finite classical protocol tree, collect all branch contact times into one finite ordered set. At each of these times use a fixed record-controlled instrument, applying the identity on branches that do not contact the system then. Complete instruments keep every outcome in an orthogonal register, so these maps are completely positive and trace preserving. This represents the adaptive subroutine by a fixed sequence of channels independent of the Hamiltonian's strength parameter.

Multiply the Hamiltonian by a real parameter $`\alpha`$ and expand the resulting map as an absolutely convergent Dyson series,

```math
\mathcal F_{\alpha H}
=\sum_{k=0}^{\infty}\alpha^k\mathcal F^{(k)}.
```

The Hamiltonian commutator superoperator has diamond norm at most $`2\|H(t)\|_\infty`$. Every intervening complete instrument, environment initialization, and final partial trace has diamond norm one. Ordered integration therefore gives

```math
\|\mathcal F^{(k)}\|_\diamond
\leq\frac{(2a)^k}{k!}.
```

Conjugation by $`Z_E`$ changes $`\alpha`$ to $`-\alpha`$. It leaves the initial environment invariant, commutes with all tester operations, and disappears under the final environmental trace. Thus

```math
\mathcal F_{\alpha H}=\mathcal F_{-\alpha H}.
```

Uniqueness of the power series forces every odd coefficient to vanish. Summing the remaining terms gives

```math
\frac12\|\mathcal F_H-\mathcal F_0\|_\diamond
\leq\frac12\sum_{k=1}^{\infty}\frac{(2a)^{2k}}{(2k)!}
=\frac{\cosh(2a)-1}{2}
=\sinh^2(a).
```

The estimate is independent of the tester memory dimension, number of branches, and number of contacts inside the cell. It therefore extends to the specified operational closure. In particular, it does not lose a square root through a Stinespring-distance estimate.

## A controlled Markov cell compared with idle

Let the target generator satisfy $`\|\mathcal L\|_\diamond\leq2\kappa`$. The same tester subroutine, subjected either to Markov evolution or to idle evolution over a cell of duration $`h`$, obeys

```math
\frac12\|\mathcal F_{\mathcal L}-\mathcal F_0\|_\diamond
\leq\kappa h.
```

For a fixed finite protocol tree, use the same union of branch contact times as above. A Duhamel expansion replaces the evolution by idle one infinitesimal interval at a time. The propagators and complete instruments before and after each replacement are trace-norm contractions, including in the presence of an arbitrary reference. The integral of the generator norm is at most $`2\kappa h`$. Division by two gives the claim.

For qubit amplitude damping, $`\kappa=\gamma`$ is valid: the jump term has diamond norm $`\gamma`$, and the two anticommutator terms together have norm at most $`\gamma`$.

Combining the two cell estimates gives

```math
\frac12\|\mathcal F_H-\mathcal F_{\mathcal L}\|_\diamond
\leq\sinh^2(a)+\kappa h.
```

If $`a\leq1`$ and $`a^2\leq\kappa h`$, convexity of $`\sinh`$ on $`[0,1]`$ yields

```math
\sinh^2(a)+\kappa h
\leq\cosh^2(1)\kappa h.
```

## Why only cells containing contacts need to be charged

Suppose a simulator is built from finitely many cells, each starting with an independent fresh bath subsystem. Each cell bath is retained but never coupled again after its cell. Assume that, in the absence of an interior system contact, the endpoint channel of the cell equals the target channel exactly. Suppose also that the controlled cell discrepancy is at most $`\varepsilon_j`$ for every permitted subroutine.

The unused future bath subsystems remain in their initial product states. Spent subsystems can be traced out for the purpose of computing future tester statistics because they never interact again. This is an analytical reduction of the explicit construction; it does not assume that an arbitrary environment can be physically discarded or reset between cells.

Use the memory-only normal form to define a classical activity flag at cell entrance. On the inactive flag, memory-only operations commute with the cell evolution and the endpoint channels agree exactly. On the active flag, the uniform controlled-cell estimate applies to the normalized conditional input. By homogeneity, for an input state $`\rho`$ the cell discrepancy obeys

```math
\frac12\|(\Phi_j-\Psi_j)(\rho)\|_1
\leq\varepsilon_j\,p_j(\rho),
```

where $`\Phi_j`$ is the simulator cell, $`\Psi_j`$ the target cell, and $`p_j(\rho)`$ the probability that the flag is active. The entrance flag instrument is common to both cells.

For an initial tester state $`\rho_0`$, expand the difference of the complete evolutions as

```math
\Phi_m\cdots\Phi_1-\Psi_m\cdots\Psi_1
=\sum_{j=1}^m
\Psi_m\cdots\Psi_{j+1}
(\Phi_j-\Psi_j)
\Phi_{j-1}\cdots\Phi_1.
```

The suffix in each term is a target channel and contracts the trace norm. The prefix is always the simulator prefix. Consequently every activity probability in the bound is evaluated under the same complete simulator execution:

```math
\frac12\|\rho_{\mathrm{sim}}-\rho_{\mathrm{target}}\|_1
\leq\sum_{j=1}^m\varepsilon_j\,\Pr_{\mathrm{sim}}\{j\text{ is active}\}.
```

On every realized branch, at most $`N`$ cells can contain a system contact. Therefore

```math
\sum_j\Pr_{\mathrm{sim}}\{j\text{ is active}\}
=\mathbb E_{\mathrm{sim}}[\text{number of active cells}]
\leq N.
```

For a uniform cell bound $`\varepsilon_j\leq\varepsilon`$, the final distance is at most $`N\varepsilon`$. Applying the tester's final binary decision cannot increase it.

This argument accommodates classically adaptive timing without counting the union of all cells that could be active on different branches. Such a union could be much larger than $`N`$ and would give the wrong bound.

Contacts exactly at a cell boundary are common zero-time operations between two matched endpoint channels. They consume the tester's contact budget but need not be charged as an active interior cell. An ordering convention at a boundary has no dynamical cost because the Hamiltonian's value at a single time does not affect its propagator.
