producto = {
    '12': {
        'nombre': 'arroz',
        'proveedores': []       
    }
    
}

prodFact = [
        {
            'nombre': 'joven',
            'precio': 12.500
        },
        {
            'nombre': 'joven1',
            'precio': 13.500
        },
        {
            'nombre': 'joven2',
            'precio': 14.500
        }
    ]

for i, prod in enumerate(prodFact):
    print(f"'#'.        'nombre'        'precio'")
    print(f"{i+1}.        {prod['nombre']}        {prod['precio']}")
    
#print(producto['12']['nombre'])