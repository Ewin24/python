import json
import os


def create(filename, data):
    file = open('data/'+filename, 'w')
    jsonObj = json.dumps(data, indent=4)
    data = file.write(jsonObj)
    file.close()


def loadFile(filename):
    file = open('data/'+filename)
    data = json.load(file)
    return data

def delete(filename,id):
    dataFile = loadFile(filename)
    itemI = -1
    for i, item in dataFile:
        if item['id'] == id:
            print(f"Busqueda exitosa en: {filename}")
            itemI = i
    if(itemI == -1):
        print(f"Busqueda fallida en: {filename}")
    else:
        if(bool("Confirmar la eliminacion (Enter) cancelar, (S) confirmar: " + dataFile[itemI]) == False):    
            dataFile[itemI].pop(itemI)
            create(filename,dataFile)
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

def checkFile(filename):
    return os.path.exists('data/'+filename)
    