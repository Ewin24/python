# Crea un programa que solicite al usuario ingresar una contraseña y verifique si
# cumple con los siguientes requisitos: debe tener al menos 8 caracteres y contener al
# menos un número. Si la contraseña cumple con los requisitos, muestra el mensaje
# "Contraseña válida". De lo contrario, muestra el mensaje "Contraseña inválida".

caracteres = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
clave = input("Ingrese una contraseña:")
if len(clave) < 8:
    print("Contraseña inválida")
for x in clave:
    if (x in caracteres):
        print("Contraseña valida")
        break
    else:
        print("Contraseña inválida, falta numero")


