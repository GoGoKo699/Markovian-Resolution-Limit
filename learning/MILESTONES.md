# Thirty conceptual milestones

[Shared educational anchor](ANCHOR.md) · [Project tutorial](TUTORIAL.md) · [Sister sensing route](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/learning/MILESTONES.md)

This map follows the scientific structure of **Markovian Resolution Limit**. Its sole educational anchor, shared with **Noise-Rate-Activated Sensing**, is Ángel Rivas and Susana F. Huelga, [*Open Quantum Systems: An Introduction*, arXiv:1104.5242v2][rh]. Section numbers refer to that version. The anchor supplies the open-system foundation; local bridges teach instruments, controlled experiments and global estimation. The canonical science pages own the operational definitions and proofs. Research references remain attribution and proof dependencies, not additional educational anchors.

There are exactly thirty project-defined milestones: **M01–M11 cover background and preliminaries; M12–M30 develop the narrative and innovation.** The eleven background targets connect states, channels, norms, generators and environmental memory to a controlled experiment. The nineteen project targets establish the matching resolution law, then study global frequency estimation in the separately specified collision device. Known systematic displacement and hidden timing jitter close that sensing route without changing the headline theorem's quantifiers.

| Route | Milestones | Connection established |
|---|---|---|
| Shared foundation | M01–M11 | Reduced dynamics, microscopic descriptions and the meaning of intervention |
| Resolution theorem | M12–M16 | Resource model, optimization order, intrinsic rate and universal witness |
| Matching construction | M17–M23 | Exact cells, control-uniform bounds, adaptive counting and the resolution law |
| Global sensing consequence | M24–M27 | Fixed-band estimation, retained phases, paid contacts and a matching converse |
| Timing and synthesis | M28–M30 | Supplied timing information, restricted jitter obstruction and complete physical scope |

Each phase proceeds from local objects to a global explanation. The final sensing results require their own estimator and converse; they are not consequences of endpoint agreement or reciprocal local information. This is a reader-independent dependency map, not a schedule or record of personal progress. The sister route uses the same foundation while following the distinct coupling-menu comparison.

## Phase I — Background and preliminaries: M01–M11

<a id="m01"></a>

### M01 — States, probabilities, and the protected reference

