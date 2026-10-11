#!/usr/bin/env python3
"""Exact scalar certificate, conditional on the support-refinement proof."""
import json
import sys
from fractions import Fraction as Q
sys.dont_write_bytecode = True
from reverse_support import log_bounds
from certify_activation_split import certify as previous_certificate


def fair_bits(p):
    assert p.denominator & (p.denominator-1) == 0
    return p.denominator.bit_length()-1


def certify():
    k,rho,h,t = 164,Q(93,256),Q(3,4),Q(23,2**18)
    theta,L = Q(261,256),256
    mu,nu = Q(105,8),Q(113,8)
    u,w,v,d = Q(1,864),Q(1,4000),Q(1,624),Q(253,250)
    p = rho+(1-rho)*t
    assert p > Q(3,4)**4
    A = rho*(3+Q(4,3)*v)
    # Integer powers prove rho*(p^(mu-1/4)+3*p^mu/v) < u
    # and (1-p)*p^nu/v < w, with no floating arithmetic.
    assert A**8*p**105 < (u*v)**8
    assert (1-p)**8*p**113 < (w*v)**8
    lam_lo = log_bounds(1/p)[0]
    assert mu*lam_lo > log_bounds(A/(u*v))[1]
    assert nu*lam_lo > log_bounds((1-p)/(w*v))[1]
    assert lam_lo > d
    x = (1-p)/(1+p)
    direct_lo = sum((2*x**(2*i+1)/Q(2*i+1) for i in range(20)),Q(0))
    assert direct_lo > d
    assert theta**L > 140 and L*(theta-1) == 5
    by = (Q(2,3)*u*(1/rho-1)+w)/(1+u)+2*v
    gamma = rho/4-by/d
    error = mu*rho/k+u/d
    K,additive = k+nu,1/d
    loss = error+K*t+(K*t+K*rho/k)/139
    slack = (1-h)*(gamma-loss/h)
    c = (1-t)*Q(139,140)**2*t*slack/(5*K)
    assert k>=4 and all(0<r<1 for r in (rho,h,t,u,w,v))
    assert mu>Q(1,4) and nu>0 and 0<gamma<rho/4 and slack>0
    assert (1-t)*(gamma*k+additive)/K < Q(1,4)
    old = Q(previous_certificate()['certified_coefficient_lower_bound'])
    assert old == Q(8003458533570087953,16807475946150704657203200000)
    assert c == Q(4084754449786906742230661,8009094702029267287249256448000000)
    assert c > Q(35,32)/2**31 and c < Q(1,2**30)
    assert c > Q(1071,1000)*old
    c0 = Q(9652683394380719,637507023635152349901619200)
    seed_per_label = sum(fair_bits(r) for r in (h,rho,t,t,Q(1,2)))
    seed_shared = 8+fair_bits(1-t)+1
    assert (seed_per_label,seed_shared) == (47,27)
    return dict(parameters=dict(kappa=k,density_rate=str(rho),filter_rate=str(h),
                guard_and_test_rate=str(t),mesh=str(theta),phases=L,main_probability=str(1-t)),
                analysis_parameters=dict(active_generator_penalty=str(mu),
                activation_generator_penalty=str(mu-Q(1,4)),witness_penalty=str(nu),
                generator_tilt=str(u),witness_tilt=str(w),arrangement_tilt=str(v),
                effective_kappa=str(K)),
                certified_bounds=dict(decay_lower=str(d),base_lower=140,
                gamma_lower=str(gamma),error_upper=str(error),additive_upper=str(additive),
                slack_lower=str(slack),tilts='PASS: integer powers and outward log intervals',
                decay='PASS: log interval and separate 20-term positive series'),
                certified_coefficient_lower_bound=str(c),ratio_over_2_minus_31=str(c*2**31),
                ratio_over_previous_certificate=str(c/old),ratio_over_original_certificate=str(c/c0),
                previous_certificate_recomputed=str(old),simplified_guarantee='(35/32)*2^-31',
                seed_bits='47n+27',base='(261/256)^256 > 140',result='PASS (exact scalar certificate, conditional on written proof)')


if __name__ == '__main__':
    print(json.dumps(certify(),indent=2))
