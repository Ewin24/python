# Campus requiere administrar algunos datos de sus Campers como por ejemplo, la creación,
# eliminación o búsqueda de los developers, entre otros, por tal razón, ha solicitado el diseño de
# un programa que cuente con el siguiente menú como panel de control:
# 1. CREAR GRUPO ARTEMIS
# 1.1   LISTAR CAMPERS DE ARTEMIS
# 1.2   AGREGAR CAMPERS DE ARTEMIS
# 1.3   ELIMINAR CAMPERS DE ARTEMIS
# 1.4   ORDENAR CAMPERS DE ARTEMIS
# 1.5   BUSCAR CAMPERS DE ARTEMIS
# 2. LISTAR CAMPERS DE SPUTNIK
# 2.1   lISTAR CAMPERS DE SPUTNIK
# 2.2   AGREGAR CAMPERS DE SPUTNIK
# 2.3   ELIMINAR CAMPERS DE SPUTNIK
# 2.4   ORDENAR CAMPERS DE SPUTNIK
# 2.5   BUSCAR CAMPERS DE SPUTNIK
# Digite su opcion:


artemisC = []
sputnikC = []
opc = 0
flag = True

while flag:
    print('\n||||||||||||||||||||||||||||||||||')
    print('||PROGRAMA DE GESTION DE CAMPERS||')
    print('||||||||||||||||||||||||||||||||||\n')
    print('1. CREAR GRUPO ARTEMIS', '1.1   LISTAR CAMPERS DE ARTEMIS', '1.2   AGREGAR CAMPERS DE ARTEMIS', '1.3   ELIMINAR CAMPERS DE ARTEMIS', '1.4   ORDENAR CAMPERS DE ARTEMIS', '1.5   BUSCAR CAMPERS DE ARTEMIS',
          '\n2. CREAR GRUPO SPUTNIK', '2.1  lISTAR CAMPERS DE SPUTNIK', '2.2   AGREGAR CAMPERS DE SPUTNIK', '2.3   ELIMINAR CAMPERS DE SPUTNIK', '2.4   ORDENAR CAMPERS DE SPUTNIK', '2.5   BUSCAR CAMPERS DE SPUTNIK', sep="\n")
    print("0. SALIR \n")
    opc = input("Ingrese la opcion seleccionada: ")
    if (opc == '1'):
        print("Se creo el grupo de artemis correctamente")
    if (opc == '1.1'):
        if (len(artemisC) == 0):
            print("No hay estudiantes registrados")
        for i in artemisC:
            print(f"Estudiante: {i}")
    if (opc == '1.2'):
        name = input("Digite el nombre del camper que desea ingresar: ")
        if name == "":
            print("No se admiten nombres vacios.")
        else:
            artemisC.append(name)
            print("Se creo el inserto correctamente")
    if (opc == '1.3'):
        name = input("Digite el nombre del camper que desea eliminar: ")
        if name == "":
            print("No se admiten nombres vacios.")
        else:
            index = artemisC.index(name.lower())
            artemisC.remove(index)
            print("Se elimino correctamente correctamente")
    if (opc == '1.4'):
        artemisC.sort()
        for i in artemisC:
            print(f"Estudiante: {i}")
    if (opc == 1.5):
        name = input("Digite el nombre del camper que desea buscar: ")
        if name == "":
            print("No se admiten nombres vacios.")
        else:
            index = artemisC.index(name.lower())
            if index > -1:
                print("Se encontro en la lista de artemis")
            else:
                print("No se encontro en la lista de artemis")
# parte 2

    if (opc == '2'):
        print("Se creo el grupo de sputnik correctamente")
    if (opc == '2.1'):
        if (len(sputnikC) == 0):
            print("No hay estudiantes registrados")
        for i in sputnikC:
            print(f"Estudiante: {i}")
    if (opc == '2.2'):
        name = input("Digite el nombre del camper que desea ingresar: ")
        if name == "":
            print("No se admiten nombres vacios.")
        else:
            sputnikC.append(name)
            print("Se creo el inserto correctamente")
    if (opc == '2.3'):
        name = input("Digite el nombre del camper que desea eliminar: ")
        if name == "":
            print("No se admiten nombres vacios.")
        else:
            index = sputnikC.index(name.lower())
            sputnikC.remove(index)
            print("Se elimino correctamente correctamente")
    if (opc == '2.4'):
        sputnikC.sort()
        for i in sputnikC:
            print(f"Estudiante: {i}")
    if (opc == 1.5):
        name = input("Digite el nombre del camper que desea buscar: ")
        if name == "":
            print("No se admiten nombres vacios.")
        else:
            index = sputnikC.index(name.lower())
            if index > -1:
                print("Se encontro en la lista de sputnik")
            else:
                print("No se encontro en la lista de sputnik")
    if (opc == 0 or opc == 0.0):
        flag = False
