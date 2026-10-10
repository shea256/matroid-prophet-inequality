#!/usr/bin/env python3
"""Exact finite checks for weighted residual entropy and rank charging.

These are adversarial finite checks, not a proof for every matroid. The
joint affine encoding itself is separately tested by check_joint_residual.
"""
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from math import comb
sys.dont_write_bytecode = True
from reverse_support import cases, log_bounds
from check_online_rule import Rule, bits, subsets, union


def generating_checks(counts):
    for n in range(0, 13):
        for v in (Q(1,2),Q(1,4),Q(1,1280)):
            for eta in (Q(1,64),Q(1,4096)):
                direct=Q(0)
                for j in range(n+1):
                    for z in range(n+1):
                        S=sum(comb(2*n,i) for i in range(min(j+z,2*n)+1))
                        assert v**(j+z)*S <= (1+v)**(2*n)
                        direct += comb(n,j)*comb(n,z)*48**j*4**z*S*eta**(j+z)
                        counts['binomial_dimension_bounds']+=1
                bound=(1+48*eta/v)**n*(1+4*eta/v)**n*(1+v)**(2*n)
                assert direct<=bound
                counts['weighted_generating_bounds']+=1


def adaptive_tail_checks(counts):
    # Arbitrary overlapping labelled residual families are fixed before O.
    # The selector maximizes the charged residual after seeing the entire O.
    for n in range(1,7):
        full=(1<<n)-1
        for design in range(4):
            family=[]
            for R in subsets(full):
                size=R.bit_count() if hasattr(int,'bit_count') else len(tuple(bits(R)))
                j=(R+design)%3 if R else 0
                z=(size+design)%3 if R else 0
                family.append((R,j,z))
            for p in (Q(1,4),Q(7,16),Q(3,4)):
                for a,b in ((1,1),(1,2),(2,1)):
                    mass=sum((p**(a*j+b*z) for _,j,z in family),Q(0))
                    distribution=Counter()
                    for O in subsets(full):
                        size=len(tuple(bits(O)))
                        prob=p**size*(1-p)**(n-size)
                        error=max([0]+[len(tuple(bits(R)))-a*j-b*z
                                      for R,j,z in family if R & ~O == 0])
                        distribution[error]+=prob
                    assert sum(distribution.values())==1
                    for x in range(n+1):
                        tail=sum((prob for e,prob in distribution.items() if e>x),Q(0))
                        assert tail<=min(1,mass*p**x)
                        counts['adaptive_weighted_tail_checks']+=1
                    expectation=sum((e*prob for e,prob in distribution.items()),Q(0))
                    upper=(log_bounds(mass)[1]+1)/log_bounds(1/p)[0]
                    assert expectation<=upper
                    counts['adaptive_integrated_expectations']+=1


def path_checks(counts):
    # Small stress penalties, rather than the final 39/2, exercise positive
    # and zero excess residuals on actual paths.
    mu,nu=Q(1,4),Q(1,2)
    for M,w in cases():
        U=sum(1<<e for e in range(M.n) if w[e]>0 and M.rank[1<<e])
        Y=M.greedy(w,(1<<M.n)-1)
        for D in subsets(U):
            for C in subsets(U):
                rule=Rule(M,{e:w[e] for e in bits(D|C)},0,D,C,2)
                if not rule.m:
                    counts['unlisted_outcomes']+=1
                groups=[0]+[sum(1<<e for e in range(M.n)
                                 if w[e]==v and rule.candidate(e,v)) for v in rule.values]
                for h in range(1,rule.m+1):
                    incoming,X,a=rule.F[h-1],rule.X[h],-3*h
                    generators=0
                    for k in range(a,1):
                        span=M.closure[incoming[k]|generators]
                        for e in bits(rule.Dh[h]&X[k]):
                            if not (span>>e&1):
                                generators|=1<<e
                                span=M.closure[span|(1<<e)]
                        assert span==X[k]
                    j=len(tuple(bits(generators)))
                    d=len(tuple(bits(rule.Dh[h])))
                    assert rule.kappa*j<=d
                    lower=sum(1<<e for e in bits(U) if w[e]<rule.values[h-1])
                    for T in subsets(lower):
                        for parity in (0,1):
                            residual=z=sigma=0
                            for b in range(a+2,1):
                                if b%2!=parity: continue
                                K=union(T&groups[l]&rule.X[l][b]&~rule.X[l][b-1]
                                        for l in range(1,h))
                                P=groups[h]&X[b]&~X[b-1]
                                span=M.closure[X[b-2]|K]
                                for e in bits(P&~(D|C)):
                                    if not (span>>e&1):
                                        z+=1;span=M.closure[span|(1<<e)]
                                residual |= P & ~span
                                sigma+=len(tuple(bits(P&rule.Dh[h]&Y&~rule.q(h,incoming[b-2]|K))))
                            r=len(tuple(bits(residual)))
                            assert residual & ~(D|C)==0
                            assert sigma<=rule.kappa*z+r
                            excess=max(Q(0),r-mu*j-nu*z)
                            assert sigma<=(rule.kappa+nu)*z+mu*d/rule.kappa+excess
                            counts['charged_actual_paths']+=1
                            counts['positive_excess_paths' if excess else 'zero_excess_paths']+=1
                            if z: counts['positive_rank_paths']+=1
                            if j: counts['positive_generator_paths']+=1
        counts['matroid_weight_instances']+=1
    assert counts['positive_excess_paths']>0
    assert counts['positive_rank_paths']>0
    assert counts['positive_generator_paths']>0
    # Abstract numeric negative controls: the residual penalty cannot simply
    # be discarded without charging rank / expected density. These are not
    # claimed hard matroid instances.
    k,mu,nu=Q(2),Q(2),Q(2)
    for j,z,d,r,sigma in ((0,1,0,2,4),(1,0,2,2,2)):
        e=max(Q(0),r-mu*j-nu*z)
        assert k*j<=d and sigma<=k*z+r
        assert sigma <= (k+nu)*z+mu*d/k+e
        assert sigma > k*z+e
        counts['omitted_charge_negative_controls']+=1


def main():
    c=Counter()
    generating_checks(c)
    adaptive_tail_checks(c)
    path_checks(c)
    print(json.dumps(dict(counts=c,stress_threshold=2,
                         path_penalties={'generator':'1/4','witness':'1/2'},
                         arithmetic='Exact integer/rational checks; outward rational log intervals',
                         result='PASS (finite checks, not a universal proof)'),indent=2))


if __name__=='__main__': main()
