"""
EJERCICIO DE PRÁCTICA - SISTEMA DE MAS CAFE
"""

# ---------------- Bloque diccionarios ----------------


def crear_datos_producto(nombre: str, categoria: str, tamaño: str, tipo_leche: str, temporada: bool) -> list:
    datos_producto = [nombre.strip(), categoria.strip().lower(), tamaño.strip().lower(), tipo_leche.strip().lower(), temporada]
    return datos_producto


def crear_datos_venta(precio: int, stock: int) -> list:
    datos_venta = [precio, stock]
    return datos_venta

# ---------------- Bloque de validacion ----------------

def validar_codigo(codigo: str) -> bool:
    codigo = codigo.upper().strip()

    if codigo != "" and len(codigo) == 4 and codigo[0] == "P" and codigo[1:].isdigit():
        return True
    else:
        return False
    
def validar_nombre(nombre: str) -> bool:
    nombre = nombre.strip()

    if nombre != "" and nombre.replace(" ", "").isalpha():
        return True
    else:
        return False

def validar_categoria(categoria: str) -> bool:
    categoria = categoria.lower().strip()

    if categoria in ["cafe", "te", "bebida"]:
        return True
    else:
        return False

def validar_tamaño(tamaño: str) -> bool:
    tamaño = tamaño.lower().strip()

    if tamaño in ["chico", "mediano", "grande"]:
        return True
    else:
        return False

def validar_tipo_leche(tipo_leche: str) -> bool:
    tipo_leche = tipo_leche.lower().strip()

    if tipo_leche in ["entera", "descremada", "sin leche"]:
        return True
    else:
        return False

def validar_temporada(temporada: str) -> bool:
    temporada = temporada.lower().strip()

    if temporada in ["si","s","no","n"]:
        return True
    else:
        return False

def validar_precio(precio: int) -> bool:
    if precio > 0:
        return True
    else:
        return False
    
def validar_stock(stock: int) -> bool:
    if stock >= 0:
        return True
    else:
        return False

# ---------------- Bloque menu ----------------

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")


