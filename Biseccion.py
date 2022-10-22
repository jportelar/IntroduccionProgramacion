#Metodo de Biseccion
import math
import pylab as p
to=1E-5
a1=1.0
b1=2.0
Nmax=30
X=[]
Y=[]
Z=[]
delta=(2.0-1.0)/1000.0
def fun(xo):
    ff=xo**3+4*xo**2-10
    return ff
for j in range(1000):
    xm=a1+(j*delta)
    X.append(xm)
    Y.append(fun(xm))
    Z.append(0)
for i in range(Nmax):
    p1=(a1+b1)/2.0
    print (i, a1, b1, p1, fun(p1), abs(a1-b1))
    if fun(p1)==0 or abs(a1-b1)<to:
        print ('la raiz es', p1)
        break
    elif fun(a1)*fun(p1)<0:
        b1=p1
    else:
        a1=p1
p.plot(X,Y,X,Z)
p.show()
    
        




