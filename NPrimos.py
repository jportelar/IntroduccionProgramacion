import sys
n=int(sys.argv[1])
a=[]
contador=0

print ('Los numeros primos menores que',n,'son:')

for i in range(2,n+1):
    kk=0
    if i%2==0:
        nlim=i//2
    else:
        nlim=(i-1)//2
    for j in range(2,nlim+1):
        contador=contador+1
        if i%j==0:
            kk=kk+1
            break
    if kk==0:
        a.append(i)

print (a)

print ('El numero de operaciones fue:',contador)
        
