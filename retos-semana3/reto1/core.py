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
'''


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
        jsonObj = json.dumps({filename[0:-5]: [data]}, indent=4)
        file.write(jsonObj)
        file.close()


def loadFile(filename):
    file = open('data/'+filename)
    data = json.load(file)
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
                    jsonObj = json.dumps({filename[0:-5]: dataFile[filename[0:-5]]}, indent=4)
                    file.write(jsonObj)
                    file.close()
                else:
                    print("El usuario cancelo la eliminacion")
            else:
                print(f"Busqueda fallida en: {filename[0:-6]}")
    else:
        print("No se tienen registros aun, no es posible hacer una eliminacion")
    # TODO: HAY QUE TERMINAR LA FUNCION, HAY UN ERROR EN COMO SE ELIMINA EL OBJ EN EL JSON (solved)


def update():
    pass


def listAll(filename):
    dataFile = loadFile(filename)
    print(dataFile)
    # TODO: HACER QUE CADA REGISTRO SE DIVIDA DE MANERA CORRECTA Y QUEDE ORDENADO EN UNA TABLA


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


def checkId(filename):
    bandera = ''
    if (checkFile(filename)):
        file = loadFile(filename)
        id = input(f"Ingrese el id del {filename[0:-6]}: ")
        for i, item in enumerate(file[filename[0:-5]]):
            if id in (item['id']):
                bandera = False
            else:
                bandera = id
        return bandera
    else:
        id = input(f"Ingrese el id del {filename[0:-6]}: ")
        bandera = id
        return bandera
