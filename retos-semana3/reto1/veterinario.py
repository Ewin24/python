import os
import core


def menu():
    flag = True
    while (flag):
        os.system("clear")
        print("----ADMINISTRACION DE VETERINARIOS----")
        print("1. Agregar veterinario")
        print("2. Editar veterinario")
        print("3. Buscar veterinario")
        print("4. Mostrar veterinarios")
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
