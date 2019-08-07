from numpy import*
from sympy import*
import numpy as np
def gaussjordan1(a,b):
    n = len(b)
    c = concatenate([a,b],axis = 1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
                    print(c[i,j])
    x=c[:,n]
    return x

def gaussjordan2(a,b):
    n = len(b)
    c = concatenate([a,b],axis = 1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+n):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
                    print(c[i,j])
    x=c[:,n]
    return x

def gaussjordanIn(a,b):
    n = len(b)
    I=identity(n)
    c = concatenate([a,b],axis = 1)
    c = concatenate([c,I],axis = 1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,2*n+1):
            c[e,j]=c[e,j]/t
        for i in range(n):
            if i!=e:
                t=c[i,e]
                for j in range(e,2*n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
    Inv=c[:,n+1:]
    return Inv

def Gauss1(a,b):
    n = len(b)
    c = concatenate([a,b],axis = 1)
    for e in range(n):
        t=c[e,e]
        for j in range(e,n+1):
            c[e,j]=c[e,j]/t
        for i in range(e+1,n):
                t=c[i,e]
                for j in range(e,n+1):
                    c[i,j]=c[i,j]-t*c[e,j]
    print(c)
    x = zeros([n,1])
    x[n-1]=c[n-1,n]
    for i in range (n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s=s+c[i,j]*x[j]
        x[i]=c[i,n]-s
    return x

def jacobi (a,b,x):
    n=len(x)
    t=x.copy()
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                s=s+a[i,j]*t[j]
        x[i]=(b[i]-s)/a[i,i]
    return x

def jacobim (a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=jacobi(a,b,x)
        d=np.linalg.norm(np.array(x)-np. array(t))
        if d<e:
            return [x,k]
        else:
            t=x.copy()
    return [[],m]

def gaussidel(a,b,x):
    n=len(x)
    for i in range (n):
        s=0
        for j in range (n):
            if i!=j:
                s=s+a[i,j]*x[j]
        x[i]=(b[i]-s)/a[i][i]
    return x

def gaussidelm (a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=gaussidel(a,b,x)
        d=linalg.norm(array(x)-array(t))
        if d<e:
            return [x,k]
        else:
            t=x.copy()
    return [[],m]

def lagrange(x,y,u=None):
    n=len(x)
    t=Symbol('t')
    p=0
    for i in range(n):
        L=1
        for j in range(n):
            if j!=i:
                L=L*(t-x[j])/(x[i]-x[j])
        p=p+y[i]*L
        p=expand(p)
    if u==None:
        return p
    elif type(u) == list:
        v=[]
        for i in range (len(u)):
            v=v+[p.subs(t,u[i])]
        return v
    else:
        return p.subs(t,u)
