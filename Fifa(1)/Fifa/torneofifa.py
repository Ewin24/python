import os
def AddEquipo(myTeams : dict):
    os.system("clear")
    """
    teamName = input("Ingrese el nombre del Equipo:").upper()
    """
    codTeam = input("Ingrese el Cod del Equipo:").upper()
    equipo = {
        codTeam:{
            "codTeam": codTeam,
            "teamName": input("Ingrese el nombre del Equipo:").upper()
        }
    }
    myTeams.update(equipo)

def AddPlayer(equipos : dict):
    isAddPlayer = True
    equipo = equipos.get(input("Ingrese el codigo del equipo:").upper(),-1)
    if (equipo == -1):
        print("El equipo no esta registrado")
    else:
        while isAddPlayer:
            posiciones = ["Arquero","Defensa","Delantero","Medio Central"]
            nombrePlayer = input("Ingrese el nombre del Player : ")
            edadPlayer =int(input("Ingrese Edad player"))
            dorsalPlayer =int(input("Ingrese el Nro dorsal player"))
            while ((equipo.get("jugadores",-1) !=-1) and (equipo["jugadores"].get(dorsalPlayer,-1) != -1)):
                print("El nro del Dorsal ya se encuentra Asignado")
                dorsalPlayer =int(input("Ingrese de nuevo el Nro del dorsal: "))
            print("Seleccione la posicion del jugador")
            for i,pos in enumerate(posiciones):
                print(f"{i+1}. {pos}")
            posicionPlayer =posiciones[int(input())-1]
            jugador = {
                dorsalPlayer:{
                "nombrePlayer" : nombrePlayer,
                "edadPlayer" : edadPlayer,
                "dorsalPlayer" : dorsalPlayer,
                "posicionPlayer" : posicionPlayer
                }
            }
            try:
                rta = equipo.get("jugadores",-1)
                if rta == -1:
                    equipo.update({"jugadores":jugador})
                else:
                    equipo["jugadores"].update(jugador)            
            except Exception as e:
                    print(f"Error: {e}")
            else:
                isAddPlayer = bool(input("Desea agregar otro Jugador S(si) y Enter(No)"))
def AddCT(equipos : dict):
    isAddCt = True
    equipo = equipos.get(input("Ingrese el codigo del equipo:").upper(),-1)
    if (equipo == -1):
        print("El equipo no esta registrado")
    else:
        while isAddCt:
            cargo = ["Director tecnico","Asistente Tecnico","Entrenador De Arquero","Entrenador"]
            if ((equipo.get("ct",-1) == -1)):
                codigo = str(1).zfill(3) 
            else:
                codigo = str(len(equipo["ct"])+1).zfill(3)
            nombreTecnico = input("Ingrese el nombre del tecnico : ")
            edadTecnico =int(input("Ingrese Edad tecnico: "))
            print("Seleccione el cargo del experto")
            for i,pos in enumerate(cargo):
                print(f"{i+1}. {pos}")
            cargoTecnico =cargo[int(input())-1]
            ct = {
                codigo:{
                "codigo" : codigo,
                "nombreTecnico" : nombreTecnico,
                "edadTecnico" : edadTecnico,
                "cargoTecnico" : cargoTecnico
                }
            }
            try:
                rta = equipo.get("ct",-1)
                if rta == -1:
                    equipo.update({"ct":ct})
                else:
                    equipo["ct"].update(ct)            
            except Exception as e:
                    print(f"Error: {e}")
            else:
                isAddCt = bool(input("Desea agregar otro Jugador S(si) y Enter(No)"))

def VerPlayers(equipos : dict):
    isAddCt = True
    equipo = equipos.get(input("Ingrese el codigo del equipo:").upper(),-1)
    if (equipo == -1):
        print("El equipo no esta registrado")
    else:
        if (equipo.get("jugadores",-1) != -1):
            for llave,valor in equipo.get("jugadores").items():
                print(f'Nombre del jugador : {valor["nombrePlayer"]}')
        else:
            print("No se encuentran los jugadores registrado")
            os.system("pause")
def DeletePlayer(equipos : dict):
    equipo = equipos.get(input("Ingrese el codigo del equipo a eliminar:").upper(),-1)
    if (equipo == -1):
        print("El equipo no esta registrado")
    else:
        print(equipo)
        if (bool(input("Desea confirmar elimiminacion Pess Enter o N para cancelar")) == False):
            equipos.pop(equipo["codTeam"])
        else:
            print("Proceso cancelado por el usuario")
        os.system("pause")
def EditarTeam(equipos : dict):
    equipo = equipos.get(input("Ingrese el codigo del equipo a Editar:").upper(),-1)
    opcion = 1
    while (opcion != 0):
        print("1.Modificar el nombre\n0.Terminar")
        if(opcion == 1):
             teamName = input("Ingrese el nombre del Equipo:").upper()

    # print(f'El equipo actual es {equipo["teamName"]}')
    # if(bool(input("Presione enter para modificar el nombre"))==False):
    #     teamName = input("Ingrese el nombre del Equipo:").upper()
    # else:
    #     teamName = equipo["teamName"]

    equipo = {
        equipo["codTeam"]:{
            "codTeam": equipo["codTeam"],
            "teamName": teamName
        }
    }
    equipos.update(equipo)
    print(equipos)     
    os.system("pause")    


