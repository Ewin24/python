import os
import paciente
import cita
import veterinario

if __name__ == "__main__":
    import os

    flag = True
    while (flag):
        os.system("clear")
        print("----ADMINISTRACION DEL CENTRO VETERINARIO----")
        print("1. Gestion de pacientes")
        print("2. Gestion de veterinarios")
        print("3. Gestion de citas medicas")
        print("4. Salir")
        opc = int(input(":)_ "))

        if opc == 1:
            paciente.menu()
        if opc == 2:
            veterinario.menu()
        if opc == 3:
            cita.menu()
        if opc == 4:
            flag = False
