import equipo

players = {
    "name" : "",
    "age" : "",
    "position" : ""
}

flag = True
opc = 0
while(flag):
    print("1. Ingreso de Jugador","2. Mostrar Jugadores",sep="\n")
    opc = input(":) ")
    if(opc == '1'):
        equipo.addPlayer(players)
    if(opc == '2'):
        print(players)