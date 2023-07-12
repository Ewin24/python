import core


def addCamper(dataCamper):
    camper = ''
    if (not core.checkFile('campers.json')):
        core.crearInfo('campers.json', dataCamper)

    print('+', '-'*55, '+')
    print("|{:^20}{}{:^23}|".format(' ', 'Agregar Camper', ' '))
    print('+', '-'*55, '+')

    camper = {
        'id': int(input("Ingrese la identificacion del camper: ")),
        'nombre': input("Ingrese el nombre o nombres del camper: "),
        'apellidos': input("Ingrese los apellidos del camper: "),
        'edad': int(input("Ingrese la edad del camper: ")),
        'correo': input("Ingrese el correo del camper: "),
        'ciudad': input("Ingrese la ciudad del camper: "),
        'estadoC': input("Ingrese el estado civil del camper: "),
        'genero': input("Ingrese el genero del camper: "),
        'nroTelefono': input("Ingrese el numero de telefono del camper: "),
    }

    if (camper['edad'] < 18):
        print("-----Camper menor de edad, diligenciar acudiente-----")
        idA = int(input("Ingrese la identificacion del acudiente: "))
        nombreA = int(input("Ingrese el nombre o nombres del acudiente: "))
        apellidoA = int(input("Ingrese el apellido del acudiente: "))
        parentescoA = int(input("Ingrese el parentesco del acudiente: "))

        acudiente = {
            'idA': idA,
            'nombreA': nombreA,
            'apellidoA': apellidoA,
            'parentescoA': parentescoA
        }

        camper.update({'acudiente': acudiente})
        core.crearInfo('campers.json', camper)  # 0 nombre, 1 datos
    elif (camper['edad'] > 18):
        core.crearInfo('campers.json', camper)  # 0 nombre, 1 datos
    else:
        print("Las edades no son validas")


def editCamper():
    camper = core.LoadInfo('campers.json')


def deleteCamper():
    pass


def listCamper():
    pass


def listCampers():
    pass
