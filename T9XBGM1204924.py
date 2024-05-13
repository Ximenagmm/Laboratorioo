#
#Laboratorio Semana 9 
print("Mediciones de los estudiantes de la URL")
nombre=input("Ingrese su nombre:")
carné=int(input("Ingrese su número de carné:"))
print("Nombre: ",nombre, "No. Carné: ", carné)
print()

medida=int(input("ingrese un valor en metros:"))
milla=(medida/1000)/(1.69)
kilometro=medida/1000
pies=medida*3.28
pulgadas=(medida*3,28)*12
yardas=medida/0.914
metros=medida
print(medida,"metros =",milla,"milla")
print(medida,"metros =",kilometro, "Kilometro")
print(medida,"metros =",pies, "pies")
print(medida, "metros=",pulgadas, "pulgadas")
print(medida, "metros =",yardas, "yardas")
print(medida,"metros=",metros, "metros")
print()

