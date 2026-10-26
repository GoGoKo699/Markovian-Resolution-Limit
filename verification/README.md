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
the reference files. Each script can also be run directly to print its full
JSON result.

For a scientifically reviewed change, regenerate the reference outputs
explicitly and then run the ordinary verification:

```bash
python3 verification/run_all.py --record
python3 verification/run_all.py
```

Recording an output does not independently validate it. Changes to a
calculation require checking its equations and physical meaning.

## Explanatory report build

The [44-page report PDF](../learning/report/Markovian_Resolution_Limit_Report.pdf) has a matching [self-contained LaTeX source](../learning/source/Markovian_Resolution_Limit_Report.tex). All text, macros and the analytic TikZ figure are inline; no external figures, bibliography or additional TeX inputs are needed. Its scientific account corresponds to revision `4d01c0b8fb8a0f8a76baaea36ee897ec3a25cd61` and the shared sensing results at companion revision `a46faa43faff046217d587a5248c27419294433e`.

Use **pdfLaTeX from TeX Live 2025**, with the packages named in the source preamble. A full TeX Live 2025 installation includes them. The checked engine is pdfTeX 3.141592653-2.6-1.40.28. With that installation on `PATH`, run from the repository root:

```bash
python3 verification/build_report.py --output /tmp/mrl-report-build
```

The output directory must not already exist. Alternatively, select the engine explicitly with `--pdflatex /path/to/texlive/2025/bin/x86_64-linux/pdflatex`. The [build script](build_report.py) checks the engine year, copies the source into the new directory, compiles three times, and requires a fresh PDF and final log with resolved references and no layout or missing-character warnings. It retains the compiler transcripts and writes `build.json` with the engine version and source, PDF and log SHA-256 hashes. It never overwrites the stored report.

The fresh PDF and corresponding final log establish that the relocated source compiles; the stored PDF alone cannot establish that. PDF bytes may differ between builds because of timestamps and identifiers. Compare page content and inspect rendered pages before replacing the stored PDF. Compilation, visual inspection and scientific validation are separate checks. The scientific runner above does not install TeX or compile the report.

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

The companion repository supplies the following additional checks. Run
`python scripts/check.py` in the Noise-Rate-Activated-Sensing checkout to
include them in its 144-test suite; they are not part of this repository's
three-script runner.

| Companion suite | Checks | What is exercised |
|---|---|---|
| [Microscopic control](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_microscopic.py) | 11 | Sharp boundary-control coefficients and the same-contact midpoint echo, from sensor–ancilla–bath unitaries and complete flagged readout derivatives. A Markov endpoint surrogate gives a different interior-pulse experiment. |
| [Contact precision](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_contact_precision.py) | 8 | The [hard-activity derivative lemma](../science/intervention_bounds.md#a-derivative-bound-with-a-hard-activity-budget): rare signal-dependent histories, derivative-source decomposition, inactive orthogonality and the hard active-history budget. Measured outputs exclude the bath; early-readout checks retain the original total-contact count. Arbitrary boundary control is a converse relaxation only. |
| [Identifiability](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_identifiability.py) | 7 | [Clock aliases](../science/sensing_bridge.md#frequency-aliases-of-the-collision-clock) on entangled inputs and complete adaptive boundary records, plus fixed-band calibration risk and tails with odd outcomes and early readout charged. |
| [Global microscopic precision](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_global_microscopic.py) | 11 | The [global contact theorem](../science/global_contact_precision.md) and shared recorded-phase method: physical parity trees with echo frame and conditional correction, independent probability and reward recursions, conditional inversion, wrong-stage interval containment and deterministic budgets. Every branch pays its pulses and early readout. |
| [Timing](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/tests/test_timing_precision.py) | 8 | [Systematic displacement and hidden jitter](../science/timing_precision.md): pure versus mixed parity branches, the exact known-offset record phase, common nuisance-curve gauge and complete local readout derivatives. The small-jitter gauge envelope supports the converse, not sufficiency of the timing scale. |

The global contact and jitter lower bounds use the companion's [bounded-loss closure](https://github.com/GoGoKo699/Noise-Rate-Activated-Sensing/blob/main/science/microscopic_global_precision.md#global-risk-under-controlled-limits). This is an analytical argument for operational limits, not an inference from sampled channel continuity or local Fisher information. Known systematic displacement is a supplied input; these checks do not establish a calibration cost for an unknown offset.

## What the calculations do not establish

These are finite numerical examples. They do not optimize over testers or
compute a process diamond distance. They do not prove the uniform adaptive
upper bound, universal survival lower bound, minimax rate identity, or
bibliographic priority. Those statements have their arguments and attribution
in [the common bounds](../science/intervention_bounds.md),
[amplitude damping](../science/amplitude_damping.md),
[general dissipators](../science/dissipators.md), and
[Related work](../references/RELATED_WORK.md).
