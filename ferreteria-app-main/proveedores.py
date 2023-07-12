import core
import os
diccProveedor = {"data":[]}
"""
Metodo para cargar informacion de proveedores:
Si el archivo de recursos no existe lo crea de forma
automatica con la estructura inicia del diccionario vacio
diccCliente = {"data":[]}
"""
def LoadInfoCliente():
    global diccProveedor
    if (core.checkFile("proveedores.json")):
        diccProveedor = core.LoadInfo("proveedores.json")
    else:
        core.crearInfo("proveedores.json",diccProveedor)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^14}{}{:^14}|".format(' ','ADMINISTRACION DE PROVEEDORES',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Editar")
    print("4. Eliminar")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        data ={
            "id":input("Ingrese el Id del cliente :"),
            "nombre":input("Ingrese el Nombre del cliente :"),
            "email":input("Ingrese el Email del cliente :"),
        }
        diccProveedor["data"].append(data)
        core.crearInfo("proveedores.json",data)
        
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE PROVEEDOR',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a buscar:")
        for i,item in enumerate(diccProveedor["data"]):
            if cliSearch in item["id"]:
                print(f'Id cliente : {item["id"]}')
                print(f'Nombre cliente : {item["nombre"].upper()}')
                print(f'Email cliente : {item["email"]}')
        os.system("pause")
    elif (opcion == 3):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDICION DE PROVEEDOR',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a editar:")
        for i,item in enumerate(diccProveedor["data"]):
            if cliSearch in item["id"]:
                item["nombre"] = input("Ingrese en nuevo nombre o presione enter para omitir :") or item["nombre"]
                item["email"] = input("Ingrese en nuevo email o presione enter para omitir :") or item["email"]
                core.EditarData("proveedores.json",diccProveedor)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACION DE PROVEEDOR',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a editar:")
        for i,item in enumerate(diccProveedor["data"]):
            if cliSearch in item["id"]:
                itemDel = diccProveedor["data"].pop(i)
                core.EditarData("proveedores.json",diccProveedor)
                # os.system("pause")
                # core.crearInfo("proveedores.json",itemDel)

    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()

    
