import math


def menu():
 print("Elija uma opción : ")
 print(" a . Área de triángulo ")
 print(" b . Área de cuadrado ")
 print(" c . Área de recángulo ")
 print(" d . Área de circulo ")
opcion= input()
def ObtenerAreaTriangulo(base,altura):
  area= (base*altura)/2
  return (area)

def ObtenerAreaCuadrado(lado):
  #area= (lado*2)
  area2= lado**2 
  return (area2)

def ObtenerAreaRectangulo(base,altura):
  #area= (base*altura)
  return (base*altura)

def ObtenerAreaCirculo(radio):
  area4= math.pi *radio 
  return area4 

#Area de interacción con el usuario 
print("Semana No. 15 - ejercicio 1")
match menu(()):
  case "a":
    print ("El area del triangulo es: " , ObtenerAreaTriangulo(float(input( "Ingrese la base del triangulo:  "))))(float (input ("Ingrese la altura del triangulo ")))
  case"b": 
    print ("El area del cuadrado es: " , ObtenerAreaCuadrado(float(input( "Ingrese el lado del cuadrado:  "))))
  case "c":
    print("El area del recangulo es: " , ObtenerAreaRectangulo(float(input( "Ingrese la base del rectangulo:  "))))(float (input ("Ingrese la altura del rectangulo  ")))
  case "d":
    print("El area del rectangulo es: " , round( ObtenerAreaCirculo(float(input( "Ingrese el radio del circulo:  ")))))
          

print (int("Ingrese una coordenada"))

def menu():
  print("seleccione una opcion ")
  print("a. sube ")
  print("b. baja ")
  print("c. izquierda ") 
  print("d. derecha ")
opcion= input()

def MoverArriba ():
  global y 
  y+1

def MoverAbajo ():
  global y 
  y-1

def MoveraIzquierda ():
  global x
  x-1 

def MoverDerecha ():
  global x 
  x+1

print("Semana No. 12 ejercicio 2")
match menu(()):
  case "a":
    print (" sube : ", MoverArriba(float(input( "Ingrese cuantas cantidades desea que corra hacia arriba :  ")))) 
  case "b":
    print (" baja : ", MoverAbajo(float(input( "Ingrese cuantas cantidades desea que corra hacia abajo :  ")))) 
  case "c":
    print (" va hacia la izuierda: ",MoveraIzquierda(float(input( "Ingrese cuantas cantidades desea que corra hacia la izquierda :  ")))) 
  case "d":
    print (" va hacia la derecha : ", MoverDerecha(float(input( "Ingrese cuantas cantidades desea que corra hacia la derecha :  ")))) 
