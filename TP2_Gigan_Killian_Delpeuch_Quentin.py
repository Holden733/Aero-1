import math as m


def g1_1(x) :
    return((9-3*x)**0.25)
def g1_2(x) :
    return-((9-3*x)**0.25)
def g2_1 (x):
    return(m.acos((x+2)/3))
def g2_2 (x):
    return(-(m.acos((x+2)/3)))
def g3 (x):
    return(m.log(7)-m.log(x))
def g4_1 (x):
    return(m.exp(x)-10)
def g4_2 (x):
    return(m.log(x+10))
def g5_2 (x):
    return(m.atan((x+5)/2))
def g6 (x) :
    return (m.log(x**2+3))
def g7 (x) :
    return((-4*m.log(x)+7)/3)
def g8_1 (x):
    return((17-4*x+2*x**2)**0.25)
def g8_2 (x):
    return(-(17-4*x+2*x**2)**0.25)
def g9(x):
    return (m.log(7+2*m.sin(x)))
def g10(x):
    return (m.log(10/(m.log(x**2+4))))


def Point_fixe (g,x0,e,Nitermax):
    xold= x0
    xnew = g(xold)
    difference = xnew - xold
    xold = xnew
    n = 1
    while abs(difference)>e and n< Nitermax :
        xnew = g(xold)
        difference = xnew-xold
        xold = xnew
        n =n+1
    return xnew,n


print("f1+ : ",Point_fixe (g1_1,1.5,1e-3,5e4))
print("f1- : ",Point_fixe (g1_2,-1.5,1e-3,5e4))
print("f2+ : ",Point_fixe (g2_1,0.5,1e-3,5e4))
print("f2- : ",Point_fixe (g2_2,-1.5,1e-3,5e4))
print("f3 : ",Point_fixe (g3,1.5,1e-3,5e4))
print("f4- : ",Point_fixe (g4_1,-9.5,1e-3,5e4))
print("f4+ : ",Point_fixe (g4_2,2.5,1e-3,5e4))
print("f5 : ",Point_fixe (g5_2,1.2,1e-3,5e4))
print("f6 : ",Point_fixe (g6,1.5,1e-3,5e4))
print("f7 : ",Point_fixe (g7,1.6,1e-3,5e4))
print("f8+ : ",Point_fixe (g8_1,2.5,1e-3,5e4))
print("f8- : ",Point_fixe (g8_2,-2.5,1e-3,5e4))
print("f9 : ",Point_fixe (g9,2.25,1e-3,5e4))
print("f10 : ",Point_fixe (g10,1.5,1e-3,5e4))
