
op = ""

productos ={
    '8475HD': ['HP', 15.6, '8GB', 'DD','1T','Intel Core i5', 'Nvidia GTX1050'],
    'JjfFDH' : ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i3', 'Integrada']
    }


stock = {
    '8475HD' : [387990 , 10],
    'JjfFDH' : [424990 , 1]
    }

def encontrar_clave_por_valor( productos , esT_marca_M):
    for clave, valor in productos.items():
        if valor == esT_marca_M:
            return clave
    return None

while True:
    print("**Menu Principal**")
    print("1- Stock Marca ")
    print("2- Buscar ")
    print("3- Actualizar precio ")
    print("4- Salir ")
    op = input("Ingrese una opción ")

    if op == "1":

        esT_marca = input("Ingrese marca a consultar: ")

        esT_marca_M = esT_marca.upper

        clave_encontrada = encontrar_clave_por_valor(productos, esT_marca_M)

        for esT_marca_M in productos:

            if 

        if clave_encontrada:
            print(f"La clave que corresponde al valor {esT_marca} es: {clave_encontrada}")
        else:
            print(f"No se encontró ninguna clave para el valor {esT_marca}")
        

        