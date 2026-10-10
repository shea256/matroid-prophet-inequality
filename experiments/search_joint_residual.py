#!/usr/bin/env python3
"""Reproducible numerical exploration; no global optimum or proof claim.

Three attacks: finer parameters alone, a density cutoff, and a joint pivot
count plus that cutoff. Only certify_joint_residual.py certifies constants.
"""
import json
import math
import random


def coefficient(x, mode, phases=256):
    lk, lt, rho, h, lB, cap = x
    if not (math.log(4) < lk < 16 and -24 < lt < 0
            and 0 < rho < cap <= 1 and 0 < h < 1 and .01 < lB < 12):
        return -1.
    k, t, B = math.exp(lk), math.exp(lt), math.exp(lB)
    decay = -math.log(rho+(1-rho)*t)
    if mode == 'parameters_only':
        entropy = 5*lk+5+4*math.log(2)
        tail = 0.
    else:
        kl = (cap*math.log(cap/rho)
              +(1-cap)*math.log((1-cap)/(1-rho)))
        tail = math.exp(-k*kl)
        entropy = (cap*(5*math.log(k/cap)+5+4*math.log(2)) if mode == 'density_cutoff'
                   else cap*(4*math.log(k/cap)+4+6*math.log(2)+math.log(3)))
    error = rho/(2*k)+(entropy+1)/(k*decay)+tail
    loss = error+t*k+(t*k+rho)/(B-1)
    slack = (1-h)*(rho/4-loss/h)
    return (1-t)*(1-1/B)**2*t*slack/(phases*math.expm1(lB/phases)*k)


def search(mode):
    rng, best = random.Random(111), (-1., None)
    for start in range(12):
        rho = rng.uniform(.3, .65)
        x = ([math.log(900), math.log(3e-5), .44, .77, math.log(120), .53]
             if start == 0 else [rng.uniform(6, 9), rng.uniform(-13, -10),
                                rho, rng.uniform(.6, .9), rng.uniform(3, 7), rho+.09])
        step = [.5, .5, .05, .06, .5, .04]
        if mode == 'parameters_only':
            x[5], step[5] = .99, 0.
        while max(step) > 2e-7:
            changed = False
            for j in range(6):
                for sign in (-1, 1):
                    y = x[:]
                    y[j] += sign*step[j]
                    if coefficient(y, mode) > coefficient(x, mode):
                        x, changed = y, True
            if not changed:
                step = [s*.6 for s in step]
        c = coefficient(x, mode)
        if c > best[0]:
            best = c, x
    c, x = best
    return {'mode': mode, 'ratio_over_2^-36': c*2**36,
            'negative_log2': -math.log2(c),
            'parameters': dict(zip(('kappa', 't', 'rho', 'h', 'B', 'cap'),
                                   (math.exp(x[0]), math.exp(x[1]), x[2], x[3], math.exp(x[4]), x[5])))}


def main():
    grid = []
    for k in range(560, 721, 16):
        for i in range(12, 17):
            for j in range(i*2+4, i*2+9):
                x = [math.log(k), math.log(1/32768), i/32, .75,
                     256*math.log(261/256), j/64]
                grid.append((coefficient(x, 'joint_count'), k, i, j))
    best = sorted(grid, reverse=True)[:5]
    chosen = [math.log(640), math.log(1/32768), 7/16, 3/4,
              256*math.log(261/256), 33/64]
    print(json.dumps({
        'scope': 'Floating-point discovery only; no global optimality or proof claim',
        'seed': 111, 'starts_per_attack': 12, 'phases': 256,
        'attacks': [search(m) for m in ('parameters_only', 'density_cutoff', 'joint_count')],
        'grid_tuples': len(grid),
        'grid_fixed': {'t': '1/32768', 'h': '3/4', 'mesh': '261/256', 'phases': 256},
        'grid_top': [{'ratio_over_2^-34': c*2**34, 'kappa': k,
                      'rho': f'{i}/32', 'cap': f'{j}/64'} for c, k, i, j in best],
        'chosen_ratio_over_2^-34': coefficient(chosen, 'joint_count')*2**34,
        'note': 'Exact certificate rounds logarithms, exception probability, and base conservatively.'
    }, indent=2))


if __name__ == '__main__':
    main()
