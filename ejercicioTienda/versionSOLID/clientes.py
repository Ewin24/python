import os
import core

def CreateData(*args):
    return core.LoadInfo("clientes.json")

def mainMenu():
    os.system("clear")
    isCliRun = True
    print('+', '-'*66, '+')
    print("|{:15}{}{:^20}|".format('','ADMINISTRACION DE CLIENTES', ''))
    print('+', '-'*66, '+')
    while(isCliRun):
        print("1. Crear cliente")
        print("2. Buscar cliente")
        print("3. Editar cliente")
        print("4. Regresar menu principal")