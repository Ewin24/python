africa = ['Egipto', 'Sudáfrica', 'Kenia']
america = ['Estados Unidos', 'Brasil', 'Canadá']
asia = ['China', 'India', 'Japón']
europa = ['Francia', 'Alemania', 'España']
oceania = ['Australia', 'Nueva Zelanda', 'Fiyi']

pais = input("Ingrese el nombre de un país: ")

if pais in africa:
    print(f"El país {pais} se encuentra en África.")
elif pais in america:
    print(f"El país {pais} se encuentra en América.")
elif pais in asia:
    print(f"El país {pais} se encuentra en Asia.")
elif pais in europa:
    print(f"El país {pais} se encuentra en Europa.")
elif pais in oceania:
    print(f"El país {pais} se encuentra en Oceanía.")
else:
    print(f"No se pudo determinar el continente del país {pais}.")
