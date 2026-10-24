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

The runner executes both scripts with assertions enabled, checks their
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

## What the calculations do not establish

These are finite numerical examples. They do not optimize over testers or
compute a process diamond distance. They do not prove the uniform adaptive
upper bound, universal survival lower bound, minimax rate identity, or
bibliographic priority. Those statements have their arguments and attribution
in [the common bounds](../science/intervention_bounds.md),
[amplitude damping](../science/amplitude_damping.md),
[general dissipators](../science/dissipators.md), and
[Related work](../references/RELATED_WORK.md).
