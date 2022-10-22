import math
import pylab as p

xmin=math.pi
xmax=4.0*math.pi
npuntos=30
deltax=(xmax-xmin)/float(npuntos-1)
xx=[xmin+i*deltax for i in range (npuntos)]
def fun(x):
    fx=math.cos(2.0*x)
    return fx
funcion=[fun(xx[j]) for j in range (npuntos)]

def inter(x):
    pol=0.0
    for k in range (npuntos):
        num=1.0
        den=1.0
        for n in range (npuntos):
            if n!=k:
                num*=(x-xx[n])
                den*=(xx[k]-xx[n])
        pol+=fun(xx[k])*(num/den)
    return pol 

npuntos2=300
deltax2=(xmax-xmin)/float(npuntos2-1)
xx2=[xmin+m*deltax2 for m in range(npuntos2)]
interpollag=[inter(xx2[l]) for l in range(npuntos2)]

p.plot(xx2,interpollag,'*y',xx,funcion,'+r')
p.show()

