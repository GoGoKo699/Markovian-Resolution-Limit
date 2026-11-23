#!/usr/bin/env python3
"""Check the hidden-jitter instrument, signed paths and local mean inversion."""

from collections import defaultdict
from itertools import product
import json

import numpy as np
from scipy.linalg import expm


IDENTITY = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
EVEN, ODD = 0, 1
PARITY = (np.diag([1, 0, 0, 1]), np.diag([0, 1, 1, 0]))
BELL = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
BELL_DENSITY = np.outer(BELL, BELL.conj())
TOLERANCE = 2e-12


def transverse_axis(phi):
    return np.cos(phi) * X + np.sin(phi) * Y


def exact_bath_kraus(chi, frequency, phi, displacement=None):
    """Exponentiate the physical sensor-bath generators at h=1."""
    drift = (frequency / 2) * np.kron(Z, IDENTITY)
    coupling = chi * np.kron(transverse_axis(phi), X)
    if displacement is None:
        propagator = expm(-1j * (drift + coupling))
    else:
        first = expm(-1j * (0.5 + displacement) * (drift + coupling))
        second = expm(-1j * (0.5 - displacement) * (drift - coupling))
        propagator = second @ first
    return propagator[::2, ::2], propagator[1::2, ::2]


def closed_echo(chi, frequency, displacement):
    radius = np.hypot(chi, frequency / 2)
    cosine = np.cos(radius)
    difference = np.cos(2 * radius * displacement) - cosine
    u = cosine + (chi / radius) ** 2 * difference
    v = (frequency / (2 * radius)) * np.sin(radius)
    w = (chi / radius) * np.sin(2 * radius * displacement)
    a = frequency * chi * difference / (2 * radius**2)
    return u, v, w, a


def signed_transfer(chi, frequency, jitter):
    """Rows are incoming parity, columns are observed outgoing parity."""
    u, v, w, a = closed_echo(chi, frequency, jitter)
    radius = np.hypot(chi, frequency / 2)
    plain_flip = ((chi / radius) * np.sin(radius)) ** 2
    echo_flip = a**2 + w**2
    probability = np.array([[1 - echo_flip, echo_flip], [plain_flip, 1 - plain_flip]])
    signed = probability.copy()
    signed[EVEN, ODD] = a**2 - w**2
    phases = 2 * np.arctan2(v, u), 2 * np.arctan2(v, np.cos(radius))
    return probability, signed, phases


def direct_instrument(chi, frequency, phi, jitter):
    """Average the two exact propagator channels before conditioning on parity."""
    echo = [
        operator / np.sqrt(2)
        for sign in (-1, 1)
        for operator in exact_bath_kraus(chi, frequency, phi, sign * jitter)
    ]
    plain = exact_bath_kraus(chi, frequency, phi)
    instruments = {}
    for incoming, outgoing in product((EVEN, ODD), repeat=2):
        operators = echo if incoming == EVEN else plain
        correction = Z if (incoming, outgoing) == (EVEN, ODD) else IDENTITY
        instruments[incoming, outgoing] = [
            np.kron(correction @ operator, IDENTITY) @ PARITY[incoming]
            for operator in operators
        ]
    return instruments


def apply_instrument(instruments, incoming, outgoing, state):
    projected = PARITY[outgoing]
    return sum(
        (projected @ operation) @ state @ (projected @ operation).conj().T
        for operation in instruments[incoming, outgoing]
    )


def exact_paths(instruments, length):
    paths = {(): BELL_DENSITY}
    for _ in range(length):
        updated = {}
        for record, state in paths.items():
            incoming = record[-1] if record else EVEN
            for outgoing in (EVEN, ODD):
                updated[record + (outgoing,)] = apply_instrument(
                    instruments, incoming, outgoing, state
                )
        paths = updated
    return paths


