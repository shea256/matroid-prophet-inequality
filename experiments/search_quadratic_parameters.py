#!/usr/bin/env python3
"""Declared rational grid; candidate selection, not a global optimum."""
from fractions import Fraction as Q
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'verification'))
from certify_quadratic_constants import parameters


def main():
    best, examined, feasible = [], 0, 0
    for a in range(9, 15):
        for d in range(a+3, a+10):
            for h in (Q(i, 16) for i in range(8, 16)):
                for q in (Q(33, 32), Q(17, 16), Q(69, 64), Q(35, 32), Q(9, 8), Q(5, 4)):
                    for phases in (16, 32, 64, 128):
                        p = parameters(a, d, h, q, phases)
                        examined += 1
                        if p['slack'] > 0:
                            assert (1-p['main_probability'])/4 >= p['main_probability']*p['t']*p['gamma']
                            feasible += 1
                            best.append((p['coefficient'], a, d, h, q, phases))
    best.sort(reverse=True)
    print('density rate fixed at 5/8; entropy/decay bounds as in scalar certificate')
    print('examined:', examined, 'feasible:', feasible)
    for c, a, d, h, q, phases in best[:5]:
        print('a,d,H,mesh,phases:', a, d, str(h), str(q), phases,
              'approximate_ratio_over_2^-36:', float(c*2**36))
    chosen = parameters()
    print('chosen (11,16,3/4,69/64,64), approximate_ratio_over_2^-36:',
          float(chosen['coefficient']*2**36))
    print('Ratios ordered by exact fractions; displayed decimals are not certificates.')
    print('No global optimality or novelty claim. The certificate uses the simpler bound B>120.')


if __name__ == '__main__':
    main()
