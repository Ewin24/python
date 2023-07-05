import os
def addProduct(prods : dict):
    os.system("clear")
    codProduct = input("Ingrese el Cod del producto:").upper()
    if(prods.get(codProduct, False)):
        print("El producto ya se encuentra registrado")
    else:
        product = {
            codProduct:{
                "codProduct": codProduct,
                "productName": input("Ingrese el nombre del producto: ").upper(),
                'prodMins': int(input("Ingrese la cantidad minima disponible de producto: ")),
                'ProdMax': int(input("Ingrese la cantidad maxima disponible de producto: ")),
                'estado': int(input("Ingrese el estado (1: disponible,  2: no disponible): "))
            }
        }

    prods.update(product)   

def addProv(prods : dict):
    flag = True
    prod = prods.get(input("Ingrese el codigo producto al que adicionara proveedor: ").upper(),False)
    if prod:
        while flag:
            try:
                provName = input("Ingrese el nombre de su proveedor: ")
                if(prod.get("proveedores",False)):
                    prod["proveedores"].append(provName)
                else:
                    prod.update({'proveedores': []})
                    prod["proveedores"].append(provName)            
            except Exception as e:
                    print(f"Error: {e}")
            else:
                flag = bool(input("Desea agregar otro proveedor S(si) y Enter(No)"))
    else:
        print("El producto no esta registrado")       
    
# 3. Compras : El programa debe permitir controlar las compras de los productos. La información que se
# maneja en las compras es: Nro documento de compra, fecha de compra. Valor compra,cantidad comprada.
def addBuy(prods : dict):
        flag = True
        while flag:
            prod = prods.get(input("Ingrese el codigo producto que compro: ").upper(),False)
            if prod:
                try:
                    print(" -- Producto ya axiste, se hacen actualizaciones de datos -- ")
                    codigo = input("Ingrese el nombre de su proveedor: ")
                    provName = input("Ingrese el nombre de su proveedor: ")
                    provName = input("Ingrese el nombre de su proveedor: ")
                    provName = input("Ingrese el nombre de su proveedor: ")
                    if(prod.get("proveedores",False)):
                        prod["proveedores"].append(provName)
                    else:
                        prod.update({'proveedores': []})
                        prod["proveedores"].append(provName)            
                except Exception as e:
                        print(f"Error: {e}")
                else:
                    flag = bool(input("Desea agregar otro proveedor S(si) y Enter(No)"))
            else:
                print("El producto no esta registrado")       
    

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

def showProducts(prods : dict):
    if (prods):
        print(prods)
    else:
        print("No hay productos registrados")

def showProduct(prods : dict):
    codProd = prods.get(input("Ingrese el codigo del producto: ").upper(),False)
    if (codProd):
        print(codProd)
    else:
        print("El producto no esta registrado")

