import os
import clientes
import compras
import ventas
import productos
import proveedores

isActive = True

if __name__ == "__main__":
    os.system("clear")
    while (isActive):
        print('+', '-'*55, '+')
        print("|{:^22}{}{:^21}|".format(' ', 'MENU PRINCIPAL', ' '))
        print('+', '-'*55, '+')
        print("1. Gestion de clientes")
        print("2. Gestion de producto")
        print("3. Gestion de Proveedores")
        print("4. Gestion de Compras")
        print("5. Gestion de ventas")
        print("6. Terminar")
        opcion = int(input(":)_"))
        if (opcion == 1):
            clientes.mainMenu()
        elif (opcion == 2):
            productos.mainMenu()
        elif (opcion == 3):
            proveedores.mainMenu()
        elif (opcion == 4):
            compras.mainMenu()
        elif (opcion == 5):
            ventas.mainMenu()
        elif (opcion == 6):
            isActive = False
        else:
            print("opcion no valida: ")
