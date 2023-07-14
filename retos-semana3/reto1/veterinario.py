import os
import core


def menu():
    flag = True
    while (flag):
        os.system("clear")
        print("----ADMINISTRACION DE VETERINARIOS----")
        print("1. Agregar veterinario")
        print("2. Eliminar veterinario")
        print("3. Buscar veterinario")
        print("4. Mostrar veterinarios")
        print("5. Regresar")
        opc = int(input(":)_ "))

        if opc == 1:
            addVaterinario()
        if opc == 2:
            core.delete("veterinarios.json")
        if opc == 3:
            core.listId("veterinarios.json")
        if opc == 4:
            core.listAll("veterinarios.json")
        if opc == 5:
            flag = False


def addVaterinario():
    veterinario = {}
    idValid = core.checkId('veterinarios.json')
    if idValid != False:
        print("----AGREGAR VETERINARIOS----")
        veterinario = {
            'id': idValid,
            'nombre': input("Ingrese nombre del veterinario: "),
            'especialidad': input("Ingrese especialidad del veterinario: "),
            'telefono': int(input("Ingrese telefono del veterinario: "))
        }
        core.create('veterinarios.json', veterinario)

    else:
        print("El id ya se encuentra registrado")
