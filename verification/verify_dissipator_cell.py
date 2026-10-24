#!/usr/bin/env python3
"""Check exact centered-dissipator cells in one nonnormal qutrit example.

This is a bounded numerical check of the exact-cell construction and
the absence of a first-order-in-action error under adaptive, recorded joint
system-reference instruments. It is not an optimization over testers.

Run: python3 verification/verify_dissipator_cell.py
Dependencies: NumPy and SciPy. Output: JSON on standard output.
"""

from __future__ import annotations

import json

import numpy as np
from scipy.linalg import eigh, expm


def adjoint(a):
    return a.conj().T


def spectral_norm(a):
    return float(np.linalg.norm(a, 2))


def trace_norm_hermitian(a):
    return float(np.abs(eigh((a + adjoint(a)) / 2, eigvals_only=True)).sum())


def lindblad_superoperator(jumps):
    d = jumps[0].shape[0]
    eye = np.eye(d)
    q = sum(adjoint(j) @ j for j in jumps)
    generator = sum(np.kron(j.conj(), j) for j in jumps)
    generator -= (np.kron(eye, q) + np.kron(q.T, eye)) / 2
    return generator, q


def channel_choi(superoperator, d):
    result = np.zeros((d * d, d * d), complex)
    for i in range(d):
        for j in range(d):
            output = superoperator[:, i + d * j].reshape((d, d), order="F")
            result[i * d : (i + 1) * d, j * d : (j + 1) * d] = output
    return (result + adjoint(result)) / 2


def exact_cell(generator, q, h):
    """Build the no-jump Kraus column and its parity-odd direct rotation."""
    d = q.shape[0]
    qvalues, qvectors = eigh(q)
    avalues = np.exp(-h * qvalues / 2)
    svalues = np.sqrt(-np.expm1(-h * qvalues))
    theta_values = np.arccos(avalues)
    a0 = (qvectors * avalues) @ adjoint(qvectors)
    theta = (qvectors * theta_values) @ adjoint(qvectors)
    sin_inverse = (qvectors * np.where(svalues > 1e-14, 1 / svalues, 0)) @ adjoint(qvectors)

    ideal = expm(h * generator)
    a0vector = a0.ravel(order="F")
    remainder_choi = channel_choi(ideal, d) - np.outer(a0vector, a0vector.conj())
    remainder_choi = (remainder_choi + adjoint(remainder_choi)) / 2
    eigenvalues, eigenvectors = eigh(remainder_choi)
    positive = eigenvalues > 1e-14
    kraus = [
        np.sqrt(value) * vector.reshape((d, d), order="F")
        for value, vector in zip(eigenvalues[positive], eigenvectors[:, positive].T)
    ]
    b = np.vstack(kraus)
    jpartial = b @ sin_inverse
    c = jpartial @ theta
    d_excited = b.shape[0]
    kh = np.block(
        [[np.zeros((d, d), complex), -1j * adjoint(c)],
         [1j * c, np.zeros((d_excited, d_excited), complex)]]
    )
    hamiltonian = kh / h
    unitary = expm(-1j * kh)
    vacuum_column = unitary[:, :d]
    cell_kraus = [vacuum_column[k : k + d, :] for k in range(0, unitary.shape[0], d)]
    physical = sum(np.kron(k.conj(), k) for k in cell_kraus)
    z = np.diag(np.r_[np.ones(d), -np.ones(d_excited)])
    diagnostics = {
        "remainder_min_choi_eigenvalue": float(eigenvalues.min()),
        "remainder_kraus_rank_at_1e_minus_14": int(positive.sum()),
        "discarded_positive_choi_weight": float(eigenvalues[(eigenvalues > 0) & ~positive].sum()),
        "bath_dimension": len(kraus) + 1,
        "action_norm": spectral_norm(kh),
        "predicted_action_norm": float(theta_values.max()),
        "parity_anticommutator_norm": spectral_norm(z @ kh + kh @ z),
        "kraus_column_residual": spectral_norm(vacuum_column - np.vstack([a0, b])),
        "endpoint_max_matrix_unit_residual": float(np.max(np.abs(physical - ideal))),
        "kraus_completeness_residual": spectral_norm(sum(adjoint(k) @ k for k in [a0] + kraus) - np.eye(d)),
    }
    return hamiltonian, len(kraus) + 1, diagnostics


def seeded_unitary(rng, size):
    raw = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    q, r = np.linalg.qr(raw)
    phases = np.diag(r)
    return q @ np.diag(phases.conj() / np.abs(phases))


def weak_instrument(unitary, weights):
    return [np.diag(np.sqrt(weights)) @ unitary,
            np.diag(np.sqrt(1 - weights)) @ unitary]


def apply_system_channel(rho_sr, channel, d, reference_dimension):
    input_tensor = rho_sr.reshape(d, reference_dimension, d, reference_dimension)
    output_tensor = np.empty(input_tensor.shape, dtype=complex)
    for a in range(reference_dimension):
        for b in range(reference_dimension):
            block = input_tensor[:, a, :, b]
            output_tensor[:, a, :, b] = (channel @ block.ravel(order="F")).reshape((d, d), order="F")
    return output_tensor.reshape(d * reference_dimension, d * reference_dimension)


