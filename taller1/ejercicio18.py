# Construya un algoritmo en Python, que permita ingresar la información de un empleado e
# imprima el nombre, los apellidos y la antigüedad. Los datos que se deben solicitar
# son los siguientes:
# *Nombre
# * Teléfono
# *Año de ingreso a la empresa
# *Apellidos
# *Edad.

import datetime

nombre = input("Ingrese el nombre del empleado: ")
apellidos = input("Ingrese los apellidos del empleado: ")
telefono = input("Ingrese el número de teléfono del empleado: ")
fIngreso = int(input("Ingrese el año de ingreso a la empresa: "))
edad = int(input("Ingrese la edad del empleado: "))

fActual = datetime.datetime.now().year

antiguedad = fActual - fIngreso

print("Nombre: ", nombre)
print("Apellidos: ", apellidos)
print("Antigüedad: ", antiguedad, "años")
