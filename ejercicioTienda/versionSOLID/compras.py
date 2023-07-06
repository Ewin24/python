import core
import os


def CreateData(*args):
    core.crearInfo(args)


def mainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+', '-'*55, '+')
    print("|{:^16}{}{:^15}|".format(' ', 'ADMINISTRACION DE COMPRAS', ' '))
    print('+', '-'*55, '+')

    print("1. Crear compra")
    print("2. Buscar compra")
    print("3. Devolucion")
    print("4. Anular Factura compra")
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