def obtener_opcion():
    while True:
        try:
            opcion = int(input("Ingresa una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar una opcipon del 1 al 7.")
        except ValueError:
            print("Debe ingresar un número.")

def buscar_codigo(producto: dict, codigo: str) -> bool:
    codigo = codigo.upper().strip()
    if codigo in producto:
        return True
    else:
        return False
    
def stock_categoria(productos: dict, ventas: dict, categoria: str):
    categoria = categoria.lower().strip()
    stock_total = 0

    for codigo in productos:
        datos_producto = productos[codigo]
        categoria_producto = datos_producto[1].lower()

        if categoria_producto == categoria:
            stock_disponible = ventas[codigo][1]
            stock_total = stock_total + stock_disponible
    
    print(f"Stock total de la categoría '{categoria}': {stock_total}")

def busqueda_precio(productos: dict, ventas: dict, precio_min: int, precio_max: int):
    resultados = []

    for codigo in ventas:
        precio = ventas [codigo][0]
        stock_disponible = ventas[codigo][1]

        if precio_max >= precio >= precio_min and stock_disponible > 0:
            nombre_producto = productos[codigo][0]
            resultado = (codigo, nombre_producto, precio, stock_disponible)
            resultados.append(resultado)

    resultados.sort()

    if len(resultados) == 0:
        print("No se encontraron productos en el rango de precio especificado.")
    else:
        print("Productos encontrados:")
        for resultado in resultados:
            print(f"Nombre: {(resultado[1]).capitalize()} -- Precio: {resultado[2]}")

def actualizar_precio(productos: dict, ventas: dict, codigo: str, nuevo_precio: int) -> bool:
    codigo = codigo.upper().strip()

    if buscar_codigo(productos, codigo):
        ventas[codigo][0] = nuevo_precio
        return True
    else:
        return False

def agregar_producto(productos: dict, ventas: dict, codigo: str, datos_producto: list, datos_venta: list) -> bool:
    codigo = codigo.upper().strip()

    if buscar_codigo(productos, codigo):
        return False
    
    productos[codigo] = datos_producto
    ventas[codigo] = datos_venta
    return True

def eliminar_producto(productos: dict, ventas: dict, codigo: str) -> bool:
    codigo = codigo.upper().strip()

    if buscar_codigo(productos, codigo):
        del productos[codigo]
        del ventas[codigo]
        return True
    else:
        return False

# ---------------- Bloque main ----------------

def main():
    # Diccionarios de productos
    # Codigo: [Nombre, Categoria, Tamaño, Tipo de Leche, Temporada]
    productos = {
    "P001": ["Capuccino Clásico", "cafe", "mediano", "entera", False],
    "P002": ["Latte Vainilla", "cafe", "grande", "descremada", True],
    "P003": ["Té Verde Helado", "te", "mediano", "sin leche", False],
    "P004": ["Mocha Avellana", "cafe", "grande", "entera", True],
    "P005": ["Chocolate Caliente", "bebida", "chico", "entera", False],
    "P006": ["Té Chai Latte", "te", "mediano", "descremada", True]
    }

    # Diccionarios de ventas
    # Codigo: [Precio, Stock]
    ventas = {
        "P001": [2500, 15],
        "P002": [3200, 0],
        "P003": [2800, 10],
        "P004": [3500, 4],
        "P005": [2200, 7],
        "P006": [3100, 9]
        }


    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        # Se muestra el stock por categoría
        if opcion == 1:
            categoria = input("Ingrese la categoría (cafe, te, bebida): ")
            if validar_categoria(categoria):
                stock_categoria(productos, ventas, categoria)
            else:
                print("Categoría inválida. Debe ser 'cafe', 'te' o 'bebida'.")
        
        
        # Se realiza la búsqueda de productos por rango de precio
        # El usuario ingresa el precio mínimo y máximo, y se valida que sean números enteros y que el precio máximo no sea menor al precio mínimo.
        if opcion == 2:
            while True:
                try:
                    precio_min = int(input("Ingrese el precio mínimo: "))
                    if validar_precio(precio_min):
                        break
        
                except ValueError:
                    print("Debe ingresar un número entero para el precio mínimo.")
                    continue
                
            while True:
                try:
                    precio_max = int(input("Ingrese el precio máximo: "))
                    if validar_precio(precio_max):
                        break
                except ValueError:
                    print("Debe ingresar un número entero para el precio máximo.")
                    continue
            
            if precio_max < precio_min:
                print("El precio máximo no puede ser menor al precio mínimo.")
            else:
                busqueda_precio(productos, ventas, precio_min, precio_max)
            
        
        # Se actualiza el precio de un producto existente
        if opcion == 3:
            codigo = input("Ingrese el código del producto a actualizar: ")

            if validar_codigo(codigo):
                if buscar_codigo(productos, codigo):
                    try:
                        nuevo_precio = int(input("Ingrese el nuevo precio: "))
                        if validar_precio(nuevo_precio):
                            if actualizar_precio(productos, ventas, codigo, nuevo_precio):
                                print("Precio actualizado correctamente.")
                            else:
                                print("Error al actualizar el precio.")
                        else:
                            print("El precio debe ser mayor a 0.")
                    except ValueError:
                        print("Debe ingresar un número entero para el precio.")
                else:
                    print("El código ingresado no existe en el sistema.")
            else:
                print("Código inválido. Debe tener el formato 'PXXX' donde XXX son dígitos.")
                
        
        # Se agrega un nuevo producto al sistema
        if opcion == 4:
            codigo = input("Ingrese el código del nuevo producto: ")

            if validar_codigo(codigo):
                if not buscar_codigo(productos, codigo):
                    while True:
                        nombre = input("Ingrese el nombre del producto: ")
                        if not validar_nombre(nombre):
                            print("Nombre inválido. Debe contener solo letras y espacios.")
                            continue
                        else:   
                            break
                    
                    while True:
                        categoria = input("Ingrese la categoría (cafe, te, bebida): ")
                        if not validar_categoria(categoria):
                            print("Categoría inválida. Debe ser 'cafe', 'te' o 'bebida'.")
                            continue
                        else:
                            break
                    
                    while True:
                        tamaño = input("Ingrese el tamaño (chico, mediano, grande): ")
                        if not validar_tamaño(tamaño):
                            print("Tamaño inválido. Debe ser 'chico', 'mediano' o 'grande'.")
                            continue
                        else:
                            break
                    
                    while True:
                        tipo_leche = input("Ingrese el tipo de leche (entera, descremada, sin leche): ")
                        if not validar_tipo_leche(tipo_leche):
                            print("Tipo de leche inválido. Debe ser 'entera', 'descremada' o 'sin leche'.")
                            continue
                        else:
                            break

                    while True:
                        temporada = input("¿Es un producto de temporada? (si/no): ")
                        if not validar_temporada(temporada):
                            print("Respuesta inválida. Debe ser 'si' o 'no'.")
                            continue
                        else:
                            break

                    while True:
                        try:
                            precio = int(input("Ingrese el precio del producto: "))
                            if not validar_precio(precio):
                                print("El precio debe ser mayor a 0.")
                                continue
                            break
                        except ValueError:
                            print("Debe ingresar un número entero para el precio.")
                    
                    while True:
                        try:
                            stock = int(input("Ingrese el stock del producto: "))
                            if not validar_stock(stock):
                                print("El stock no puede ser negativo.")
                                continue
                            break
                        except ValueError:
                            print("Debe ingresar un número entero para el stock.")
                    
                    datos_producto = crear_datos_producto(nombre, categoria, tamaño, tipo_leche, temporada.lower() in ["si", "s"])
                    datos_venta = crear_datos_venta(precio, stock)

                    if agregar_producto(productos, ventas, codigo, datos_producto, datos_venta):
                        print("Producto agregado correctamente.")
                    
                else:
                    print("El código ingresado ya existe en el sistema.") 
            else:
                print("Código inválido. Debe tener el formato 'PXXX' donde XXX son dígitos.")
        
        
        # Se elimina un producto del sistema
        # Es necesario validar que el código ingresado sea válido y que exista en el sistema antes de eliminarlo.
        if opcion == 5:
            codigo = input("Ingrese el código del producto a eliminar: ")

            resultado = eliminar_producto(productos, ventas, codigo)

            if resultado:
                print("Producto eliminado correctamente.")
            
            else:
                print("El código ingresado no existe en el sistema.")
        

        # Se sale del programa
        elif opcion == 6:
            print("Saliendo del programa...")
            break
    

# ---------------- Bloque de ejecución ----------------

if __name__ == "__main__":
    main()
            

                