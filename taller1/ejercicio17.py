# Crea un programa que solicite al usuario ingresar un número y luego muestre la suma de los dígitos
# de ese número utilizando un bucle while.
numero = int(input("Ingrese un número: "))  
sumaDigitos = 0
numTemp = numero

while numTemp != 0:
    digito = numTemp % 10  
    sumaDigitos += digito  
    numTemp //= 10 

print("La suma de los dígitos de", numero, "es:", sumaDigitos)
