import campers
import os

if __name__ == "__main__":
    isActivate = True
    opcion = 0
    dataCamper = {'data': []}
    while isActivate:
        os.system("clear")
        print('+', '-'*55, '+')
        print("|{:^20}{}{:^24}|".format(' ', 'Menu Pricipal', ' '))
        print('+', '-'*55, '+')
        print("1. Agregar camper")
        print("2. Editar camper")
        print("3. Buscar camper")
        print("3. Eliminar camper")
        print("4. Listado completo de campers")
        print("5. Salir")
        opcion = int(input(":)_"))
        if (opcion == 1):
            campers.addCamper(dataCamper)
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            pass
        elif (opcion == 5):
            pass
        elif (opcion == 6):
            isActivate = False
        else:
            print("Opcion no valida....")
            os.system("pause")
