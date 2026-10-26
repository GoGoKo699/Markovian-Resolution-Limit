"""Finite checks for the sensing/resolution interface.

Checks independent channel constructions, retained outcome records, the
survival bound with bath memory, and local response against a classical
reward calculation. These samples are not a uniform theorem or a converse
against every sensing protocol on the same microscopic hardware.
"""
from __future__ import annotations
import json
import numpy as np
from scipy.linalg import expm

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
E0 = np.diag([1, 0]).astype(complex)
EVEN = (np.eye(4) + np.kron(Z, Z)) / 2
PARITY = (EVEN, np.eye(4) - EVEN)
YL = np.zeros((4, 4), dtype=complex)
YL[0, 3], YL[3, 0] = -1j, 1j
bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
INITIAL = np.outer(bell, bell.conj())

def axis(phi):
    return np.cos(phi) * X + np.sin(phi) * Y

def parameters(gamma, h):
    p = -np.expm1(-2 * gamma * h) / 2
    chi = np.arcsin(np.sqrt(p))
    return float(p), float(chi), float(chi / h)

def conjugate(u, rho):
    return u @ rho @ u.conj().T

def trace_env(rho, dimension):
    return np.trace(rho.reshape(dimension, 2, dimension, 2), axis1=1, axis2=3)

def kraus(gamma, h, omega, phi):
    _, _, g = parameters(gamma, h)
    radius = np.sqrt(g * g + omega * omega / 4)
    sinc = np.sin(radius * h) / radius
    return (np.cos(radius * h) * I - 0.5j * omega * sinc * Z,
            -1j * g * sinc * axis(phi))

def markov_matrix(gamma, h, omega, phi):
    n, signal = axis(phi), omega * Z / 2
    generator = (-1j * (np.kron(I, signal) - np.kron(signal.T, I))
                 + gamma * (np.kron(n.conj(), n) - np.eye(4)))
    return expm(h * generator)

def apply_markov(matrix, rho):
    """Apply the independently exponentiated sensor map to sensor--ancilla."""
    blocks = rho.reshape(2, 2, 2, 2)
    result = np.zeros_like(blocks)
    for a in range(2):
        for b in range(2):
            result[:, a, :, b] = (matrix @ blocks[:, a, :, b].reshape(4, order="F")).reshape(2, 2, order="F")
    return result.reshape(4, 4)

def distance(left, right):
    difference = left - right
    difference = (difference + difference.conj().T) / 2
    return float(np.abs(np.linalg.eigvalsh(difference)).sum() / 2)

def tree(rates, h, omega, phi, steps, microscopic):
    """Every outcome history survives; rate uses the last measured sector."""
    maps = {s: (tuple(np.kron(k, I) for k in kraus(g, h, omega, phi))
                if microscopic else markov_matrix(g, h, omega, phi))
            for s, g in enumerate(rates)}
    states = {(): INITIAL.copy()}
    for _ in range(steps):
        following = {}
        for history, rho in states.items():
            last = history[-1] if history else 0
            evolved = (sum(conjugate(k, rho) for k in maps[last]) if microscopic
                       else apply_markov(maps[last], rho))
            for sector, projector in enumerate(PARITY):
                following[history + (sector,)] = conjugate(projector, evolved)
        states = following
    assert abs(sum(float(np.trace(rho).real) for rho in states.values()) - 1) < 2e-12
    return states

def success_output(states):
    return sum((rho for history, rho in states.items() if history[-1] == 0),
               np.zeros((4, 4), dtype=complex))

def reward_chain(rates, h, steps):
    """Independent classical computation of probability and weighted reward."""
    probability, reward = np.array([1., 0.]), np.zeros(2)
    data = [parameters(gamma, h) for gamma in rates]
    for _ in range(steps):
        next_probability, next_reward = np.zeros(2), np.zeros(2)
        for sector, (p, chi, g) in enumerate(data):
            q, sign, d = 1 - p, 1 - 2 * sector, np.tan(chi) / g
            next_probability[sector] += q * probability[sector]
            next_reward[sector] += q * (reward[sector] + probability[sector] * sign * d)
            next_probability[1 - sector] += p * probability[sector]
            next_reward[1 - sector] += p * reward[sector]
        probability, reward = next_probability, next_reward
    return probability, reward

