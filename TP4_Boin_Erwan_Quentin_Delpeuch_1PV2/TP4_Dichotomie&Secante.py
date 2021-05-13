"""BOIN Erwan - DELPEUCH Quentin- 1PV2
Analyse numerique - TP4"""

from math import *


def Dichotomie(f,a0,b0,epsilon, Nintermax):
    an=a0
    bn=b0
    n=1
    while abs(bn - an)> epsilon and n<Nintermax:
        m=(an + bn)/2
        if (f(an)*f(m)<=0):
            bn = m
        else:
            an = m
        n=n+1
    
    return m,n

def Secante(f,x0,x1,epsilon,Nitermax):
    xold2 = x0
    xold = x1
    xnew = xold - ((xold-xold2)*f(xold))/(f(xold)-f(xold2))
    erreur = xnew - xold
    xold = xnew
    n = 1
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = xold - ((xold-xold2)*f(xold))/(f(xold)-f(xold2))
        erreur = xnew - xold
        xold = xnew
        n = n + 1
    return xnew, n
    

def f1(x):
    return x**4+3*x-9

def f2(x) :
    return 3*cos(x)-x-2

def f3(x) :
    return x*exp(x)-7

print("Question 1: Methode de la dichotomie:\n")
print("Equation 1: f(x)=0 avec environ x=",Dichotomie(f1, 1 ,2, 1e-10, 50000),"iterations.")
print("Equation 1: f(x)=0 avec environ x=",Dichotomie(f1, -3 ,-1, 1e-10, 50000),"iterations.\n")

print("Equation 2: f(x)=0 avec environ x=",Dichotomie(f2, 0 ,1, 1e-10, 50000),"iterations.")
print("Equation 2: f(x)=0 avec environ x=",Dichotomie(f2, -1 ,-2, 1e-10, 50000),"iterations.")
print("Equation 2: f(x)=0 avec environ x=",Dichotomie(f2, -3 ,-4, 1e-10, 50000),"iterations.\n")

print("Equation 3: f(x)=0 avec environ x=",Dichotomie(f3, 1 ,2, 1e-10, 50000),"iterations.\n")

print("Question 2: Methode de la secante:\n")
print("Equation 1: f(x)=0 avec environ x=",Secante(f1,3,2,1e-10, 50000),"iterations.")
print("Equation 1: f(x)=0 avec environ x=",Secante(f1,-3,-2,1e-10, 50000),"iterations.\n")

print("Equation 2: f(x)=0 avec environ x=",Secante(f2,2,1,1e-10, 50000),"iterations.")
print("Equation 2: f(x)=0 avec environ x=",Secante(f2,-3,-2,1e-10, 50000),"iterations.")
print("Equation 2: f(x)=0 avec environ x=",Secante(f2,-3,-3.5,1e-10, 50000),"iterations.\n")

print("Equation 3: f(x)=0 avec environ x=",Secante(f3,3,2,1e-10, 50000),"iterations.")
