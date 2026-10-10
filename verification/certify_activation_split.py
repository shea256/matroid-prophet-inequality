#!/usr/bin/env python3
"""Exact coefficient certificate, conditional on the activation-split proof."""
import json
import sys
from fractions import Fraction as Q
sys.dont_write_bytecode = True
from reverse_support import log_bounds
from certify_retained_basis import certify as previous_certificate


def fair_bits(probability):
    denominator = probability.denominator
    assert denominator & (denominator-1) == 0
    return denominator.bit_length()-1


def certify():
    k, rho, h, t = 176, Q(3, 8), Q(3, 4), Q(11, 2**17)
    theta, phases = Q(261, 256), 256
    u, w, v = Q(1, 1056), Q(1, 4096), Q(1, 648)
    mu, nu, decay = Q(113, 8), Q(117, 8), Q(49, 50)
    mu0 = mu-Q(1, 4)
    p = rho+(1-rho)*t
    lam_lo = log_bounds(1/p)[0]
    assert lam_lo > decay
    # p^(-1/4) < 4/3 bounds the fixed-activation contribution.
    assert p > Q(3, 4)**4
    A = rho*(4+Q(4, 3)*v)
    assert mu*lam_lo > log_bounds(A/(u*v))[1]
    assert nu*lam_lo > log_bounds((1-p)/(w*v))[1]
    # Separate exact integer-power comparisons establish the same two tilts.
    assert A**8*p**113 < (u*v)**8
    assert (1-p)**8*p**117 < (w*v)**8
    x = (1-p)/(1+p)
    direct_decay_lo = sum((2*x**(2*i+1)/Q(2*i+1) for i in range(20)), Q(0))
    assert direct_decay_lo > decay
    assert theta**phases > 140 and phases*(theta-1) == 5
    K, additive = k+nu, 1/decay
    # p >= rho and log(1+x) <= x give this rational entropy bound.
    y_charge = (u*(1/rho-1)+w)/(1+u)+2*v
    gamma = rho/4-y_charge/decay
    error = mu*rho/k+u/decay  # the activation charge has cancelled
    loss = error+K*t+(K*t+K*rho/k)/139
    slack = (1-h)*(gamma-loss/h)
    c = (1-t)*Q(139, 140)**2*t*slack/(5*K)
    assert k >= 4 and all(0 < q < 1 for q in (rho,h,t,u,w,v))
    assert mu0 > 0 and nu > 0 and 0 < gamma < rho/4 and slack > 0
    assert (1-t)*(gamma*k+additive)/K < Q(1, 4)
    old = Q(previous_certificate()['certified_coefficient_lower_bound'])
    published = Q(9652683394380719, 637507023635152349901619200)
    assert old == Q(548933908320757, 1325382348737372749824000)
    assert c == Q(8003458533570087953, 16807475946150704657203200000)
    assert c > Q(51, 50)/2**31 and c < Q(1, 2**30)
    assert c > Q(1149, 1000)*old
    per_label = sum(fair_bits(q) for q in (h,rho,t,t,Q(1,2)))
    shared = (phases.bit_length()-1)+fair_bits(1-t)+1
    assert (per_label, shared) == (40, 26)
    return dict(parameters=dict(kappa=k,density_rate=str(rho),filter_rate=str(h),
                                guard_and_test_rate=str(t),mesh=str(theta),phases=phases,
                                main_probability=str(1-t)),
                analysis_parameters=dict(active_generator_penalty=str(mu),
                                         activation_generator_penalty=str(mu0),
                                         witness_penalty=str(nu),generator_tilt=str(u),
                                         witness_tilt=str(w),arrangement_tilt=str(v),
                                         effective_kappa=str(K)),
                certified_bounds=dict(decay_lower=str(decay),base_lower=140,
                                      gamma_lower=str(gamma),error_upper=str(error),
                                      additive_upper=str(additive),slack_lower=str(slack),
                                      tilt_inequalities='PASS: outward log intervals and separate integer-power comparisons',
                                      decay_cross_check='PASS: separate 20-term positive atanh sum'),
                certified_coefficient_lower_bound=str(c),ratio_over_2_minus_31=str(c*2**31),
                ratio_over_previous_certificate=str(c/old),
                ratio_over_published_certificate=str(c/published),
                simplified_guarantee='(51/50)*2^-31',seed_bits='40n+26',
                base='(261/256)^256 > 140',previous_certificate_recomputed=str(old),
                result='PASS (exact scalar certificate, conditional on the written proof)')


if __name__ == '__main__':
    print(json.dumps(certify(), indent=2))
