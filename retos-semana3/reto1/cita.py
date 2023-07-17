from datetime import datetime
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
    filePaciente = 'pacientes.json'
    fileVeterinario = 'veterinarios.json'
    filename = 'citas.json'
    idValid = core.checkId(filename)
    if idValid != False:
        print("----AGREGAR CITAS----")
        cita = {
            'id': idValid,
            'fecha': datetime.now(),
        }
        # relacionar id de paciente
        dataFile = core.loadFile(filePaciente)
        id = input(f"Inserte el id de {filePaciente[0:-6]}: ")
        for i, item in enumerate(dataFile[filePaciente[0:-5]]):
            if id in (item['id']):
                print(
                    f"El paciente de la cita sera: {dataFile[filePaciente[0:-5]][i]}")
                cita.update({'idPaciente': id})
                input()
            else:
                print(f"No se encontro el id de: {filePaciente[0:-6]}")

        # relacionar el id de veterinario a la cita
        dataFile = core.loadFile(fileVeterinario)
        id = input(f"Inserte el id de {fileVeterinario[0:-6]}: ")
        for i, item in enumerate(dataFile[fileVeterinario[0:-5]]):
            if id in (item['id']):
                print(
                    f"El veterinario de la cita sera: {dataFile[fileVeterinario[0:-5]][i]}")
                cita.update({'idVeterinario': id})
                input()
            else:
                print(f"No se encontro el id de: {fileVeterinario[0:-6]}")

        # relacionar hora y fecha de cita
        validarHora()
        core.create('citas.json', cita)

    else:
        print("El id ya se encuentra registrado")


def validarHora():
    # TODO: VALIDACIONES PARA PERMITIR QUE SE INGRESE HORA DE CITA,
    # validar dias ocupados
    # validar horas ocupadas en el dia

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
    else:
        while True:
            fecha_str = input('\n Ingrese fecha "aaaa/mm/dd"...: ')
            try:
                fechaIni = datetime.today()
                fechaFin = datetime.strptime(fecha_str, '%Y/%m/%d')
                diff = fechaFin - fechaIni
                if((diff.days) > 5):
                    hora = input("Ingrese un rango de horas en formato 24h, tener en cuenta que cada cita dura 1na hora")
                    
                    print(str(fecha))
            except ValueError:
                print("\n No ha ingresado una fecha correcta...")
            else:
                break
                fecha = input(
                    "Ingrese la fecha en un rango de los proximos 5 dias")