- **Central question:** Which quantum state determines an observed probability when the system has both an inaccessible environment and a protected reference?
- **Understanding target:** Distinguish the observed system $`S`$, inaccessible bath $`E`$, and tester memory $`R`$. A reduced state determines local probabilities, while correlations with a retained reference can matter for later joint observations. The initial product requirement separates the bath from the entire prepared $`SR`$ state, without requiring $`S`$ and $`R`$ to be uncorrelated.
- **Earlier dependencies and story role:** This is the starting point. It fixes the physical meaning of the tensor factors used by every subsequent map, instrument, and survival projector.
- **Conceptual connection:** Partial tracing is a statement about available observations. Protecting a reference changes those observations without granting access to the environment.
- **Sources:** [Rivas–Huelga, §§3 and 4.1][rh]; [microscopic alternatives](../science/model.md#microscopic-alternatives); [tester access](../science/model.md#what-the-tester-may-do).

<a id="m02"></a>

### M02 — Complete positivity and channel representations

- **Central question:** What makes a reduced dynamical map valid for every allowed preparation, including entangled inputs?
- **Understanding target:** Connect complete positivity, trace preservation, a Kraus representation, and a unitary realization with an initially independent environment. Equality of channels must continue to hold after adjoining an untouched reference. Different microscopic realizations can implement the same channel at a chosen time.
- **Earlier dependencies and story role:** Builds on [M01](#m01). It supplies the channel language needed for both the Markov target and the exact collision construction.
- **Conceptual connection:** A channel records accessible input-output behavior; a dilation also specifies where correlations are stored. This difference later permits exact endpoint agreement with different responses to an interior contact.
- **Sources:** [Rivas–Huelga, §§4.1–4.2][rh]; [noise laws and controlled experiments](../science/model.md#a-noise-law-is-a-prediction-for-controlled-experiments); [the qubit endpoint channel](../science/amplitude_damping.md#exact-endpoint-channel).

<a id="m03"></a>

### M03 — Instruments, conditional states, and retained records

- **Central question:** How can a measurement both update a quantum state and become part of the data used by later controls?
- **Understanding target:** Treat each instrument outcome as a completely positive branch map whose output trace is its probability. Keeping all branches in a classical register gives a trace-preserving evolution. A recorded event such as all successful projections has an ordinary probability; it is different from renormalizing a postselected ensemble and discarding failed runs.
- **Earlier dependencies and story role:** Uses [M01](#m01)–[M02](#m02). It makes adaptive experiments and the universal survival record mathematically comparable under both hypotheses.
- **Conceptual connection:** Conditional state changes and complete record statistics belong to the same instrument. The uniform bounds apply to the complete experiment, even when individual branches are rare.
- **Sources:** [Rivas–Huelga, §4.2][rh] for the channel background; [tester instruments](../science/model.md#what-the-tester-may-do); [the survival record](../science/amplitude_damping.md#a-universal-survival-experiment).

<a id="m04"></a>

### M04 — Operational distances and contraction

- **Central question:** Which norm controls the largest change of an observable probability, and which norm limits microscopic motion?
- **Understanding target:** Separate the operator norm of a Hamiltonian from trace distance between states and the diamond norm of a map. The diamond norm keeps the comparison valid with a protected reference. Complete trace-preserving processing cannot amplify distinguishability, and a final binary decision is one such processing step.
- **Earlier dependencies and story role:** Uses [M02](#m02)–[M03](#m03). These distinctions prevent a bound on a selected input from being mistaken for a bound against every tester.
- **Conceptual connection:** Norm contraction is what allows a local discrepancy to survive comparison through an arbitrary common continuation without increasing its magnitude.
- **Sources:** [Rivas–Huelga, §§2.1 and 4.3][rh]; [operational discrimination quantities](../science/model.md#two-different-orders-of-optimization); [controlled Markov-to-idle comparison](../science/intervention_bounds.md#a-controlled-markov-cell-compared-with-idle).

<a id="m05"></a>

### M05 — Bounded unitary action and the bath interaction picture

- **Central question:** Which part of a microscopic Hamiltonian can move the system away from an initially occupied subspace?
- **Understanding target:** Relate the size of a unitary rotation over a short interval to the integrated norm of its generator. Bath-only motion can be removed in an interaction picture without changing tester operations or the survival projector. Every retained term acting nontrivially on $`S`$ remains charged to the strength bound $`\Lambda`$.
- **Earlier dependencies and story role:** Uses [M01](#m01) and [M04](#m04). It prepares the microscopic side of the short-time comparison while fixing what the strength resource means.
- **Conceptual connection:** A large bath energy by itself need not produce fast system leakage. An uncharged system drive would change the problem, because it can move the tested subspace directly.
- **Sources:** [Rivas–Huelga, §§2.4 and 3][rh]; [microscopic Hamiltonian convention](../science/model.md#microscopic-alternatives); [bounded-interaction survival](../science/intervention_bounds.md#survival-under-a-bounded-retained-interaction).

<a id="m06"></a>

### M06 — Generators, exponentials, and time-dependent propagation

- **Central question:** How does a local evolution rule determine evolution over a complete interval?
- **Understanding target:** Connect the generator $`\mathcal L`$ to the semigroup $`e^{t\mathcal L}`$, its composition rule, and its short-time expansion. Distinguish that time-homogeneous target from a microscopic evolution family whose Hamiltonian changes with time. Both descriptions compose, but their generators and physical assumptions differ.
- **Earlier dependencies and story role:** Uses [M04](#m04)–[M05](#m05). It supplies the language for Taylor remainders, ordered expansions, and the scheduled collision grid.
- **Conceptual connection:** Local-to-global reasoning requires both a generator estimate and control of the intervening propagators. The semigroup property alone is not a statement about an arbitrary microscopic dilation under interventions.
- **Sources:** [Rivas–Huelga, §§2.2–2.4][rh]; [the target process](../science/model.md#a-noise-law-is-a-prediction-for-controlled-experiments); [controlled-interval comparison](../science/intervention_bounds.md#a-controlled-markov-cell-compared-with-idle).

<a id="m07"></a>

### M07 — Dissipative jumps and coherent motion

- **Central question:** Which parts of a Markov generator describe coherent rotation and which describe dissipation?
- **Understanding target:** Recognize the Hamiltonian commutator and the jump-plus-anticommutator structure of a finite-dimensional GKSL generator. The jump representation need not be unique. A representation change must preserve the complete generator, including any associated coherent term.
- **Earlier dependencies and story role:** Uses [M02](#m02) and [M06](#m06). It provides the ingredients from which the project's intrinsic rate and drift restriction will be defined.
- **Conceptual connection:** Choosing useful coordinates for a generator is different from physically compensating a drive. That distinction determines which targets the general theorem covers.
- **Sources:** [Rivas–Huelga, §5.2][rh]; [generator and intrinsic rate](../science/dissipators.md#1-generator-intrinsic-rate-and-scope); [the centering counterexample](../science/dissipators.md#8-why-centering-does-not-remove-a-hamiltonian-for-free).

<a id="m08"></a>

### M08 — Amplitude damping as the concrete prototype

- **Central question:** What does a simple irreversible Markov law predict for a qubit's population and coherence?
- **Understanding target:** Relate the jump $`\sqrt\gamma\,|0\rangle\langle1|`$ to excited-state survival $`e^{-\gamma t}`$ and coherence decay $`e^{-\gamma t/2}`$. The calibrated lifetime $`1/\gamma`$ supplies a physical unit of time. A dissipative channel's inverse is not generally an admissible channel, even when an algebraic inverse exists.
- **Earlier dependencies and story role:** Uses [M02](#m02), [M06](#m06), and [M07](#m07). This example keeps later abstract constructions tied to an explicit physical process.
- **Conceptual connection:** Irreversibility of the reduced channel can coexist with reversible joint evolution on a larger space. The collision model will realize this coexistence exactly at selected times.
- **Sources:** [Rivas–Huelga, §§4.4 and 5.2][rh]; [the amplitude-damping generator](../science/model.md#a-noise-law-is-a-prediction-for-controlled-experiments); [its exact endpoint realization](../science/amplitude_damping.md#exact-endpoint-channel).

<a id="m09"></a>

### M09 — Reduced evolution and environmental memory

- **Central question:** Where can information about earlier system evolution remain after the environment is inaccessible?
- **Understanding target:** Track the difference between an initially independent bath and a bath that remains independent at later times. Joint evolution can create correlations that influence later reduced evolution. A conditional bath state can change after an observation without being reset or supplied anew.
- **Earlier dependencies and story role:** Uses [M01](#m01)–[M03](#m03) and [M05](#m05). It explains the microscopic freedom admitted by the lower bound and the memory stored inside an exact collision cell.
- **Conceptual connection:** Loss of accessible information does not imply its destruction in the joint state. An intervention can change which correlations affect a subsequent observation.
- **Sources:** [Rivas–Huelga, §§4.1, 6.2.7, and 7][rh]; [microscopic alternatives](../science/model.md#microscopic-alternatives); [a decay curve and its continuation](../science/interpretation.md#a-decay-curve-does-not-specify-a-controlled-process).

<a id="m10"></a>

### M10 — What a microscopic Markov limit establishes

- **Central question:** Why can Markov evolution be an accurate effective description of microscopic dynamics, and what assumptions enter that accuracy?
- **Understanding target:** Place weak-coupling and singular-coupling limits in the relationship between microscopic time scales and an effective semigroup. Recognize that an approximation needs a specified regime and comparison criterion. Accuracy for uninterrupted reduced evolution does not by itself quantify accuracy for every intervention protocol with a stated contact budget.
- **Earlier dependencies and story role:** Uses [M06](#m06), [M07](#m07), [M08](#m08), and [M09](#m09). It gives the conventional physical setting against which the project's finite-strength operational question is posed.
- **Conceptual connection:** Taking a limit that produces a Markov law and testing that law at a finite control resolution ask related but different quantitative questions.
- **Sources:** [Rivas–Huelga, §§6.2–6.3][rh]; [why the resolution scale is quadratic](../science/interpretation.md#why-the-scale-is-quadratic); [physical resources and scope](../science/interpretation.md#physical-resources-and-scope).

<a id="m11"></a>

### M11 — From a decay curve to a controlled process

- **Central question:** Why is agreement with an entire endpoint channel insufficient to settle agreement in experiments that act earlier?
- **Understanding target:** Assemble the background into the project's motivating distinction: the target specifies continuations between contacts, while a microscopic model carries an environment through the run. The experiment can retain quantum memory and classical records. Its joint statistics contain information that a terminal channel or population curve need not determine.
- **Earlier dependencies and story role:** Synthesizes [M08](#m08), [M09](#m09), and [M10](#m10), with their earlier dependencies, and closes the background phase. It motivates measuring validity by the strength of all allowed controlled experiments.
- **Conceptual connection:** The physical question shifts from reproducing an isolated input-output relation to reproducing a process under specified access. The next phase makes that access and its optimization precise.
- **Sources:** [Rivas–Huelga, §§4.5 and 7][rh] for the dynamical background; [controlled-experiment formulation](../science/model.md#a-noise-law-is-a-prediction-for-controlled-experiments); [physical interpretation of endpoint agreement](../science/interpretation.md#a-decay-curve-does-not-specify-a-controlled-process).

## Phase II — Narrative and innovation: M12–M30

<a id="m12"></a>

### M12 — The resource model and the counted contact

- **Central question:** Which experiments and microscopic alternatives belong to the comparison?
- **Understanding target:** Fix the horizon $`T`$, the complete system-affecting bound $`\|K(t)\|\le\Lambda`$, an initially independent finite bath of unrestricted size, and protected tester memory. Every interior system instrument, pulse, reset or swap counts toward $`N`$. Initial preparation, memory-only processing and readout at the fixed terminal time are free. Real contact times may adapt classically; the simulator is fixed before the tester is selected.
- **Earlier dependencies and story role:** Uses [M03](#m03), [M05](#m05), and [M11](#m11). It fixes the domain of both theorem directions.
- **Conceptual connection:** A resource law depends on a precise access model. An early readout is a contact, and an externally prescribed switching schedule does not establish an autonomous clock implementation.
- **Sources:** [Microscopic class](../science/model.md#microscopic-alternatives); [tester class](../science/model.md#what-the-tester-may-do); [terminal convention](../science/model.md#endpoint-and-single-run-conventions).

<a id="m13"></a>

### M13 — A universal signed witness and a minimax distance

- **Central question:** What changes when the tester is chosen before the microscopic alternative instead of after it?
- **Understanding target:** Distinguish $`\Gamma_N=\sup_{\mathsf T}\inf_D(p_D^{\mathsf T}-p_M^{\mathsf T})`$ from $`\Delta_N=\inf_D\sup_{\mathsf T}|p_D^{\mathsf T}-p_M^{\mathsf T}|`$. The first requires one binary decision with the same orientation against every alternative. The second permits the best tester for each fixed device. The relation $`0\le\Gamma_N\le\Delta_N\le1`$ does not assert equality of the optimization orders.
- **Earlier dependencies and story role:** Uses [M04](#m04) and [M12](#m12). It identifies the distinct quantifiers needed by the witness and construction.
- **Conceptual connection:** One test against every device and one device against every test are stronger statements than a successful experiment on one chosen model.
- **Sources:** [Two optimization orders](../science/model.md#two-different-orders-of-optimization); [one universal decision rule](../science/interpretation.md#one-universal-decision-rule).

<a id="m14"></a>

### M14 — The intrinsic rate, maximizing probe and generator norm

- **Central question:** Which dissipative rate and probe calibrate both sides of a reference-assisted resource law?
- **Understanding target:** The maximum sum of jump variances defines $`\nu`$. In an optimally centered representation, $`\nu=\|Q\|`$ with $`Q=\sum_aM_a^\dagger M_a`$. The theorem requires zero coherent drift in that representation. Purifying a maximizing state gives a rank-one survival target $`P_*`$ with initial Markov loss rate $`\nu`$; the same construction proves $`\|\mathcal L\|_\diamond=2\nu`$. Check normalization against damping, dephasing and depolarization, where the maximizing system state need not be pure.
- **Earlier dependencies and story role:** Uses [M07](#m07), [M08](#m08), and [M13](#m13). It supplies the natural horizon and the probe/norm estimates used below.
- **Conceptual connection:** A representation-invariant dissipative scale does not remove physical coherent motion. A protected reference can be essential for attaining the maximal initial escape rate.
- **Sources:** [Intrinsic rate and norm](../science/dissipators.md#1-generator-intrinsic-rate-and-scope); [three calibrated examples](../science/dissipators.md#7-three-explicit-examples); [coherent-drift boundary](../science/dissipators.md#8-why-centering-does-not-remove-a-hamiltonian-for-free).

<a id="m15"></a>

### M15 — Linear Markov loss and quadratic microscopic loss

- **Central question:** At what short-time scale do the two descriptions separate under survival observations?
- **Understanding target:** Compare Markov failure $`\nu\tau+O(\nu^2\tau^2)`$ from $`P_*`$ with microscopic failure at most $`\Lambda^2\tau^2`$. Bounded subspace leakage controls the latter for every conditional bath state. Balancing the two scales gives $`\tau\asymp\nu/\Lambda^2`$, so a lifetime contains order $`(\Lambda/\nu)^2`$ such intervals.
- **Earlier dependencies and story role:** Uses [M05](#m05), [M06](#m06), and [M14](#m14). It identifies the local physical mechanism of the witness.
- **Conceptual connection:** The Zeno short-time mechanism is inherited physics. A matching operational theorem additionally needs a uniform lower witness and a construction against every permitted control.
- **Sources:** [Bounded-interaction survival](../science/intervention_bounds.md#survival-under-a-bounded-retained-interaction); [quadratic resolution scale](../science/interpretation.md#why-the-scale-is-quadratic).

<a id="m16"></a>

### M16 — The universal survival record and its tolerance

- **Central question:** How does a local mismatch become one robust signed signal against every admissible bath?
- **Understanding target:** Repeated successful projections restore $`P_*`$ with a conditional bath state. Multiplying conditional survival bounds needs no bath reset or independent microscopic outcomes. Retaining the all-success event gives a positive gap of order $`\min\{1,N(\nu/\Lambda)^2\}`$. The witness tolerates spacings in $`[\nu/(16\Lambda^2),\nu/(8\Lambda^2)]`$; contact errors $`\eta_j`$ in half diamond norm reduce its signed gap by at most $`2\sum_j\eta_j`$.
- **Earlier dependencies and story role:** Uses [M03](#m03), [M04](#m04), [M13](#m13), and [M15](#m15). It completes the universal lower direction and specifies its stability.
- **Conceptual connection:** All-success is an event in the complete record, not a discarded-failure ensemble. The timing margin and additive instrument bound do not implement finite-duration measurements.
- **Sources:** [General survival witness](../science/dissipators.md#3-a-universal-survival-witness); [timing tolerance](../science/interpretation.md#timing-tolerance-of-the-survival-witness); [instrument errors](../science/interpretation.md#instrument-errors).

<a id="m17"></a>

### M17 — An exact exchange cell and an interior echo

- **Central question:** How can identical uninterrupted channels respond differently to a single intervention?
- **Understanding target:** A qubit exchange with $`\cos\theta=e^{-\gamma h/2}`$ realizes the amplitude-damping channel exactly at duration $`h`$, including on entangled inputs. A midpoint $`Z`$ pulse reverses the exchange and removes microscopic damping in that cell, while the phase-covariant Markov process retains damping. Their excited-state output distance is $`1-e^{-\gamma h}=\sin^2\theta`$.
- **Earlier dependencies and story role:** Uses [M02](#m02), [M08](#m08), [M09](#m09), and [M12](#m12). It supplies the concrete prototype for the upper construction and for useful interior access.
- **Conceptual connection:** Endpoint equality is compatible with hidden memory during a cell. This echo displays local discrepancy; it neither optimizes the full tester class nor proves a global estimation law.
- **Sources:** [Exact endpoint channel](../science/amplitude_damping.md#exact-endpoint-channel); [single-pulse echo](../science/amplitude_damping.md#a-single-pulse-displays-the-cells-hidden-memory).

<a id="m18"></a>

### M18 — Exact parity-odd cells for the general dissipator

- **Central question:** What replaces the exchange cell for several noncommuting jumps?
- **Understanding target:** The exact channel has positive no-jump Kraus operator $`A_0=e^{-hQ/2}`$ and a completely positive remainder with Kraus column $`B`$ satisfying $`B^\dagger B=I-A_0^2`$. Its polar decomposition supplies a direct rotation from the vacuum sector with angle operator $`\Theta=\arccos A_0`$. One dilation must provide exact endpoint action, bounded Hamiltonian norm and odd bath parity simultaneously.
- **Earlier dependencies and story role:** Uses [M02](#m02), [M14](#m14), and [M17](#m17). It generalizes the explicit construction beyond amplitude damping.
- **Conceptual connection:** An arbitrary channel dilation need not have the symmetry required by the control-uniform bound. Exact implementation and small controlled error are separate requirements of the same construction.
- **Sources:** [Exact cells with bounded action](../science/dissipators.md#4-exact-cells-with-bounded-hamiltonian-action).

<a id="m19"></a>

### M19 — A finite bath and a calibrated collision grid

- **Central question:** How do the exact cells form one admissible device over the full lifetime?
- **Understanding target:** Choose $`M=\lfloor(\Lambda/\nu)^2\rfloor`$ cells of duration $`h=1/(\nu M)`$. Their action obeys $`\theta^2\le\nu h`$ and their strength is at most $`\nu\sqrt M\le\Lambda`$. Every bath cell is prepared at time zero, used once and retained afterward. The device and switching schedule are independent of the tester and its contact budget.
- **Earlier dependencies and story role:** Uses [M05](#m05), [M12](#m12), [M14](#m14), and [M18](#m18). It turns an endpoint dilation into a complete microscopic process.
- **Conceptual connection:** A fresh cell is a previously unused part of the initial bath. The construction allows a growing bath and externally prescribed switching; it makes no claim of efficient preparation or autonomous control.
- **Sources:** [Collision-grid calibration](../science/dissipators.md#5-uniform-error-of-an-interrupted-cell); [explicit strength bound](../science/amplitude_damping.md#strength-bound); [resource ledger](../science/interpretation.md#physical-resources-and-scope).

<a id="m20"></a>

### M20 — A uniform bound for every interrupted cell

- **Central question:** Why do arbitrary permitted controls preserve quadratic small-action error?
- **Understanding target:** Bath parity reverses the microscopic Hamiltonian while preserving the initial bath state, tester operations and final bath trace. The complete recorded output is even in coupling, so odd Dyson terms vanish and distance from idle is at most $`\sinh^2\theta`$. The controlled Markov cell is within $`\nu h`$ of the same idle experiment. Together these give an interrupted-cell error at most $`\cosh^2(1)\nu h`$.
- **Earlier dependencies and story role:** Uses [M03](#m03), [M04](#m04), [M06](#m06), [M14](#m14), and [M19](#m19). It completes the local estimate for the upper direction.
- **Conceptual connection:** The same instruments, records and protected reference are used in both comparisons. Contraction concerns physical output states; no monotonicity of an arbitrary Choi-state distance is assumed.
- **Sources:** [Odd-parity controlled cell](../science/intervention_bounds.md#a-controlled-cell-with-odd-bath-parity); [controlled Markov-to-idle bound](../science/intervention_bounds.md#a-controlled-markov-cell-compared-with-idle); [corrected process-distance attribution](../references/RELATED_WORK.md#berk2025).

<a id="m21"></a>

### M21 — Memory-only processing and the entrance activity flag

- **Central question:** Can adaptive timing be handled when the tester measures its protected memory between contacts?
- **Understanding target:** Operations on $`R`$ commute with evolution on $`SE`$, including for correlated inputs. Collect memory-only branch maps up to the first system contact at the cell entrance. The resulting common instrument preserves subnormalized branch states and records the first contact time or a no-contact flag. The cell is therefore marked active before its parameter-dependent evolution in this normal form.
- **Earlier dependencies and story role:** Uses [M01](#m01), [M03](#m03), [M09](#m09), and [M12](#m12). It connects cell estimates to classical adaptive timing.
- **Conceptual connection:** Commutation preserves conditional steering; it does not assume an uncorrelated memory or move operations from beyond the cell into its past.
- **Sources:** [Memory-only controller normal form](../science/intervention_bounds.md#memory-only-controller-normal-form); [allowed timing](../science/model.md#what-the-tester-may-do).

<a id="m22"></a>

### M22 — The physical-prefix hybrid and active-cell counting

- **Central question:** Why does the global discrepancy depend on the paid contact budget across adaptive branches?
- **Understanding target:** Exact inactive cells contribute zero. Active-cell errors are weighted by branch probabilities. A telescoping comparison with a microscopic prefix and an ideal suffix evaluates every activity weight in the same physical execution. Its expected number of active cells is at most $`N`$, so the complete discrepancy is bounded by $`N`$ times the uniform cell error.
- **Earlier dependencies and story role:** Uses [M04](#m04), [M19](#m19), [M20](#m20), and [M21](#m21). It completes the upper direction against every permitted tester.
- **Conceptual connection:** The hybrid order fixes one distribution for all activity weights. Counting the union of contacted cells over incompatible histories would lose the desired resource bound.
- **Sources:** [Activity-weighted hybrid](../science/intervention_bounds.md#why-only-cells-containing-contacts-need-to-be-charged); [global adaptive bound](../science/dissipators.md#6-adaptive-timing-and-the-global-bound).

<a id="m23"></a>

### M23 — The matching resolution law and its strength cost

- **Central question:** What is the complete resource statement after combining the two theorem directions?
- **Understanding target:** For $`\Lambda\ge\nu>0`$, $`T=1/\nu`$ and $`q=(\nu/\Lambda)^2`$, obtain $`(1/64)\min\{1,Nq\}\le\Gamma_N\le\Delta_N\le\min\{1,2\cosh^2(1)Nq\}`$. Exact terminal agreement gives $`\Gamma_0=\Delta_0=0`$. Inverting the unsaturated bounds gives $`\Lambda_{\min}(N,\varepsilon)=\Theta(\nu\sqrt{N/\varepsilon})`$ for $`N\ge1`$ and $`0<\varepsilon<1/64`$.
- **Earlier dependencies and story role:** Synthesizes [M13](#m13), [M16](#m16), and [M22](#m22). It closes the principal discrimination argument and derives its simulation-cost consequence.
- **Conceptual connection:** Constant bias is a one-run statistical advantage, not certain identification. The strength law is distinct from bath-size, preparation and clock costs, and does not identify optimal constants.
- **Sources:** [General theorem](../science/dissipators.md#2-operational-statement); [fixed terminal time](../science/model.md#endpoint-and-single-run-conventions); [controlled-accuracy cost](../science/interpretation.md#coupling-strength-required-for-a-controlled-approximation).

<a id="m24"></a>

### M24 — The separate global frequency-estimation task

- **Central question:** What additional definitions are required before temporal access can be assigned a sensing value?
- **Understanding target:** The sensing device has fixed $`g,h,\omega_0`$, residual frequency $`\epsilon=\omega-\omega_0`$ and a common unknown transverse direction. Define worst-case mean-square error uniformly over that direction and a fixed identifiable band, with $`n`$ cells, at most $`n-1`$ total contacts and at most $`m`$ inside-cell contacts. The full duration is $`nh`$. A calibrated estimate changes measurement choices, not physical compensation. Clock aliases make the fixed-band restriction substantive.
- **Earlier dependencies and story role:** Uses [M02](#m02), [M03](#m03), [M12](#m12), and [M23](#m23). It states a new statistical task without transferring the headline theorem beyond its quantifiers.
- **Conceptual connection:** Local Fisher information does not resolve phase ambiguity. Complete-record closeness transfers bounded loss when uniform, but does not transfer parameter derivatives or establish the sensing law by itself.
- **Sources:** [Global statistical task](../science/global_contact_precision.md#statistical-task-and-resource-model); [complete records and loss](../science/sensing_bridge.md#complete-records-and-bounded-loss-estimation); [clock aliases](../science/sensing_bridge.md#frequency-aliases-of-the-collision-clock); [sensing tutorial](TUTORIAL.md#temporal-access-changes-global-sensing-precision).

<a id="m25"></a>

### M25 — A temporal menu with exact retained phases

- **Central question:** How do plain and echoed collisions remove the shared unknown direction from usable output records?
- **Understanding target:** Use the midpoint echo after even parity and a plain cell after odd parity. Include the known pulse-frame correction and conditional odd correction in the paid boundary instrument. The resulting flip operators have the same unknown axis. An even-ending record cancels that axis exactly and leaves a known nonlinear frequency-dependent phase. A parameter-independent acceptance rule selects records whose phase derivative is uniformly proportional to block length throughout one fixed band.
- **Earlier dependencies and story role:** Uses [M03](#m03), [M17](#m17), and [M24](#m24). It identifies the physical construction used by global estimation.
- **Conceptual connection:** The record remains observed and its probability depends on frequency. Treating the phase as an unobserved averaged rotation, or freezing the record distribution at compensation, would change the statistical experiment.
- **Sources:** [Exact temporal settings](../science/global_contact_precision.md#two-temporal-settings-at-one-coupling); [uniform band and gate](../science/global_contact_precision.md#a-sufficient-fixed-band); [shared recorded-phase method](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/recorded_phase_estimation.md).

<a id="m26"></a>

### M26 — Global phase inversion with every contact paid

- **Central question:** How does the record mechanism become a valid global estimator within both contact budgets?
- **Understanding target:** Coarse localization, nested frequency intervals and tapered multiscale repetitions resolve ambiguity by inverting the actual retained phase functions. Rejected blocks cost their full duration. Set $`Q=\min\{m,\lfloor(n-1)/2\rfloor\}`$: the construction uses at most $`Q`$ interior pulses and $`Q`$ boundary instruments, including its early readout, then stores the estimate through the full horizon. Choose between this quadratic design and the all-plain $`n`$-cell baseline using the known budgets.
- **Earlier dependencies and story role:** Uses [M24](#m24) and [M25](#m25). It proves attainable global order with paid calibration and failures.
- **Conceptual connection:** The estimator uses observed records for conditional concentration; within a stage, later blocks do not adapt to earlier terminal bits. Matching a contact budget requires counting frame corrections and early readout, not only sensing pulses.
- **Sources:** [Recorded-phase attainment](../science/global_contact_precision.md#attainability-by-recorded-phases); [full contact budget](../science/global_contact_precision.md#fit-the-full-contact-budget); [conditional estimator](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/recorded_phase_estimation.md#recorded-phase-estimation-lemma).

<a id="m27"></a>

### M27 — The adaptive global contact converse

- **Central question:** Why can no permitted adaptive controller outperform the contact-budget scaling?
- **Understanding target:** A common smooth nuisance curve makes untouched-cell derivative sources orthogonal. In cells with interior contacts, the full Hamiltonian derivative is bounded. Archived activity flags and the structural bound of $`m`$ active cells on every history give $`J_\epsilon\le4(a_0\sqrt n+b_0m)^2`$, with $`a_0,b_0=O(h)`$ for fixed hardware and band. A fixed smooth prior converts the uniform information bound to minimax risk. Together with attainment, $`R^*_{n,m}=\Theta_{\chi,Eh}([h^2(n+m^2)]^{-1})`$.
- **Earlier dependencies and story role:** Uses [M14](#m14), [M21](#m21), [M24](#m24), and [M26](#m26). It supplies the independent converse needed for the global sensing theorem.
- **Conceptual connection:** The hard budget includes zero-probability histories; an expected-contact constraint is weaker. Global risk extends to the specified operational limits by bounded loss, separately from the derivative-controlled closure for local information.
- **Sources:** [Uniform adaptive converse](../science/global_contact_precision.md#uniform-converse-for-arbitrary-adaptive-contacts); [hard-activity lemma](../science/intervention_bounds.md#a-derivative-bound-with-a-hard-activity-budget); [bounded-loss closure](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md#global-risk-under-controlled-limits).

<a id="m28"></a>

### M28 — Known systematic displacement as supplied information

- **Central question:** Why can a fixed timing displacement preserve quadratic global precision?
- **Understanding target:** For each supplied known $`0<|\delta|<h/2`$, a plain/displaced-one-pulse menu retains pure conditional branches. The flip axis has a known frequency-dependent shift relative to the common unknown direction; even records still cancel that direction. Their exact phases support quadratic global precision on a suitable fixed band when the interior-contact allowance is linear in $`n`$. Retiming is not required for this construction.
- **Earlier dependencies and story role:** Uses [M25](#m25), [M26](#m26), and [M27](#m27). It identifies the timing information needed by the positive extension.
- **Conceptual connection:** The displacement is supplied in the device specification. Learning an unknown offset needs a calibration model and a charged cost; the theorem provides neither free knowledge nor an exact correction from an estimate. Constants need not stay uniform as the fixed displacement approaches zero or either cell endpoint.
- **Sources:** [Exact displaced instrument](../science/timing_precision.md#exact-displaced-and-averaged-instruments); [known-displacement theorem](../science/timing_precision.md#calibrated-systematic-displacement); [timing tutorial](TUTORIAL.md#what-the-timing-record-reveals).

<a id="m29"></a>

### M29 — Hidden jitter and the local/global separation

- **Central question:** Why does unobserved random timing have a different precision consequence from a known fixed displacement?
- **Understanding target:** In each pulsed cell, independently choose $`\delta=\pm d`$ with equal probability and hide the sign. The observed odd-parity branch mixes distinct operations. On a prior interval away from compensation, an environment gauge cancels the derivative overlap for both plain and jittered cells along one nuisance curve, giving optimal fixed-band risk $`\Theta(n^{-1})`$ for fixed $`0<d<h/2`$. The same menu can retain quadratic pointwise classical score information at compensation. For $`m=\Theta(n)`$, quadratic global precision requires $`d=O(h/\sqrt n)`$; sufficiency is not proved.
- **Earlier dependencies and story role:** Uses [M24](#m24), [M27](#m27), and [M28](#m28). It exposes both the information content of timing records and the limits of local precision.
- **Conceptual connection:** The converse is a worst-case obstruction for the specified plain/jittered-one-pulse menu, not a bound at every frequency or for arbitrary pulse sequences. A hidden timing sign cannot be added to the accessible record.
- **Sources:** [Hidden-jitter global theorem](../science/timing_precision.md#global-precision-with-hidden-jitter); [necessary accuracy](../science/timing_precision.md#a-necessary-accuracy-scale); [compensated local information](../science/timing_precision.md#why-the-local-calculation-gives-a-different-answer).

<a id="m30"></a>

### M30 — The complete temporal-resource story and its evidence

- **Central question:** How do the resolution law, sensing consequence and timing limitation form one coherent contribution?
- **Understanding target:** Explain the matching controlled-process law using one universal witness and one universally hiding construction. Then explain the separately proved global contact law and its restricted timing limitation. Assign the noise-strength menu separation and shared recorded-phase estimator to the sister paper. Keep the centered drift-free class, sufficient fixed band, ideal contacts, protected memory, bath preparation and external switching assumptions visible.
- **Earlier dependencies and story role:** Synthesizes [M11](#m11), [M23](#m23), [M27](#m27), and [M29](#m29), with their earlier dependencies. It closes both theorem chains and their attribution boundaries.
- **Conceptual connection:** Temporal resolution as a resource is established prior context. The project adds quantitative matching laws under precise access assumptions. Analytical proofs, finite identity checks and reviewer judgments have different evidential roles; none supplies automatic independent certification or priority.
- **Sources:** [Principal argument](../science/interpretation.md#principal-argument-and-supporting-results); [Berk and corrected monotones](../references/RELATED_WORK.md#berk2023); [proof ingredients](../references/RELATED_WORK.md#how-the-ingredients-enter-the-proof); [verification scope](../verification/README.md); [sister scientific synthesis](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/interpretation.md).

[rh]: https://arxiv.org/html/1104.5242v2
