# Educational anchor: Rivas and Huelga

**Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_**, first edition, SpringerBriefs in Physics (2012). The selected open text is [arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2), dated 9 February 2012: [HTML](https://arxiv.org/html/1104.5242v2), [PDF](https://arxiv.org/pdf/1104.5242v2), [publisher record](https://doi.org/10.1007/978-3-642-23354-8).

**Section numbers below refer to that open version.** This is the project's single educational anchor. Other sources in [Related work](../references/RELATED_WORK.md) support research attribution.

The bridge into this project is a question about the validity of a noise model under intervention: when can bounded microscopic dynamics reproduce a prescribed Markov process, including the observations made while it runs? The anchor supplies the open-system language. The finite-contact comparison and its proof are supplied in the canonical science pages.

## Section-to-project map

The topic labels in this table summarize the relevant material; they are not a second table of contents.

| Open-version sections | Background topic | Project connection |
|---|---|---|
| §§2.1–2.4 | Norms, exponentials, semigroups and propagators | Translate norm estimates into the [controlled Markov-cell bound](../science/intervention_bounds.md#a-controlled-markov-cell-compared-with-idle). |
| §3 | Unitary evolution | Fix the microscopic dynamics and the interaction picture in [Microscopic alternatives](../science/model.md#microscopic-alternatives). |
| §§4.1–4.2 | Reduced maps, Kraus operators and dilations | Compare the [exact qubit endpoint channel](../science/amplitude_damping.md#exact-endpoint-channel) with the [general exact-cell construction](../science/dissipators.md#4-exact-cells-with-bounded-hamiltonian-action). |
| §4.3 | Trace-norm contraction | Follow the error propagation in [Why only cells containing contacts need to be charged](../science/intervention_bounds.md#why-only-cells-containing-contacts-need-to-be-charged). |
| §§4.4–4.5 | Reversibility and composition of reduced maps | Separate endpoint agreement from controlled agreement in [A decay curve does not specify a controlled process](../science/interpretation.md#a-decay-curve-does-not-specify-a-controlled-process). |
| §5.2, Theorem 5.1, Eq. (46) | Time-local GKLS generators | Specialize to the [centered, drift-free generator class](../science/dissipators.md#1-generator-intrinsic-rate-and-scope), retaining its additional assumptions. |
| §§6.1–6.3 | Projection equations and microscopic Markov limits | Connect microscopic time scales to [Why the scale is quadratic](../science/interpretation.md#why-the-scale-is-quadratic). |
| §6.2.7 | Limits of persistent factorization | Track the conditional bath state in [A universal survival witness](../science/dissipators.md#3-a-universal-survival-witness). |
| §6.4 and §§7.1–7.3 | Extensions and descriptions with memory | Locate the theorem's [physical resources and scope](../science/interpretation.md#physical-resources-and-scope); use the [single-pulse echo](../science/amplitude_damping.md#a-single-pulse-displays-the-cells-hidden-memory) as a concrete controlled comparison. |

## Notation and assumptions

| In the anchor | In this project |
|---|---|
| $`A`$ and $`B`$ denote system and environment. | $`S`$ and $`E`$; $`R`$ is protected tester memory. The inaccessible bath is distinct from that memory. |
| $`\mathcal E_{(t,s)}`$ denotes a dynamical map; $`\mathcal L_t`$ its time-local generator. | The target has a time-independent $`\mathcal L`$ and propagator $`e^{(t-s)\mathcal L}`$. Its use between interventions is part of the [operational definition](../science/model.md#a-noise-law-is-a-prediction-for-controlled-experiments). |
| Eq. (46) uses rates $`\gamma_k(t)`$ and operators $`V_k(t)`$. | In the homogeneous case, first absorb rates as $`L_k=\sqrt{\gamma_k}\,V_k`$. The optimally centered jumps $`M_k`$ require a further step; see below. |
| $`K_\alpha`$ are Kraus operators in §4.2. | $`A_0,B_j`$ label exact-cell Kraus operators; $`K(t)`$ or $`K_h`$ is instead a Hamiltonian. |
| §4.3 uses an induced trace norm. | Reference-assisted comparisons use the diamond norm, and observable distances include the factor $`1/2`$. |
| §6 separates local Hamiltonians from $`V`$; weak coupling introduces $`\alpha V`$. | The bound $`\|K(t)\|_\infty\le\Lambda`$ charges **all** system-affecting terms. Only bath-only dynamics is free. |

The generator translation does not remove a coherent term. Locally, the theorem requires

```math
\mathcal L(X)=\sum_k\left(M_kXM_k^\dagger
-\frac12\{M_k^\dagger M_k,X\}\right),
\qquad
\nu=\left\|\sum_k M_k^\dagger M_k\right\|>0
```

in an **optimal centered representation with zero coherent drift**. The value of $`\nu`$ is defined and justified in [Generator, intrinsic rate, and scope](../science/dissipators.md#1-generator-intrinsic-rate-and-scope). Scalar shifts of jumps can induce a Hamiltonian; [the explicit counterexample](../science/dissipators.md#8-why-centering-does-not-remove-a-hamiltonian-for-free) prevents a purely notational extension of the theorem.

Two further distinctions matter when crossing from the source to the project:

- The divisible map families discussed in §§4.5–5.2 do not by themselves specify the response of a microscopic model to every intervention. Here the target is expressly memoryless between contacts, while the alternative retains its environment. The [two optimization quantities](../science/model.md#two-different-orders-of-optimization) compare these complete experiments.
- Initial system–bath independence does not mean independence at every later time. Section 6.2.7 makes that distinction explicit. Locally, a successful rank-one survival projection restores a product with a **conditional** bath state; the bath is neither reset nor assumed unchanged.

## What is supplied locally

The following ingredients belong to the project's account and its research references; they are not attributed to the anchor:

1. **The experimental resource model:** at most $`N`$ instantaneous interior system contacts, classical adaptive timing, protected memory and complete records; see [What the tester may do](../science/model.md#what-the-tester-may-do).
2. **The uniform lower bound:** a survival witness against every admissible bath, using the intrinsic rate $`\nu`$ and a bounded microscopic interaction.
3. **The uniform construction:** exact endpoint cells, their parity-based error bound under arbitrary permitted contacts, and the [adaptive hybrid](../science/dissipators.md#6-adaptive-timing-and-the-global-bound).
4. **The resulting scope:** one run at fixed $`T=1/\nu`$, including $`\Gamma_0=\Delta_0=0`$; see [Endpoint and single-run conventions](../science/model.md#endpoint-and-single-run-conventions). An earlier readout counts as an interior contact.

The [main operational statement](../science/dissipators.md#2-operational-statement) is the canonical theorem. The [physical interpretation](../science/interpretation.md) explains its coupling cost and limits, and [Related work](../references/RELATED_WORK.md#how-the-ingredients-enter-the-proof) identifies the inherited ingredients.

Continue with the [connected tutorial](TUTORIAL.md), the [30-milestone map](MILESTONES.md), or the [main reading routes](../README.md).
