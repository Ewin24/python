import os
import core


def menu():
    flag = True
    while (flag):
        os.system("clear")
        print("----ADMINISTRACION DE CITAS----")
        print("1. Agregar cita")
        print("2. Editar cita")
        print("3. Buscar cita")
        print("4. Mostrar cita")
        print("5. Regresar")
        opc = int(input(":)_ "))

        if opc == 1:
            flag = True
        if opc == 2:
            flag = True
        if opc == 3:
            flag = True
        if opc == 4:
            flag = True
        if opc == 5:
            flag = False