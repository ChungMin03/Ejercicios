"""EJERCICIO 1: Sistema de Control de Equipaje
Contexto: Eres desarrollador en una aerolínea comercial. Tu jefe te solicita crear un programa en Python que
 registre de manera ordenada el equipaje de bodega para los pasajeros de un vuelo,
   valide estrictamente los datos de las maletas y genere un resumen de carga crítico antes del despegue.

Requisito 1 — Cantidad de maletas a registrar
El programa debe preguntar al usuario cuántas maletas desea registrar en el counter para este vuelo.

Este valor debe ser obligatoriamente un número entero positivo (mayor a 0).

Si el usuario ingresa un valor inválido (letras, símbolos, cero o números negativos),
 el programa debe capturar el error con manejo de excepciones, mostrar el siguiente mensaje exacto 
 y repetir la solicitud hasta que el dato sea correcto:
"¡Cantidad inválida! Ingresa un entero positivo para continuar."

Requisito 2 — Datos de cada maleta
Para cada maleta, el programa debe solicitar de forma sucesiva e independiente los siguientes datos:

a) Código de Etiqueta (texto - String): Debe tener una longitud de al menos 5 caracteres y no debe contener espacios en blanco.
Si no cumple con alguna de estas dos condiciones lógicas,
se debe repetir la solicitud de la etiqueta sin alterar los datos previos. (Ejemplos válidos: LAT99, SKY001, VLUX8)

b) Peso de la Maleta (número entero positivo): El usuario ingresa el peso estimado en kilogramos.
Si se ingresa un valor no numérico o menor/igual a cero, se debe capturar el error,
mostrar el siguiente mensaje exacto y repetir la solicitud:
"¡Error de pesaje! Ingresa un número entero positivo para el peso de la maleta."

Requisito 3 — Clasificación automática del equipaje
Una vez ingresado y validado el peso de la maleta en curso, el sistema debe determinar su categoría de forma interna:
Condición de Carga|Clasificación
Peso estrictamente mayor a 23 kilogramos|SOBREPESO
Peso menor o igual a 23 kilogramos|ESTÁNDAR 
El programa debe mantener contadores numéricos separados para maletas con Sobrepeso y maletas Estándar,
incrementándose dinámicamente.

Requisito 4 — Resumen final de la flota
Al finalizar por completo el registro de la cantidad de maletas indicada en el Requisito 1,
el programa debe desplegar en pantalla el siguiente mensaje de cierre con los contadores correspondientes:
"¡El vuelo cuenta con X maletas con Sobrepeso y Y maletas Estándar! ¡Carga distribuida con éxito!"
(Donde X e Y corresponden a los contadores acumulados durante el procesamiento)."""


'''
#Ejercicio 1
#-----------------bloque de variables e inputs--------------------
#entrada de la cantidad de maletas(Requisito 1)
flag_cant = False
while not flag_cant:
    error_quant = ""
    try:
        quant = int(input("Ingrese la cantidad de maletas que desea registrar: ").replace(" ",""))
        if quant < 1:
            raise ValueError
        else:
            flag_cant = True

    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    
print(f"Usted ingresará {quant} maletas")
#----------------------------------------------

#variables contadoras del peso
heavy = 0
normal = 0
#-----------------------------

#variable contadora de maletas
n = 0
#-----------------------------

#etiquetado y peso de las maletas(Requisito 2)
while n != quant:
    n += 1
    try:
        tag = input(f"Ingrese la etiqueta de su maleta N°{n}: ")
        if len(tag) < 5:
            raise ValueError
        
    except ValueError:
        print("Etiqueta invalida, Debe tener al menos 5 caracteres sin contar espacios")

    #bandera para dentener el while de a continuacion
    flag_weight = True
    #------------------------------------------------

    #while para capturar errores con el peso sin reiniciar el primer while
    while flag_weight:
        try:
            weight = int(input(f"Ingrese el peso de la maleta N°{n} en KG: "))
            if weight < 1:
                raise ValueError
            
            else:
                flag_weight = False
        except ValueError:
            print("¡Error de pesaje! Ingresa un número entero positivo para el peso de la maleta")
    #---------------------------------------------------------------------  
      
#----------------------------------------------

#-----------------bloque de ejecucion---------------------
#parte del mismo while pero comple la funcion de diferenciar los pesos,
#por lo que pasa a ser parte de la ejecucion.
    if weight < 24:
        normal += 1
    elif weight > 23:
        heavy += 1
#-----------------bloque de prints-------------------
print(f"¡El vuelo cuenta con {heavy} maletas con Sobrepeso y {normal} maletas Estándar! ¡Carga distribuida con éxito!")
'''






