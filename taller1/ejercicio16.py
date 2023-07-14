# Crea un programa que solicite al usuario ingresar una serie de números positivos y luego calcule e imprima el promedio
# de los números ingresados utilizando un bucle while. El programa debe terminar cuando el usuario ingrese un número
# negativo.

flag = True
lista = []
promedio = 0
while flag:
    n = int(input('Ingrese un numero a la serie :'))
    if n < 1:
        flag = False
    else:
        lista.append(n)
        
for i in lista:
    promedio += i

promedio /= len(lista)
print(f"El promedio de los numeros ingresados es: {promedio}")
