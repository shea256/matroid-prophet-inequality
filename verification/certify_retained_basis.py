#!/usr/bin/env python3
"""Exact scalar certificate, conditional on the retained-basis written proof."""
import json
import sys
from fractions import Fraction as Q
sys.dont_write_bytecode = True
from reverse_support import log_bounds


def certify():
    k, rho, h, t = 192, Q(3, 8), Q(3, 4), Q(21, 2**18)
    theta, phases = Q(261, 256), 256
    u, w, v = Q(1, 512), Q(1, 4096), Q(1, 704)
    mu, nu, decay = Q(119, 8), Q(243, 16), Q(49, 50)
    p = rho+(1-rho)*t
    lam_lo = log_bounds(1/p)[0]
    assert lam_lo > decay
    assert mu*lam_lo > log_bounds(6/(u*v))[1]
    assert nu*lam_lo > log_bounds(1/(w*v))[1]
    # A separate algebraic route checks both fractional-power tilts exactly.
    assert 6**8 * p**119 < (u*v)**8
    assert p**243 < (w*v)**16
    # Direct atanh expansion, without the helper's range reduction.
    y = (1-p)/(1+p)
    direct_decay_lo = sum((2*y**(2*i+1)/Q(2*i+1) for i in range(20)), Q(0))
    assert direct_decay_lo > decay
    # The rounded decay alone would NOT establish the generator tilt.
    assert mu*decay < log_bounds(6/(u*v))[0]
    assert theta**phases > 140
    assert phases*(theta-1) == 5
    K, additive = k+nu, 1/decay
    gamma = rho/4-(w+2*v)/decay
    error = rho/(2*k)+mu*rho/k+u/decay
    loss = error+K*t+(K*t+K*rho/k)/139
    slack = (1-h)*(gamma-loss/h)
    c = (1-t)*Q(139, 140)**2*t*slack/(5*K)
    assert k >= 4 and all(0 < q < 1 for q in (rho,h,t,u,w,v))
    assert 0 < gamma < rho/4 and slack > 0
    assert (1-t)*(gamma*k+additive)/K < Q(1, 4)
    c2 = Q(773895463001, 3203794364409053184000)
    c0 = Q(9652683394380719, 637507023635152349901619200)
    # Independently reconstruct the preceding exact scalar certificate.
    old_k, old_K, old_t = 272, Q(583,2), Q(1,16384)
    old_rho, old_mu = Q(13,32), Q(39,2)
    old_d = Q(1,640)+Q(1,8192)+Q(2,1280)
    old_error = old_rho/(2*old_k)+old_mu*old_rho/old_k+(old_d+Q(1,old_k))/Q(9,10)
    old_loss = old_error+old_K*old_t+(old_K*old_t+old_K*old_rho/old_k)/139
    old_c = (1-old_t)*Q(139,140)**2*old_t*(1-h)*(old_rho/4-old_loss/h)/(5*old_K)
    assert old_c == c2
    assert c > Q(7, 4)*Q(1, 2**32)
    assert c > Q(17, 10)*c2
    assert c < Q(1, 2**31)  # This certificate does not cross the next power of two.
    assert (2+3+18+18+1, 8+18+1) == (42, 27)
    return dict(parameters=dict(kappa=k,density_rate=str(rho),filter_rate=str(h),
                                guard_and_test_rate=str(t),mesh=str(theta),phases=phases,
                                main_probability=str(1-t)),
                analysis_parameters=dict(generator_penalty=str(mu),witness_penalty=str(nu),
                                         generator_tilt=str(u),witness_tilt=str(w),
                                         arrangement_tilt=str(v),effective_kappa=str(K)),
                certified_bounds=dict(decay_lower=str(decay),base_lower=140,
                                      gamma_lower=str(gamma),error_upper=str(error),
                                      additive_upper=str(additive),slack_lower=str(slack),
                                      tilt_inequalities='PASS: unrounded log intervals and exact integer-power comparisons',
                                      decay_cross_check='PASS: separate 20-term positive atanh sum'),
                certified_coefficient_lower_bound=str(c),ratio_over_2_minus_32=str(c*2**32),
                ratio_over_previous_certificate=str(c/c2),ratio_over_published_certificate=str(c/c0),
                simplified_guarantee='(7/4)*2^-32',seed_bits='42n+27',base='(261/256)^256 > 140',
                previous_certificate_recomputed=str(old_c),
                result='PASS (exact scalar certificate, conditional on the written proof)')


if __name__ == '__main__':
    print(json.dumps(certify(),indent=2))
