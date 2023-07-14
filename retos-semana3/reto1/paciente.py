import os
import core


def menu():
    flag = True
    while (flag):
        os.system("clear")
        print("----ADMINISTRACION DE PACIENTES----")
        print("1. Agregar paciente")
        print("2. Eliminar paciente")
        print("3. Buscar paciente")
        print("4. Mostrar pacientes")
        print("5. Regresar")
        opc = int(input(":)_ "))

        if opc == 1:
            addPaciente()
        if opc == 2:
            core.delete("pacientes.json")
        if opc == 3:
            flag = True
        if opc == 4:
            core.listAll("pacientes.json")
        if opc == 5:
            flag = False


def addPaciente():
    paciente = {}
    idValid = core.checkId('pacientes.json')
    if idValid != False:
        print("----AGREGAR PACIENTES----")
        paciente = {
            'id': idValid,
            'nombre': input("Ingrese nombre del paciente: "),
            'edad': int(input("Ingrese edad del paciente: ")),
            'propietario': int(input("Ingrese nombre del propietario: "))
        }
        print("Seleccione un tipo: ")
        tipos = core.listTipo('tipoAnimal.json')
        for i, item in enumerate(tipos):
            print(f"{i + 1 }. {item}")
        tipo = int(input(":)_ "))
        if (tipo in range(1, (len(tipos)) + 1)):
            paciente.update({'tipo': tipo})

            print("Seleccione la raza: ")
            razas = core.listRaza(tipos[tipo-1], 'tipoAnimal.json')
            for k, item2 in enumerate(razas):
                print(f"{k + 1 }. {item2}")
            raza = int(input(":)_ "))
            if (raza in range(1, (len(razas)) + 1)):
                paciente.update({'raza': raza})
                core.create('pacientes.json', paciente)
            else:
                print("La raza no fue encontrada")
        else:
            print("No se encontro su tipo de animal")
        # en caso de agregar mas animales y tipos en el json
        # se debe optimizar este codigo para buscar de forma mas facil
    else:
        print("El id ya se encuentra registrado")
