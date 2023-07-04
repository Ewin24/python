# Escribe un programa que solicite al usuario ingresar su edad y luego determine si es mayor de edad o
# no utilizando una declaración if. Si la edad es mayor o igual a 18, muestra el mensaje "Eres mayor de
# edad", de lo contrario, muestra el mensaje "Eres menor de edad".

edad = int(input("ingrese su edad: "))
if (edad < 18):
    print("eres menor de edad")
elif (edad < 0):
    print("Edad no valida")
else:
    print("eres mayor de edad")
