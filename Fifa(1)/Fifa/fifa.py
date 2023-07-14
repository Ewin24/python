import torneofifa as equipos
import os
if __name__ == "__main__":
    teams={}
    isAddTeam = True
    opcion = 0
    while isAddTeam:
        os.system("clear")
        print("1.Registrar equipo\n2.Mostrar Jugadores Por Equipo\n3.Registro de jugadores\n4.Registro de cuerpo tecnico\n5.Registro de medico\n6.Eliminar equipo\n7.Editar equipo")
        try:
            opcion = int(input(":)"))
            if (opcion == 1):
                equipos.AddEquipo(teams)
            elif (opcion == 2):
                os.system("clear")
                equipos.VerPlayers(teams)
            elif (opcion == 3):
                equipos.AddPlayer(teams)
            elif (opcion == 4):
                equipos.AddCT(teams)
            elif (opcion == 5):
                equipos.AddMedico(teams)
            elif (opcion == 6):
                equipos.DeletePlayer(teams)
            elif (opcion == 7):
                equipos.EditarTeam(teams)
        except Exception:
            print("No se reconoce el tipo de dato del valor ingresado")
        isAddTeam= bool(input("Desea continuar en el programa S(Si) o Enter(No) :"))