def local_speed(rates, h):
    pa, ca, ga = parameters(rates[0], h)
    pb, cb, gb = parameters(rates[1], h)
    return float((pb * (1 - pa) * np.tan(ca) / ga - pa * (1 - pb) * np.tan(cb) / gb)
                 / (h * (pa + pb)))

def cell_checks():
    unitary_error = endpoint_error = normalization_error = 0.
    rows = []
    for gamma, h, omega, phi in ((0.4, 0.03, -0.7, 0.13), (1.3, 0.2, 1.1, 1.27),
                               (2., 0.7, 0., 2.3), (0.7, 1e-5, 0.4, -0.6)):
        _, chi, g = parameters(gamma, h)
        assert chi * chi <= gamma * h + 1e-14
        u = expm(-1j * h * (np.kron(omega * Z / 2, I) + g * np.kron(axis(phi), X)))
        ks = kraus(gamma, h, omega, phi)
        normalization_error = max(normalization_error, float(np.linalg.norm(sum(k.conj().T @ k for k in ks) - I)))
        for i in range(2):
            for j in range(2):
                basis = np.zeros((2, 2), dtype=complex)
                basis[i, j] = 1
                direct = trace_env(conjugate(u, np.kron(basis, E0)), 2)
                reduced = sum(conjugate(k, basis) for k in ks)
                unitary_error = max(unitary_error, float(np.linalg.norm(direct - reduced)))
                zero = sum(conjugate(k, basis) for k in kraus(gamma, h, 0., phi))
                expected = (markov_matrix(gamma, h, 0., phi) @ basis.reshape(4, order="F")).reshape(2, 2, order="F")
                endpoint_error = max(endpoint_error, float(np.linalg.norm(zero - expected)))
        rows.append({"gamma": gamma, "h": h, "omega": omega, "phi": phi, "coupling": g,
                     "complete_hamiltonian_norm": float(np.sqrt(g * g + omega * omega / 4))})
    assert max(unitary_error, endpoint_error, normalization_error) < 2e-12
    return {"parameters": rows, "unitary_kraus_residual": unitary_error,
            "zero_signal_markov_residual": endpoint_error,
            "kraus_normalization_residual": normalization_error}

def record_checks():
    rows = []
    rates, steps = (0.4, 1.3), 7
    for h, omega, phi in ((0.02, 0.9, 0.2), (0.08, -1.1, 1.2), (0.2, 0.0, -0.8)):
        physical = tree(rates, h, omega, phi, steps, True)
        target = tree(rates, h, omega, phi, steps, False)
        cq_distance = sum(distance(physical[key], target[key]) for key in target)
        pa, _, _ = parameters(rates[0], h)
        all_even = float(np.trace(target[(0,) * steps]).real)
        expected = (1 - pa) ** steps
        assert abs(all_even - expected) < 2e-12
        bounds = []
        for gamma in rates:
            _, chi, _ = parameters(gamma, h)
            cell_bound = abs(omega) * h * (chi * np.sinh(2 * chi) + gamma * h) / 2
            assert cell_bound <= 2 * abs(omega) * gamma * h * h + 1e-14
            bounds.append(cell_bound)
        bound = min(1., steps * max(bounds))
        assert cq_distance <= bound + 3e-12
        if omega == 0:
            assert cq_distance < 2e-12
        distributions = []
        for states in (physical, target):
            distribution = []
            for history, rho in states.items():
                if history[-1] == 0:
                    for sign in (-1, 1):
                        distribution.append(float(np.trace((EVEN + sign * YL) @ rho).real / 2))
                else:
                    distribution.append(float(np.trace(rho).real))
            distributions.append(np.array(distribution))
        tv = float(np.abs(distributions[0] - distributions[1]).sum() / 2)
        assert tv <= cq_distance + 2e-12
        rows.append({"rates": list(rates), "h": h, "omega": omega, "phi": phi,
                     "intervals": steps, "retained_histories": len(target),
                     "complete_record_quantum_distance": cq_distance,
                     "terminal_readout_total_variation": tv, "hybrid_bound": bound,
                     "all_even_markov_probability": all_even, "all_even_formula": expected})
    return rows

