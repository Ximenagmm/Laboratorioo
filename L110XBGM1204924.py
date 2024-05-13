#Ximena Girón 1204924
print()
n2=int(input("Ingrese un número mayor a 0:"))
if (n2<=0):
    print("El valor ingresado debe ser mayor a 0")
#A 
    calculoA =0 
    for xA in range (1, n2 + 1):
        calculoA +=1/ xA
        print ("El resultado de A es ", calculoA)
print()
#B 
calculoB= 0
for xB in range (1,n2+1):
    calculoB += 1/(2**xB)
    print ("El resultado de B es" ,calculoB)
print()
#C
x= int(input("Ingrese un número entero positivo para x: "))
a= int(input("Ingrese un número entero positiv para a: "))
calculoC =0 
for xC in range (1, n2 + 1):
    calculoC += x* (xC) * a* (n2-xC)
    print("El resultado de C es", calculoC)



