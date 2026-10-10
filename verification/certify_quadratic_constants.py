#!/usr/bin/env python3
"""Exact scalar certificate for the quadratic-potential refinement."""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction as Q
import json


def parameters(a=11, d=16, filter_rate=Q(3, 4), mesh=Q(69, 64), phases=64):
    kappa, t, rho = 2**a, Q(1, 2**d), Q(5, 8)
    gamma, main_probability = rho/4, 1-t
    base = mesh**phases
    beta = (base-1)/base
    # ln(8/5)>15/32 and ln(1+3t/5)<=3t/5.
    decay = Q(15, 32)-Q(3, 5)*t
    # Entropy plus the integral tail's +1, using ln(2)<7/10.
    entropy_plus_one = (5*a+4)*Q(7, 10)+6
    error = rho/(2*kappa)+entropy_plus_one/(kappa*decay)
    loss = error+t*kappa+(t*kappa+rho)/(base-1)
    slack = (1-filter_rate)*(gamma-loss/filter_rate)
    coefficient = main_probability*beta**2*t*slack/(phases*(mesh-1)*kappa)
    return dict(kappa=kappa, t=t, density_rate=rho, filter_rate=filter_rate,
                gamma=gamma, main_probability=main_probability, mesh=mesh,
                phases=phases, base=base, beta=beta, decay=decay,
                entropy_plus_one=entropy_plus_one, error=error,
                slack=slack, coefficient=coefficient)


def certify():
    p = parameters()
    k, t, rho, gamma = (p[x] for x in ('kappa', 't', 'density_rate', 'gamma'))
    # atanh series: ln(2)<=25/36<7/10; two terms for ln(8/5).
    assert Q(25, 36) < Q(7, 10)
    assert 2*(Q(3, 13)+Q(3, 13)**3/3) == Q(1032, 2197) > Q(15, 32)
    assert p['decay'] > 0 and p['error'] < 1
    assert p['base'] > 120
    assert 69**64 > 120*64**64
    # Keep the reported coefficient compact: bound B below by 120.
    beta_lower = Q(119, 120)
    slack_lower = gamma/4-(p['error']+t*k+(t*k+rho)/119)/3
    coefficient_lower = (1-t)*beta_lower**2*t*slack_lower/(5*k)
    assert slack_lower == Q(2652290047, 256686391296) > 0
    assert p['slack'] > slack_lower
    assert p['coefficient'] > coefficient_lower > Q(1, 2**36)
    assert t/4 >= (1-t)*t*gamma
    assert p['phases']*(p['mesh']-1) == 5
    # Explicit fixed-length masks: H=3/4 (2), D=5/8 (3), C,T (16 each),
    # maximum mask (1); phase (6), branch (16), and parity (1).
    per_label = 2+3+16+16+1
    shared = 6+16+1
    assert (per_label, shared) == (38, 23)
    return {
        'parameters': {name: str(p[name]) for name in (
            'kappa', 't', 'density_rate', 'filter_rate', 'gamma',
            'main_probability', 'mesh', 'phases', 'decay',
            'entropy_plus_one', 'error')},
        'base': '(69/64)^64 > 120',
        'slack_lower_bound': str(slack_lower),
        'certified_coefficient_lower_bound': str(coefficient_lower),
        'exact_lower_bound_over_2^-36': str(coefficient_lower*2**36),
        'exact_lower_bound_over_source_2^-293': str(coefficient_lower*2**293),
        'simplified_guarantee': '2^-36',
        'exit_hazard_lower_bound': '1/2',
        'seed_bits': '38n+23',
        'result': 'PASS (exact scalar certificate; universal theorem has a written proof)',
    }


if __name__ == '__main__':
    print(json.dumps(certify(), indent=2))
