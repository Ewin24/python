# Escribe un programa que solicite al usuario ingresar un número y luego muestre la tabla de multiplicar de ese número
# del 1 al 10

x = int(input("Ingrese el numeor del que desea conocer la tabla de multiplicar: "))

for i in range(1, 11, 1):
    print(f"{x} X {i} = {x*i}")
