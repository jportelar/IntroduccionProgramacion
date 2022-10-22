import math
import pylab as p
import sys
gr=int(sys.argv[1])
xmin=-2.2*math.pi
xmax=2.2*math.pi
npuntos=20
deltax=(xmax-xmin)/float(gr-1)
Max=1E-36
x=[]
y=[]
z=[]
def Sen(x):
    sen=math.sin(x)
    return sen

def Factorial(N):
    factorial=1
    for i in range(2,N+1):
        factorial*=i
    return factorial

def SenTaylor(u):
    mn=0.0
    for j in range (0,npuntos+1):
        mn=mn+(-1)**j*u**(2*j+1)/Factorial(2*j+1)
    return mn

for i in range (0,gr+1):
    xn=(xmin+deltax*float(i))
    x.append(xn)

for k in x:
    Senx=SenTaylor(k)
    y.append(Senx)

for m in x:
    xdes=abs(SenTaylor(m)-Sen(m))
    if  abs(SenTaylor(m)-Sen(m))>Max:
        n=xdes
        Max=n
print (Max)
print (y)

p.plot(x,y)
p.show()
 


   



        

    

    

