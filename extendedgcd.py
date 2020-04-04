
import math
def gcd(r1,r2):
    s1=1
    s2=0
    t1=0
    t2=1
    while r2>0:
        q=math.floor(r1/r2)
        r=r1-(q*r2)
        r1=r2
        r2=r
        s=s1-(q*s2)
        s1=s2
        s2=s
        t=t1-q*t2
        t1=t2
        t2=t
    s=s1
    t=t1
    return r1,s,t
print(gcd(161,28))
