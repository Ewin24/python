# Escribir un programa que solicite al usuario ingresar un número entero y determine si es positivo,
# negativo o cero. Imprimir un mensaje correspondiente para cada caso.

n = int(input("Ingrese un número: "))
if n > 0:
    print("El número es positivo")
elif n < 0:
    print("El número es negativo")
else: 
    print("El número es cero")


