#!/usr/bin/env python3
"""Exact constants for proofs/hazard_potential.md, not a proof checker."""
from fractions import Fraction as Q
from math import factorial
import json


def parameters(a=12, d=20, b=8, tail_bits=12, sharp_residual=True):
    kappa, t, base = 2**a, Q(1, 2**d), 2**b
    beta, gamma = Q(base-1, base), Q(5, 128)
    decay = 2-5*t if sharp_residual else Q(1)
    entropy = 5*a+12 if sharp_residual else 6*a+13
    delta = Q(entropy+tail_bits, kappa)/decay
    error = Q(1, 8*kappa)+delta+Q(1, 2**tail_bits)
    slack = gamma/2-error-t*kappa-(t*kappa+Q(1, 4))/(base-1)
    main_probability = 1-t/4
    ratio = main_probability*beta**2*t*slack/(b*kappa)
    return dict(kappa=kappa, t=t, base=base, beta=beta, gamma=gamma,
                decay=decay, entropy_bits_coefficient=entropy,
                delta=delta, error=error, slack=slack,
                main_probability=main_probability, ratio=ratio)


def certify():
    # Positive omitted terms of exp(6/5) give the strict analytic inequality.
    exp_partial = sum((Q(6, 5)**j/factorial(j) for j in range(5)), Q(0))
    assert exp_partial == Q(2059, 625) > Q(16, 5)
    assert Q(5, 16)*(2+Q(6, 5)) == 1
    assert Q(5, 16)/2/4 == Q(5, 128)
    # ln(2)>2/3 implies 5/ln(2)+4 < 23/2 < 12, and
    # ln(1+3t)/ln(2) <= (9/2)t < 5t.
    assert 5/Q(2, 3)+4 == Q(23, 2) < 12
    assert 3/Q(2, 3) == Q(9, 2) < 5
    p = parameters()
    k, t, g, decay = (p[x] for x in ('kappa', 't', 'gamma', 'decay'))
    assert k >= 4 and 0 < t <= Q(1, 3) and decay > 0
    assert p['delta'] < 1
    assert (decay*p['delta']-Q(p['entropy_bits_coefficient'], k))*k == 12
    assert p['slack'] == Q(4790554237, 1168228319232) > Q(1, 256)
    assert (1-p['main_probability'])/4-p['main_probability']*t*g > 0
    assert p['ratio'] > Q(1, 2**43) > Q(1, 2**47)
    # Simple sufficient bounds avoid relying on a rounded numerical coefficient.
    assert p['main_probability']*p['beta']**2 > Q(127, 128)
    assert p['slack'] > Q(128, 127)*Q(1, 256)
    assert Q(127, 128)*Q(128, 127)*Q(1, 256)*t/(8*k) == Q(1, 2**43)
    # Isolate the new exit lemma using the earlier residual bound unchanged.
    exit_only = parameters(a=14, d=22, b=8, tail_bits=14, sharp_residual=False)
    assert exit_only['ratio'] > Q(1, 2**47)
    return {
        'parameters': {key: str(value) for key, value in p.items()},
        'exit_mass_strict_lower_bound': '5/16',
        'simplified_guarantee': '2^-43',
        'exact_ratio_over_2^-43': str(p['ratio']*2**43),
        'exact_ratio_over_announced_2^-47': str(p['ratio']*2**47),
        'exit_lemma_with_old_residual_ratio_over_2^-47': str(exit_only['ratio']*2**47),
        'seed_bits': '44n+26',
        'result': 'PASS (exact scalar arithmetic; new hazard lemma is a written proof)',
    }


if __name__ == '__main__':
    print(json.dumps(certify(), indent=2))
