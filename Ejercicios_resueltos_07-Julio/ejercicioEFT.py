#funciones

def mostrar_menu():
    print("============== MENU PRINCIPAL ==============")
    print("1. Stock por categoría")
    print("2. Búsqueda de producto por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("===========================================")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion < 1 or opcion > 6:
                raise ValueError
            else:
                return opcion
        except:
            print("ERROR: Ingrese una opcion válida (1-6).")


def stock_categoria(categoria, dic_productos, dic_ventas):
    count = 0
    for key, value in dic_productos.items():
        if value[1].lower() == categoria.lower():
            count += dic_ventas[key][1]
    print(f"El stock disponible para {categoria} es: {count} unidades.")

def busqueda_precio(precio_min, precio_max, dic_productos, dic_ventas):
    lista_prod_precios = []
    for key, value in dic_ventas.items():
        if (value[0] >= precio_min and value[0] <= precio_max) and value[1] > 0:
            lista_prod_precios.append(f"{dic_productos[key][0]}--{key}")
    if not lista_prod_precios:
        print("No hay productos que esten en el rango de precios")
    else:
        lista_prod_precios.sort()
        print(lista_prod_precios)
            

def buscar_codigo(codigo, dic_productos, dic_ventas):
    for key, value in dic_productos.items():
        if key.upper() == codigo.upper():
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, dic_productos, dic_ventas):
    if buscar_codigo(codigo, dic_productos, dic_ventas):
        dic_ventas[codigo.upper()][0] = nuevo_precio
        return True
    else:
        return False

def validar_codigo(codigo, dic_productos, dic_ventas):
    if codigo.strip()!= "" and codigo not in dic_productos:
        return True
    else:
        return False

def validar_nombre(nombre_producto, dic_productos, dic_ventas):
    if nombre_producto.strip() != "":
        return True
    else:
        return False

def validar_categoria(categoria, dic_productos, dic_ventas):
    if categoria.strip() != "":
        return True
    else:
        return False

def validar_tamano(tamano, dic_productos, dic_ventas):
    if tamano.lower() not in ["chico", "mediano", "grande"]:
        return False
    else:
        return True

def validar_tipo_leche(tipo_leche, dic_productos, dic_ventas):
    if tipo_leche.strip() != "":
        return True
    else:
        return False

def validar_es_temporada(es_temporada, dic_productos, dic_ventas):
    if es_temporada.lower() == "s" or es_temporada.lower() == "n":
        return True
    else:
        return False

def validar_precio(precio, dic_productos, dic_ventas):
    if precio > 0:
        return True
    else:
        return False

def validar_stock(stock, dic_productos, dic_ventas):
    if stock >= 0:
        return True
    else:
        return False

def agregar_producto(codigo, nombre_producto, categoria, tamano, tipo_leche, es_temporada, precio, stock_disponible, dic_productos, dic_ventas):
    if validar_codigo(codigo, dic_productos, dic_ventas):
        dic_productos[codigo] = [nombre_producto.title(), categoria.title(), tamano.title(), tipo_leche.title(), True if es_temporada == "s" else False]
        dic_ventas[codigo] = [precio, stock_disponible]
        return True
    else:
        return False

def eliminar_producto(codigo, dic_productos, dic_ventas):
    if buscar_codigo(codigo, dic_productos, dic_ventas):
        del dic_productos[codigo]
        del dic_ventas[codigo]
        return True
    else:
        return False

#codigo principal
productos = {}

ventas = {}
opcion = 99999999999999999

