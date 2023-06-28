# La FIFA desea crear un programa en Python que le permita llevar el registro y control de los equipos
# que van a participar en el mundial femenino sub 20 que se va a desarrollar en Colombia. El torneo
# cuenta con 16 equipos inscritos los cuales están organizados en 4 grupos y cada grupo se encuentra
# asignado a 4 diferentes ciudades de Colombia (Cali, Medellin, Bucaramanga y Bogota). Los equipos
# que participan en el torneo deben realizar el registro de los integrantes al momento de llegar al país,
# los datos que se deben registrar son los siguientes:
# - Plantel de Jugadores
# - Nombre, Nro dorsal, Posición de juego y edad.
# - Plantel Técnico
# - Nombre, cargo, edad
# - Plantel Medico
# - Nombre, especialidad y edad

# La información suministrada anteriormente debe estar agrupada por país de representación. Cada
# equipo por país debe tener el nombre del país que representa y a que grupo pertenece.

# El programa debe se permitir llevar el control de las diferentes estadísticas del torneo. La
# información estadística debe estar organizada de la siguiente forma:
# El programa debe presentar el siguiente menú de opciones:

# 1. Registro de Equipo
# 1.1. Registro de Jugador(es) : Esta opción debe permitir ingresar uno o varios jugadores
# según sea el caso (Uso while)
# 1.2. Registro Cuerpo técnico : Tener en cuenta la observación del punto 1.1.
# 1.2. Registro Cuerpo medico : Tener en cuenta la observación del punto 1.1.
# 2. Registro de fecha : En esta opción el administrador del torneo podrá realizar el registro de cada uno de los
# Partidos jugados. El administrador deberá ingresar la fecha del juego, equipo local , equipo visitante y
# el marcador obtenido en el partido. El programa debe de forma automática identificar el equipo ganador y
# El equipo perdedor y así asignar sumar los partidos jugados, perdidos, empatados y ganados según
# Sea el caso.
# 3. Mostrar tabla de estadísticas : Esta opción el usuario deberá ingresar el grupo a consultar y el programa
# Mostrara la siguiente información.
# 4. Consultar información por equipo : Esta opción permitirá buscar información de un equipo
# Equipo especifico. El usuario deberá ingresar el nombre del equipo a consultar.

# 5. Mostrar equipos clasificados a 8vos: Esta opción permitirá mostrar los 8 equipo clasificados
# a octavos. Los equipos que pasan a octavos son los dos primeros equipos con mayor puntaje.

# 6. Mostrar el listado de jugadores de un equipo : Esta opción permitirá listar los jugadores que se encuentran
# Registrados en un equipo especifico.
# 7. Equipo que mayor cantidad de goles marco por cada grupo. El programa mostrara por cada grupo el nombre
# del equipo que mas goles marco en cada grupo.

# Nota. Cada partido ganado otorga 3ptos al equipo ganador, 1 pto en caso de empate, recuerde que el total
# De puntos de cada equipo se obtiene a partir de los partidos ganados y empatados.


#
# los equipos tienen el formato: [
#                                   ['Colombia',['jose1','manuel1','pepe1'],['jose2','manuel2','pepe2'],['jose3','manuel3','pepe3']]
#                                 , ['Argentina',[jugadores] ,[medicos],[tecnicos],[]]
#                                 , ['Brazucas',[jugadores], [medicos],[tecnicos],[1,1,1,1]]
#                                ]
# nombre[0], juagadores[1], tecnicos[2], medicos[3], fechas[4]
# equipo = ['', juagadores, tecnicos, medicos, fechas]
#
grupo = []
equipo = []
equipos = []
fecha = []

