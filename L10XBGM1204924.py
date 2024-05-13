print()
print("Semana No. 10 Ejercicio 1")
mes=int(input("Ingrese el número del mes:"))

if mes >12 or mes <1:
    print("Error , el numeor no es válido")
else: 
    if mes==1:
        print("MES: Enero")
    elif mes ==2: 
        print("MES: Febrero")
    elif mes ==3: 
        print("MES: Marzo")
    elif mes ==4: 
        print("Mes: Abril")
    elif mes ==5: 
        print("MES: Mayo")
    elif mes ==6: 
        print("MES: Junio")
    elif mes ==7: 
        print("MES: Julio")
    elif mes ==8: 
        print("MES: Agosto")
    elif mes ==9: 
        print("MES: Septiembre")
    elif mes ==10: 
        print("MES: Octubre")
    elif mes ==11: 
        print("MES: Noviembre")
    else: 
        print("Diciembre")

match(mes):
    case 1: 
        print("MES: Enero")
    case 2: 
        print("MES: Febrero")
    case 3: 
        print("MES: Marzo")
    case 4: 
        print("MES: Abril")
    case 5: 
        print("MES: Mayo")
    case 6: 
        print("MES: Junio")
    case 7: 
        print("MES: Julio")
    case 8: 
        print("MES: Agosto")
    case 9: 
        print("MES: Septiembre")
    case 10: 
        print("MES: Octubre ")
    case 11: 
        print("MES: Noviembre ")
    case 12: 
        print("MES: Diciembre")

print()
print()
print("Semana No. 10: Ejercicio 2")
A=int(input("Ingrese un número mayor que cero (A)"))
B=int(input("Ingrese un numeor mayor que cero (B)"))
C=int(input("Ingrese un numeor mayor que cero (C)"))

if A<0 and B<0 and C<0:
    print("No valido")
else: 
    if A>B:
        if A>C:
            print("A es mayor a Cy B")
        else:
            if A==C:
                print("A es mayor a C y B")
            else:
                print("C es mayor a A y B")
    else:
        if A==B:
            if A>C:
                print("Ay B son mayores  C")
            else:
                if A==C:
                    print("A,By C son iguales")
        else:
            if B>C:
                print("B es mayor a A y C")
            else:
                if B==C:
                    print("By C son mayores a A")
                else : 
                    print("C es mayor a A y B")

print()

print("Semana No. 10: Ejercicio 3")
día= int (input("Ingrese el día de su nacimiento:"))
año= int(input("Ingrese su año de nacimiento"))
mes= int(input("Ingrese el mes en el que nació"))
print()
if (mes == 3 and día >=21) or (mes ==4 and día <= 19):
    signo= "Aries"
elif (mes == 4 and día >=21) or (mes == 5 and día <=20):
    signo= "Tauro" 
elif ( mes == 5 and día >=21) or (mes == 6 and día <= 20):
    signo= "Géminis"
elif (mes == 6 and día >= 21) or (mes == 7 and día <= 22):
    signo= "Cancer"
elif (mes == 7 and día >= 23) or (mes == 8 and día <= 22):
    signo= "Leo"
elif (mes == 8 and día >= 23) or (mes == 9 and día <= 22):
    signo= "Virgo"
elif (mes == 9 and día >= 23) or (mes == 10 and día <= 22):
    signo= "Libra"
elif (mes == 10 and día >= 23) or (mes == 11 and día <= 21):
    signo= "Escorpio"
elif (mes == 11 and día >= 22) or (mes == 12 and día <= 21):
    signo= "Sagitario"
elif (mes == 12 and día >= 22) or (mes == 1 and día <= 19):
    signo= "Capricornio"
elif (mes == 1 and día >= 20) or (mes == 2 and día <= 18):
    signo= "Acuario"
elif (mes == 2 and día >= 19) or (mes == 3 and día <= 20):
    signo= "Piscis"
else:
    signo = "Fecha Invalida"
print (" Tu signo zodiacal es: ", signo)