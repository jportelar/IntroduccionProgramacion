import math
import pylab as p
xm=1.5
N=1
Nmax=30
tol=1.0e-5
def ga(x):
    g1=x-(x**3)-(4*x**2)+10
    return g1
def dga(x):
    dg1=1-3*x**2-8*x
    return dg1
def gb(x):
    g2=math.sqrt(abs((10/x)-(4*x)))
    return g2
def dgb(x):
    dg2=0.5*((abs((10/x)-(4*x)))**(-0.5))*((-10/x**2)*4)
    return dg2
def gc(x):
    g3=(math.sqrt(10-x**3))/2
    return g3
def dgc(x):
    dg3=(0.25)*((10-x**3)**(-0.5))*-3*x**2
    return dg3
def gd(x):
    g4=math.sqrt(10/(4+x))
    return g4
def dgd(x):
    dg4=-(5/(4+x)**2)*((10/(4+x))**(-0.5))
    return dg4
def ge(x):
    g5=x-((x**3+4*x**2-10)/(3*x**2+8*x))
    return g5
def dge(x):
    dg5=((6*x+8)*((x**3)+(4*x**2)-10))/(((3*x**2)+(8*x))**2)
    return dg5

while N<=Nmax:
    xmi=gc(xm)
    print (N,xm,xmi,dgc(xm))
    if abs(xmi-xm)<tol:
        print ('El punto fijo corresponde a', xmi) 
        break
    elif N==Nmax:
        print ('El punto fijo no convergido corresponde a', xmi)
    N=N+1
    xm=xmi
