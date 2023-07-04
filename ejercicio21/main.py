import equipo
import os
if __name__ == "__main__":
    teams = []
    isAddTeam = True
    while isAddTeam:
        os.system("cls")
        print("1. Registrar Equipo\n2. Mostrar Equipos\n3. Registro Jugadores\n4. Registro de medicos\n5. Registro de Tecnico\n6. Mostrar Tecnicos En cada Equipo")
        try:
            opcion = int(input(":)"))
            if (opcion == 1):
                equipo.addEquipo(teams)

            if (opcion == 2):
                os.system("cls")
                print(teams)
                os.system('')

            if (opcion == 3):
                os.system("cls")
                equipo.addPlayer(teams)

            if (opcion == 4):
                os.system("cls")
                equipo.mostrarTecnicos(teams)

            if (opcion == 5):
                os.system("cls")
                equipo.addTecnico(teams)

            if (opcion == 6):
                os.system("cls")
                equipo.mostrarTecnicos(teams)

        except Exception as e:
            print('No se reconoce el valor ingresado', e)
        else:
            isAddTeam = bool(input("Desea contrinuar en el programa S(SI) o Enter(NO)"))
