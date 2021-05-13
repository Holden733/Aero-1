"""BOIN Erwan - DELPEUCH Quentin- 1PV2
Analyse numerique - TP4"""

from math import *
import numpy as np
import matplotlib.pyplot as plt


#Fonction pour dicho et secante:
def f1(x):
    return x**4+3*x-9

def f2(x) :
    return 3*cos(x)-x-2

def f3(x) :
    return x*exp(x)-7

#Fonction pour Newton:
def fder1(x) :
    return (4*x**3+3)

def fder2(x) :
    return -3*sin(x)-1

def fder3(x) :
    return exp(x)+x*exp(x)

#Fonction pour Point Fixe:
def g1plus(x):
    return (9-3*x)**0.25
def g1moins(x):
    return -(9-3*x)**0.25

def g2alpha(x):
    return acos((x+2)/3)
def g2beta(x):
    return - (acos((x+2)/3))

def g3(x):
    return log(7/x)

#Fonction exemple question 2:
def g_exemple_PF(x):
    return (1+sin(x))/2
def f_exemple(x):
    return 2*x-(1+sin(x))
def fder_exemple(x):
    return 2-cos(x)


#Fonction methode:
def PointFixe (g, x0, epsilon, Nitermax):
    xold = x0
    xnew = g(xold)
    erreur = xnew - xold
    xold = xnew
    n = 1
    liste_n=[]
    liste_x=[]
    liste_e=[]
    while abs(erreur) > epsilon and n < Nitermax : 
        xnew = g(xold)
        erreur = xnew - xold 
        xold = xnew
        n = n+1
        liste_n.append(n)
        liste_x.append(xold)
        liste_e.append(abs(erreur))
    return xnew, n,liste_n,liste_x, liste_e

def Newton(f,fder, x0, epsilon, Nitermax):
    xold = x0
    xnew = xold-(f(xold)/fder(xold))
    erreur = xnew - xold
    xold = xnew
    n = 1
    liste_n=[]
    liste_x=[]
    liste_e=[]
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = xold-(f(xold)/fder(xold))
        erreur = xnew - xold
        xold = xnew
        n = n + 1
        liste_n.append(n)
        liste_x.append(xold)
        liste_e.append(abs(erreur))
    return xnew, n,liste_n,liste_x, liste_e

def Dichotomie(f,a0,b0,epsilon, Nintermax):
    an=a0
    bn=b0
    n=1
    liste_n=[]
    liste_x=[]
    liste_e=[]
    while abs(bn - an)> epsilon and n<Nintermax:
        m=(an + bn)/2
        if (f(an)*f(m)<=0):
            bn = m
        else:
            an = m
        n=n+1
        liste_n.append(n)
        liste_x.append(an)
        liste_e.append(abs(bn - an))
    return m,n,liste_n,liste_x, liste_e

def Secante(f,x0,x1,epsilon,Nitermax):
    xold2 = x0
    xold = x1
    xnew = xold - ((xold-xold2)*f(xold))/(f(xold)-f(xold2))
    erreur = xnew - xold
    xold = xnew
    n = 1
    liste_n=[]
    liste_x=[]
    liste_e=[]
    while abs(erreur) > epsilon and n < Nitermax:
        xnew = xold - ((xold-xold2)*f(xold))/(f(xold)-f(xold2))
        erreur = xnew - xold
        xold = xnew
        n = n + 1
        liste_n.append(n)
        liste_x.append(xold)
        liste_e.append(abs(erreur))
    return xnew, n,liste_n,liste_x, liste_e

#Solution de la fonction exemple:
print("Methode du Point Fixe:\n")
print("f(x)=0 avec environ x=",PointFixe(g_exemple_PF, 0, 1e-10, 5e4),"iterations.\n")

print("Methode de Newton:\n")
print("f(x)=0 avec environ x=",Newton(f_exemple,fder_exemple, 0, 1e-10, 5e4),"iterations.\n")

print("Methode de dichotomie:\n")
print("f(x)=0 avec environ x=",Dichotomie(f_exemple,0,1, 1e-10, 5e4),"iterations.\n")

print("Methode de la secante:\n")
print("f(x)=0 avec environ x=",Secante(f_exemple,0,1,1e-10, 5e4),"iterations.\n")

#Graphique comparaison des fonctions:
#Graph Point Fixe:
plt.subplot(221)
xnew, n,liste_n,liste_x, liste_e=PointFixe(g1plus, 1.5, 1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'b')

xnew, n,liste_n,liste_x, liste_e=PointFixe(g1moins, -1.5, 1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'g')

