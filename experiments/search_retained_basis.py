#!/usr/bin/env python3
"""Numerical discovery for three refinements; no optimality or proof claim."""
import json
import math
import random


def evaluate(x, mode):
    lk, lt, rho, h, lb, lu, lw, lv = x
    if not (math.log(4) < lk < 14 and -24 < lt < -2 and .01 < rho < .99
            and .1 < h < .99 and .5 < lb < 12
            and all(-30 < a < 0 for a in (lu, lw, lv))):
        return -1., {}
    k, t, B, u, w, v = map(math.exp, (lk, lt, lb, lu, lw, lv))
    lam = -math.log(rho+(1-rho)*t)
    A, C = (48, 4) if mode == 'baseline' else (6, 1)
    mu, nu = math.log(A/(u*v))/lam, math.log(C/(w*v))/lam
    K = k+nu
    gamma = rho/4
    entropy = math.log1p(u)+math.log1p(w)+2*math.log1p(v)
    if mode == 'projected':
        gamma -= (math.log1p(w)+2*math.log1p(v))/lam
        entropy = math.log1p(u)
    error = rho/(2*k)+mu*rho/k+entropy/lam
    additive = 1/lam if mode in ('additive', 'projected') else 0
    if not additive:
        error += 1/(k*lam)
    if gamma <= 0 or (1-t)*(gamma*k+additive)/K > .25:
        return -1., {}
    loss = error+K*t+(K*t+K*rho/k)/(B-1)
    slack = (1-h)*(gamma-loss/h)
    coefficient = (1-t)*(1-1/B)**2*t*slack/(256*math.expm1(lb/256)*K)
    return coefficient, dict(kappa=k, t=t, rho=rho, h=h, B=B, u=u, w=w, v=v,
                             generator_penalty=mu, witness_penalty=nu,
                             effective_kappa=K, gamma=gamma, error=error,
                             additive_error=additive, slack=slack)


def search(mode):
    rng = random.Random(11132)
    best = (-1., None)
    for i in range(16):
        k, rho = rng.uniform(120, 500), rng.uniform(.3, .65)
        x = ([math.log(272), math.log(1/16384), 13/32, .75, math.log(140),
              math.log(1/640), math.log(1/8192), math.log(1/1280)] if i == 0 else
             [math.log(k), rng.uniform(-11, -8), rho, rng.uniform(.65, .9),
              rng.uniform(3, 6), math.log(rho/k), math.log(1/k**2), math.log(rho/(2*k))])
        steps = [.35, .35, .05, .05, .4, .5, .5, .5]
        while max(steps) > 1e-7:
            improved = False
            for j in range(len(x)):
                for sign in (-1, 1):
                    y = x[:]
                    y[j] += sign*steps[j]
                    if evaluate(y, mode)[0] > evaluate(x, mode)[0]:
                        x, improved = y, True
            if not improved:
                steps = [s*.6 for s in steps]
        if evaluate(x, mode)[0] > best[0]:
            best = evaluate(x, mode)[0], x
    c, p = evaluate(best[1], mode)
    return dict(mode=mode, negative_log2=-math.log2(c), ratio_over_2_minus_32=c*2**32,
                parameters=p)


def main():
    print(json.dumps(dict(seed=11132, starts_per_mode=16, phases=256,
                         scope='Floating-point exploration; no global optimum or proof claim',
                         attacks=[search(mode) for mode in
                                  ('baseline', 'retained', 'additive', 'projected')]), indent=2))


if __name__ == '__main__':
    main()