"""EJERCICIO 2: Sistema de Control de Inventario — Distribuidora de Bebidas
Contexto: Una distribuidora local requiere un software de consola para administrar las cajas de bebidas disponibles
en su bodega central. El sistema inicia con un stock inicial de 150 cajas disponibles precargadas y permite al operario
despachar pedidos, procesar devoluciones y auditar los movimientos de la sesión de manera cíclica.

Requisito 1 — Inicio y Persistencia del Programa
Al iniciar la ejecución, el sistema debe imprimir una única vez el mensaje:
"¡Bienvenido al sistema de control de inventario de la Distribuidora Central!"

El stock arranca automáticamente en 150 unidades. A continuación,
debe desplegarse el Menú Principal y mantenerse activo de forma cíclica e indefinida hasta que se seleccione la opción de Salir.

Requisito 2 — Menú Principal y Manejo de Excepciones
El menú interactivo debe mostrar las siguientes opciones exactas en pantalla:

Stock disponible

Despachar productos

Devolver productos

Historial de movimientos

Salir

Validación del Menú: Si el operario ingresa una opción no válida (letras, espacios vacíos o números fuera del rango 1-5),
el programa debe capturar el error obligatoriamente con un bloque try-except,
emitir un mensaje de aviso claro y volver a presentar el menú sin romper la ejecución.

Requisito 3 — Funcionalidades Detalladas del Sistema
Opción 1 — Stock Disponible: Muestra la cantidad actual de cajas remanentes en la bodega central.
Este valor debe actualizarse inmediatamente tras cada transacción exitosa.

Opción 2 — Despachar Productos: Solicita al usuario la cantidad de cajas a retirar.
Se debe validar mediante excepciones que el ingreso sea numérico, mayor a 0 y que no supere el stock disponible actual.
De ser exitoso, se descuenta del stock y se añade al historial neto.
*Candado crítico: Si el stock actual es 0, debe denegar el acceso directo con un mensaje de error sin solicitar datos.

Opción 3 — Devolver Productos: Solicita la cantidad de cajas devueltas por el cliente.
Debe validarse que el número sea mayor a 0 y que la suma del stock actual más la devolución
no sobrepase las 150 cajas máximas de la capacidad física de la bodega.
De ser exitoso, aumenta el stock y se resta del historial.
*Candado crítico: Si la bodega ya está en su capacidad máxima (150), debe arrojar un error inmediato.

Opción 4 — Historial de Movimientos: Muestra el total acumulado neto de transacciones de la sesión.
Se calcula restando las cajas devueltas a las cajas despachadas exitosamente (puede ser un número negativo o positivo).

Opción 5 — Salir: Termina la ejecución rompiendo el ciclo y mostrando el mensaje exacto:
"Gracias por utilizar nuestro software, hasta la próxima."""


#Ejercicio 2

#requisito 1
#-----------------bloque de variables------------------
#mensaje de intruduccion al programa 
print("¡Bienvenido al sistema de control de inventario de la Distribuidora Central!")
#-----------------------------------
cajas = 150
opcion = 0
max_cajas = 150
#listas con datos de despachos y devoluciones
historial_despacho = []
historial_devolucion = []
#contadores de instancias de ventas y devoluciones
cant_desp = 0
cant_devo = 0
#acumuladores de ventas y devoluciones
venta = 0
devolucion = 0
#------------------------------------------------------

#-----------------bloque de ejecucion----------------------
#requisito 2
#menú
while opcion != 5:
    print("----------------------------")
    print("1.- Stock disponible")
    print("2.- Despachar productos")
    print("3.- Devolver productos")
    print("4.- Historial de movimientos")
    print("5.- Salir")
    print("----------------------------")


    error_menu = ""
    try:
        opcion = int(input("Ingrese la opcion que desea usar: "))
        if opcion < 1 or opcion > 5:
            error_menu += "La opcion debe estar entre 1 y 5"

    except ValueError:
        if error_menu == "":
            print("un valor numerico valido")

        else:
            print(error_menu)

    #opcion 1, cantidad de cajas actuales
    if opcion == 1:
        print(f"Actualmente tenemos un stock de: {cajas} cajas")
    #------------------------------------

    #opcion 2, gestor de ventas
    if opcion == 2:
        if cajas == 0:
            print("Stock acabado")

        else:
            cant_desp += 1

            #creamos un while para no terminar la instancia de devolucion con los errores
            flag_despacho = True
            while flag_despacho:
                #almacen de errores, se guardan para mostrarlos mas adelante en los prints
                error_despacho = ""
                try:
                    desp = int(input("Ingrese la cantidad de cajas a despachar: "))
                    if desp < 1:
                        error_despacho += "Debe ingresar un valor numerico positivo\n"
                        raise ValueError
                    
                    if desp > cajas:
                        error_despacho += "No puede despachar mas cajas de las que hay"
                        raise ValueError
                    
                    else:
                        historial_despacho.append(desp)
                        cajas -= desp 
                        venta += desp
                        flag_despacho = False

                except ValueError:
                    if error_despacho == "":
                        print("ERROR: Ingrese valores numericos")

                    elif error_despacho != "":
                        print(f"ERROR: {error_despacho}")
    #--------------------------

    #opcion 3, gestor de devoluciones
    if opcion == 3:
        if cajas == max_cajas:
            print("Stock de cajas al máximo, no se aceptan devoluciones")
        
        elif cajas < max_cajas:
            cant_devo += 1

            #creamos un while para no terminar la instancia de devolucion con los errores
            flag_devolucion = True
            while flag_devolucion:
                #almacen de errores, se guardan para mostrarlos mas adelante en los prints
                error_devo = ""
                try:
                    devo = int(input("Ingrese la cantidad de cajas a devolver"))
                    if devo < 1:
                        error_devo += "Debe ingresar valores numericos positivos\n"
                        raise ValueError
                    
                    if (devo + cajas) > max_cajas:
                        error_devo += "Las devoluciones no pueden superar el maximo del Stock"
                        raise ValueError
                    
                    else:
                        historial_devolucion.append(devo)
                        cajas += devo
                        devolucion += devo
                        flag_devolucion = False

                except ValueError:
                    if error_devo == "":
                        print("ERROR: Ingrese valores numericos")
                    elif error_devo != "":
                        print(f"ERROR: {error_devo}")
    #--------------------------------


    #opcion 4, historial de ventas
    if opcion == 4:
        print(f"Ventas netas: {venta-devolucion}")
        print(f"Despachos totales: {venta}, en {cant_desp} instancias de venta")
        print(f"Devoluciones totales: {devolucion}, en {cant_devo} instancias de devoluciones")
        print(f"Cantidades despachadas: {historial_despacho}")
        print(f"Cantidades devueltas: {historial_devolucion}")
    #------------------------------

    #opcion 5, despedida
    if opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
    #-------------------
        