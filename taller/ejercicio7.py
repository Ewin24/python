# Escribe un programa que solicite al usuario ingresar una contraseña y verifique si es correcta. Si la contraseña
# ingresada es "secreto123", muestra el mensaje "Acceso concedido". Si la contraseña es diferente, muestra el
# mensaje "Acceso denegado".

clave = input("Ingrese la contraseña: ")
if clave == "secreto123":
    print("Acceso concedido")
else:
    print("Acceso denegado")
    