flag = True
while flag:
    print("=== MENU ===")
    print("1. Registro de Equipo")
    print("   1.1. Registro de Jugadores")
    print("   1.2. Registro Cuerpo técnico")
    print("   1.3. Registro Cuerpo medico")
    print("2. Registro de fecha")
    print("3. Mostrar tabla de estadísticas")
    print("4. Consultar información por equipo")
    print("5. Mostrar equipos clasificados a 8vos")
    print("6. Mostrar el listado de jugadores de un equipo")
    print("7. Equipo que mayor cantidad de goles marco por cada grupo")
    print("0. Salir")
    opc = input("Ingrese la opción seleccionada: ")

    if opc == '1':
        if (len(equipos) < 16):
            name = input("Ingrese el nombre del equipo que desea ingresar: ")
            equipo.append(name)
            equipos.append(equipo)
        else:
            print("Unicamente se permiten 16 Equipos")

    if opc == '1.1':
        name = input(
            "Ingrese el nombre del equipo que al que registrara el jugador: ")
        for idx, sublist in enumerate(equipos):
            if sublist[0] == name:
                jugador = []
                jugadorName = input("Ingrese el nombre del jugador: ")
                nroDorsal = int(
                    input("Ingrese el dorsal de jugador en numero: "))
                posicionJuego = input("Posicion que desempeña el jugador: ")
                edad = int(input("Ingrese la edad del jugador: "))
                jugador = [jugadorName, nroDorsal, posicionJuego, edad]
                equipos[idx].append(jugador)
                break
            else:
                print("El equipo no fue encontrado, primero debe crear el equipo")

    if opc == '1.2':
        name = input(
            "Ingrese el nombre del equipo al que registrara el Tecnico: ")
        for idx, sublist in enumerate(equipos):
            if sublist[0] == name:
                tecnico = []
                tecnicoName = input("Ingrese el nombre del tecnico: ")
                cargo = input("Ingrese el cargo del tecnico: ")
                edad = int(input("Ingrese la edad del tecnico: "))
                tecnico = [tecnicoName, cargo, edad]
                equipos[idx].append(tecnico)
                break
            else:
                print("El equipo no fue encontrado, primero debe crear el equipo")

    if opc == '1.3':
        name = input(
            "Ingrese el nombre del equipo al que registrara el Medico: ")
        for idx, sublist in enumerate(equipos):
            if sublist[0] == name:
                tecnico = []
                tecnicoName = input("Ingrese el nombre del tecnico: ")
                cargo = input("Ingrese el cargo del tecnico: ")
                edad = int(input("Ingrese la edad del tecnico: "))
                tecnico = [tecnicoName, cargo, edad]
                equipos[idx].append(tecnico)
                break
            else:
                print("El equipo no fue encontrado, primero debe crear el equipo")

    if opc == '2':
        name = input(
            "Ingrese el nombre del equipo que fue local en la fecha: ")
        for idx, sublist in enumerate(equipos):
            equipoLocal = ''
            fechaLocal = []
            fechaVisitante = []
            if sublist[idx] == name:
                ganadosV, ganadosL, perdidosV, perdidosL,  empateV, empateL = 0, 0, 0, 0, 0, 0
                # TODO: BUSCAR LA FORMA DE OPTIMIZAR, VALIDANDO QUE PRIMERO MIRE LOS RESULTADOS QUE YA TIENE Y LUEGO LOS USE
                fechaJuego = input("Ingrese la fecha (DD-MM-AAAA): ")
                equipoLocal = name
                equipoVisitante = input(
                    "ingrese el nombre del equipo visitante: ")
                if (equipoLocal.lower != equipoVisitante.lower):
                    marcadorV = int(
                        input(f"Ingrese el marcador de visitante {equipoVisitante}: "))
                    marcadorL = int(
                        input(f"Ingrese el marcador de local {equipoLocal}: "))
                    if (marcadorL > marcadorV):
                        ganadosL += 1
                        perdidosV += 1
                    if (marcadorV > marcadorL):
                        ganadosV += 1
                        perdidosL += 1
                    if (marcadorL == marcadorV):
                        empateV += 1
                        empateL += 1
                    fechaLocal = [ganadosL, perdidosL, empateL]
                    equipos[idx].append(fechaLocal)
                    fechaVisitante = [ganadosV, perdidosV, empateV]
                else:
                    print("Los equipos no pueden ser los mismos")

            if sublist[0].lower() == equipoLocal.lower():
                equipos[idx].append(fechaVisitante)
            else:
                print("El equipo no fue encontrado, primero debe crear el equipo")

    if opc == '3':
        name = input("Ingrese el equipo del que desea ver las estadisticas: ")
        for idx, sublist in enumerate(equipos):
            if sublist[0] == name:

                for j in range(len(equipos[idx])):
                    print(equipos[idx][j], end='\n')
            else:
                print("No se encontro el equipo, primero debe crearse")

        print("|{:^5}{}{:^20}|".format('  ', 'TABLA DE PUNTUACIONES','  '))
        print('+', '-'*50, '+')
    if opc == '4':
        name = input("Ingrese el equipo del que desea ver las estadisticas: ")
        for idx, sublist in enumerate(equipos):
            if sublist[0] == name:
                for j in range(len(equipos[idx])):
                    print(equipos[idx][j], end='\n')
            else:
                print("No se encontro el equipo, primero debe crearse")

    if opc == 5:
        pass

    if opc == 6:
        pass

    if opc == 7:
        pass

    if opc == 0:
        flag = False
