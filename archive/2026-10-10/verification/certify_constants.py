#!/usr/bin/env python3
"""Exact scalar certificates for the proof in proofs/parameter_refinement.md.

This checks arithmetic, not the universal matroid lemmas or their Lean proofs.
Python standard library only; no floating-point comparisons decide a claim.
"""
from fractions import Fraction as Q
import json


def parameters(a=18, d=29, b=16, m=4, tail_bits=18):
    kappa, t, base = 2**a, Q(1, 2**d), 2**b
    beta = Q(base - 1, base)
    exit_failure = Q(2)**(1-m) * (Q(7, 10)*(m+2) + 1)
    gamma = Q(1, 2**m) * (1-exit_failure) / 8
    delta = Q(6*a + 13 + tail_bits, kappa)
    error = Q(1, 8*kappa) + delta + Q(1, 2**tail_bits)
    slack = gamma/2 - error - t*kappa - (t*kappa+Q(1, 4))/(base-1)
    main_probability = 1-t/64
    ratio = main_probability * beta**2 * t * slack / (b*kappa)
    return dict(kappa=kappa, t=t, base=base, beta=beta,
                exit_failure=exit_failure, gamma=gamma, delta=delta,
                error=error, slack=slack, main_probability=main_probability,
                ratio=ratio)


def certify():
    # ln(2) = 2 sum_{j>=0} 1/((2j+1)3^(2j+1)).
    # Its first term is 2/3; bounding later denominators by 3 gives 25/36.
    assert Q(2, 3) < Q(25, 36) < Q(7, 10)
    # Reproduce the stronger *published* constant and its lossless transfer.
    baseline = Q(1, 2**140)*Q(1, 2**16)/(32*2**100*2**32)
    assert baseline == Q(1, 2**293)
    original_error = Q(1, 2**23)+Q(1, 2**40)+(1+Q(1, 2**40))/(2**32-1)
    assert original_error < Q(1, 2**21)
    rounding_only = Q(1, 2**261)*Q(2**32-1, 32*2**32)
    assert rounding_only == (1-Q(1, 2**32))*Q(1, 2**266)

    p = parameters()
    k, t, B, beta, g = [p[x] for x in ('kappa', 't', 'base', 'beta', 'gamma')]
    assert k >= 4 and 0 < t <= Q(1, 3)
    assert p['exit_failure'] == Q(13, 20)
    assert g == Q(7, 2560)
    assert p['delta'] == Q(139, 2**18) < 1
    # Residual union bound at n=kappa; it decreases for every n>=kappa.
    entropy_bits_per_label = Q(6*18+13, k)
    assert (p['delta']-entropy_bits_per_label)*k == 18
    assert p['error'] == Q(1121, 2**21)
    assert p['slack'] == Q(3120271, 9162457088)
    assert p['slack'] > Q(1, 3072)
    mix = p['main_probability']
    assert mix == 1-Q(1, 2**35)
    assert (1-mix)/4 - mix*t*g > 0  # coefficient of maximum weight
    assert mix*beta**2 > Q(3, 4)
    assert t/k == Q(1, 2**47)
    simple = Q(3, 4)*Q(1, 3072)*Q(1, 2**47)/16
    assert simple == Q(1, 2**63)
    assert p['ratio'] > simple
    # Isolate the gain from retuning/accounting before random offsets.
    deterministic_ratio = mix*beta*t*p['slack']/(k*B)
    assert deterministic_ratio > Q(1, 2**75)
    assert p['ratio']/deterministic_ratio == Q(B-1, 16)
    # Arithmetic points used in the analytic (not grid-only) template limitation.
    assert parameters(m=5)['gamma'] == Q(101, 40960) < Q(7, 2560)
    assert Q(1, 512) < Q(7, 2560) < Q(1, 256)
    assert Q(109, 2**16) > Q(7, 5120)
    assert Q(1, 256)**2/(16*(2**17)**2) == Q(1, 2**54)
    assert p['ratio'] < Q(1, 2**54) < Q(1, 2**47)
    return {
        'baseline': str(baseline),
        'rounding_only_ratio': str(rounding_only),
        'chosen_parameters': {key: str(value) for key, value in p.items()},
        'certified_simplified_ratio': '2^-63',
        'exact_ratio_over_2^-63': str(p['ratio']*2**63),
        'deterministic_offset_ratio_exceeds': '2^-75',
        'gain_over_published_2^-293_at_least': '2^230',
        'external_announcement': '2^-47 (stronger; proof unverified here)',
        'conservative_certificate_family_upper_bound': 'strictly below 2^-54',
        'checks': 'PASS (exact rational arithmetic; not a universal proof checker)',
    }


if __name__ == '__main__':
    print(json.dumps(certify(), indent=2))
