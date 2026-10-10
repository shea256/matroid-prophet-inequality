#!/usr/bin/env python3
"""Exact certificate for the rank-charged residual refinement.

All logarithms use outward rational intervals. This certifies scalar
assertions, conditional on the written proof; it is not a universal proof.
"""
import json
import sys
from fractions import Fraction as Q
sys.dont_write_bytecode = True
from reverse_support import log_bounds


def certify():
    k,rho,h,t=272,Q(13,32),Q(3,4),Q(1,16384)
    theta,L=Q(261,256),256
    u,w,v=Q(1,640),Q(1,8192),Q(1,1280)
    a=b=Q(39,2)
    pO=rho+(1-rho)*t
    decay_lo=log_bounds(1/pO)[0]
    assert decay_lo > Q(9,10)
    # These use the actual rigorous decay interval, NOT its coarser 9/10
    # replacement. The latter alone is insufficient for the second bound.
    assert a*decay_lo > log_bounds(48/(u*v))[1]
    assert b*decay_lo > log_bounds(4/(w*v))[1]
    assert b*Q(9,10) < log_bounds(4/(w*v))[0]  # coarse-bound negative control
    assert theta**L > 140
    assert L*(theta-1)==5
    assert 0<u<1 and 0<w<1 and 0<v<1 and k>=4
    K=Q(k)+b
    D=u+w+2*v
    error=rho/(2*k)+a*rho/k+(D+Q(1,k))/Q(9,10)
    loss=error+K*t+(K*t+K*rho/k)/139
    slack=(1-h)*(rho/4-loss/h)
    c=(1-t)*Q(139,140)**2*t*slack/(5*K)
    old34=Q(14995972860899,244123247301151948800000)
    old36=Q(9652683394380719,637507023635152349901619200)
    assert slack>0
    assert t/4 >= (1-t)*t*(rho/4)*k/K
    assert c > Q(33,32)*Q(1,2**32)
    assert c > Q(39,10)*old34
    per_label=2+5+14+14+1
    shared=8+14+1
    assert (per_label,shared)==(36,23)
    return dict(
        parameters=dict(kappa=k,density_rate=str(rho),filter_rate=str(h),
                        guard_and_test_rate=str(t),mesh=str(theta),phases=L,
                        main_probability=str(1-t)),
        analysis_parameters=dict(generator_penalty=str(a),witness_penalty=str(b),
                                 generator_tilt=str(u),witness_tilt=str(w),
                                 arrangement_tilt=str(v),effective_kappa=str(K)),
        certified_bounds=dict(decay_lower='9/10',entropy_per_element_upper=str(D),
                              base_lower=140,tilt_inequalities='PASS, using unrounded log intervals'),
        error_upper=str(error),slack_lower=str(slack),certified_coefficient_lower_bound=str(c),
        ratio_over_2_minus_32=str(c*2**32),ratio_over_PR_certificate=str(c/old34),
        ratio_over_published_certificate=str(c/old36),
        simplified_guarantee='2^-32',stronger_simple_guarantee='(33/32)*2^-32',
        seed_bits='36n+23',base='(261/256)^256 > 140',
        result='PASS (exact scalar certificate, conditional on the written proof)')


if __name__=='__main__':
    print(json.dumps(certify(),indent=2))
