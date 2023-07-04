# Desarrollar un programa que solicite al usuario ingresar un número y determine si es par. Si lo es,
# imprimir el mensaje "El número es par"; de lo contrario, no hacer nada.

n = int(input("Ingrese un número: "))
if n % 2 == 0:
    print("El número es par")