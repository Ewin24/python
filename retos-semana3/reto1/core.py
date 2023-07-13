import json
import os


def create(filename, data: dict):
    if (checkFile(filename)):
        # cargamos los nuevos datos a los que ya estan

        fileExist = loadFile(filename)
        fileExist['pacientes'].append(data)
        # volvemos a subir los datos antiguos con actualizacion
        file = open('data/'+filename, 'w')
        jsonObj = json.dumps(fileExist, indent=4)
        file.write(jsonObj)
        file.close()
    else:
        file = open('data/'+filename, 'w')
        # ponemos el mismo nombre que se mande y quitamos .json
        jsonObj = json.dumps({filename[0:-5]: [data]}, indent=4)
        file.write(jsonObj)
        file.close()


def loadFile(filename):
    file = open('data/'+filename)
    data = json.load(file)
    return data


def delete(filename, id):
    dataFile = loadFile(filename)
    itemI = -1
    for i, item in dataFile:
        if item['id'] == id:
            print(f"Busqueda exitosa en: {filename}")
            itemI = i
    if (itemI == -1):
        print(f"Busqueda fallida en: {filename}")
    else:
        if (bool("Confirmar la eliminacion (Enter) cancelar, (S) confirmar: " + dataFile[itemI]) == False):
            dataFile[itemI].pop(itemI)
            create(filename, dataFile)
        else:
            print("El usuario cancelo la eliminacion")


def update():
    pass


def listAll(filename):
    dataFile = loadFile(filename)
    print(dataFile)


def listById():
    pass


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


def checkId(filename, id):
    bandera = True
    file = loadFile(filename)
    for i, item in enumerate(file):
        if id in (item['id']):
            print(f"El id {id} ya se encuentra registrado")
            return False
        else:
            for i, item in enumerate(file):
                if id in (item['id']):
                    print(f"El id {id} ya se encuentra registrado")
                    return False
