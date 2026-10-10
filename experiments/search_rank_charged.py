#!/usr/bin/env python3
"""Numerical discovery for rank-charged residual entropy; not a proof."""
import json
import math
import random


def evaluate(x, mode='direct', phases=256):
    lk, lt, rho, h, lB, lu, lw, lv, cap = x
    if not (math.log(4) < lk < 14 and -24 < lt < -2 and .01 < rho < .99
            and .1 < h < .999 and .5 < lB < 12 and -30 < lu < 0
            and -30 < lw < 0 and -30 < lv < 0):
        return -1., {}
    k,t,B,u,w,v=map(math.exp,(lk,lt,lB,lu,lw,lv))
    lam=-math.log(rho+(1-rho)*t)
    b=math.log(4/(w*v))/lam
    K=k+b
    common=math.log1p(u)+math.log1p(w)+2*math.log1p(v)
    if mode=='direct':
        a=math.log(48/(u*v))/lam
        error=rho/(2*k)+a*rho/k+(common+1/k)/lam
    else:
        if not rho < cap < 1:
            return -1., {}
        # Sum j<=floor(cap*n/k); u is the binomial tilt for generators.
        A=cap*math.log(48/(u*v))+k*common
        kl=cap*math.log(cap/rho)+(1-cap)*math.log((1-cap)/(1-rho))
        error=rho/(2*k)+(A+1)/(k*lam)+math.exp(-k*kl)
    loss=error+K*t+(K*t+K*rho/k)/(B-1)
    slack=(1-h)*(rho/4-loss/h)
    c=(1-t)*(1-1/B)**2*t*slack/(phases*math.expm1(lB/phases)*K)
    return c,dict(kappa=k,t=t,rho=rho,h=h,B=B,u=u,w=w,v=v,cap=cap,
                  effective_kappa=K,error=error,slack=slack)


def search(mode):
    rng=random.Random(11134)
    best=(-1.,None)
    for i in range(16):
        rho=rng.uniform(.3,.65)
        k=rng.uniform(120,500)
        x=([math.log(300), math.log(1/16384), .45,.75, math.log(120),
            math.log(.45/300),math.log(1/300**2),math.log(.45/600),.55]
           if i==0 else [math.log(k),rng.uniform(-11,-8),rho,rng.uniform(.65,.9),
                         rng.uniform(3,6),math.log(rho/k),math.log(1/k**2),
                         math.log(rho/(2*k)),min(.98,rho+.15)])
        steps=[.35,.35,.05,.05,.4,.5,.5,.5,.05 if mode!='direct' else 0]
        while max(steps)>1e-7:
            improved=False
            for j in range(len(x)):
                for sign in (-1,1):
                    y=x[:];y[j]+=sign*steps[j]
                    if evaluate(y,mode)[0]>evaluate(x,mode)[0]:
                        x,improved=y,True
            if not improved:
                steps=[s*.6 for s in steps]
        if evaluate(x,mode)[0]>best[0]:
            best=(evaluate(x,mode)[0],x)
    c,p=evaluate(best[1],mode)
    return dict(mode=mode,ratio_over_2_minus_34=c*2**34,
                negative_log2=-math.log2(c),parameters=p)


def main():
    grid=[]
    for k in (256,264,272,280,288):
        for rho in (3/8,13/32,7/16):
            x=[math.log(k),math.log(1/16384),rho,3/4,256*math.log(261/256),
               math.log(1/640),math.log(1/8192),math.log(1/1280),.6]
            c,_=evaluate(x)
            grid.append(dict(kappa=k,rho=rho,ratio_over_2_minus_32=c*2**32))
    print(json.dumps(dict(scope='Floating-point exploration; no global optimum or proof claim',
                         seed=11134,starts_per_mode=16,phases=256,
                         attacks=[search(m) for m in ('cutoff','direct')],
                         grid_fixed=dict(t='1/16384',h='3/4',mesh='261/256',phases=256,
                                         u='1/640',w='1/8192',v='1/1280'),
                         grid_tuples=len(grid),grid=grid,
                         grid_best=max(grid,key=lambda row:row['ratio_over_2_minus_32']),
                         note='The exact certificate further rounds both penalties to 39/2, decay to 9/10, base to 140, and log(1+x) to x.'),indent=2))


if __name__=='__main__': main()
