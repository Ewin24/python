import core
import os

dicCliente = {'data': []}

def mainMenu():
    os.system("clear")
    isCliRun = True

    os.system("clear")
    print('+', '-'*55, '+')
    print("|{:^16}{}{:^15}|".format(' ', 'ADMINISTRACION DE CLIENTES', ' '))
    print('+', '-'*55, '+')

    print("1. Crear cliente")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Regresar menu principal")
    opcion = int(input(":)_"))
    if (opcion == 1):
        data = {
            "id": input("Ingrese el Id del cliente: "),
            "nombre": input("Ingrese el Nombre del cliente: "),
            "email": input("Ingrese el Email del cliente: ")
        }
        if (core.checkFile("clientes.json") == False):
            dicCliente["data"].append()
        core.crearInfo("clientes.json",data)
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        isCliRun = False

    if (isCliRun):
        mainMenu()
