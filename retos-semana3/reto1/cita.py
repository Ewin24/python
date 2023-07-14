import datetime
import os
import core


def menu():
    flag = True
    while (flag):
        os.system("clear")
        print("----ADMINISTRACION DE VETERINARIOS----")
        print("1. Agendar cita")
        print("2. Eliminar cita")
        print("3. Buscar cita")
        print("4. Mostrar citas")
        print("5. Regresar")
        opc = int(input(":)_ "))

        if opc == 1:
            addCita()
        if opc == 2:
            core.delete("citas.json")
        if opc == 3:
            core.listId("citas.json")
        if opc == 4:
            core.listAll("citas.json")
        if opc == 5:
            flag = False


def addCita():
    idValid = core.checkId('citas.json')
    if idValid != False:
        print("----AGREGAR CITAS----")
        cita = {
            'id': idValid,
            'fecha': datetime.now(),
        }
        #TODO: VALIDACIONES PARA PERMITIR QUE SE INGRESEN HORA DE CITA, 
        # TAMBIEN PARA RELACIONAR PACIENTES Y VETERINARIOS 
        core.create('citas.json', cita)

    else:
        print("El id ya se encuentra registrado")

def validarHora():
    filename = 'citas.json'

    if (core.checkFile(filename)):
        file = core.loadFile(filename)
        id = input(f"Ingrese el id de {filename[0:-6]}: ")
        for i, item in enumerate(file[filename[0:-5]]):
            ids.append(item['id'])
        if id in ids:
            print(f"El id: {id} ya se encuentra registrado")
            input()
            return False
        else:
            return id