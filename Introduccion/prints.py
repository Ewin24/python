import datetime

#declaracion de variables
variable_num = 3
variable_texto = 'hola'

#metodos de pintado consola
print("hola " + variable_texto)
print(f"hola {variable_texto}")

#peticion de valores en cconsola
name = input("ingrese su nombre: ")
print(variable_texto + " " + name)

#casteos
peso = float(input("Escriba su peso: "))
print(peso)
edad = int(input("escriba su edad: "))
print(edad)

#ejercicios
print("---programa para calcular cubos y cuadrados---")
num = int(input("ingrese el numero a evaluar: "))
print(f"Su numero base es: {num} \n cuadrado: {num * num} \n cubo: {num * num * num}")

print("---programa para calcular diferenci de edad---")
nom = input("Ingrese su nombre: ")
edad_i = int(input("Ingrese su edad: "))
edad_mia = 34
print(f"soy mayor que tu: {edad_mia - edad_i} años")

print("---programa para obtener tu edad actual---")
nacimiento = int(input("Ingrese su año de nacimiento: "))
fecha_actual = datetime.datetime.now().year
print(f"Su edad actual es: {fecha_actual - nacimiento} ")