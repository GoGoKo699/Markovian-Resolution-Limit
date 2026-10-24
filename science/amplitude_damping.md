# Amplitude damping: the matching intervention law

Consider the amplitude-damping generator and microscopic alternatives defined in [the model](model.md). Write

```math
T=\frac1\gamma,
\qquad
r=\frac\Lambda\gamma,
\qquad r\geq1.
```

All bounds refer to one run over the fixed horizon $`T`$. The contact count includes intermediate measurements and pulses, while preparation at zero and final readout at $`T`$ are free.

## Matching bounds

**Theorem.** For every integer $`N\geq0`$,

```math
\frac{5}{64}\min\!\left\{1,\frac{N}{r^2}\right\}
\leq\Gamma_N(\mathcal M_\gamma;\Lambda,T)
\leq\Delta_N(\mathcal M_\gamma;\Lambda,T)
\leq
\min\!\left\{1,2\cosh^2(1)\frac{N}{r^2}\right\}.
```

The lower bound uses one tester independent of the microscopic model. The upper bound uses one microscopic model independent of the tester. The constants are not optimized.

It follows that a constant positive signed probability gap can be guaranteed with $`N=\Theta(r^2)`$ contacts, and no smaller asymptotic contact budget can guarantee such a gap. Both optimization quantities are exactly zero at $`N=0`$.

## A universal survival experiment

For $`N\geq1`$, prepare $`S`$ in $`P=|1\rangle\langle1|`$ and set

```math
n=\min\{N,\lfloor r^2\rfloor\},
\qquad
\tau=\frac{\gamma}{4\Lambda^2}
=\frac{1}{4\gamma r^2}.
```

Measure $`\{P,I-P\}`$ at $`\tau,2\tau,\ldots,n\tau`$. Retain the bit indicating whether every measurement returned $`P`$, and report this bit at time $`T`$. Every contact occurs by $`T/4`$. Failed branches remain part of the experiment; the all-success event is a recorded outcome, not a postselected ensemble.

