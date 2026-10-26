#!/usr/bin/env python3
"""Run the finite scientific checks and compare stable recorded quantities."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
CHECKS = (
    ("verify_amplitude_cell.py", "amplitude_cell.json"),
    ("verify_dissipator_cell.py", "dissipator_cell.json"),
    ("verify_sensing_bridge.py", "sensing_bridge.json"),
)
# Near-zero Choi eigenvalues can cross a numerical Kraus truncation threshold.
# These diagnostics are still reported and bounded by the calculation itself.
ROUNDING_DEPENDENT = {
    "remainder_kraus_rank_at_1e_minus_14",
    "bath_dimension",
}


def compare(actual, expected, path="result"):
    if isinstance(expected, dict):
        if set(actual) != set(expected):
            raise AssertionError(f"{path}: output fields differ")
        for key in expected:
            if key not in ROUNDING_DEPENDENT:
                compare(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        if len(actual) != len(expected):
            raise AssertionError(f"{path}: list lengths differ")
        for index, (left, right) in enumerate(zip(actual, expected)):
            compare(left, right, f"{path}[{index}]")
    elif isinstance(expected, (float, int)) and not isinstance(expected, bool):
        if not math.isfinite(actual) or not math.isclose(
            actual, expected, rel_tol=1e-8, abs_tol=5e-11
        ):
            raise AssertionError(f"{path}: {actual!r} differs from {expected!r}")
    elif actual != expected:
        raise AssertionError(f"{path}: {actual!r} differs from {expected!r}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--record", action="store_true",
        help="explicitly replace reference outputs after scientific review",
    )
    args = parser.parse_args()
    if not __debug__:
        raise SystemExit("Run without -O: scientific assertions must be enabled.")
    for script, reference in CHECKS:
        result = subprocess.run(
            [sys.executable, str(ROOT / script)], check=True,
            text=True, capture_output=True,
        )
        actual = json.loads(result.stdout)
        destination = ROOT / "expected" / reference
        if args.record:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(json.dumps(actual, indent=2) + "\n")
        else:
            compare(actual, json.loads(destination.read_text()), script)
        print(f"PASS {script}: scientific assertions and reference quantities")
    if args.record:
        print("Reference outputs recorded; recording is not an independent validation.")
    else:
        print("All finite checks passed. Uniform theorems are established by the proofs.")


if __name__ == "__main__":
    main()
