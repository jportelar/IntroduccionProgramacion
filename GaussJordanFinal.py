import math
E1=[1.0,1.0,0.0,3.0,4.0]
E2=[2.0,1.0,-1.0,1.0,1.0]
E3=[3.0,-1.0,-1.0,2.0,-3.0]
E4=[-1.0,2.0,3.0,-1.0,4.0]

A=[E1,E2,E3,E4]

NE=len(A)
#################recorrido por la diagonal principal#
for k in range (NE):
################Para pinta cada vector#    
    for t in range (NE):
        print (A[t])
################Revisar en la diagonal principal#    
    if A[k][k]==0:
        for l in range (k+1,NE):
            if A[l][k] !=0:
                AUX=A[k]
                A[k]=A[l]
                A[l]=AUX
                print (k, 'cambia por', l)
                break
            elif l==NE-1:
                print ('el sistema no tiene solucion unica')
                break
################Eliminacion Gaussina hacia abajo#
    if A[k][k]!=0.0:
        for i in range (NE):
            ai=A[i][k]/float(A[k][k])
            for j in range (k, NE+1):
                A[i][j]=A[i][j]-ai*A[k][j]
    print ('\n')
###############Si un elemento de la diagonal se hace 0#    
if A[NE-1][NE-1]==0.0:
    print ('el sistema no tiene solucion unica')

##########Eliminacion Gaussiana hacia arriba#
x=[0.0 for i in range(NE)]
for i in range (NE-1,-1,-1):
    sume=0.0
    for j in range (i,NE):
        sume+=A[i][j]*x[j]
    x[i]=(A[i][NE]-sume)/A[i][i]

for m in range(1,NE+1):
    print ('x',m,'=',x[m-1])
                                                                
                      
