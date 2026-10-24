"""Small scientific checks for the controlled collision-cell estimate.

Needs numpy and scipy. Tests endpoint equality, an exact echo counterexample,
and one seeded ancilla-assisted instrument tree with outcome-adaptive times.
Finite examples are not proofs of the minimax theorem.
"""

import json
import numpy as np
from scipy.linalg import expm

I = np.eye(2, dtype=complex)
z = np.diag([1, -1]).astype(complex)
lower = np.array([[0, 1], [0, 0]], dtype=complex)
upper = lower.conj().T
e0 = np.array([[1, 0], [0, 0]], dtype=complex)
g_se = np.kron(upper, lower) + np.kron(lower, upper)
g_sre = np.kron(np.kron(upper, I), lower) + np.kron(np.kron(lower, I), upper)


def conjugate(u, rho):
    return u @ rho @ u.conj().T


def trace_env(rho, d_sr):
    return np.trace(rho.reshape(d_sr, 2, d_sr, 2), axis1=1, axis2=3)


def amplitude_damping(rho, duration, with_reference=False):
    eta = np.exp(-duration)
    k0 = np.diag([1, np.sqrt(eta)]).astype(complex)
    k1 = np.sqrt(1 - eta) * lower
    if with_reference:
        k0, k1 = np.kron(k0, I), np.kron(k1, I)
    return conjugate(k0, rho) + conjugate(k1, rho)


def trace_distance(a, b):
    x = a - b
    x = (x + x.conj().T) / 2
    return np.linalg.eigvalsh(x).__abs__().sum() / 2


def haar(rng, d):
    q, r = np.linalg.qr(rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)))
    diagonal = np.diag(r)
    return q @ np.diag(diagonal / np.abs(diagonal))


rng = np.random.default_rng(726104)
tree = {}


def make_tree(history=(), previous=0.0):
    if len(history) == 3:
        return
    fraction = 0.2 if not history else (0.22 if history[-1] == 0 else 0.57)
    time = previous + fraction * (1.0 - previous)
    u = haar(rng, 4)
    ks = []
    for outcome in (0, 1):
        projector = np.kron(I, np.diag([int(outcome == 0), int(outcome == 1)]))
        ks.append(haar(rng, 4) @ projector @ u)
    assert np.linalg.norm(sum(k.conj().T @ k for k in ks) - np.eye(4)) < 1e-12
    tree[history] = (time, ks)
    for outcome in (0, 1):
        make_tree(history + (outcome,), time)


make_tree()
bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
bell_state = np.outer(bell, bell.conj())


def adaptive_instrument_distance(theta, duration):
    outputs = []

    def recurse(history, previous, physical, ideal):
        time = 1.0 if len(history) == 3 else tree[history][0]
        fraction = time - previous
        physical = conjugate(expm(-1j * theta * fraction * g_sre), physical)
        ideal = amplitude_damping(ideal, duration * fraction, with_reference=True)
        if len(history) == 3:
            outputs.append((trace_env(physical, 4), ideal))
            return
        for outcome, k in enumerate(tree[history][1]):
            recurse(history + (outcome,), time,
                    conjugate(np.kron(k, I), physical), conjugate(k, ideal))

    recurse((), 0.0, np.kron(bell_state, e0), bell_state.copy())
    physical_trace = sum(np.trace(p).real for p, _ in outputs)
    ideal_trace = sum(np.trace(q).real for _, q in outputs)
    assert abs(physical_trace - 1) < 1e-12
    assert abs(ideal_trace - 1) < 1e-12
    return sum(trace_distance(p, q) for p, q in outputs)


rows = []
for theta in (0.005, 0.01, 0.02, 0.05, 0.1, 0.2):
    duration = -2 * np.log(np.cos(theta))  # gamma=1; exact endpoint matching.
    u = expm(-1j * theta * g_se)
    choi_residual = 0.0
    for i in range(2):
        for j in range(2):
            matrix_unit = np.zeros((2, 2), dtype=complex)
            matrix_unit[i, j] = 1
            physical = trace_env(conjugate(u, np.kron(matrix_unit, e0)), 2)
            ideal = amplitude_damping(matrix_unit, duration)
            choi_residual = max(choi_residual, np.linalg.norm(physical - ideal))
    assert choi_residual < 1e-12

    half_u = expm(-0.5j * theta * g_se)
    echo_u = half_u @ np.kron(z, I) @ half_u
    echo_unitary_residual = np.linalg.norm(echo_u - np.kron(z, I))
    assert echo_unitary_residual < 1e-12
    excited = np.diag([0, 1]).astype(complex)
    physical_echo = trace_env(conjugate(echo_u, np.kron(excited, e0)), 2)
    ideal_echo = amplitude_damping(conjugate(z, amplitude_damping(excited, duration/2)), duration/2)
    echo_distance = trace_distance(physical_echo, ideal_echo)
    assert abs(echo_distance - np.sin(theta)**2) < 1e-12

    adaptive_distance = adaptive_instrument_distance(theta, duration)
    uniform_bound = np.sinh(theta)**2 + duration
    assert adaptive_distance <= uniform_bound + 1e-12
    rows.append({
        "theta": theta,
        "endpoint_basis_residual": float(choi_residual),
        "echo_distance": float(echo_distance),
        "echo_over_theta_squared": float(echo_distance/theta**2),
        "adaptive_record_distance": float(adaptive_distance),
        "adaptive_over_theta_squared": float(adaptive_distance/theta**2),
        "uniform_cell_bound": float(uniform_bound),
    })

print(json.dumps({"seed": 726104, "internal_interventions": 3, "outcome_branches": 8,
                  "checks": rows}, indent=2))
