"""BOIN Erwan - Delpeuch Quentin - TP3
Ma123 - Methode de Newton"""

from math import * 

#Code Question 1
def Newton(f,fder, x0, epsilon, Nitermax):
    xold = x0
    xnew = xold-(f(xold)/fder(xold))
    erreur = xnew - xold
    xold = xnew
    n = 1
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = xold-(f(xold)/fder(xold))
        erreur = xnew - xold
        xold = xnew
        n = n + 1
    return xnew, n

#Equation 1
def f1(x) :
    return x**4+3*x-9
def fder1(x) :
    return (4*x**3+3)

#Equation 2
def f2(x) :
    return 3*cos(x)-x-2
def fder2(x) :
    return -3*sin(x)-1
#Equation 3
def f3(x) :
    return x*exp(x)-7
def fder3(x) :
    return exp(x)+x*exp(x)
#Equation 4
def f4(x) :
    return exp(x)-x-10
def fder4(x) :
    return exp(x)-1
#Equation 5
def f5(x) :
    return 2*tan(x)-x-5
def fder5(x) :
    return (2/cos(x)**2)-1

#Equation 6
def f6(x) :
    return (exp(x)-x**2-3)
def fder6(x) :
    return (exp(x)-2*x)
#Equation 7
def f7(x) :
    return (3*x+4*log(x)-7)
def fder7(x) :
    return (3+(4/x))
#Equation 8
def f8(x) :
    return (x**4-2*x**2+4*x-17)
def fder8(x) :
    return (4*x**3-4*x+4)
def f81(x) :
    return (x**4-2*x**2+4*x-17)
def fder81(x) :
    return (4*x**3-4*x+4)
#Equation 9
def f9(x) :
    return (exp(x)-2*sin(x)-7)
def fder9(x) :
    return (exp(x)-2*cos(x))
#Equation 10
def f10(x) :
    return (log(x**2+4)*exp(x)-10)
def fder10(x) :
    return ((2*x)/(x**2+4))+log(x**2+4)*exp(x)



print("Equation 1: f(x)=0 avec environ x=",Newton(f1,fder1,1.5,1e-10,5e4),"iterations.")
print("Equation 1: f(x)=0 avec environ x=",Newton(f1,fder1,-1.5,1e-10,5e4),"iterations.\n")

print("Equation 2: f(x)=0 avec environ x=",Newton(f2,fder2,0.3,1e-10,5e4),"iterations.")
print("Equation 2: f(x)=0 avec environ x=",Newton(f2,fder2,-1.9,1e-10,5e4),"iterations.")
print("Equation 2: f(x)=0 avec environ x=",Newton(f2,fder2,-5.3,1e-10,5e4),"iterations.\n")

print("Equation 3: f(x)=0 avec environ x=",Newton(f3,fder3,1.5,1e-10,5e4),"iterations.\n")

print("Equation 4: f(x)=0 avec environ x=",Newton(f4,fder4,2.5,1e-10,5e4),"iterations.")
print("Equation 4: f(x)=0 avec environ x=",Newton(f4,fder4,-9.8,1e-10,5e4),"iterations.\n")

print("Equation 5: f(x)=0 avec environ x=",Newton(f5,fder5,1.5,1e-10,5e4),"iterations.\n")

print("Equation 6: f(x)=0 avec environ x=",Newton(f6,fder6,1,1e-10,5e4),"iterations.\n")
print("Equation 7: f(x)=0 avec environ x=",Newton(f7,fder7,1,1e-10,5e4),"iterations.\n")
print("Equation 8: f(x)=0 avec environ x=",Newton(f8,fder8,2,1e-10,5e4),"iterations.")
print("Equation 8: f(x)=0 avec environ x=",Newton(f81,fder81,-3,1e-10,5e4),"iterations.\n")
print("Equation 9: f(x)=0 avec environ x=",Newton(f9,fder9,2,1e-10,5e4),"iterations.\n")
print("Equation 10: f(x)=0 avec environ x=",Newton(f10,fder10,1,1e-10,5e4),"iterations.")
