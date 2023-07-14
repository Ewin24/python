import core
import os
diccProducto = {"data":[]}
"""
Metodo para cargar informacion de productos:
Si el archivo de recursos no existe lo crea de forma
automatica con la estructura inicia del diccionario vacio
diccCliente = {"data":[]}
"""
def LoadInfoCliente():
    global diccProducto
    if (core.checkFile("productos.json")):
        diccProducto = core.LoadInfo("productos.json")
    else:
        core.crearInfo("productos.json",diccProducto)

def MainMenu():
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^14}{}{:^14}|".format(' ','ADMINISTRACION DE PRODUCTOS',' '))
    print('+','-'*55,'+')
    print("1. Registrar")
    print("2. Buscar")
    print("3. Editar")
    print("4. Activar o Inactivar")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        data ={
            "id":input("Ingrese el Id del producto :"),
            "nombre":input("Ingrese el Nombre del producto :"),
            "cantidad":0,
            "stockMin":int(input("Ingrese el Stock minimo :")),
            "stockMax":int(input("Ingrese el Stock maximo :")),
            "valorCompra":float(input("Ingrese el valor de compra :")),
            "valorVenta":float(input("Ingrese el valor de venta :")),
            "estado":True
        }
        diccProducto["data"].append(data)
        core.crearInfo("productos.json",data)
        
    elif (opcion == 2):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE PRODUCTOS',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a buscar:")
        for i,item in enumerate(diccProducto["data"]):
            if cliSearch in item["id"]:
                print(f'Id cliente : {item["id"]}')
                print(f'Nombre cliente : {item["nombre"].upper()}')
                print(f'Email cliente : {item["email"]}')
        os.system("pause")
    elif (opcion == 3):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDICION DE PRODUCTOS',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a editar:")
        for i,item in enumerate(diccProducto["data"]):
            if cliSearch in item["id"]:
                item["nombre"] = input("Ingrese en nuevo nombre o presione enter para omitir :") or item["nombre"]
                item["precio"] =float(input("Ingrese en nuevo precio o presione enter para omitir :")) or item["precio"]
                item["stockMin"]=float(input("Ingrese en nuevo precio o presione enter para omitir :")) or item["stockMin"]
                item["stockMax"]=float(input("Ingrese en nuevo precio o presione enter para omitir :")) or item["stockMax"]
                core.EditarData("productos.json",diccProducto)
    elif (opcion == 4):
        os.system("clear")
        print('+','-'*49,'+')
        print("|{:^16}{}{:^15}|".format(' ','ELIMINACION DE PRODUCTOS',' '))
        print('+','-'*49,'+')
        cliSearch = input("Ingrese el codigo del cliente a editar:")
        for i,item in enumerate(diccProducto["data"]):
            if cliSearch in item["id"]:
                print("1.Activar\n2.Inactivar")
                diccProducto["data"][i]["estado"] = True if int(input(":")) == 1 else False 
                core.EditarData("productos.json",diccProducto)
                # os.system("pause")
                # core.crearInfo("productos.json",itemDel)

    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu()