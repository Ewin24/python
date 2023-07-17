import json
import os

'''
-----------------------------------------------------------------
###    Instrucciones de uso    ###
-----------------------------------------------------------------
filename[0:-6] : 

Lo que indica es el nombre del archivo con el que se trabaja, 
de esta forma es posible que sea generico

error : 'paciente'
Es generado cuando se busca mal la llave del json, puesto que 
alli es llamado 'pacientes', esto por el corte de cadena ej:
filename[0:-6] = 'paciente'
filename[0:-5] = 'pacientes'
filename[0:-4] = 'pacientes.'
-----------------------------------------------------------------
listRaza, listTipo:

Funcionan unicamente con pacientes, son genericos, por lo que
van a funcionar con cualquier modificacion den el tipoAnimal.json
-----------------------------------------------------------------
input():

se usan para frenar programa, 
en windows se puede usar: os.system('pause')
en linux se puede usar: time.sleep()
-----------------------------------------------------------------
'''


def create(filename, data: dict):
    if (checkFile(filename)):
        # cargamos los nuevos datos a los que ya estan
        fileExist = loadFile(filename)
        fileExist[filename[0:-5]].append(data)
        # volvemos a subir los datos antiguos con actualizacion
        file = open('data/'+filename, 'w')
        jsonObj = json.dumps(fileExist, indent=4)
        file.write(jsonObj)
        file.close()
    else:
        file = open('data/'+filename, 'w')
        jsonObj = json.dumps({filename[0:-5]: [data]}, indent=4)
        file.write(jsonObj)
        file.close()


def loadFile(filename):
    file = open('data/'+filename)
    data = json.load(file)
    file.close()
    return data


def delete(filename):
    if (checkFile(filename)):
        dataFile = loadFile(filename)
        id = input(f"Ingrese el id del {filename[0:-6]}: ")
        for i, item in enumerate(dataFile[filename[0:-5]]):
            if id in (item['id']):
                print(dataFile[filename[0:-5]][i])
                if (bool("Confirmar la eliminacion (Enter) cancelar, (S) confirmar: ")):
                    dataFile[filename[0:-5]].pop(i)
                    file = open('data/'+filename, 'w')
                    jsonObj = json.dumps(
                        {filename[0:-5]: dataFile[filename[0:-5]]}, indent=4)
                    file.write(jsonObj)
                    file.close()
                else:
                    print("El usuario cancelo la eliminacion")
            else:
                print(f"Busqueda fallida en: {filename[0:-6]}")
    else:
        print("No se tienen registros aun, no es posible hacer una eliminacion")


def update():
    pass


def listAll(filename):

    if (checkFile(filename)):
        dataFile = loadFile(filename)
        for i, item in enumerate(dataFile[filename[0:-5]]):
            print(f"{'Id': <10}{'Nombre': <15}")
            print(f"{item['id']:<10}{item['nombre']}")
            print(f"----------------")
        input()
    else:
        print(f"No se encontraron {filename[0:-5]}")


def listId(filename):
    dataFile = loadFile(filename)
    id = input(f"Inserte el id de {filename[0:-6]}: ")
    for i, item in enumerate(dataFile[filename[0:-5]]):
        if id in (item['id']):
            print(dataFile[filename[0:-5]][i])
            input()
        else:
            print(f"Busqueda fallida en: {filename[0:-6]}")


def listRaza(tipo, filename):
    # listamos las razas que se encuentran relacionadad a ese tipo
    file = open('data/'+filename)
    data = json.load(file)
    file.close()
    # retorna una lista con las razas
    return list(data[tipo]['razas'])


def listTipo(filename):
    file = open('data/'+filename)
    data = json.load(file)
    file.close()
    # retorna una lista con las razas
    return list(data.keys())


def checkFile(fileName):
    try:
        with open('data/'+fileName, 'r') as f:
            return True
    except FileNotFoundError as e:
        print("Errr")
        return False
    except IOError as e:
        return False


def checkId(filename):
    ids = []
    if (checkFile(filename)):
        file = loadFile(filename)
        id = input(f"Ingrese el id del {filename[0:-6]}: ")
        for i, item in enumerate(file[filename[0:-5]]):
            ids.append(item['id'])
        if id in ids:
            print(f"El id: {id} ya se encuentra registrado")
            input()
            return False
        else:
            return id
