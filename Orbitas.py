import math
import pylab as p
G=6.67384E-11
Rt=6.378E+6
Mt=5.9722E+24
hmin=20000000.0
hmax=40000000.0
dia=86160
ranh=1001
minimo=10
deltah=(hmax-hmin)/(ranh-1)
def Orbitas(h):
    orbitas =(dia/(2*math.pi))*math.sqrt((G*Mt)/(Rt+h)**3)
    return orbitas
fhand = open('orbitas.out','w')
x=[]
y=[]
z=[]

for i in range (1,ranh):
    he=hmin+(i-1)*deltah
    heorb=Orbitas(he)
    if abs(heorb-1)<minimo:
        altura=he
        minimo=abs(heorb-1)
    x.append(he)
    y.append(heorb)
    z.append(1)
    fhand.write(str(he))
    fhand.write(' ')
    fhand.write(str(heorb))
    fhand.write('\n')
fhand.close()

print('La altura geoestacionaria es',altura,'metros')

p.plot(x,y,x,z)
p.show()


