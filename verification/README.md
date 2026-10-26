# Reproduce the finite checks

The universal statements are analytical. These calculations test concrete
implementation risks in the exact collision channels and their response to
interventions. They include complex nonnormal jumps, protected references,
retained outcome records and classical adaptation of a contact time.

## Run

The recorded environment uses Python 3.12, NumPy 2.3.5 and SciPy 1.17.0.
From the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The runner executes all three scripts with assertions enabled, checks their
results against the committed reference quantities, and exits unsuccessfully
if a scientific assertion or comparison fails. A normal run does not modify
the reference files. Either script can also be run directly to print its full
JSON result.

For a scientifically reviewed change, regenerate the reference outputs
explicitly and then run the ordinary verification:

```bash
python3 verification/run_all.py --record
python3 verification/run_all.py
```

Recording an output does not independently validate it. Changes to a
calculation require checking its equations and physical meaning.

## What each calculation checks

| Script | Independent comparisons | Scope |
|---|---|---|
| [Qubit cell](verify_amplitude_cell.py) | Exchange-unitary reduction versus the amplitude-damping Kraus channel on all four matrix units; an exact midpoint phase echo; a Bell-input instrument tree with three contacts and eight retained histories | Checks endpoint equality, the attained quadratic cell discrepancy and one adaptive ancilla-assisted example |
| [General dissipative cell](verify_dissipator_cell.py) | Exponentiated Lindblad superoperator versus the positive-no-jump-Kraus direct rotation on all nine qutrit matrix units; parity and sign reversal; two joint qutrit-reference instruments with four histories and an outcome-dependent second time | Checks the exact-cell completion for three nonnormal, noncommuting jumps and a non-diagonal loss operator |
| [Sensing bridge](verify_sensing_bridge.py) | Direct joint unitary versus analytic Kraus operators; independently exponentiated Markov channel; 128-history adaptive parity trees; reuse of one correlated bath; finite-difference readout response versus a classical reward recursion | Checks the explicit two-rate device, complete-record bounds, parity witness, and microscopic local coefficient at sampled parameters |

The general example is analytically optimally centered, as shown in
[the dissipator account](../science/dissipators.md#9-numerical-check-of-the-exact-general-cell).
Its jump operators are normalized to intrinsic rate one. The independent
channel representations help detect errors in vectorization, complex
conjugation, subsystem order and Kraus completion.

The qutrit routine obtains a finite Kraus representation from the Choi matrix
of the completely positive no-jump remainder. It retains eigenvalues above
`1e-14`, reports discarded positive weight and the minimum eigenvalue, and
checks the resulting endpoint error against `2e-12`. This numerical
truncation belongs to the check; the analytical construction is exact and
does not discard eigenvalues.

## Recorded results and numerical comparisons

The [qubit reference result](expected/amplitude_cell.json) has maximum
endpoint residual below 2.5e-16. The
[qutrit reference result](expected/dissipator_cell.json) has maximum endpoint
matrix-unit residual below 3.6e-15. All sampled controlled-cell distances lie
below the analytical bounds. The exact echo and parity identities are
checked numerically at the stated script tolerances.

Reference comparisons use relative tolerance `1e-8` and absolute tolerance
`5e-11`, accommodating floating-point variation across linear-algebra
backends. Roundoff-sensitive Kraus rank and bath dimension are reported but
are not required to agree exactly with their reference values; discarded
weight, endpoint equality and the physical output quantities remain checked.
The scripts enforce the tighter local identity and error-bound assertions
independently of the reference comparison. Both deterministic random seeds
and every sampled parameter appear in the outputs.

The [sensing reference result](expected/sensing_bridge.json) records endpoint
and Kraus residuals below `3e-16`, complete classical–quantum output distances
below the analytical cell-hybrid bounds, and local readout derivatives within
`2e-11` of the independent reward recursion. The retained-bath check uses one
mixed bath throughout all projections, with noncommuting time-dependent
couplings and bath motion; a second example saturates the survival bound.
These are finite checks of the [shared derivation](../science/sensing_bridge.md)
and the companion [microscopic sensing proof](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_sensing.md).
They do not certify derivative transfer from total variation, global sensing
advantage, or optimization against every microscopic controller.

The companion [microscopic control suite](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_microscopic.py)
adds eleven checks of the sharp boundary-control coefficients and the
same-contact midpoint echo in the sensing bridge. It propagates the actual
sensor–ancilla–bath unitaries around each interior pulse and finite-differences
the complete flagged readout probabilities. A Markov endpoint surrogate is
explicitly checked to give a different interior-pulse experiment. Run
`python scripts/check.py` in the Noise-Rate-Activated-Sensing checkout to
include these checks; they are not part of this repository's three-script
runner. The universal control bounds remain analytical statements.

The companion [contact-precision suite](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_contact_precision.py)
adds eight checks of the [hard-activity derivative lemma](../science/intervention_bounds.md#a-derivative-bound-with-a-hard-activity-budget)
and its sensing application. A purified adaptive controller retains rare,
signal-dependent activity histories and tests the derivative-source
decomposition, inactive orthogonality and active-history budget bound.
Its measured output excludes bath access. Separate early-readout experiments
verify the attaining probabilities and the original total-contact count.
The arbitrary-boundary-control relaxation is used only for upper-bound
checks. These checks run in the companion repository's 144-test suite;
this repository's three-script runner is unchanged.

The companion [identifiability suite](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_identifiability.py)
adds seven checks of the [clock-alias obstruction](../science/sensing_bridge.md#frequency-aliases-of-the-collision-clock)
and the fixed-band calibration experiment. Exact joint unitaries are checked
on entangled inputs and through complete adaptive boundary records at
resonances. The calibration checks retain odd outcomes, enumerate estimator
risk and tail probabilities, and charge early readout. These also run in the
companion suite; the universal alias statement remains an analytical proof.

The companion [global microscopic suite](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_global_microscopic.py)
adds eleven checks supporting the [global contact theorem](../science/global_contact_precision.md)
and the shared recorded-phase method. Complete physical parity trees include
the echo frame and conditional correction, while independent recursions
check record probabilities and derivative rewards. Conditional readout
inversion, wrong-stage interval containment and deterministic trial schedules
exercise the estimator mechanism. Every branch pays its interior pulses and
early readout; no failed block becomes a free retry.

The companion [timing suite](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_timing_precision.py)
adds eight direct-unitary checks for [systematic displacement and hidden jitter](../science/timing_precision.md).
It distinguishes a pure displaced parity branch from an unobserved mixture,
checks the exact known-offset record phase and common nuisance-curve gauge,
and finite-differences complete local readout probabilities. The tested
small-jitter gauge envelope supports the converse calculation, not a
sufficiency claim. Both suites run with `python scripts/check.py` in the
companion repository; this repository's three-script runner is unchanged.

## What the calculations do not establish

These are finite numerical examples. They do not optimize over testers or
compute a process diamond distance. They do not prove the uniform adaptive
upper bound, universal survival lower bound, minimax rate identity, or
bibliographic priority. Those statements have their arguments and attribution
in [the common bounds](../science/intervention_bounds.md),
[amplitude damping](../science/amplitude_damping.md),
[general dissipators](../science/dissipators.md), and
[Related work](../references/RELATED_WORK.md).
