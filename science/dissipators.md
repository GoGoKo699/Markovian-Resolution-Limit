# Centered finite-dimensional dissipators

The quadratic intervention law extends beyond amplitude damping. For every finite-dimensional dissipator that has an optimally centered jump representation with no coherent term, the same intrinsic rate controls a universal survival experiment and an explicit microscopic simulator. Over the inverse of that rate, a constant distinguishing gap requires a number of system contacts proportional to the square of the ratio between microscopic strength and dissipative rate.

The simulator constructed here reproduces the target channel exactly at every collision-cell boundary. This includes the endpoint experiment with no interventions. Within a cell, a parity symmetry makes its discrepancy under arbitrary permitted controls quadratic in the Hamiltonian action. The result therefore concerns the full controlled process, including retained records and a protected reference, rather than only an uncontrolled reduced channel.

## 1. Generator, intrinsic rate, and scope

Let $`S`$ have dimension $`d<\infty`$, set $`\hbar=1`$, and write

```math
\mathcal L(X)=\sum_{a=1}^{r}\left(
M_aXM_a^\dagger-\frac12\{M_a^\dagger M_a,X\}\right),
\qquad Q=\sum_{a=1}^{r}M_a^\dagger M_a.
```

We assume that this jump representation is **optimally centered**, meaning

```math
\nu:=\|Q\|
=\max_{\rho\in\mathsf D(S)}
\sum_a\left(\operatorname{Tr}(\rho M_a^\dagger M_a)
-|\operatorname{Tr}(\rho M_a)|^2\right)>0,
```

and that there is **no coherent Hamiltonian term in this centered representation**. This is a physical restriction on the generator, or an explicit assumption of compensated drift. It is not a choice of notation that can be made without changing every generator; Section 8 gives a counterexample to that interpretation.

For arbitrary jumps $`L_a`$, the rate has the equivalent form

```math
\begin{aligned}
\nu
&=\max_\rho\sum_a\left(
\operatorname{Tr}(\rho L_a^\dagger L_a)
-|\operatorname{Tr}(\rho L_a)|^2\right)\\
&=\min_{\alpha\in\mathbb C^r}
\left\|\sum_a(L_a-\alpha_aI)^\dagger(L_a-\alpha_aI)\right\|.
\end{aligned}
```

