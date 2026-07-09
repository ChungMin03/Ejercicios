#Bloque de funciones
def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >=1 and opcion <=6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def stock_categoria(categoria, productos, ventas):
    total_stock = 0
    for codigo, datos in productos.items():
        if datos[1].lower() == categoria.lower():
            total_stock += ventas[codigo][1]

    print(f"El total de stock disponible es: {total_stock}")

def busqueda_precio(precio_min, precio_max, ventas, productos):
    resultados = []
    for codigo, datos in ventas.items():
        if datos[0] >= precio_min and datos[0] <= precio_max and datos[1]!=0:
            nombre = productos[codigo][0]
            texto = f"{nombre}--{codigo}"
            resultados.append(texto)

    resultados.sort()
    if resultados == []:
        print("No hay productos en ese rango de precios.")

    else:
        print(f"Los productos encontrados son: {resultados}")


def buscar_codigo(codigo, ventas):
    codigo = codigo.upper()          
    return codigo in ventas

def actualizar_precio(codigo, ventas, nuevo_precio):
    codigo = codigo.upper()
    if buscar_codigo(codigo, ventas):
        ventas[codigo][0] = nuevo_precio
        return True
    else:
        return False 
            
def eliminar_producto(codigo, productos,ventas):
    codigo = codigo.upper()
    if buscar_codigo(codigo, ventas):
        ventas.pop(codigo)
        productos.pop(codigo)
        return True
    else:
        return False

#Funciones de validacion

def validar_texto(texto):
    return texto.strip() != ""

def validar_codigo(codigo, productos):
    if codigo.strip() == "":
        return False
    if codigo.upper() in productos:
        return False
    return True

def validar_tamano(tamano):
    return tamano.lower() in ['chico', 'mediano', 'grande']


def validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False

def validar_stock(stock):
    try:
        return int(stock) >= 0
    except ValueError:
        return False

#la funcion qla mas importante
def agregar_producto(codigo, nombre_producto, categoria, tamano, tipo_leche, es_temporada, precio, stock_disponible, productos, ventas):
    codigo = codigo.upper()
    if codigo in productos:
        return False
    productos[codigo] = [nombre_producto, categoria, tamano, tipo_leche, es_temporada]
    ventas[codigo] = [precio, stock_disponible]
    return True

        
def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

#programa principal

productos = {
    'P001': ['Capuccino Clásico', 'cafe', 'mediano', 'entera', False],
    'P002': ['Latte Vainilla', 'cafe', 'grande', 'descremada', True],
    'P003': ['Té Verde Helado', 'te', 'mediano', 'sin leche', False],
    'P004': ['Mocha Avellana', 'cafe', 'grande', 'entera', True],
    'P005': ['Chocolate Caliente', 'bebida', 'chico', 'entera', False],
    'P006': ['Té Chai Latte', 'te', 'mediano', 'descremada', True],
}

ventas = {
    'P001': [2500, 15],
    'P002': [3200, 0],
    'P003': [2800, 10],
    'P004': [3500, 4],
    'P005': [2200, 7],
    'P006': [3100, 9],
}

continuar = True
while continuar:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        categoria = input("Ingrese categoría a consultar: ")
        stock_categoria(categoria, productos, ventas)

    elif opcion == 2:
        while True:
            try:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(precio_min, precio_max, ventas, productos)

    elif opcion == 3:
        seguir = "s"
        while seguir == "s":
            codigo = input("Ingrese código del producto: ")
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if actualizar_precio(codigo, nuevo_precio, ventas):
                print("Precio actualizado")
            else:
                print("El código no existe")
            seguir = input("¿Desea actualizar otro precio (s/n)?: ").lower()

    elif opcion == 4:
        codigo = input("Ingrese código del producto: ")
        nombre_producto = input("Ingrese nombre del producto: ")
        categoria = input("Ingrese categoría: ")
        tamano = input("Ingrese tamaño (chico/mediano/grande): ")
        tipo_leche = input("Ingrese tipo de leche: ")
        respuesta = input("¿Es producto de temporada? (s/n): ")
        es_temporada = respuesta.lower() == "s"
        precio = input("Ingrese precio: ")
        stock_disponible = input("Ingrese stock disponible: ")

        if not validar_codigo(codigo, productos):
            print("El código ya existe o es inválido")
        elif not validar_texto(nombre_producto):
            print("El nombre del producto es inválido")
        elif not validar_texto(categoria):
            print("La categoría es inválida")
        elif not validar_tamano(tamano):
            print("El tamaño es inválido")
        elif not validar_texto(tipo_leche):
            print("El tipo de leche es inválido")
        elif not validar_precio(precio):
            print("El precio es inválido")
        elif not validar_stock(stock_disponible):
            print("El stock es inválido")
        else:
            agregar_producto(codigo, nombre_producto, categoria, tamano, tipo_leche, es_temporada, int(precio), int(stock_disponible), productos, ventas)
            print("Producto agregado")

    elif opcion == 5:
        codigo = input("Ingrese código del producto que desea eliminar: ")
        if eliminar_producto(codigo, productos, ventas):
            print("Producto eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        continuar = False
        print("Programa finalizado.")
            
            


    
        
    

            
            
    
