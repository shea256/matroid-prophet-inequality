#!/usr/bin/env python3
"""Exact scalar certificate for the joint residual encoding follow-up.

Rational log enclosures certify the analytic inequalities; this does not
verify the universal combinatorial proof or constitute independent review.
"""
import json
import sys
from fractions import Fraction as Q

sys.dont_write_bytecode = True
from reverse_support import log_bounds


def certify():
    k, rho, cap, h, t = 640, Q(7, 16), Q(33, 64), Q(3, 4), Q(1, 32768)
    theta, phases = Q(261, 256), 256
    pO = rho+(1-rho)*t
    # All comparisons below are between exact fractions. The logarithm
    # intervals use 24 atanh-series terms after dyadic range reduction.
    lambda_lo = log_bounds(1/pO)[0]
    entropy_hi = cap*(4*log_bounds(Q(k)/cap)[1]+4
                     +6*log_bounds(Q(2))[1]+log_bounds(Q(3))[1])
    kl_lo = (cap*log_bounds(cap/rho)[0]
             +(1-cap)*log_bounds((1-cap)/(1-rho))[0])
    assert entropy_hi+1 < Q(41, 2)
    assert lambda_lo > Q(413, 500)
    assert k*kl_lo > 11*log_bounds(Q(2))[1]
    assert theta**phases > 140
    assert phases*(theta-1) == 5
    assert Q(4) <= k and 0 < rho < cap < 1
    # For every n>=k, Chernoff gives P(|D|>cap*n)<2^-11.
    error = rho/(2*k)+Q(41, 2)/(k*Q(413, 500))+Q(1, 2048)
    loss = error+t*k+(t*k+rho)/139
    slack = (1-h)*(rho/4-loss/h)
    beta = Q(139, 140)
    coefficient = (1-t)*beta**2*t*slack/(5*k)
    old = Q(9652683394380719, 637507023635152349901619200)
    assert slack > 0
    assert t/4 >= (1-t)*t*rho/4  # maximum branch cancels the affine loss
    assert coefficient > Q(21, 20)*Q(1, 2**34)
    assert coefficient > 4*old
    per_label, shared = 2+4+15+15+1, 8+15+1
    assert (per_label, shared) == (37, 24)
    return {
        'parameters': {'kappa': k, 'density_rate': str(rho),
                       'density_cap': str(cap), 'filter_rate': str(h),
                       'guard_and_test_rate': str(t), 'mesh': str(theta),
                       'phases': phases, 'main_probability': str(1-t)},
        'certified_bounds': {'entropy_plus_one_upper': '41/2',
                             'decay_lower': '413/500',
                             'density_exception_upper': '1/2048',
                             'base_lower': 140},
        'error_upper': str(error), 'slack_lower': str(slack),
        'certified_coefficient_lower_bound': str(coefficient),
        'ratio_over_2^-34': str(coefficient*2**34),
        'ratio_over_published_coefficient': str(coefficient/old),
        'simplified_guarantee': '2^-34',
        'stronger_simple_guarantee': '(21/20)*2^-34',
        'seed_bits': '37n+24',
        'base': '(261/256)^256 > 140',
        'result': 'PASS (exact scalar certificate, conditional on the written proof)',
    }


if __name__ == '__main__':
    print(json.dumps(certify(), indent=2))