xnew, n,liste_n,liste_x, liste_e=PointFixe(g2alpha, 0.3, 1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'r')

xnew, n,liste_n,liste_x, liste_e=PointFixe(g2beta, -1.9, 1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'c')

xnew, n,liste_n,liste_x, liste_e=PointFixe(g3, 1.5, 1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'y')

xnew, n,liste_n,liste_x, liste_e=PointFixe(g_exemple_PF, 0, 1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'k')

plt.title('Methode du Point Fixe', loc='left')
plt.xlabel('Iteration')
plt.ylabel('Erreur')

#Graph Newton:
plt.subplot(222)
xnew, n,liste_n,liste_x, liste_e=Newton(f1,fder1,1.5,1e-10,5e4)
plt.semilogy(liste_n,liste_e,'b')

xnew, n,liste_n,liste_x, liste_e=Newton(f1,fder1,-1.5,1e-10,5e4)
plt.semilogy(liste_n,liste_e,'g')

xnew, n,liste_n,liste_x, liste_e=Newton(f2,fder2,0.3,1e-10,5e4)
plt.semilogy(liste_n,liste_e,'r')

xnew, n,liste_n,liste_x, liste_e=Newton(f2,fder2,-1.9,1e-10,5e4)
plt.semilogy(liste_n,liste_e,'c')

xnew, n,liste_n,liste_x, liste_e=Newton(f2,fder2,-5.3,1e-10,5e4)
plt.semilogy(liste_n,liste_e,'m')

xnew, n,liste_n,liste_x, liste_e=Newton(f3,fder3,1.5,1e-10,5e4)
plt.semilogy(liste_n,liste_e,'y')

xnew, n,liste_n,liste_x, liste_e=Newton(f_exemple,fder_exemple, 0, 1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'k')

plt.title('Methode de Newton', loc='left')
plt.xlabel('Iteration')
plt.ylabel('Erreur')

#Graph Dichotomie:
plt.subplot(223)
xnew, n,liste_n,liste_x, liste_e=Dichotomie(f1, 1 ,2, 1e-10, 50000)
plt.semilogy(liste_n,liste_e,'b')

xnew, n,liste_n,liste_x, liste_e=Dichotomie(f1, -3 ,-1, 1e-10, 50000)
plt.semilogy(liste_n,liste_e,'g')

xnew, n,liste_n,liste_x, liste_e=Dichotomie(f2, 0 ,1, 1e-10, 50000)
plt.semilogy(liste_n,liste_e,'r')

xnew, n,liste_n,liste_x, liste_e=Dichotomie(f2, -1 ,-2, 1e-10, 50000)
plt.semilogy(liste_n,liste_e,'c')

xnew, n,liste_n,liste_x, liste_e=Dichotomie(f2, -3 ,-4, 1e-10, 50000)
plt.semilogy(liste_n,liste_e,'m')

xnew, n,liste_n,liste_x, liste_e=Dichotomie(f3, 1 ,2, 1e-10, 50000)
plt.semilogy(liste_n,liste_e,'y')

xnew, n,liste_n,liste_x, liste_e=Dichotomie(f_exemple,0,1, 1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'k')

plt.title('Methode de Dichotomie', loc='left')
plt.xlabel('Iteration')
plt.ylabel('Erreur')

#Graph Secante:
plt.subplot(224)
xnew, n,liste_n,liste_x, liste_e=Secante(f1,3,2,1e-10, 50000)
plt.semilogy(liste_n,liste_e,'b')

xnew, n,liste_n,liste_x, liste_e=Secante(f1,-3,-2,1e-10, 50000)
plt.semilogy(liste_n,liste_e,'g')

xnew, n,liste_n,liste_x, liste_e=Secante(f2,2,1,1e-10, 50000)
plt.semilogy(liste_n,liste_e,'r')

xnew, n,liste_n,liste_x, liste_e=Secante(f2,-3,-2,1e-10, 50000)
plt.semilogy(liste_n,liste_e,'c')

xnew, n,liste_n,liste_x, liste_e=Secante(f2,-3,-3.5,1e-10, 50000)
plt.semilogy(liste_n,liste_e,'m')

xnew, n,liste_n,liste_x, liste_e=Secante(f3,3,2,1e-10, 50000)
plt.semilogy(liste_n,liste_e,'y')

xnew, n,liste_n,liste_x, liste_e=Secante(f_exemple,0,1,1e-10, 5e4)
plt.semilogy(liste_n,liste_e,'k')

plt.title('Methode de la Secante', loc='left')
plt.xlabel('Iteration')
plt.ylabel('Erreur')
plt.show()