def summarize_path(record, probability, signed):
    incoming = EVEN
    even_stays = odd_stays = 0
    mass = amplitude = 1.0
    for outgoing in record:
        mass *= probability[incoming, outgoing]
        amplitude *= signed[incoming, outgoing]
        even_stays += incoming == outgoing == EVEN
        odd_stays += incoming == outgoing == ODD
        incoming = outgoing
    return (incoming, even_stays, odd_stays), (mass, amplitude)


def enumerated_transfers(length, probability, signed):
    totals = defaultdict(lambda: np.zeros(2))
    for record in product((EVEN, ODD), repeat=length):
        state, weights = summarize_path(record, probability, signed)
        totals[state] += weights
    return totals


def dynamic_transfers(length, probability, signed):
    totals = {(EVEN, 0, 0): np.ones(2)}
    for _ in range(length):
        updated = defaultdict(lambda: np.zeros(2))
        for (incoming, even_stays, odd_stays), weights in totals.items():
            for outgoing in (EVEN, ODD):
                key = (
                    outgoing,
                    even_stays + (incoming == outgoing == EVEN),
                    odd_stays + (incoming == outgoing == ODD),
                )
                step = np.array([probability[incoming, outgoing], signed[incoming, outgoing]])
                updated[key] += weights * step
        totals = updated
    return totals


def accepted(state, length):
    parity, even_stays, _ = state
    return parity == EVEN and 4 * even_stays >= 3 * length


def phase_angle(state, phases):
    _, even_stays, odd_stays = state
    return even_stays * phases[0] - odd_stays * phases[1]


def signed_mean(length, chi, frequency, jitter, center):
    probability, signed, phases = signed_transfer(chi, frequency, jitter)
    _, _, center_phases = signed_transfer(chi, center, jitter)
    relative = np.subtract(phases, center_phases)
    totals = dynamic_transfers(length, probability, signed)
    mass = mean = 0.0
    for state, (probability_weight, signed_weight) in totals.items():
        if accepted(state, length):
            mass += probability_weight
            mean += signed_weight * np.sin(phase_angle(state, relative))
    return mean, mass


def exact_mean(length, chi, frequency, phi, jitter, center):
    probability, signed, center_phases = signed_transfer(chi, center, jitter)
    instruments = direct_instrument(chi, frequency, phi, jitter)
    mean = 0.0
    for record, state in exact_paths(instruments, length).items():
        summary, _ = summarize_path(record, probability, signed)
        if accepted(summary, length):
            rotated = np.exp(1j * phase_angle(summary, center_phases)) * state[0, 3]
            mean -= 2 * rotated.imag
    return mean


def check_propagators_and_paths():
    largest = dict(kraus=0.0, probability=0.0, coherence=0.0, mean=0.0)
    path_count = signed_echo_count = 0
    for chi, frequency, jitter, phi in product(
        (0.21, 0.53, 0.77),
        (-0.18, -0.04, 0.0, 0.04, 0.18),
        (0.0, 0.015, 0.09, 0.31, 0.499999, np.nextafter(0.5, 0.0)),
        (0.0, 0.41, 1.52),
    ):
        for displacement in sorted({-jitter, jitter}):
            u, v, w, a = closed_echo(chi, frequency, displacement)
            exact = exact_bath_kraus(chi, frequency, phi, displacement)
            closed = (
                u * IDENTITY - 1j * v * Z,
                -1j * (w * transverse_axis(phi) + a * transverse_axis(phi + np.pi / 2)),
            )
            for actual, predicted in zip(exact, closed):
                largest["kraus"] = max(largest["kraus"], float(np.max(np.abs(actual - predicted))))
            signed_echo_count += 1

        probability, signed, phases = signed_transfer(chi, frequency, jitter)
        instruments = direct_instrument(chi, frequency, phi, jitter)
        for length in range(1, 6):
            total = 0.0
            for record, rho in exact_paths(instruments, length).items():
                state, (mass, amplitude) = summarize_path(record, probability, signed)
                observed = float(np.trace(rho).real)
                total += observed
                largest["probability"] = max(largest["probability"], abs(observed - mass))
                if state[0] == EVEN:
                    predicted = amplitude * np.exp(-1j * phase_angle(state, phases))
                    largest["coherence"] = max(largest["coherence"], abs(2 * rho[0, 3] - predicted))
                path_count += 1
            assert abs(total - 1) < TOLERANCE

        if phi == 0.41:
            center = frequency + 0.006
            predicted, _ = signed_mean(5, chi, frequency, jitter, center)
            observed = exact_mean(5, chi, frequency, phi, jitter, center)
            largest["mean"] = max(largest["mean"], abs(observed - predicted))

    assert max(largest.values()) < TOLERANCE, largest
    return largest, path_count, signed_echo_count


