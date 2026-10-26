# Markovian Resolution Limit

**How many interventions are needed to resolve bounded microscopic dynamics behind a memoryless quantum-noise law?**

This project proves a matching operational law for finite-dimensional dissipators with an optimally centered jump representation and no coherent Hamiltonian term in that representation. A microscopic model can retain an arbitrarily large finite environment, while the experimenter can use protected quantum memory, keep every measurement outcome, and choose contact times through classical feedback.

Let $`\nu>0`$ be the intrinsic short-time loss rate of the target, let $`\Lambda\ge\nu`$ bound the complete system-affecting microscopic interaction, and observe one run over $`T=1/\nu`$. With at most $`N`$ instantaneous interior system contacts,

```math
\boxed{
\frac1{64}\min\!\left\{1,N\frac{\nu^2}{\Lambda^2}\right\}
\le\Gamma_N\le\Delta_N
\le
\min\!\left\{1,2\cosh^2(1)N\frac{\nu^2}{\Lambda^2}\right\}.
}
```

Here $`\Delta_N`$ is the distance to the closest microscopic model, maximized over all allowed testers after fixing that model. The stronger lower guarantee $`\Gamma_N`$ uses one binary experiment, with the same decision rule, against every microscopic alternative. The [operational model](science/model.md) defines both quantities precisely.

- **Universal witness:** repeated survival projections give a positive probability gap for every bounded-strength microscopic model, without identifying its bath.
- **Uniform converse:** one finite-bath simulator, fixed independently of the tester and its contact budget, stays close to the Markov prediction for every allowed experiment. Its uninterrupted collision cells match the target channels exactly.

Thus a constant single-run distinguishing advantage has a worst-case contact cost proportional to $`(\Lambda/\nu)^2`$. The constants are universal and are not optimized.

## Results and physical scope

| Result | Supported statement |
|---|---|
| General dissipative law | The displayed bounds hold in any finite system dimension for the centered, drift-free generator class. |
| Qubit amplitude damping | For excited-state decay rate $`\gamma`$, $`\nu=\gamma`$; the lower coefficient improves from $`1/64`$ to $`5/64`$. |
| Terminal-only observation | $`\Gamma_0=\Delta_0=0`$: an admissible microscopic construction reproduces the specified final channel exactly, including on entangled inputs. |
| Accuracy versus coupling | For $`N\ge1`$ and $`0<\epsilon<1/64`$, the required strength is $`\Lambda_{\min}(N,\epsilon)=\Theta(\nu\sqrt{N/\epsilon})`$. |
| Timing tolerance | A factor-two range of waiting intervals preserves the universal survival witness's scaling; accumulated instrument errors have an explicit additive bound. |

The generator condition is substantive. Shifting Lindblad jumps by scalar multiples of the identity can change the coherent Hamiltonian needed to represent the same physical dynamics. The [rate definition and counterexample](science/dissipators.md) make that restriction explicit.

The familiar Zeno scale, collision models, variance normalization and one-channel dilation costs are established ingredients. The contribution studied here is their combination into the matching **controlled-process** law, including the converse against every permitted adaptive tester. [Related work](references/RELATED_WORK.md) compares the exact assumptions with prior decoupling, reset-simulation, channel time-energy and continuum-process results.

## Read the science

Start with [the operational model](science/model.md), then follow the construction or proof route of interest.

| Question | Authoritative account |
|---|---|
| What is counted, what is fixed, and which optimization comes first? | [Model and theorem statements](science/model.md) |
| Why do arbitrary adaptive instruments obey the same cell bound? | [Controlled-interval estimates and the adaptive hybrid](science/intervention_bounds.md) |
| How does the theorem work for one decaying qubit? | [Amplitude damping, exchange collisions and an exact echo](science/amplitude_damping.md) |
| Why does the same law hold in arbitrary finite dimension? | [Intrinsic rate, universal witness and exact dissipative cells](science/dissipators.md) |
| What does the law imply for observation and simulation resources? | [Physical interpretation, accuracy cost and robustness](science/interpretation.md) |
| How does the resolution mechanism constrain an actual sensing record? | [Controlled-noise sensing bridge](science/sensing_bridge.md) |
| Which ingredients are inherited and which operational models differ? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

The [LLM reading guide](llms.txt) maps these routes and records the distinctions that must survive a summary.

## Learn the project

The single educational anchor is **Ángel Rivas and Susana F. Huelga, _Open Quantum Systems: An Introduction_ (2012)**, using the [open author version, arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2). It supplies the dynamical-map, semigroup and microscopic-model foundations. The learning route connects those foundations to the operational law proved here.

| Reading need | Route |
|---|---|
| Follow the physical mechanism through a complete example | [From a decay curve to an intervention law](learning/TUTORIAL.md), including a one-pulse experiment with equal uncontrolled endpoints. |
| Connect the selected source to this project's notation and assumptions | [Rivas–Huelga anchor bridge](learning/ANCHOR.md). Section numbers refer to the specified open version. |
| Study the full conceptual structure | [30-milestone map](learning/MILESTONES.md): 11 background/preliminary targets and 19 narrative/innovation targets, each with dependencies and scientific sources. |

The map is common to every reader. The exact theorem statements and complete proofs remain in the scientific pages above.

## Reproduce the finite checks

With Python 3.12 and the pinned dependencies, run from the repository root:

~~~bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
~~~

The checks compare independent channel constructions and exercise reference-assisted adaptive instruments. They cover an exact qubit echo and a centered qutrit example with three nonnormal, noncommuting jumps. The [verification account](verification/README.md) gives the recorded outputs, tolerances and limits. The universal statements follow from the written proofs, not from these finite examples.

## Resource boundaries

The interaction bound includes all system-affecting terms; bath-only evolution is free. Preparation, protected-memory processing and the final readout at fixed $`T`$ are free, while each interior contact with the system is counted. All outcomes are retained, and contact times are classically selected.

The [sensing bridge](science/sensing_bridge.md) separately studies a device with a classical rate input and a signal Hamiltonian. It applies the survival lemma to a retained parity record and constructs a finite-coupling approximation for measurements at collision boundaries. Its full-record error bound transfers bounded-loss risk. The companion [microscopic precision theorem](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_precision.md) proves that boundary-only controls give optimal linear local information at one fixed coupling and quadratic information with two couplings. Moving the same number of contacts to collision midpoints already gives fixed-coupling quadratic information, as the bridge proves directly. This identifies contact placement as a resource. The fixed-generator minimax theorem above is not silently extended to the controlled sensing device or to a global estimation task.

The hiding construction initializes all bath cells at time zero, retains spent cells, and uses an externally prescribed switching schedule. Its bath dimension can grow exponentially in $`(\Lambda/\nu)^2`$. The result is a coupling-and-contact bound, with no claim of efficient bath preparation, autonomous clock implementation or finite-duration control. Independent repetitions of the whole experiment are a separate resource.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
