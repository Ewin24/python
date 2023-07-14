# Escribe un programa que solicite al usuario ingresar una frase y luego cuente cuántas veces aparece la letra 'a' en la
# frase utilizando un bucle for.

x = input("Ingrese una frase: ")
count = 0
for i in x.lower():
    if(i == 'a'):
        count += 1
print(f"La letra 'a', aparece: {count}")
        
 