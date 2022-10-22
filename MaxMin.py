import math 
def fun(x,y):
    ff=math.sin(x)*math.cos(x)-math.cos(y/2+math.pi/3)
    return ff
Nx=101
Ny=101
xmin=-math.pi
xmax=math.pi
ymin=-math.pi/2
ymax=math.pi/2
deltax=(xmax-xmin)/(Nx-1)
deltay=(ymax-ymin)/(Ny-1)
minimo=100
maximo=1E-6
Max=[]
Min=[]
for i in range(0,Nx):
    xn=xmin+i*deltax
    for j in range(0,Ny):
        yn=ymin+j*deltay
        m=fun(xn,yn)
        if fun(xn,yn)<minimo:
            minimo=m
            xmini=xn
            ymini=yn
        elif fun(xn,yn)>maximo:
            maximo=m
            xmaxi=xn
            ymaxi=yn
Min.append(xmini)
Min.append(ymini)
Max.append(xmaxi)
Max.append(ymaxi)
print ('La funcion alcanza un valor minimo de',minimo,'en el punto',Min,'y a su vez alcanza un valor maximo de',maximo,'en el punto',Max)
