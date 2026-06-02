"""
Sistema de Control de Inventario — Distribuidora de Bebidas
-----------------------------------------------------------

Contexto: Una distribuidora local requiere un software de consola para administrar las cajas de bebidas disponibles en su bodega central. El sistema inicia con un 
stock inicial de 150 cajas disponibles precargadas y permite al operario despachar pedidos, procesar devoluciones y auditar los movimientos de la sesión de manera 
cíclica.

    - Requisito 1: Inicio y Persistencia del Programa
        -> Al iniciar la ejecución, el sistema debe imprimir una única vez el mensaje:
           "¡Bienvenido al sistema de control de inventario de la Distribuidora Central!"

El stock arranca automáticamente en 150 unidades. A continuación, debe desplegarse el Menú Principal y mantenerse activo de forma cíclica e indefinida 
hasta que se seleccione la opción de Salir.

    - Requisito 2: Menú Principal y Manejo de Excepciones
        -> El menú interactivo debe mostrar las siguientes opciones exactas en pantalla:

                1.- Stock disponible
                2.- Despachar productos
                3.- Devolver productos
                4.- Historial de movimientos
                5.- Salir

Validación del Menú: Si el operario ingresa una opción no válida (letras, espacios vacíos o números fuera del rango 1-5), el programa debe capturar el error 
obligatoriamente con un bloque try-except, emitir un mensaje de aviso claro y volver a presentar el menú sin romper la ejecución.

    - Requisito 3: Funcionalidades Detalladas del Sistema 
        -> Opción 1 — Stock Disponible: Muestra la cantidad actual de cajas remanentes en la bodega central. Este valor debe actualizarse inmediatamente 
        tras cada transacción exitosa.

        -> Opción 2 — Despachar Productos: Solicita al usuario la cantidad de cajas a retirar. Se debe validar mediante excepciones que el ingreso sea numérico, 
        mayor a 0 y que no supere el stock disponible actual. De ser exitoso, se descuenta del stock y se añade al historial neto.
        -> Candado crítico: Si el stock actual es 0, debe denegar el acceso directo con un mensaje de error sin solicitar datos.

        -> Opción 3 — Devolver Productos: Solicita la cantidad de cajas devueltas por el cliente. Debe validarse que el número sea mayor a 0 y que la suma del stock 
        actual más la devolución no sobrepase las 150 cajas máximas de la capacidad física de la bodega. De ser exitoso, aumenta el stock y se resta del historial.
        -> Candado crítico: Si la bodega ya está en su capacidad máxima (150), debe arrojar un error inmediato.

        -> Opción 4 — Historial de Movimientos: Muestra el total acumulado neto de transacciones de la sesión. Se calcula restando las cajas devueltas a las cajas 
        despachadas exitosamente (puede ser un número negativo o positivo).

        -> Opción 5 — Salir: Termina la ejecución rompiendo el ciclo y mostrando el mensaje exacto:
        "Gracias por utilizar nuestro software, hasta la próxima."
"""

# ----------------- Bloque variables -----------------

stock = 150
historial = 0

# ----------------- Bloque ejecución -----------------

print ("¡Bienvenido al sistema de control de inventario de la Distribuidora Central!")

menu = True

while menu:
    print("\n-------------<<< MENU >>>-------------")
    print("1.- Stock disponible")
    print("2.- Despachar productos")
    print("3.- Devolver productos")
    print("4.- Historial de movimientos")
    print("5.- Salir")

    opc = False
    while not opc:
        try: 
            opcion = int(input("Ingrese la opción: "))
            
            if opcion < 1 or opcion > 5:
                print("¡Opción inválida! Por favor, ingresa un número entero entre 1 y 5 para continuar.")
            else:
                opc = True

        except ValueError:
            print("Debe ingresar un número entero.")
    
    if opcion == 1:
        print(f"\nEl stock disponible es de {stock} cajas.")
    
    if opcion == 2:
        if stock == 0:
            print("\n¡ERROR! No hay stock disponible para despachar.")
        
        else:
            opc2 = False
            while not opc2:
                try: 
                    cantidad = int(input("\nIngrese la cantidad de cajas a despachar: "))

                    if cantidad <= 0:
                        print("¡Cantidad inválida! Ingresa un número entero positivo para continuar.")
                    
                    elif cantidad > stock:
                        print(f"¡ERROR! No se puede despachar {cantidad} cajas. El stock disponible es de {stock} cajas.")
                    
                    elif cantidad <= stock:
                        stock = stock - cantidad
                        historial = historial + cantidad
                        print(f"¡Despacho exitoso! Se han despachado {cantidad} cajas")
                        opc2 = True

                except ValueError:
                    print("Debe ingresar un número entero.")
                
    if opcion == 3:

        if stock == 150:
            print("\n¡ERROR! No se pueden aceptar más devoluciones.")
        
        else:
            opc3 = False
            while not opc3:
                try:
                    devolucion = int(input("\nIngrese la cantidad de cajas a devolver: "))

                    if devolucion <= 0:
                        print("¡Cantidad inválida! Ingresa un número entero positivo para continuar.")
                    
                    elif devolucion > historial:
                        print(f"¡ERROR! No se pueden devolver {devolucion} cajas. El historial neto de transacciones es de {historial} cajas.")
                    
                    elif devolucion <= historial:
                        stock = stock + devolucion
                        historial = historial - devolucion
                        print(f"¡Devolución exitosa! Se han devuelto {devolucion} cajas.")
                        opc3 = True

                except ValueError:
                    print("Debe ingresar un número entero.")

    if opcion == 4:
        print(f"\nEl historial neto de transacciones de la sesión es de {historial} cajas con {devolucion} cajas devueltas y {historial + devolucion} cajas despachadas.")
    
    if opcion == 5:
        print("\nGracias por utilizar nuestro software, hasta la próxima.")
        menu = False


