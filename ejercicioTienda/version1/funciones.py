import os
import random
import datetime

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
                'prodMax': int(input("Ingrese la cantidad maxima disponible de producto: ")),
                'state': int(input("Ingrese el estado (1: disponible,  2: no disponible): ")),
                'unitValue': float(input("Ingrese el valor unitario del producto: "))
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

def addBuy(prods : dict, shopping : dict):
        flag = True
        while flag:
            codProd = input("Ingrese el codigo producto que compro: ")
            prod = prods.get(codProd.upper(),False)
            if prod:
                try:
                    print(" -- Producto ya axiste, se hacen actualizaciones de datos -- ")
                    buyDate = input("Ingrese la fecha de compra: ")
                    buyValue = input("Ingrese el valor de la compra: ")
                    buyAmount = int(input("Ingrese la cantidad comprada: "))
                    #actualizacion en datos actuales
                    prod['prodMax'] += buyAmount
                    
                    #registro en la parte de compras
                    buy = {
                        'codCompra': codProd,
                        'fechaCompra': buyDate,
                        'cantidadCompra': buyAmount, 
                        'valorCompra': buyValue
                    }
                    shopping.update(buy)           
                except Exception as e:
                        print(f"Error: {e}")
                else:
                    flag = bool(input("Desea agregar otro producto S(si) y Enter(No)"))
            else:
                print("El producto no esta registrado, debe registrarlo: ")       
                addProduct(prods)
                #TODO: HACER REVISION DE CASOS DE EXEPCION O "VALIDACIONES"

def addCustomer(clientes: dict):
    os.system("clear")
    codCliente = input("Ingrese el código del cliente: ").upper()
    if codCliente in clientes:
        print("El cliente ya se encuentra registrado")
    else:
        nombreCliente = input("Ingrese el nombre del cliente: ").capitalize()

        cliente = {
            codCliente: {
                "codigo": codCliente,
                "nombre": nombreCliente
            }
        }
        clientes.update(cliente)
        #TODO:hacer pruebas del cliente

def addSales(prods:dict, sales:dict, customers:dict):
    #TODO: VER SI ES RENTABLE CREAR UNA SOLA LISTA DE CLIENTES, DE TAL MANERA QUE A LA HORA DE VENTA 
    #SOLO SEA RELACIONAR DATOS DE CLIENTE Y PRODUCTO, Y LUEGO AGREGAR LOS DATOS EXTRA DE VENTA
    flag = True
    totalFactura = 0
    prodFact = []
    if(not flag):
        for i, prod in enumerate(prodFact):#AQUI PODRIA MODIFICAR PARA MOSTRAR NOMBRES U OTROS DATOS DEL PROD
            print(f"#    CODIGO    CANTIDAD    PRECIO")
            print(f"{i+1}.   {prod['codProd']}   {prod['prodAmount']}   {prod['unitValue']}")
        print(f"TOTAL DE LA FACTURA ==   {totalFactura}")
    while(flag):
        try:
            print("-----REGISTRO DE VENTA-----")
            customerId = input("Ingrese el codigo del cliente: ")
            if(customers.get(customerId,False)):
                customerName = customers[customerId]['nombre']
                prodId = input("Ingrese el codigo del producto: ")
                if(prods.get(prodId,False)): 
                    nInvoice = random.randint(1,100000) #id random para facturas
                    sellDate = datetime.today() #fecha actual venta
                    unitValue = prods[prodId]['initValue'] #valor prdo
                    prodAmount = int(input("Ingrese la cantidad de productos que vendió: ")) #prod comprado
                    if(prodAmount > prods[prodId]['prodMax'] or prodAmount > prods[prodId]['prodMin'] and prodAmount > 0):
                        #contruccion de factura
                        prods[prodId]['prodMax'] -= prodAmount
                        
                        detalleFact = {
                            'codProd': prodId,
                            'prodAmount' : prodAmount,
                            'unitValue': unitValue 
                        }
                        prodFact.append(detalleFact)
                        totalFactura += unitValue * prodAmount
                        
                    else:
                        print("No puede comprar menos de un producto, tampoco puede comprar mas de la cantidad stock de bodega")    
                else:
                    print("Producto no encontrado, ingrese uno.")
                    addProduct()
            else:
                print("Cliente no envontrado, ingresa un nuevo cliente.")
                addCustomer()
            
        except Exception as e:
            print("La exepcion del error es: " + e)
        else:
            flag = bool(input("Desea agregar otra venta S(si) y Enter(No)"))
      

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

def showAll(prods : dict, sales:dict, shopping:dict, customers: dict):
    if (prods):
        print(prods)
        print(sales)
        print(shopping)
        print(customers)
    else:
        print("No registros en nuestra base de datos")

def showProduct(prods : dict):
    codProd = prods.get(input("Ingrese el codigo del producto: ").upper(),False)
    if (codProd):
        print(codProd)
    else:
        print("El producto no esta registrado")
#TODO:aqui debe hacer que se reciba tambien las compras y filtrar por el cod del producto para mostrar
