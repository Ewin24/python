def addPlayer(players):
    playerName = input("Ingrese el nombre del Jugador: ")
    playerAge = input("Ingrese la edad del Jugador: ")
    print("1. Delantero, 2.MedioCampista, 3.Arquero")
    playerPosition = int(input("Escoja la posicion del jugador: "))

    if(playerPosition in [1,2,3]):
        players["name"] = playerName
        players["Age"] = playerAge
        players["Position"] = playerPosition
    else:
        print("posicion incorrecta")
        #TODO: esto hace sobreescritura, hacer de otra forma
        
def showPlayers(players):
    print(players)