while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        if not productos:
            print("No hay productos registrados en el sistema para consultar stock.")
        else:
            print("STOCK POR CATEGORIA")
            categoria = input("Ingrese la categoria a buscar: ")
            stock_categoria(categoria, productos, ventas)

    elif opcion == 2:
        if not productos:
            print("No hay productos registrados en el sistema para buscar.")
        else:
            print("BUSQUEDA DE PRODUCTOS POR RANGO DE PRECIO")
            while True:
                try:
                    precio_min = int(input("Ingrese el precio minimo: "))
                    precio_max = int(input("Ingrese el precio maximo: "))
                    if precio_min < 0 or precio_max < 0:
                        raise ValueError
                    if precio_min > precio_max:
                        print("El precio minimo no puede ser mayor al precio maximo")
                    else:
                        break
                except ValueError:
                    print("Debe ingresar valores enteros.")
                
                
            busqueda_precio(precio_min, precio_max, productos, ventas)

    elif opcion == 3:
        if not productos:
            print("No hay productos registrados en el sistema para actualizar.")
        else:
            while True:
                print("ACTUALIZAR PRECIO DE PRODUCTO")
                codigo_producto = input("Ingrese el codigo del producto: ")
                while True:
                    try:
                        precio_nuevo = int(input("Ingrese el precio nuevo del producto: "))
                        if precio_nuevo <= 0:
                            raise ValueError
                        else:
                            break
                    except ValueError:
                        print("Debe ingresar un numero entero positivo.")
                actualizacion = actualizar_precio(codigo_producto, precio_nuevo, productos, ventas)
                if actualizacion:
                    print("Precio actualizado")
                else:
                    print("El codigo no existe")
                while True:
                    respuesta = input("¿Desea actualizar otro precio (s/n)?").lower()
                    if respuesta not in ["si","no","s","n"]:
                        print("Debe ingresar una opcion valida (s/n)")
                        continue
                    else:
                        break
                if respuesta == "n":
                    break

    elif opcion == 4:
        print("AGREGAR PRODUCTO")
        while True:
            codigo_producto = input("Ingrese el codigo del producto: ").upper()
            if validar_codigo(codigo_producto, productos, ventas):
                break
            else:
                print("ERROR: Codigo ingresado invalido o ya existe en el registro.")
        while True:
            nombre_producto = input("Ingrese el nombre del producto: ")
            if validar_nombre(nombre_producto, productos, ventas):
                break
            else:
                print("ERROR: Nombre ingresado invalido.")
        while True:
            categoria = input("Ingrese la categoria del producto: ")
            if validar_categoria(categoria, productos, ventas):
                break
            else:
                print("ERROR: Categoria ingresada invalida.")
        while True:
            tamano = input("Ingrese el tamano del producto (chico/mediano/grande): ")
            if validar_tamano(tamano, productos, ventas):
                break
            else:
                print("ERROR: Tamano ingresado invalido (chico/mediano/grande).")
        while True:
            tipo_leche = input("Ingrese el tipo de leche del producto: ")
            if validar_tipo_leche(tipo_leche, productos, ventas):
                break
            else:
                print("ERROR: Tipo de leche ingresada no valida.")
        while True:
            es_temporada = input("Es temporada de este producto? (s/n)")
            if validar_es_temporada(es_temporada, productos, ventas):
                break
            else:
                print("ERROR: Respuesta ingresada no valida (s/n).")
        while True:
            try:
                precio_producto = int(input("Ingrese el precio del producto: "))
                if validar_precio(precio_producto, productos, ventas):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("ERROR: Debe ingresar un numero mayor a cero.")
        
        while True:
            try:
                stock_producto = int(input("Ingrese el stock del producto: "))
                if validar_stock(stock_producto, productos, ventas):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("ERROR: Debe ingresar un numero mayor o igual a cero.")
        producto_agregado = agregar_producto(codigo_producto,nombre_producto,categoria,tamano,tipo_leche,es_temporada,precio_producto,stock_producto,productos, ventas)
        if producto_agregado:
            print("Producto agregado.")
        else:
            print("El codigo ya existe.")

    elif opcion == 5:
        if not productos:
            print("No hay productos registrados en el sistema para eliminar.")
        else:
            print("ELIMINAR PRODUCTO")
            while True:
                codigo_eliminar = input("Ingrese el codigo del producto que desea eliminar: ").upper()
                if codigo_eliminar.strip() != "":
                    break
                else:
                    print("ERROR: El codigo ingresado es invalido.")
            eliminacion = eliminar_producto(codigo_eliminar, productos, ventas)
            if eliminacion:
                print("Producto eliminado.")
            else:
                print("El codigo no existe.")

    elif opcion == 6:
        print("PROGRAMA FINALIZADO")