Under the microscopic hypothesis, the [survival lemma](intervention_bounds.md#survival-under-a-bounded-retained-interaction) applies after every success, regardless of the conditional bath state. It gives

```math
p_{\mathcal D}^{\mathsf T}
\geq\cos^{2n}\!\left(\frac{1}{4r}\right)
\geq\left(1-\frac{1}{16r^2}\right)^n
\geq1-\frac{n}{16r^2}.
```

The first elementary inequality uses $`\sin^2 x\leq x^2`$, and the second uses Bernoulli's inequality.

Under the Markov hypothesis, each successful measurement restores the excited state, whose survival probability over a gap $`\tau`$ is $`e^{-\gamma\tau}`$. Thus

```math
p_{\mathcal M_\gamma}^{\mathsf T}
=e^{-\gamma n\tau}
=e^{-n/(4r^2)}.
```

Put $`y=n/r^2\leq1`$. Since $`e^{-z}\leq1-z+z^2/2`$ for $`z\geq0`$,

```math
p_{\mathcal D}^{\mathsf T}-p_{\mathcal M_\gamma}^{\mathsf T}
\geq\frac{3y}{16}-\frac{y^2}{32}
\geq\frac{5y}{32}.
```

For $`r\geq1`$, $`\lfloor r^2\rfloor\geq r^2/2`$. Consequently

```math
y\geq\frac12\min\!\left\{1,\frac{N}{r^2}\right\}.
```

The lower bound follows with the same positive sign for every microscopic alternative. The protocol requires only the calibrated parameters $`\gamma`$ and $`\Lambda`$, not the bath dimension, state, or Hamiltonian path.

## One finite bath that hides from every low-contact tester

Let

```math
m=\lfloor r^2\rfloor,
\qquad
h=\frac{T}{m},
\qquad
\theta=\arccos(e^{-\gamma h/2}).
```

Initialize $`m`$ environment qubits in $`|0\rangle^{\otimes m}`$. During cell $`j`$, couple $`S`$ only to the $`j`$th qubit through

```math
K_j=\frac{\theta}{h}
\left(\sigma_+\otimes\sigma_-^{(j)}
+\sigma_-\otimes\sigma_+^{(j)}\right).
```

Take $`H_E=0`$. After its cell, each bath qubit is retained and never coupled again. The environment dimension is $`2^m`$, and the model uses a prescribed switching schedule. It has no post-initialization resets or supply of fresh external ancillas.

### Exact endpoint channel

The exchange unitary sends

```math
|0\rangle|0\rangle\longmapsto|0\rangle|0\rangle,
\qquad
|1\rangle|0\rangle\longmapsto
\cos\theta\,|1\rangle|0\rangle
-i\sin\theta\,|0\rangle|1\rangle.
```

Its reduced channel therefore has Kraus operators

```math
A_0=|0\rangle\langle0|+\cos\theta\,|1\rangle\langle1|,
\qquad
A_1=-i\sin\theta\,|0\rangle\langle1|.
```

Because $`\cos\theta=e^{-\gamma h/2}`$, this is exactly $`e^{h\mathcal L_\gamma}`$. The equality holds on inputs entangled with any reference. Uninterrupted cells therefore match the target without an approximation error.

### Strength bound

For $`0\leq\theta<\pi/2`$,

```math
-2\log\cos\theta
=2\int_0^\theta\tan u\,du
\geq\theta^2.
```

It follows that $`\theta^2\leq\gamma h=1/m`$ and

```math
\|K_j\|_\infty
=\frac\theta h
\leq\sqrt{\frac\gamma h}
=\gamma\sqrt m
\leq\Lambda.
```

Thus the simulator belongs to the microscopic class. Its construction depends on the calibrated task parameters and the horizon, but not on a tester's contacts. The tester may know the entire collision schedule; the following bound still applies.

## A tester can damage only the cells it contacts

The exchange Hamiltonian is odd under $`Z`$ on its bath qubit, and that qubit starts in a parity eigenstate. Its integrated action is $`a=\theta\leq1`$. The [controlled-cell estimate](intervention_bounds.md#a-controlled-cell-with-odd-bath-parity), followed by the comparison to a controlled Markov cell, gives

```math
\varepsilon_{\mathrm{cell}}
\leq\sinh^2\theta+\gamma h
\leq\frac{\cosh^2(1)}{m}.
```

This estimate includes arbitrary quantum references and complete adaptive measurement records. It is independent of the number of contacts inside that particular cell.

Cells with no interior system contact agree exactly with the target. The [activity-weighted hybrid](intervention_bounds.md#why-only-cells-containing-contacts-need-to-be-charged) therefore bounds every allowed tester's final absolute probability gap by

```math
N\varepsilon_{\mathrm{cell}}
\leq\cosh^2(1)\frac Nm
\leq2\cosh^2(1)\frac{N}{r^2}.
```

Cap the bound at one to obtain the theorem. At $`N=0`$, all cells are inactive, so the entire endpoint channel is exactly $`e^{T\mathcal L_\gamma}`$. This proves $`\Delta_0=0`$ and then $`\Gamma_0=0`$.

## A single pulse displays the cell's hidden memory

The exact endpoint equality does not imply equality under an interior control. Let $`U(\theta/2)`$ be half of one collision. A Pauli $`Z`$ on $`S`$ anticommutes with its exchange generator, so

```math
U(\theta/2)(Z\otimes I)U(\theta/2)=Z\otimes I.
```

The microscopic damping is completely echoed within that cell. Under the target amplitude-damping process, phase covariance instead gives

```math
e^{(h/2)\mathcal L_\gamma}
\circ\mathrm{Ad}_Z
\circ e^{(h/2)\mathcal L_\gamma}
=\mathrm{Ad}_Z\circ e^{h\mathcal L_\gamma}.
```

On an initially excited state, the two cell outputs have trace distance

```math
1-e^{-\gamma h}=\sin^2\theta.
```

This example shows how an interior contact reveals the environmental memory and confirms that the quadratic small-action order of the controlled-cell estimate is attained. It does not replace the uniform upper bound against all testers.
