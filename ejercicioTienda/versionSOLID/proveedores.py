import core
import os


def CreateData(*args):
    core.crearInfo(args)


def mainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+', '-'*55, '+')
    print("|{:^16}{}{:^15}|".format(' ', 'ADMINISTRACION DE PROVEEDORES', ' '))
    print('+', '-'*55, '+')

    print("1. Crear proveedores")
    print("2. Buscar proveedores")
    print("3. Editar proveedores")
    print("4. Eliminar proveedores")
    print("5. Regresar menu principal")
    opcion = int(input(":)_"))
    if (opcion == 1):
        pass
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        mainMenu()
