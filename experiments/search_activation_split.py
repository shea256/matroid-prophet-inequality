#!/usr/bin/env python3
"""Numerical discovery only; no global optimum or universal proof claim."""
import math,random,json

def evaluate(x, mode):
    lk,lt,rho,h,lb,lu,lw,lv=x
    if not (math.log(4)<lk<14 and -24<lt<-2 and .01<rho<.99 and .1<h<.99 and .5<lb<12 and all(-30<a<0 for a in (lu,lw,lv))): return -1,{}
    k,t,B,u,w,v=map(math.exp,(lk,lt,lb,lu,lw,lv))
    p=rho+(1-rho)*t
    lam=-math.log(p)
    mu=math.log(6/(u*v))/lam
    nu=math.log(1/(w*v))/lam
    gamma=rho/4-(math.log1p(w)+2*math.log1p(v))/lam
    error=rho/(2*k)+mu*rho/k+math.log1p(u)/lam
    if mode=='safe': error-=rho/(4*k)
    if mode in ('split','membership'):
        A=4+v*math.exp(lam/4)
        mu=math.log(A/(u*v))/lam
        error=mu*rho/k+math.log1p(u)/lam
    if mode=='membership':
        mu=math.log(rho*A/(u*v))/lam
        nu=math.log((1-p)/(w*v))/lam
        gamma=rho/4-(math.log1p(u/p+w)-math.log1p(u)+2*math.log1p(v))/lam
        error=mu*rho/k+math.log1p(u)/lam
    K=k+nu
    additive=1/lam
    if gamma<=0 or (1-t)*(gamma*k+additive)/K>.25:return -1,{}
    loss=error+K*t+(K*t+K*rho/k)/(B-1)
    slack=(1-h)*(gamma-loss/h)
    coefficient=(1-t)*(1-1/B)**2*t*slack/(256*math.expm1(lb/256)*K)
    return coefficient,dict(kappa=k,t=t,rho=rho,h=h,B=B,u=u,w=w,v=v,mu=mu,nu=nu,gamma=gamma,error=error,slack=slack)
def search(mode):
    rng=random.Random(11133);best=(-1,None)
    for i in range(24):
        x=[math.log(192), math.log(21/2**18),3/8,.75,math.log(140),math.log(1/512),math.log(1/4096),math.log(1/704)] if i==0 else [math.log(rng.uniform(100,350)), rng.uniform(-11,-8),rng.uniform(.3,.65),rng.uniform(.65,.9),rng.uniform(3,6), math.log(rng.uniform(.001,.003)),math.log(.0002),math.log(.001)]
        steps=[.3,.3,.04,.04,.3,.4,.4,.4]
        while max(steps)>1e-7:
            improved=False
            for j in range(8):
                for sign in [-1,1]:
                    y=x[:];y[j]+=sign*steps[j]
                    if evaluate(y,mode)[0]>evaluate(x,mode)[0]:x=y;improved=True
            if not improved:steps=[s*.6 for s in steps]
        c,p=evaluate(x,mode)
        if c>best[0]:best=(c,p)
    return dict(mode=mode,coefficient=best[0],ratio_2_minus_31=best[0]*2**31,parameters=best[1])
if __name__ == '__main__':
    print(json.dumps(dict(seed=11133, starts_per_mode=24, phases=256,
                          scope='Floating-point search; not a proof or global optimum',
                          attacks=[search(m) for m in ['baseline','safe','split','membership']]),indent=2))