def survival_checks():
    """The same bath is retained through every success, without resets."""
    rows = []
    strength, omega, phi, steps = 1.7, 1.1, 0.37, 8
    projector = np.kron(EVEN, I)
    bath = np.array([[0.65, 0.17j], [-0.17j, 0.35]], dtype=complex)
    assert np.linalg.eigvalsh(bath).min() > 0
    free = 0.5 * omega * np.kron(np.kron(Z, I), I) + np.kron(np.eye(4), 2.1 * X + 0.8 * Z)
    for h in (0.015, 0.05, 0.15):
        state = np.kron(INITIAL, bath)
        for index in range(steps):
            coupling = (np.cos(0.31 * index) * np.kron(np.kron(axis(phi), I), X)
                        + 0.7 * np.sin(0.23 + index) * np.kron(np.kron(Z, I), Y)
                        + 0.4 * np.kron(np.kron(Y, I), Z))
            coupling *= strength / np.linalg.norm(coupling, 2)
            assert np.linalg.norm(coupling, 2) <= strength + 1e-12
            state = conjugate(projector, conjugate(expm(-1j * h * (free + coupling)), state))
        probability = float(np.trace(state).real)
        lower = float(np.cos(strength * h) ** (2 * steps))
        assert probability >= lower - 2e-12
        saturation_state = np.kron(INITIAL, bath)
        saturation_u = expm(-1j * strength * h * np.kron(np.kron(axis(phi), I), X))
        for _ in range(steps):
            saturation_state = conjugate(projector, conjugate(saturation_u, saturation_state))
        saturation = float(np.trace(saturation_state).real)
        assert abs(saturation - lower) < 2e-12
        rows.append({"h": h, "intervals": steps, "coupling_bound": strength,
                     "same_bath_survival": probability, "universal_lower_bound": lower,
                     "saturating_transverse_survival": saturation})
    return rows

def response_checks():
    rows = []
    rates, phi, steps, epsilon = (0.4, 1.3), 0.71, 8, 1e-6
    for h in (0.03, 0.2, 0.7):
        positive = success_output(tree(rates, h, epsilon, phi, steps, True))
        negative = success_output(tree(rates, h, -epsilon, phi, steps, True))
        derivative = float(np.trace(YL @ (positive - negative)).real / (2 * epsilon))
        probability, reward = reward_chain(rates, h, steps)
        residual = abs(derivative - reward[0])
        assert residual < 2e-8
        speed = local_speed(rates, h)
        assert speed > 0
        _, long_reward = reward_chain(rates, h, 10000)
        empirical = float(long_reward.sum() / (10000 * h))
        assert abs(empirical - speed) < 1 / (10000 * h)
        rows.append({"rates": list(rates), "h": h, "phi": phi, "intervals": steps,
                     "difference_step": epsilon, "readout_derivative": derivative,
                     "classical_chain_success_reward": float(reward[0]),
                     "success_probability": float(probability[0]), "finite_difference_residual": residual,
                     "stationary_local_speed": speed, "long_chain_mean_speed": empirical})
    return rows

def witness_examples():
    """Stable evaluation of a nonvacuous all-even record certificate."""
    a, strength, horizon = 1., 10., 1.
    rows = []
    previous = 0.
    for steps in (1000, 10000, 100000):
        h = horizon / steps
        p, _, _ = parameters(a, h)
        markov = float(np.exp(steps * np.log1p(-p)))
        lower = float(np.exp(2 * steps * np.log(np.cos(strength * h))))
        certificate = max(0., lower - markov)
        assert strength * h <= np.pi / 2
        assert certificate > previous
        assert certificate < 1 - np.exp(-a * horizon)
        previous = certificate
        rows.append({"rate_a": a, "coupling_bound": strength, "horizon": horizon,
                     "parity_interval": h, "parity_results": steps,
                     "interior_contacts": steps - 1, "markov_all_even": markov,
                     "microscopic_survival_lower": lower, "certified_record_distance": certificate})
    assert abs(rows[1]["certified_record_distance"] - 0.6221519975) < 1e-8
    return rows

def main():
    if not __debug__:
        raise SystemExit("Run without -O: scientific assertions must be enabled.")
    print(json.dumps({"cell_checks": cell_checks(), "record_checks": record_checks(),
                      "memory_survival_checks": survival_checks(),
                      "local_response_checks": response_checks(),
                      "witness_examples": witness_examples()}, indent=2))

if __name__ == "__main__":
    main()
