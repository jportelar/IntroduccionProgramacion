import math
import pylab as p
import sys
t=int(sys.argv[1])
xmin=-1
xmax=1
N=400
deltax=(xmax-xmin)/float(N-1)
x=[]
y=[]
def Factorial(N):
    factorial=1
    for i in range(2,N+1):
        factorial*=i
    return factorial

def Com(n,r):
    c=Factorial(n)/(Factorial(r)*Factorial(n-r))
    return c


def Polinomio(n):
    p=0.0
    for i in range(0,t+1):
        p=p+(1/float(2**t))*(float(Com(t,i)**2))*((n+1)**float(t-i))*((n-1)**i)
    return p
        
f = open('PolinomiodeLegendre.out','w')
for j in range (0,N):
    mn=xmin+j*deltax
    pmn=Polinomio(mn)
    f.write(str(mn))
    f.write(' ')
    f.write(str(pmn))
    f.write('\n')
    x.append(mn)
    y.append(pmn)
f.close()
p.plot(x,y)
p.show()

