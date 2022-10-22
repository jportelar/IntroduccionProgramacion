import math
E1=[1.0, -1.0, 2.0, -1.0]
E2=[1.0, 1.0, 1.0, 0.0]
E3=[2.0, -2.0, 3.0, -3.0]
E4=[1.0, -1.0, 4.0, 3.0]
b1=[8.0, 7.0, 14.0, -7.0]
b2=[9.0, 6.0, 12.0, -5.0]
b3=[-8.0, -2.0, -20.0, 4.0]

A=[E1,E2,E3,E4]
U=[]
L=[]
NE=len(A)
MD=0
##################Para obtener la matriz triangular superior#
for k in range (NE):
    if A[k][k]!=0.0:
        for i in range (k+1,NE):
            ai=A[i][k]/A[k][k]
            for j in range (k, NE):
                A[i][j]=A[i][j]-ai*A[k][j]
print ('U=')
for t in range(NE):
    U.append(A[t])
    print (U[t])
print ('\n')
            
###################Para obtener la matriz triuangular inferior#
for q in range(NE-1,-1,-1):
    for f in range(NE):
        print (A[f])
    if A[q][q]!=0.0:
        for r in range (q-1,-1,-1):
            bi=A[r][q]/A[q][q]
            MD=MD+1
            for s in range (NE,q-1,-1):
                A[r][s]=A[r][s]-bi*A[q][s]
                SR=SR+1
                MD=MD+1
    print ('\n')


    
