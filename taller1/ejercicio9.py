# Escribe un programa que solicite al usuario ingresar el día, el mes y el año de una fecha. Luego, verifica si la fecha es
# válida o no. Considera los diferentes casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
# indicando si la fecha es válida o no.
print("Fecha con cormato dia-mes-año")
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
if(dia > 31 or dia < 1):
    print("Tu fecha no puede tener mas de 31 dias ni menos de 1")
elif(dia > 29 and mes == 2):
    print("Febrero no tiene mas de 29 dias")
elif(mes > 12 or mes < 1) :
    print("No existen mas de 12 meses ni menos de 1 mes")
elif(año < 0) :
    print("No existen años menores a 0")

print(f"Su fecha es: {dia} - {mes} - {año}")