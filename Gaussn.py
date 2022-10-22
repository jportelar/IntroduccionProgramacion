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
            elif l==NE-1:
                print ('el sistema no tiene solucion unica')
                break
################Eliminacion Gaussina hacia abajo#
    if A[k][k]!=0.0:
        for i in range (k+1,NE):
            ai=A[i][k]/A[k][k]
            for j in range (k, NE+1):
                A[i][j]=A[i][j]-ai*A[k][j]
    print ('\n')
###############Si un elemento de la diagonal se hace 0#    
if A[NE-1][NE-1]==0.0:
    print ('el sistema no tiene solucion unica')

##########Eliminacion Gaussiana hacia arriba#
for i in range (NE-1,-1,-1):
    xn=A[i][NE]/A[i][i]
    for j in range (i+1,NE-1):
        xn=xn-((xn*A[i][j])/A[i][i])
    print (xn)
    





