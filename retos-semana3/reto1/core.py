import json


def create():
    file = open('data/')


def delete():
    pass


def update():
    pass


def listAll():
    pass


def listById():
    pass


def listRaza(tipo, filename):
    # listamos las razas que se encuentran relacionadad a ese tipo
    file = open('data/'+filename)
    data = json.load(file)
    file.close()
    # retorna una lista con las razas
    return list(data[tipo]['razas'])

    pass


def listTipo(filename):
    file = open('data/'+filename)
    data = json.load(file)
    file.close()
    # retorna una lista con las razas
    return list(data.keys())
