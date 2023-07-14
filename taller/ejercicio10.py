# Crea un programa que solicite al usuario ingresar tres longitudes y determine si esas longitudes pueden formar un
# triángulo válido. Utiliza la desigualdad triangular para realizar la comprobación y muestra un mensaje indicando si se
# puede formar un triángulo o no.

print("Comprobemos si puedes crear un triangulo valido, ingresa 3 valores (uno para cada lado)")
x = int(input("lado 1: "))
y = int(input("lado 2: "))
z = int(input("lado 3: "))

if (x + y > z and z + y > x and z + x > y):
    print("Tu triangulo es valido")
else:
    print("Tu triangulo no es valido")

