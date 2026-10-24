# Related work and attribution

## The operational question

The main theorem compares a prescribed memoryless dissipative process with microscopic unitary models whose system-affecting Hamiltonian has operator norm at most $`\Lambda`$. The experiment lasts one intrinsic dissipative time, $`T=1/\nu`$. A tester can use a protected reference, retain every outcome, and make at most $`N`$ instantaneous contacts with the system at classically adaptive times. Preparation and the observation at the fixed final time are free.

For the centered, drift-free dissipators specified in the theorem, the optimal microscopic approximation satisfies

```math
\Delta_N
=\Theta\!\left(\min\left\{1,\frac{N\nu^2}{\Lambda^2}\right\}\right),
\qquad \Lambda\geq\nu .
```

The lower bound uses one survival experiment against every admissible microscopic model. The upper bound constructs one microscopic model that works against every admissible tester. Its collision cells reproduce the target channel exactly at their boundaries, including the final channel when $`N=0`$. The estimate controls observations inside the cells and the complete adaptive record.

The distinctions below concern those quantifiers and assumptions. Quadratic short-time survival, the Zeno crossover, fresh-ancilla collision models, the intrinsic variance rate, and the time-energy cost of a single channel are established ingredients.

## Comparison by source class

| Source class | Representative sources | Established result used or compared | Additional question addressed here |
|---|---|---|---|
| Zeno dynamics and jump time | [Misra–Sudarshan](#misra1977), [Schulman](#schulman2001) | Repeated projections suppress decay; the crossover combines a quadratic survival time with a decay lifetime. | Optimal distinguishability at each finite intervention budget, uniformly over microscopic models. |
| Dynamical decoupling | [Viola–Knill](#viola2005), [Hillier et al.](#hillier2015), [Arenz et al.](#arenz2015) | Fast control suppresses bounded environmental noise and can distinguish it from intrinsic Markovian noise. | A matching simulator that hides against all allowed experiments, including nonunitary adaptive instruments. |
| Reset and collision simulation | [Cleve–Wang](#cleve2017), [Cattaneo et al.](#cattaneo2021), [Pocrnic et al.](#pocrnic2025) | Resource bounds and convergence for prescribed repeated-interaction simulations of endpoint channels. | Retained bath memory, arbitrary microscopic alternatives, and probes at arbitrary times inside collision cells. |
| Quantum trajectories and channel time-energy cost | [Dalibard et al.](#dalibard1992), [Fung–Chau](#fung2013), [Fung et al.](#fung2015) | No-jump evolution and bounded-angle unitary extensions of channels. | Use of an explicit parity-odd extension to bound a whole controlled collision cell. |
| Lindblad metrology | [Gardner et al.](#gardner2025) | Maximum jump variance, its centered-operator minimax form, and measure-and-reset sensing. | Comparison of ideal Markov dynamics with finite-coupling microscopic dynamics. |
| Dilation obstructions and dependence on the dilation | [vom Ende](#vomende2023), [Burgarth et al. 2023](#burgarth2023) | Exact nonunitary semigroups require singular resources in the relevant dilation setting; controlled behavior depends on the dilation. | Quantitative approximation at fixed coupling and finite intervention count. |
| Operational descriptions of memory | [Pollock et al.](#pollock2018), [Milz–Modi](#milz2021) | A multi-time process maps sequences of interventions to their output statistics. | A resource-constrained comparison of a Markov process with microscopic realizations. |
| Hidden memory and continuum approximation | [Burgarth et al. 2021](#burgarth2021), [Fuksa et al.](#fuksa2026) | Exact finite-window hiding with a singular bath; density of bounded-Hamiltonian representations in a continuum process topology. | A fixed operator-norm budget and uniform error for instantaneous intervention testers. |
| Recent controlled-process comparisons | [Salzmann et al.](#salzmann2026), [Wang](#wang2026) | Adaptive discrimination of Lindbladians; complete-record decoupling estimates under specified random control. | A matched minimax law between a Markov target and a class of bounded-coupling microscopic models. |

## Zeno dynamics and dynamical decoupling

<a id="misra1977"></a>
### Misra and Sudarshan (1977)

B. Misra and E. C. G. Sudarshan, “The Zeno's paradox in quantum theory,” *Journal of Mathematical Physics* **18**, 756–763 (1977). [Publisher and DOI](https://doi.org/10.1063/1.523304).

This is a foundational source for inhibition of quantum transitions by repeated projections. The lower-bound mechanism in this project belongs to that tradition: bounded microscopic motion gives quadratic leakage, whereas the target dissipator has a linear initial loss. The finite-budget minimax comparison requires additional estimates and a converse construction.

<a id="schulman2001"></a>
### Schulman (2001)

L. S. Schulman, “Jump time and passage time: the duration of a quantum transition,” [arXiv:quant-ph/0103151v1](https://arxiv.org/abs/quant-ph/0103151v1), 27 March 2001.

Schulman's jump time is $`\tau_J=\tau_Z^2/\tau_L`$, with $`\tau_Z=\hbar/\Delta H`$. With a decay rate $`\nu`$ and a microscopic energy scale $`\Lambda`$, this identifies the scale $`\nu/\Lambda^2`$ that also appears here. The crossover scale itself is therefore established. The present statement resolves the best achievable discrimination bias, including the regime below constant bias.

<a id="viola2005"></a>
### Viola and Knill (2005)

Lorenza Viola and Emanuel Knill, “Random decoupling schemes for quantum dynamical control and error suppression,” *Physical Review Letters* **94**, 060502 (2005). [DOI](https://doi.org/10.1103/PhysRevLett.94.060502); [arXiv:quant-ph/0511120v1](https://arxiv.org/html/quant-ph/0511120v1).

Theorem 2 bounds random-decoupling error for bounded, possibly time-dependent interactions by order $`T\,\delta t\,\Lambda^2`$. At $`T=1/\nu`$, this already gives the square-law control scale $`N\sim(\Lambda/\nu)^2`$. It is an error guarantee for a specified control protocol. It does not construct a microscopic model whose error is small for every possible tester.

<a id="hillier2015"></a>
### Hillier, Arenz, and Burgarth (2015)

Robin Hillier, Christian Arenz, and Daniel Burgarth, “A continuous-time diffusion limit theorem for dynamical decoupling and intrinsic decoherence,” *Journal of Physics A: Mathematical and Theoretical* **48**, 155301 (2015). [DOI](https://doi.org/10.1088/1751-8113/48/15/155301); [arXiv:1405.7666v3](https://arxiv.org/html/1405.7666v3).

Theorem 14 gives asymptotic fidelity bounds for random decoupling and distinguishes bounded microscopic decoherence from intrinsic decoherence. The control-spacing dependence is a close precursor to the lower-bound intuition. The estimates concern the chosen decoupling dynamics and their limiting regime, rather than an infimum over microscopic simulators followed by a supremum over all intervention strategies.

<a id="arenz2015"></a>
### Arenz, Hillier, Fraas, and Burgarth (2015)

Christian Arenz, Robin Hillier, Martin Fraas, and Daniel Burgarth, “Distinguishing decoherence from alternative quantum theories by dynamical decoupling,” *Physical Review A* **92**, 022102 (2015). [DOI](https://doi.org/10.1103/PhysRevA.92.022102); [arXiv:1405.7644v4](https://arxiv.org/html/1405.7644v4).

This work already proposes fast-control discrimination of environmental decoherence and intrinsic Lindblad noise. Its amplitude-damping example uses a two-qubit dilation with coupling divergent at the initial time, and the necessary control rate depends on the dilation. The conceptual discrimination proposal is inherited background. Here the norm budget is fixed across the microscopic model class and both directions of the operational bound are proved.

## Collision simulation and channel implementation

<a id="cleve2017"></a>
### Cleve and Wang (2017; extended version 2019)

Richard Cleve and Chunhao Wang, “Efficient Quantum Algorithms for Simulating Lindblad Evolution,” *ICALP 2017*, LIPIcs **80**, 17:1–17:14. [Publisher and DOI](https://doi.org/10.4230/LIPIcs.ICALP.2017.17); [extended arXiv:1612.09512v3](https://arxiv.org/html/1612.09512v3), 4 January 2019.

Appendix A, Definition 3, specifies repeated identical bounded-Hamiltonian stages with an ancillary reset and accuracy at prescribed grid endpoints. Theorem 4 requires total normalized Hamiltonian time $`\Omega(\sqrt m)`$ for $`m`$ stages approximating amplitude damping at fixed accuracy. Their square-root dilation resource divergence and standard short-step dilation are direct predecessors. The specified reset architecture differs from the present class of time-dependent models with retained environments, and their endpoint criterion does not include arbitrary interventions between grid points.

<a id="cattaneo2021"></a>
### Cattaneo and collaborators (2021)

Marco Cattaneo, Gabriele De Chiara, Sabrina Maniscalco, Roberta Zambrini, and Gian Luca Giorgi, “Collision Models Can Efficiently Simulate Any Multipartite Markovian Quantum Dynamics,” *Physical Review Letters* **126**, 130403 (2021). [DOI](https://doi.org/10.1103/PhysRevLett.126.130403); [arXiv:2010.13910v2](https://arxiv.org/html/2010.13910v2).

The construction simulates multipartite GKLS evolution with collision scaling $`g_I^2\delta t`$ held fixed. Endpoint induced trace-norm estimates have order $`t^2/m`$; the analysis uses cancellation of odd exchange terms after tracing the fresh bath. These are established collision ingredients. Exact endpoint channels alone do not control experiments performed during a collision; the present upper bound supplies a uniform estimate for each cell containing interventions.

<a id="pocrnic2025"></a>
### Pocrnic, Segal, and Wiebe (2025 version)

Matthew Pocrnic, Dvira Segal, and Nathan Wiebe, “Quantum Simulation of Lindbladian Dynamics via Repeated Interactions,” [arXiv:2312.05371v4](https://arxiv.org/html/2312.05371v4), 18 March 2025.

Theorem 2 supplies explicit induced trace-norm convergence bounds for repeated-interaction approximations to Lindblad endpoint evolution. It further develops the simulation side of the problem. The norm comparison is between endpoint maps for the prescribed simulator; it is not the adaptive process distance optimized here.

<a id="garg2025"></a>
### Garg and collaborators (2025)

Kushagra Garg, Zeeshan Ahmed, Subhadip Mitra, and Shantanav Chakraborty, “Simulating quantum collision models with Hamiltonian simulations using early fault-tolerant quantum computers,” *Physical Review A* **112**, 022425 (2025). [DOI](https://doi.org/10.1103/3trk-smbh); [arXiv:2504.21564v2](https://arxiv.org/html/2504.21564v2).

This work develops collision-model implementation algorithms and endpoint-observable resource estimates. It is relevant to implementation costs, which are separate from this project's coupling-norm and intervention-count tradeoff. The present construction does not claim efficient bath size, circuit depth, or clock implementation.

<a id="dalibard1992"></a>
### Dalibard, Castin, and Mølmer (1992)

Jean Dalibard, Yvan Castin, and Klaus Mølmer, “Wave-function approach to dissipative processes in quantum optics,” *Physical Review Letters* **68**, 580–583 (1992). [DOI](https://doi.org/10.1103/PhysRevLett.68.580); [author-hosted article](https://pro.college-de-france.fr/jean.dalibard/publications/MCWF92.pdf).

Quantum-jump trajectories separate non-Hermitian no-jump evolution from jump events. The exact-cell proof uses this standard decomposition. For a drift-free generator with $`Q=\sum_k M_k^\dagger M_k`$, the zero-jump term has Kraus operator $`A_0=e^{-hQ/2}`$; all trajectories with jumps form a completely positive remainder. Positivity of $`A_0`$ is useful for a low-angle unitary extension.

<a id="fung2013"></a>
### Fung and Chau (2013)

Chi-Hang Fred Fung and H. F. Chau, “Time-energy measure for quantum processes,” *Physical Review A* **88**, 012307 (2013). [DOI](https://doi.org/10.1103/PhysRevA.88.012307); [arXiv:1305.5776v2](https://arxiv.org/html/1305.5776v2).

Section V.4 and Eq. (44) construct unitary extensions using rotations on orthogonal two-dimensional subspaces when a Kraus operator is diagonal. Applied to the positive $`A_0`$, this gives an implementation with angle at most
```math
\arccos\lambda_{\min}(A_0)=\arccos e^{-h\nu/2}\leq\sqrt{h\nu}.
```
Thus the one-channel time-energy estimate is already available from this work. The explicit parity-odd realization in the present proof additionally lets the same norm estimate control arbitrary system interventions during the cell.

<a id="fung2015"></a>
### Fung, Chau, Li, and Sze (2015)

Chi-Hang Fred Fung, H. F. Chau, Chi-Kwong Li, and Nung-Sing Sze, “Solution to time-energy costs of quantum channels,” *Quantum Information and Computation* **15**, 685–693 (2015). [Publisher DOI](https://doi.org/10.26421/QIC15.7-8-9); [arXiv:1404.4134v2](https://arxiv.org/html/1404.4134v2).

Theorem 1 solves the optimal unitary-extension cost using the smallest eigenvalue of the Hermitian part of a linear combination of Kraus operators. Selecting the positive no-jump Kraus operator reproduces the bound above. That selection supplies a sufficient implementation bound; it need not minimize the channel's cost. A single-channel speed estimate does not itself establish approximation of an entire controlled process.

## The intrinsic dissipative rate

<a id="gardner2025"></a>
### Gardner and collaborators (2025)

James W. Gardner, Simon A. Haine, Joseph J. Hope, Yanbei Chen, and Tuvia Gefen, “Lindblad estimation with fast and precise quantum control,” *Physical Review Applied* **24**, 044055 (2025). [DOI](https://doi.org/10.1103/6yzb-43rs); [arXiv:2501.03364v2](https://arxiv.org/html/2501.03364v2).

Section II.4.1, Eq. (23), identifies the maximum sum of jump-operator variances in noiseless Lindblad estimation. Appendix A supplies its minimax form, with purification allowing a mixed system state:
```math
\nu=\max_\rho\sum_k\!\left(\mathrm{Tr}\,\rho L_k^\dagger L_k-
|\mathrm{Tr}\,\rho L_k|^2\right)
=\min_{\alpha_k}\left\|\sum_k(L_k-\alpha_k I)^\dagger(L_k-\alpha_k I)\right\|.
```
The optimal-state projection strategy is also established there. Both the normalization and this choice of probe are inherited. Here the microscopic hypothesis has bounded coupling, while their estimation model assumes Lindblad evolution under fast control. The separate requirement of zero coherent drift in an optimal centered representation remains an explicit assumption of this project's theorem.

## Dilation obstructions and controlled processes

<a id="pollock2018"></a>
### Pollock and collaborators (2018)

Felix A. Pollock, César Rodríguez-Rosario, Thomas Frauenheim, Mauro Paternostro, and Kavan Modi, “Non-Markovian quantum processes: Complete framework and efficient characterization,” *Physical Review A* **97**, 012127 (2018). [DOI](https://doi.org/10.1103/PhysRevA.97.012127); [arXiv:1512.00589v3](https://arxiv.org/abs/1512.00589v3).

The process-tensor framework describes multi-time quantum dynamics through the statistics produced by sequences of interventions, including environmental memory. This is the operational perspective underlying the present comparison. Agreement of reduced channels at selected times is a weaker requirement than agreement of the corresponding controlled experiments.

<a id="milz2021"></a>
### Milz and Modi (2021)

Simon Milz and Kavan Modi, “Quantum Stochastic Processes and Quantum non-Markovian Phenomena,” *PRX Quantum* **2**, 030201 (2021). [DOI](https://doi.org/10.1103/PRXQuantum.2.030201); [arXiv:2012.01894v2](https://arxiv.org/abs/2012.01894v2).

This tutorial develops quantum stochastic processes using quantum combs and explains their operational treatment of memory. It supplies broader context for the distinction between a one-time dynamical map and a controlled multi-time process. The coupling norm and intervention budget in this project are additional resource restrictions on that setting.

<a id="vomende2023"></a>
### vom Ende (2023)

Frederik vom Ende, “Quantum-Dynamical Semigroups and the Church of the Larger Hilbert Space,” *Open Systems & Information Dynamics* **30**, 2350003 (2023). [DOI](https://doi.org/10.1142/S1230161223500038); [arXiv:2211.08351v3](https://arxiv.org/html/2211.08351v3).

Theorem 1 shows that a finite-dimensional dynamical semigroup admits a bounded, time-independent Hamiltonian Stinespring representation only if it is unitary. Its initial derivative is Hamiltonian; Theorem 2 characterizes the dissipative second derivative. This gives a qualitative obstruction to exact bounded dilation. The present result concerns approximate controlled behavior at finite coupling, permits time-dependent microscopic interactions, and quantifies finite observational resources.

<a id="burgarth2023"></a>
### Burgarth, Facchi, and Hillier (2023)

Daniel Burgarth, Paolo Facchi, and Robin Hillier, “Control of quantum noise: on the role of dilations,” *Annales Henri Poincaré* **24**, 325–347 (2023). [DOI](https://doi.org/10.1007/s00023-022-01211-y); [arXiv:2010.00279v2](https://arxiv.org/html/2010.00279v2).

The same GKLS evolution can admit autonomous dilations with different responses to dynamical decoupling. Their constructions make clear that the family of reduced channels does not determine controlled behavior. A bound on the microscopic interaction, and a process-level comparison, are therefore substantive hypotheses rather than details inferable from a master equation.

<a id="burgarth2021"></a>
### Burgarth, Facchi, Lonigro, and Modi (2021)

Daniel Burgarth, Paolo Facchi, Davide Lonigro, and Kavan Modi, “Quantum non-Markovianity elusive to interventions,” *Physical Review A* **104**, L050404 (2021). [DOI](https://doi.org/10.1103/PhysRevA.104.L050404); [arXiv:2108.05750v1](https://arxiv.org/html/2108.05750v1).

A microscopic process can reproduce a Markov process under every intervention over a prescribed finite window and reveal memory later. The construction uses singular point interactions in a continuum bath, with non-square-integrable form factors and a renormalized singular limit. It does not have the finite interaction-norm budget assumed here. The present finite-coupling bounds quantify a limitation that such singular realizations evade.

<a id="fuksa2026"></a>
### Fuksa, Wassner, Eisert, and White (2026)

Jonáš Fuksa, Clara Wassner, Jens Eisert, and Gregory A. L. White, “Dilation theorem for continuum quantum stochastic processes,” [arXiv:2609.35403v1](https://arxiv.org/html/2609.35403v1), 28 September 2026.

Theorem 1 proves density of finite-dimensional bounded-Hamiltonian process representations in a continuum Fock norm. Definition 5 and Eq. (8) connect that norm to output statistics with a tester-dependent instrument norm. Instantaneous insertions require distributional treatment; the stronger topology discussed for them does not impose one uniform Hamiltonian bound along all approximations. Density in that topology therefore does not yield the fixed-$`\Lambda`$, uniform-$`N`$-tester estimate considered here.

<a id="salzmann2026"></a>
### Salzmann, Lami, Plenio, and Huelga (2026)

Robert Salzmann, Ludovico Lami, Martin B. Plenio, and Susana F. Huelga, “Discriminating Lindbladian Dynamics,” [arXiv:2610.03629v1](https://arxiv.org/html/2610.03629v1), 2 October 2026.

This work studies discrimination of fixed Lindbladians with adaptive durations and control, including the role of temporal resolution and Zeno strategies. Both hypotheses remain Markovian under the interventions. Here one hypothesis is a prescribed Markov process and the other ranges over bounded-coupling microscopic models whose environmental memory is retained.

<a id="wang2026"></a>
### Wang (2026)

He Wang, “Continuous-Process Randomized Compilation for Quantum Process Tensors,” [arXiv:2610.01521v2](https://arxiv.org/html/2610.01521v2), 3 October 2026.

Theorem 2 bounds the complete adaptive experimental record under bounded centered coupling, autonomous random control, and pointwise-covariant finite-duration instruments. Its reference experiment removes the centered interaction while retaining the environment propagation. This is directly relevant process-level error control. The result is a decoupling guarantee for its specified control model; it does not construct bounded-coupling approximations to a dissipative Markov target or supply the corresponding minimax converse.

## General background

<a id="ciccarello2022"></a>
### Ciccarello, Lorenzo, Giovannetti, and Palma (2022)

Francesco Ciccarello, Salvatore Lorenzo, Vittorio Giovannetti, and G. Massimo Palma, “Quantum collision models: Open system dynamics from repeated interactions,” *Physics Reports* **954**, 1–70 (2022). [DOI](https://doi.org/10.1016/j.physrep.2022.01.001); [arXiv:2106.11974v2](https://arxiv.org/abs/2106.11974v2).

This pedagogical review develops collision maps, their continuous-time limits, quantum trajectories, and mechanisms of non-Markovianity. The discussion of diverging coupling in the Markov limit gives a direct physical introduction to the resource constraint studied here.

<a id="rivas2012"></a>
### Rivas and Huelga (2012)

Ángel Rivas and Susana F. Huelga, *Open Quantum Systems: An Introduction*, first edition, SpringerBriefs in Physics, Springer (2012). [Publisher and DOI](https://doi.org/10.1007/978-3-642-23354-8); [author preprint, arXiv:1104.5242v2](https://arxiv.org/abs/1104.5242v2).

The mathematical structure of dynamical maps and semigroups, and their microscopic derivations, provides background for the theorem's assumptions.

<a id="breuer2002"></a>
### Breuer and Petruccione (2002)

Heinz-Peter Breuer and Francesco Petruccione, *The Theory of Open Quantum Systems*, Oxford University Press (2002), ISBN 9780198520634. [Publisher's 2002 hardcover record](https://global.oup.com/academic/product/the-theory-of-open-quantum-systems-9780198520634).

The treatment of master equations, quantum operations, trajectories, and non-Markovian dynamics provides broader physical background.

## How the ingredients enter the proof

The lower bound combines the established quadratic-survival estimate with the established maximum-variance probe and keeps the observed failure flag until the common final time. It is uniform in the bath state, bath memory, and allowed time dependence.

The upper bound combines quantum-jump channel decompositions with bounded-angle Stinespring extensions. Its additional controlled-process step is a uniform estimate for a collision cell containing arbitrary interventions. Cells containing no system contact agree exactly at their endpoints. In the adaptive hybrid argument, replacements preserve a common physical prefix, so the activation probabilities belong to a single experiment and sum to at most $`N`$. Trace-norm contractivity then controls every retained output register.

The resulting contribution is the matching operational law with these microscopic and experimental quantifiers. No assumption of efficient bath size, autonomous switching, finite-duration control pulses, or unrestricted coherent drift is part of that statement.

Machine-readable entries, with keys matching the explicit anchors above, are in [references.bib](references.bib). Comparisons refer to the linked versions.