def run_tester(kind, h, generator, hamiltonian, bath_dimension, instruments, sign=1):
    """Two contacts, four retained histories; second time depends on outcome."""
    d = 3
    ref = 3
    sr = d * ref
    initial_vector = np.eye(d).reshape(-1) / np.sqrt(d)
    initial = np.outer(initial_vector, initial_vector.conj()).astype(complex)
    if kind == "microscopic":
        vacuum = np.zeros((bath_dimension, bath_dimension), complex)
        vacuum[0, 0] = 1
        initial = np.kron(vacuum, initial)

    def evolve(state, duration):
        if kind == "idle":
            return state
        if kind == "markov":
            return apply_system_channel(state, expm(duration * generator), d, ref)
        unitary = np.kron(expm(-1j * sign * duration * hamiltonian), np.eye(ref))
        return unitary @ state @ adjoint(unitary)

    def contact(state, kraus):
        if kind == "microscopic":
            kraus = np.kron(np.eye(bath_dimension), kraus)
        return kraus @ state @ adjoint(kraus)

    def finish(state):
        if kind != "microscopic":
            return state
        return sum(state[k * sr : (k + 1) * sr, k * sr : (k + 1) * sr]
                   for k in range(bath_dimension))

    first_time = 0.31 * h
    first_input = evolve(initial, first_time)
    outputs = []
    for first_outcome in range(2):
        first_output = contact(first_input, instruments[0][first_outcome])
        second_time = (0.63 if first_outcome == 0 else 0.82) * h
        second_input = evolve(first_output, second_time - first_time)
        for second_outcome in range(2):
            second_output = contact(second_input, instruments[1][second_outcome])
            outputs.append(finish(evolve(second_output, h - second_time)))
    return outputs


def record_distance(first, second):
    return sum(trace_norm_hermitian(a - b) for a, b in zip(first, second)) / 2


def main():
    d = 3
    first = np.zeros((d, d), complex)
    first[0, 1], first[0, 2] = 1, 0.3j
    second = np.zeros((d, d), complex)
    second[0, 1], second[0, 2] = 0.4, 0.8
    third = np.zeros((d, d), complex)
    third[1, 0] = 0.5
    jumps = [first, second, third]
    _, q_raw = lindblad_superoperator(jumps)
    raw_nu = float(eigh(q_raw, eigvals_only=True).max())
    jumps = [jump / np.sqrt(raw_nu) for jump in jumps]
    generator, q = lindblad_superoperator(jumps)
    qvalues, qvectors = eigh(q)
    maximizer = qvectors[:, -1]
    means = [np.vdot(maximizer, jump @ maximizer) for jump in jumps]
    nu = float(qvalues[-1])
    assert max(abs(z) for z in means) < 1e-13
    assert abs(nu - 1) < 1e-13

    rng = np.random.default_rng(20261024)
    instruments = [
        weak_instrument(seeded_unitary(rng, 9), np.linspace(0.16, 0.84, 9)),
        weak_instrument(seeded_unitary(rng, 9), np.linspace(0.79, 0.21, 9)),
    ]
    rows = []
    for h in [0.000625, 0.0025, 0.01, 0.04, 0.16, 0.64]:
        hamiltonian, bath_dimension, diagnostics = exact_cell(generator, q, h)
        physical = run_tester("microscopic", h, generator, hamiltonian, bath_dimension, instruments)
        sign_flipped = run_tester("microscopic", h, generator, hamiltonian, bath_dimension, instruments, sign=-1)
        ideal = run_tester("markov", h, generator, hamiltonian, bath_dimension, instruments)
        idle = run_tester("idle", h, generator, hamiltonian, bath_dimension, instruments)
        action = diagnostics["action_norm"]
        micro_idle = record_distance(physical, idle)
        micro_markov = record_distance(physical, ideal)
        micro_bound = float(np.sinh(action) ** 2)
        full_bound = micro_bound + nu * h
        row = {
            "h": h,
            "x_nu_h": nu * h,
            **diagnostics,
            "record_trace_total_physical": float(sum(np.trace(state).real for state in physical)),
            "micro_idle_half_trace_distance": micro_idle,
            "micro_idle_distance_over_x": micro_idle / (nu * h),
            "micro_idle_upper_bound": micro_bound,
            "micro_markov_half_trace_distance": micro_markov,
            "micro_markov_distance_over_x": micro_markov / (nu * h),
            "micro_markov_upper_bound": full_bound,
            "coupling_sign_flip_distance": record_distance(physical, sign_flipped),
        }
        assert row["remainder_min_choi_eigenvalue"] > -1e-12
        assert row["endpoint_max_matrix_unit_residual"] < 2e-12
        assert row["coupling_sign_flip_distance"] < 2e-12
        assert micro_idle <= micro_bound + 2e-12
        assert micro_markov <= full_bound + 2e-12
        assert action * action <= nu * h + 2e-12
        rows.append(row)

    output = {
        "purpose": "One nonnormal, noncommuting three-jump qutrit checks exact no-jump-cell completion and even-action error under two adaptive recorded joint qutrit-reference instruments.",
        "scope": "Finite numerical evidence, not a diamond-norm computation or optimization over testers.",
        "seed": 20261024,
        "reference_dimension": 3,
        "contacts": 2,
        "retained_outcome_histories": 4,
        "raw_nu_before_normalization": raw_nu,
        "normalized_Q_eigenvalues": qvalues.tolist(),
        "maximizing_state_jump_means_abs": [float(abs(z)) for z in means],
        "jump_nonnormality_norms": [spectral_norm(j @ adjoint(j) - adjoint(j) @ j) for j in jumps],
        "jump_commutator_1_3_norm": spectral_norm(jumps[0] @ jumps[2] - jumps[2] @ jumps[0]),
        "rows": rows,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
