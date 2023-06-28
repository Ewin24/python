# En su casa le solicitan que realice un algoritmo en Python, que permita calcular el valor a pagar por concepto
# de energía eléctrica. Los datos que se conocen son los siguientes:

# - Mes de consumo
# - Valor kw
# -Total kw consumido en el mes
# - estrato

mes = input("Ingrese el mes de consumo: ")
valorKw = float(input("Ingrese el valor por kilovatio (kW): "))
totalKw = float(input("Ingrese el total de kilovatios consumidos en el mes: "))
estrato = int(input("Ingrese el estrato: "))

if estrato == 1:
    tarifa = 5000
elif estrato == 2:
    tarifa = 8000
elif estrato == 3:
    tarifa = 10000
elif estrato == 4:
    tarifa = 15000
else:
    tarifa = 20000

valor_consumo = valorKw * totalKw
valor_total = tarifa + totalKw

print("Factura de energía eléctrica")
print("---------------------------")
print("Mes de consumo:", mes)
print("Valor kW:", valorKw)
print("Total kW consumidos:", totalKw)
print("Estrato:", estrato)
print("---------------------------")
print("Valor consumo: $", valor_consumo)
print("Valor total a pagar: $", valor_total)
