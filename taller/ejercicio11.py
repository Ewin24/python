# Escribe un programa que solicite al usuario ingresar el nombre de un mes y determine cuántos días
# tiene ese mes. Utiliza estructuras condicionales para asociar cada mes con la cantidad
# correspondiente de días y muestra un mensaje con el resultado.
meses31 = ['enero', 'marzo', 'diciembre', 'octubre', 'mayo', 'julio', 'agosto']
meses30 = ['noviembre', 'abril', 'septiembre', 'junio']

mes = input("Ingresa el nombre del mes y te dare los dias: ")
if mes.lower() in meses31:
    print("Tu mes tiene 31 dias")
if mes.lower() in meses30:
    print("Tu mes tiene 30 dias")
if (mes.lower() == 'febrero'):
    print("su mes tiene 28 o 29 dias.")
