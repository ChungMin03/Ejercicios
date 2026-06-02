"""#EJERCICIO 1
#--------------- BLOQUE DE VARIABLES ---------------------
premium = 0
estandar = 0

#-------------- BLOQUE DE EJECUCION --------------------
#requisito 1
flag = False
while not flag:
    try:
        cant_registros = int(input("Ingrese la cantidad de clientes que registrara: "))
        if cant_registros <= 0:
            raise ValueError
        else:
            flag = True
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        

#requisito 2
for i in range(1, cant_registros + 1):
    flag2 = False
    while not flag2:
        errores = ""
        print(f"-------------- Registro usuario {i} --------------------")
        try:
            rut = input(f"Ingrese su rut, sin guion ni puntos: ")
            if len(rut) < 8:
                print("\n - Debe tener al menos 8 caracteres.")
                if " " in rut:
                    print("\n - No debe contener espacios.")
                    continue
                continue
            if " " in rut:
                print("\n - No debe contener espacios.")
                if len(rut) < 8:
                    print("\n - Debe tener al menos 8 caracteres.")
                    continue
                continue

            if len(rut) >= 8 and " " not in rut:
                flag2 = True
                flag3 = False
                while not flag3:
                    try:
                        saldo_inicial = int(input("Ingrese su saldo: "))
                        if saldo_inicial <= 0:
                            raise ValueError
                        else:
                            flag3 = True
                            #requisito 3
                            if saldo_inicial > 1000000:
                                premium += 1
                            else:
                                estandar += 1
                    except ValueError:
                        print("¡Error bancario! Ingresa un saldo inicial válido (entero positivo).")
        except ValueError:
            print(f"ERRORES: {errores}")
        
        
                
#requisito 4
print(f"¡Registro completado! {premium} clientes Premium y {estandar} clientes Estándar incorporados al sistema.")

"""

"""Ejercicio 2
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

#---------------- BLOQUE DE VARIABLES --------------------
cajas_fijas = 150 #no se modifica
stock_disponible = 150
count_despacho = 0
count_devoluciones = 0

#--------------- BLOQUE DE EJECUCION ---------------------
print("¡Bienvenido al sistema de control de inventario de la Distribuidora Central!") #mensaje de bienvenida

opcion = 21921094124211
while opcion != 5:
    print("--------------- [MENU PRINCIPAL] ---------------")
    print("1.- Stock disponible.")
    print("2.- Despachar productos.")
    print("3.- Devolver productos.")
    print("4.- Historial de movimientos.")
    print("5.- Salir.")
    print("------------------------------------------------")
    
    flag_menu = False
    while not flag_menu:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 5:
                raise ValueError
            else:
                flag_menu = True
        except ValueError:
            print("Opcion invalida, ingrese un numero entre 1 y 5.")
            print("-----------------------------------------------")
            
    if opcion == 1:
        print(f"Stock disponible: {stock_disponible}.")
        print("--------------------------------------")
    elif opcion == 2:
        if stock_disponible == 0:
            print("No hay stock disponible.")
            print("------------------------")
        else:
            flag_despacho = False
            while not flag_despacho:
                try:
                    cant_despacho = int(input("Ingrese la cantidad de cajas a retirar: "))
                    if cant_despacho > stock_disponible:
                        print(f"Cantidad invalida, supera el stock disponible: {stock_disponible}.")
                        print("-------------------------------------------------------------------")
                    elif cant_despacho < 1:
                        print("Cantidad invalida, ingrese un numero mayor a 0.")
                        print("-----------------------------------------------")
                    else:
                        flag_despacho = True
                        count_despacho += cant_despacho
                        stock_disponible -= cant_despacho
                except ValueError:
                    print("Cantidad invalida, debe ingresar un valor numerico.")
                    print("---------------------------------------------------")
    elif opcion == 3:
        if stock_disponible == cajas_fijas:
            print("El stock esta en su capacidad maxima.")
            print("-------------------------------------")
        else:
            flag_devolucion = False
            while not flag_devolucion:
                try:
                    cant_devolucion = int(input("Ingrese la cantidad de cajas a devolver: "))
                    if cant_devolucion + stock_disponible > cajas_fijas:
                        print(f"Cantidad invalida, supera el stock. Puede realizar la devolucion de hasta {cajas_fijas - stock_disponible} cajas.")
                        print("------------------------------------------------------------------------------------------------------------------")
                    elif cant_devolucion < 1:
                        print("Cantidad invalida, ingrese un numero mayor a 0.")
                        print("-----------------------------------------------")
                    else:
                        flag_devolucion = True
                        stock_disponible += cant_devolucion
                        count_devoluciones += cant_devolucion
                except ValueError:
                    print("Cantidad invalida, debe ingresar un valor numerico.")
                    print("---------------------------------------------------")
                    
    elif opcion == 4:
        total_neto = count_despacho - count_devoluciones
        print(f"Total acumulado neto: {total_neto}.")
        print("------------------------------------")
        
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        print("--------------------------------------------------------")