The maximum-variance formula, its minimax form, and the associated optimal measure-and-reset strategy are established ingredients from [Gardner et al.](../references/RELATED_WORK.md#gardner2025), particularly their Eq. (23) and Appendix A. They are used here as a normalization and a witness, not claimed as new.

For completeness, define

```math
F(\rho,\alpha)=\operatorname{Tr}\left[
\rho\sum_a(L_a-\alpha_aI)^\dagger(L_a-\alpha_aI)\right].
```

This function is affine in $`\rho`$, convex in $`\alpha`$, and coercive in $`\alpha`$. Minimizing at fixed $`\rho`$ gives $`\alpha_a=\operatorname{Tr}(\rho L_a)`$. Finite-dimensional convex minimax then permits exchanging the maximum and minimum. At an optimal pair, with $`M_a=L_a-\alpha_aI`$, there is a state $`\rho_*`$ such that

```math
\operatorname{Tr}(\rho_*M_a)=0,
\qquad \operatorname{Tr}(\rho_*Q)=\nu,
\qquad \operatorname{supp}\rho_*
\subseteq\ker(Q-\nu I).
```

Purify $`\rho_*`$ to $`P_*=|\Psi_*\rangle\langle\Psi_*|`$ on $`S R_0`$, with $`\dim R_0\le d`$. The vectors $`|\phi_a\rangle=(M_a\otimes I)|\Psi_*\rangle`$ are orthogonal to $`|\Psi_*\rangle`$, and

```math
(\mathcal L\otimes\mathrm{id})(P_*)
=\sum_a|\phi_a\rangle\langle\phi_a|-\nu P_*.
```

Consequently

```math
-\left.\frac{d}{dt}
\operatorname{Tr}\left[P_*(e^{t\mathcal L}\otimes\mathrm{id})(P_*)\right]
\right|_{t=0}=\nu.
```

Thus $`\nu`$ is the maximum instantaneous entanglement-infidelity slope. Scalar shifts of jumps and isometric mixing of jump labels leave it invariant. In the centered, drift-free setting used here one also has the useful identity

```math
\|\mathcal L\|_\diamond=2\nu.
```

Indeed the completely positive gain map has diamond norm $`\|Q\|=\nu`$, and the anticommutator part has diamond norm at most $`\nu`$. The displayed decomposition of $`\mathcal L(P_*)`$ has trace norm $`2\nu`$, giving the reverse inequality. The reference system is essential in general: the maximizing system state $`\rho_*`$ can be mixed.

## 2. Operational statement

Use the microscopic and tester classes in [the operational model](model.md). In particular, microscopic alternatives have an initially input-independent bath and

```math
H_{SE}(t)=I_S\otimes H_E(t)+K_{SE}(t),
\qquad \|K_{SE}(t)\|\le\Lambda.
```

Bath-only motion is unrestricted when its interaction picture is well defined. All system-affecting terms, including system-local drives, count toward $`K`$. The lower bound permits arbitrary bath memory and mixed bath states. The construction for the upper bound uses a finite bath and $`H_E=0`$.

A tester has a protected reference and memory, a fixed final observation time, retained classical outcomes, and at most $`N`$ instantaneous contacts with $`S`$. Contacts may be arbitrary joint system-reference instruments. Their times may depend classically on earlier outcomes; coherent superpositions of contact times and uncounted continuous access to $`S`$ are excluded. Memory-only processing may be free. Initial preparation and the final readout at the fixed horizon are free.

For a binary tester $`\mathsf T`$, write $`p_D^{\mathsf T}`$ and $`p_M^{\mathsf T}`$ for its output-one probabilities under microscopic model $`D`$ and the target Markov process, respectively. Define

```math
\Gamma_N=\sup_{\mathsf T}\inf_{D}
\left(p_D^{\mathsf T}-p_M^{\mathsf T}\right),
\qquad
\Delta_N=\inf_D\sup_{\mathsf T}
\left|p_D^{\mathsf T}-p_M^{\mathsf T}\right|.
```

The first quantity asks for one signed witness that works against every admissible microscopic model. The second asks how well the best microscopic model withstands every allowed tester. Constant-output testers and weak minimax give $`0\le\Gamma_N\le\Delta_N\le1`$.

**Theorem.** Let $`\Lambda\ge\nu>0`$, set $`T=1/\nu`$ and $`q=(\nu/\Lambda)^2\in(0,1]`$, and let $`N\ge0`$ be an integer. Then

```math
\boxed{
\frac1{64}\min\{1,Nq\}
\le\Gamma_N\le\Delta_N
\le\min\{1,2\cosh^2(1)Nq\}.
}
```

In particular, $`\Gamma_0=\Delta_0=0`$. The constants are independent of the system dimension and jump count. One simulator, chosen independently of the tester and its contact budget, supplies the upper bound for all $`N`$.

## 3. A universal survival witness

For $`N\ge1`$, set

```math
\tau=\frac{q}{8\nu}=\frac{\nu}{8\Lambda^2},
\qquad n=\min\{N,\lfloor1/q\rfloor\}.
```

Prepare $`P_*`$ and measure $`\{P_*,I-P_*\}`$ at $`\tau,2\tau,\ldots,n\tau`$. Store whether every outcome was successful, and read this binary record at $`T`$. The last contact occurs no later than $`T/8`$.

After each success, the system-reference state is exactly the rank-one state $`P_*`$. Any joint state with the bath therefore factors as $`P_*\otimes\omega_E`$ on that branch. The conditional bath state may depend arbitrarily on previous successes. No bath reset or fresh-noise assumption is made.

For $`\Pi=P_*\otimes I_E`$, bath-only evolution commutes with $`\Pi`$. The subspace leakage estimate from [the intervention bounds](intervention_bounds.md) gives

```math
\|(I-\Pi)U(t)\Pi\|\le\Lambda t.
```

It follows that every conditional microscopic failure probability is at most

```math
\Lambda^2\tau^2=\frac q{64}.
```

For the ideal process, let

```math
p(t)=\operatorname{Tr}\left[
P_*(e^{t\mathcal L}\otimes\mathrm{id})(P_*)\right].
```

The first derivative is $`p'(0)=-\nu`$. Since the semigroup is CPTP and $`\|\mathcal L\|_\diamond=2\nu`$, its second-order integral remainder obeys

```math
\|e^{t\mathcal L}-\mathrm{id}-t\mathcal L\|_\diamond
\le\frac{t^2}{2}\|\mathcal L\|_\diamond^2
=2\nu^2t^2.
```

Therefore

```math
p(\tau)\le1-\frac q8+\frac{q^2}{32}
\le1-\frac q{16}.
```

Each ideal success returns the state to $`P_*`$, so Markovianity fixes the next success probability to $`p(\tau)`$. For the all-success event,

```math
p_D\ge(1-q/64)^n,
\qquad p_M\le(1-q/16)^n.
```

The gap is uniform over microscopic models. The difference-of-powers identity and Bernoulli's inequality yield

```math
\begin{aligned}
p_D-p_M
&\ge\frac{3nq}{64}(1-q/16)^{n-1}\\
&\ge\frac{45nq}{1024}\\
&\ge\frac1{64}\min\{1,Nq\}.
\end{aligned}
```

The last line uses $`nq\ge\tfrac12\min\{Nq,1\}`$. This proves the lower bound for $`\Gamma_N`$, hence also for $`\Delta_N`$. When $`Nq\ge1`$, the protocol uses only $`\lfloor1/q\rfloor`$ contacts and gives a fixed positive gap. The saturation statement is an order-one guarantee; it does not assert that perfect discrimination is reached.

## 4. Exact cells with bounded Hamiltonian action

The upper bound uses an exact channel completion. We give the construction because the positivity of its distinguished Kraus operator, its parity, and its norm are all needed. Unitary channel completions and their eigenphase costs are established tools; the relevant precedent is [Fung et al.](../references/RELATED_WORK.md#fung2015). No minimization over all Kraus representations or claim of globally minimum channel cost is needed here.

Fix a duration $`h>0`$ and define

```math
A_0=e^{-hQ/2}.
```

The map $`e^{h\mathcal L}-A_0(\cdot)A_0`$ is completely positive. To see this, split $`\mathcal L=\mathcal G+\mathcal J`$ with

```math
\mathcal G(X)=-\tfrac12\{Q,X\},
\qquad \mathcal J(X)=\sum_aM_aXM_a^\dagger.
```

The time-ordered Dyson expansion in $`\mathcal J`$ is a norm-convergent sum of completely positive maps, since $`e^{s\mathcal G}(X)=e^{-sQ/2}Xe^{-sQ/2}`$. Its zero-jump term is $`A_0(\cdot)A_0`$; every remaining term is completely positive. This is the standard no-jump decomposition, used here in a finite-dimensional channel construction.

Choose Kraus operators $`B_1,\ldots,B_s`$ for that remainder, with $`s\le d^2`$, and stack them as the column operator $`B`$. Trace preservation gives

```math
B^\dagger B=I-A_0^2.
```

Let

```math
\Theta=\arccos A_0,
\qquad B=J\sin\Theta
```

be the polar decomposition of $`B`$. The partial isometry $`J`$ has initial support $`\operatorname{supp}\Theta`$. In particular, $`\Theta`$ vanishes on its kernel, so no inverse or extension of $`J`$ on that kernel is required.

Decompose the cell Hilbert space into the vacuum sector $`S\otimes|0\rangle`$ and its excited sectors, and define

```math
K_h=\frac1h
\begin{pmatrix}
0&-i\Theta J^\dagger\\
iJ\Theta&0
\end{pmatrix}.
```

Its action on the vacuum column is

```math
e^{-ihK_h}
\begin{pmatrix}I\\0\end{pmatrix}
=\begin{pmatrix}\cos\Theta\\J\sin\Theta\end{pmatrix}
=\begin{pmatrix}A_0\\B\end{pmatrix}.
```

Tracing the cell therefore gives **exactly** $`e^{h\mathcal L}`$. Moreover,

```math
\|K_h\|=\frac{\|\Theta\|}{h}
=\frac{\arccos(e^{-\nu h/2})}{h}
\le\sqrt{\frac\nu h}.
```

For the final inequality, put $`\theta=\arccos(e^{-\nu h/2})`$ and use $`-\log\cos\theta\ge\theta^2/2`$ for $`0\le\theta<\pi/2`$. The Hamiltonian is odd under the bath parity

```math
Z=I_S\otimes\left(|0\rangle\langle0|
-\sum_{a=1}^{s}|a\rangle\langle a|\right),
\qquad ZK_hZ=-K_h.
```

The cell needs at most $`d^2+1`$ bath levels. The construction asserts existence with a bounded operator norm; it does not claim a minimal bath, an efficient circuit synthesis, or an autonomous switching controller.

## 5. Uniform error of an interrupted cell

Choose

```math
m=\lfloor1/q\rfloor,\qquad
h=\frac{T}{m},\qquad x=\nu h=\frac1m.
```

Then $`x\le1`$, $`x\le2q`$, and $`\|K_h\|\le\nu\sqrt m\le\Lambda`$. Use $`m`$ fresh cells, initially in their vacuum states, with the preceding Hamiltonian during successive intervals of length $`h`$. Spent cells never interact again. The total bath dimension is at most $`(d^2+1)^m`$; bath size is not the resource optimized by this theorem.

A cell with no interior system contact is exact, including on system-reference inputs. For an active cell, compare its controlled microscopic and controlled Markov outputs through a common controlled idle evolution.

Every tester operation acts outside the cell bath and therefore commutes with $`Z`$. The even-Dyson lemma in [the intervention bounds](intervention_bounds.md) applies to all recorded instruments and classical feedforward inside that cell. With the **actual** action $`\theta=h\|K_h\|\le\sqrt{x}`$, it gives the half-diamond bound

```math
\tfrac12\|\mathcal F_D-\mathcal F_{\mathrm{idle}}\|_\diamond
\le\frac{\cosh(2\theta)-1}{2}
=\sinh^2\theta.
```

The vanishing odd terms are essential: a bound merely linear in $`\theta`$ would not imply the theorem. The same lemma can be proved by purifying the controller and moving its operations into an interaction picture. The transformed coupling remains parity-odd and has the same norm; the initial bath is a parity eigenstate and the final bath trace removes every odd Dyson term.

For the controlled ideal cell, a Duhamel estimate with CPTP contractions gives

```math
\tfrac12\|\mathcal F_M-\mathcal F_{\mathrm{idle}}\|_\diamond
\le\frac h2\|\mathcal L\|_\diamond=x.
```

Thus, independently of the number and placement of contacts inside an active cell,

```math
\tfrac12\|\mathcal F_D-\mathcal F_M\|_\diamond
\le\sinh^2\theta+x
\le\cosh^2(1)x.
```

These are bounds on complete output channels, including a reference and the classical outcome register. No conditioning on an individual low-probability outcome is used.

## 6. Adaptive timing and the global bound

An adaptive protocol can activate different cells on different histories. Counting their union would give the wrong bound. Instead use the memory-controller normal form and the activity-weighted hybrid from [the intervention bounds](intervention_bounds.md).

Before the next contact with $`S`$, combine the controller's memory-only processing into an instrument that outputs the next contact time or a no-contact flag. Its Kraus operations commute branchwise with every system-bath propagator. Moving this instrument to the cell entrance preserves each subnormalized branch state, even when the memory is entangled with the system or bath. The cell's activity is consequently a classical flag at its entrance. Exact boundary contacts can be assigned to the adjacent controller steps.

Use a telescoping hybrid with a microscopic prefix and an ideal suffix. If $`p_j`$ is the probability that cell $`j`$ is active under the genuine microscopic experiment, the cell contributes at most $`p_j\cosh^2(1)x`$ to half trace distance. The common ideal suffix contracts the discrepancy. All $`p_j`$ belong to the same microscopic execution, and each history contains at most $`N`$ active cells, so

```math
\sum_{j=1}^{m}p_j\le N.
```

The final accessible quantum-plus-classical states therefore satisfy

```math
\tfrac12\|\rho_D^{\mathsf T}-\rho_M^{\mathsf T}\|_1
\le\frac{\cosh^2(1)N}{m}
\le2\cosh^2(1)Nq.
```

This proves the upper bound for every binary final measurement. At $`N=0`$ every cell is inactive, and exact composition gives $`e^{T\mathcal L}`$ at the fixed final horizon. Hence $`\Delta_0=0`$. A readout at an earlier time would be an interior system contact under the present convention.

The proof directly covers finite controllers with finite classical outcome trees and arbitrary real contact times. Continuous-outcome controllers are included if the tester class is defined as their operational closure, with approximation preserving the contact budget. The uniform bounds survive that closure. Coherently controlled contact times and continuous system monitoring are outside the model.

## 7. Three explicit examples

The rate depends on the generator convention. The following choices state both the physical decay law and the resulting $`\nu`$.

| Process | Generator and jump convention | Intrinsic rate | A maximizing system state |
| --- | --- | --- | --- |
| Qubit amplitude damping | $`M=\sqrt\gamma\,\lvert0\rangle\langle1\rvert`$; excited population decays as $`e^{-\gamma t}`$ | $`\nu=\gamma`$ | $`\lvert1\rangle\langle1\rvert`$ |
| Qubit dephasing | $`\mathcal L(X)=(\kappa/2)(ZXZ-X)`$, $`M=\sqrt{\kappa/2}\,Z`$; off-diagonal entries decay as $`e^{-\kappa t}`$ | $`\nu=\kappa/2`$ | Any state with $`\operatorname{Tr}(\rho Z)=0`$, including $`\lvert+\rangle`$ |
| Qubit depolarization | $`\mathcal L(X)=\kappa[(I/2)\operatorname{Tr}X-X]`$, $`M_a=\sqrt{\kappa/4}\,\sigma_a`$ for $`a=x,y,z`$; Bloch vectors decay as $`e^{-\kappa t}`$ | $`\nu=3\kappa/4`$ | $`\rho_*=I/2`$, purified by a Bell pair |

For amplitude damping, the variance is $`\gamma(\rho_{11}-|\rho_{01}|^2)`$, maximized at the excited state. For dephasing it is $`(\kappa/2)[1-\operatorname{Tr}(\rho Z)^2]`$. For depolarization, writing $`\rho=(I+\mathbf r\cdot\boldsymbol\sigma)/2`$ gives

```math
\sum_a\operatorname{Var}_\rho(M_a)
=\frac\kappa4(3-|\mathbf r|^2).
```

The depolarizing example shows why ancilla assistance enters the generic witness: pure system states achieve only $`\kappa/2`$, while a purification of $`I/2`$ achieves $`3\kappa/4`$. These examples require no coherent compensation in their displayed centered representations. Their theorem horizons are respectively $`1/\gamma`$, $`2/\kappa`$, and $`4/(3\kappa)`$.

## 8. Why centering does not remove a Hamiltonian for free

For $`L_a=M_a+\alpha_aI`$, direct expansion gives

```math
\sum_a D[L_a](X)
=\sum_aD[M_a](X)-i[H_c,X],
\qquad
H_c=\frac i2\sum_a(\alpha_a^*M_a-\alpha_aM_a^\dagger).
```

For example, take one qubit jump

```math
L=\sqrt\gamma\left(|0\rangle\langle1|+aI\right),
\qquad a\in\mathbb R\setminus\{0\}.
```

The optimally centered jump is $`M=\sqrt\gamma\,|0\rangle\langle1|`$, with $`\nu=\gamma`$. Nevertheless,

```math
D[L]=D[M]-i[H_c,\cdot],
\qquad
H_c=\frac{i\gamma a}{2}
\left(|0\rangle\langle1|-|1\rangle\langle0|\right)
=-\frac{\gamma a}{2}Y,
```

where $`Y=\begin{pmatrix}0&-i\\ i&0\end{pmatrix}`$. The coherent scale can be made arbitrarily large while $`\nu`$ stays fixed. The original generator, although written using a single dissipator, is therefore outside the centered drift-free theorem unless that coherent term is physically compensated. Moving to a rotating frame with arbitrarily fast drift would also rotate the witness and jumps; no drift-uniform extension is asserted here.

## 9. Numerical check of the exact general cell

The accompanying [qutrit check](../verification/verify_dissipator_cell.py) checks one specific risk: whether the general exact-cell completion and the even-action estimate remain correct for nonnormal, noncommuting jumps, a non-diagonal $`Q`$, and recorded adaptive joint system-reference instruments.

Before a common normalization, the three qutrit jumps are

```math
\begin{aligned}
L_1&=|0\rangle\langle1|+0.3i|0\rangle\langle2|,\\
L_2&=0.4|0\rangle\langle1|+0.8|0\rangle\langle2|,\\
L_3&=0.5|1\rangle\langle0|.
\end{aligned}
```

The top eigenspace of $`Q`$ lies in $`\operatorname{span}\{|1\rangle,|2\rangle\}`$, and every jump has zero expectation there. This analytically certifies optimal centering: the maximum variance equals $`\|Q\|`$. Dividing all jumps by $`\sqrt{\|Q\|}`$ sets $`\nu=1`$ while retaining off-diagonal entries of $`Q`$ and noncommutativity.

The tester starts with a maximally entangled qutrit pair, applies two joint instruments, retains all four outcome histories, and selects its second contact time from the first outcome. Six cell durations were checked. The largest endpoint matrix-unit residual was $`3.59\times10^{-15}`$. Reversing the sign of the cell Hamiltonian produced identical reduced recorded outputs at the displayed numerical precision, consistent with odd-order cancellation. The microscopic-to-Markov half trace distance divided by $`x=\nu h`$ was

| $`x`$ | Recorded output distance divided by $`x`$ |
| ---: | ---: |
| 0.000625 | 0.374788 |
| 0.0025 | 0.374504 |
| 0.01 | 0.373370 |
| 0.04 | 0.368881 |
| 0.16 | 0.352199 |
| 0.64 | 0.298109 |

Every instance satisfied the analytic active-cell bound. These numbers are a reproducible finite check of the implementation and scaling, not a computation of a diamond norm, an optimization over testers, or a substitute for the uniform proof. The full output is in [the committed reference result](../verification/expected/dissipator_cell.json); [verification instructions](../verification/README.md) describe reproduction and numerical tolerances.
