import os

def addEquipo(equipos):
    os.system('cls')
    teamName = input("Ingrese el nombre del equipo: ")
    myTeam = [teamName, [], [], []]
    equipos.append(myTeam)

def addPlayer(equipos):
    equipo = input("Ingrese el nombre del equipo: ").upper()
    isAddPlayer = True
    for item in equipos:
        if equipo in item:
            while isAddPlayer:
                posicion = ["Arquero", "Delantero", "Medio Campo"]
                nombrePlayer = input("Ingrese el nombre del jugador: ")
                edadPlayer = input("Ingrese el Edad del jugador: ")
                print("Ingrese la especialidad del jugador: ")
                for i, pos in enumerate(posicion):
                    print(f"{i+1}. {pos}")
                posicionPlayer = posicion[int(input()-1)]
                tecnico = [nombrePlayer, edadPlayer,posicionPlayer]
                item[2].append(tecnico)
                isAddPlayer = bool(input("Desea agregar otro jugador S(SI) Enter(NO)"))

def addTecnico(equipos):
    equipo = input("Ingrese el nombre del equipo: ").upper()
    isAddTecnico = True
    for item in equipos:
        if equipo in item:
            while isAddTecnico:
                especialidad = ["Director tecnico", "Asistente Tecnico", "Entrenador de Arquero"]
                nombreTecnico = input("Ingrese el nombre del Tecnico: ")
                edadTecnico = input("Ingrese el Edad del Tecnico: ")
                print("Ingrese la especialidad del Tecnico: ")
                for i, pos in enumerate(especialidad):
                    print(f"{i+1}. {pos}")
                especialidadTecnico = especialidad[int(input()-1)]
                tecnico = [nombreTecnico, edadTecnico,especialidadTecnico]
                item[2].append(tecnico)
                isAddTecnico = bool(input("Desea agregar otro tecnico S(SI) Enter(NO)"))

def addMedico(equipos):
    equipo = input("Ingrese el nombre del equipo: ").upper()
    isAddMedico = True
    for item in equipos:
        if equipo in item:
            while isAddMedico:
                especialidad = ["Psicologo", "Fisioterapeuta"]
                nombreMedico = input("Ingrese el nombre del medico: ")
                edadMedico = input("Ingrese el Edad del medico: ")
                print("Ingrese la especialidad del medico: ")
                for i, pos in enumerate(especialidad):
                    print(f"{i+1}. {pos}")
                especialidadMedico = especialidad[int(input()-1)]
                tecnico = [nombreMedico, edadMedico,especialidadMedico]
                item[3].append(tecnico)
                isAddMedico = bool(input("Desea agregar otro medico S(SI) Enter(NO)"))

def mostrarTecnicos(equipos):
    print('+', '-'*68, '+')
    print('+', '-'*68, '+')

    especialidad = input("Ingrese Especialidad del tecnico a buscar: ").upper()
    for i, equipo in enumerate(equipos):
        for j, tec in enumerate(equipos[2]):
            if "Director tecnico" in tec:
                    print(f"{equipo[0]} - {tec[0]}")
            
                
             