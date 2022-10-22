import math 
import pylab as p
from ElimGaussSyb.py import ElimGauss

xmin=1.0*math.pi
xmax=6.0*math.pi
npuntos=10
deltax=(xmax-xmin)/float(npuntos-1)
x=[xmin+i*deltax for i in range (npuntos)]
def fun(x):
    f=math.cos(x)
    return f
y=[fun(x[j]) for j in range (npuntos)]