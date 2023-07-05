# Construir un programa en Python que permita llevar el control del inventario de una ferretería.
# La información
# Que la ferreteria maneja de cada producto es la siguiente:

# 1. Codigo del producto
#    Nombre del producto
#    stockMinimo
#    Stockmaximo
#    Estado (Disponible. No disponible)
# 2. Proveedor. Un producto lo puede suministrar varios proveedores
# 3. Compras : El programa debe permitir controlar las compras de los productos. La información que se
# maneja en las compras es: Nro documento de compra, fecha de compra. Valor compra,cantidad comprada.
# 4. Ventas : El programa debe permitir controlar las ventas a clientes la información que se tiene en
# cuenta en el proceso de compra es la siguiente: Nro factura venta, fecha venta, Nro Id del cliente, Nombre
# del cliente, total de factura y el detalle de venta (Cod producto, Cantidad vendida, valor unitario)
# 5. ACTUALIZAR
# 6. ver info de un producto
# 7. ver info de todos los productos

# producto = {
# 	'codigo':
# 	'nombre':
# 	'mins':
# 	'max':
# 	'estado':
#   'proveedor' :['name']
# }

#'compras' :{
#       'nroCompra':
#       'fechaCompra':
#       'valorCompra':
#       'cantidadCompra':
#   }

#'ventas' :{
#       'NroFactura':
#       'fechaVenta':
#       'nroIdCliente':
#       'nombreCliente':
#       'totalFactura':
#       'detalleVenta': {
#           'codProducto':
#           'cantidadVendida':
#           'valorUnitario':
#        }
# }
#'ventas' :{
#       'NroFactura':
#       'fechaVenta':
#       'nroIdCliente':
#       'nombreCliente':
#       'totalFactura':
#       'detalleVenta': {
#           'codProducto':
#           'cantidadVendida':
#           'valorUnitario':
#        }
# }




import funciones as funciones
import os
if __name__ == "__main__":
    products = {}
    shopping = {}
    sales = {}
    customers = {}
    flag = True
    opc = 0
    while flag:
        os.system("clear")
        print("1.Registrar producto\n2.Proveedores de productos\n3.Compras de producto\n4.Ventas de producto\n5.Agregar un cliente\n6.Ver un producto\n7.ver todos los productos")
        try:
            opc = int(input(":) "))
            if (opc == 1):
                funciones.addProduct(products)
            elif (opc == 2):
                os.system("clear")
                funciones.addProv(products)
            elif (opc == 3):
                funciones.addBuy(products,shopping)
            elif (opc == 4):
                funciones.addSales(products,sales,customers)
            elif (opc == 5):
                funciones.addCustomer(customers)
            elif (opc == 6):
                funciones.showProduct(products)
            elif (opc == 7):
                funciones.showProducts(products, sales, shopping)
        except Exception:
            print("No se reconoce el tipo de dato del valor ingresado")
        flag = bool(input("Desea continuar en el programa S(Si) o Enter(No) :"))