def check_dynamic_program():
    largest = 0.0
    negative_flip_cases = 0
    cases = product((0.21, 0.63), (-0.15, 0.0, 0.15), (0.0, 0.031, 0.13, 0.499999))
    for chi, frequency, jitter in cases:
        probability, signed, _ = signed_transfer(chi, frequency, jitter)
        negative_flip_cases += signed[EVEN, ODD] < 0
        for length in (1, 4, 8, 9):
            reference = enumerated_transfers(length, probability, signed)
            dynamic = dynamic_transfers(length, probability, signed)
            assert set(dynamic) == set(reference)
            assert abs(sum(weights[0] for weights in dynamic.values()) - 1) < TOLERANCE
            for state in reference:
                largest = max(largest, float(np.max(np.abs(dynamic[state] - reference[state]))))
    assert negative_flip_cases > 0
    assert largest < TOLERANCE
    return largest


def check_local_slope():
    step = 1e-5
    smallest_normalized_slope = float("inf")
    smallest_acceptance = 1.0
    largest_direct_error = 0.0
    largest_step_difference = 0.0
    for length, center, jitter in product((5, 12, 30), (-0.015, 0.0, 0.017), (0.0, 0.02, 0.05)):
        chi, phi = 0.53, 0.41
        assert length * jitter**2 <= 0.08
        for offset in (-0.08, 0.0, 0.08):
            frequency = center + offset / length

            def mean_at(value):
                return signed_mean(length, chi, value, jitter, center)[0]

            slope = (mean_at(frequency + step) - mean_at(frequency - step)) / (2 * step)
            refined = (mean_at(frequency + step / 2) - mean_at(frequency - step / 2)) / step
            largest_step_difference = max(largest_step_difference, abs(slope - refined))
            smallest_normalized_slope = min(smallest_normalized_slope, refined / length)
            _, acceptance = signed_mean(length, chi, frequency, jitter, center)
            smallest_acceptance = min(smallest_acceptance, acceptance)
            if length == 5:
                direct_plus = exact_mean(length, chi, frequency + step / 2, phi, jitter, center)
                direct_minus = exact_mean(length, chi, frequency - step / 2, phi, jitter, center)
                direct_slope = (direct_plus - direct_minus) / step
                largest_direct_error = max(largest_direct_error, abs(refined - direct_slope))

    assert smallest_normalized_slope > 0.5, smallest_normalized_slope
    assert smallest_acceptance > 32 / 41, smallest_acceptance
    assert largest_step_difference < 1e-6, largest_step_difference
    assert largest_direct_error < 1e-8, largest_direct_error
    return dict(
        minimum_slope_per_cell=smallest_normalized_slope,
        minimum_gate_acceptance=smallest_acceptance,
        maximum_slope_step_difference=largest_step_difference,
        maximum_slope_difference_vs_propagators=largest_direct_error,
    )


def main():
    if not __debug__:
        raise SystemExit("Run without -O so that verification assertions are enabled.")
    errors, path_count, echo_count = check_propagators_and_paths()
    result = {
        "signed_displacement_checks": echo_count,
        "resolved_paths_through_five_cells": path_count,
        "maximum_propagator_comparison_error": errors,
        "maximum_dynamic_program_vs_enumeration_error": check_dynamic_program(),
        "local_mean": check_local_slope(),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
