import random 
print("Semana No. 16: Ejercicio 1")

a=[]
for i in range (10):
    r=random.randint(1,100) 
    a.append(r)

promedio=0
for num in a:
    promedio += num
promedio=promedio/len(a)

print(a)
print("La cantidad de elementos es: ",len(a))
print("El promedio es: ", promedio)
sumap=0
sumai=0
contador=0
for i in range (len(a)):
    if i%2==0:
        sumap+=a[i]
        contador+=1
    else:
        sumai+=a[i]
        contador+=1
print ("La suma par es: ",sumap)
print("La suma impar es:", sumai )

#ejercicio 2 

print("\n semana 16. Ejercicio No 2")
filas= int(input("Ingrese la cantidad de filas: "))
columnas =int(input("Ingrese la cantidad de columnas: "))
B=[[]]
for i in range(filas):
    temporal=[]
    for j in range(columnas):
        r=random.randint(1,100)
        temporal.append(r)
    B.append(temporal)
print(B)
B[0][0]=500
print(B)

#Ejecicio clase 
import random
def NumMayor (arreglo):
    mayor=arreglo[0][0]
    for i in range (len(arreglo )):
        for j in range (len (arreglo[i])):
            if arreglo [i][j]>mayor :
                mayor= arreglo [i][j]
    return mayor 

import random 
def NumMenor(arreglo):
    menor=arreglo[0][0]
    for x in range (len(arreglo) ):
        for s in range (len(arreglo)):
            if arreglo[x][s]<menor:
                menor=arreglo[x][s]




