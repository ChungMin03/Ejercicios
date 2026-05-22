
#---------------- DECLARACION DE VARIABLES --------------
vehiculo_flag = False
errores = ""
pesado = 0
ligero = 0

#--------------- BLOQUE DE EJECUCION ------------------

#INICIO EJERCICIO 1
print("------------------- INICIO EJERCICIO 1 ---------------------------")

#REQUISITO 1
while not vehiculo_flag:
    try:
        cant_vehi = int(input("Ingrese la cantidad de vehículos que desea registrar: "))
        if cant_vehi < 1:
            raise ValueError
        else:
            vehiculo_flag = True
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        print("---------------------------------------------------------------------")

#REQUISITO 2
count_vehi = 1
while count_vehi <= cant_vehi:
    print(f"--------- Vehículo {count_vehi} de {cant_vehi} -------------")
    placa = input("Ingrese la placa vehicular: ")
    if len(placa) < 6 or (" " in placa):
        count_vehi = count_vehi
        print("¡Placa inválida! Ingrese una placa con al menos 6 caracteres y sin espacios. ")
        continue
    


    capacidad_flag = False
    while not capacidad_flag:
        try:
            capacidad_carga = int(input("Ingrese la capacidad de carga del vehículo (toneladas): "))
            
            if capacidad_carga <= 0:
                raise ValueError
            else:
                capacidad_flag = True
                #REQUISITO 3
                if capacidad_carga > 55:
                    pesado += 1
                else:
                    ligero += 1

            
        except ValueError:
            print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga.")


    count_vehi += 1

#REQUISITO 4
print(f"¡La flota cuenta con {pesado} vehículos Pesados y {ligero} vehículos Ligeros! ¡Rutas asignadas!")
print("------------------- FIN EJERCICIO 1 ---------------------------")
print("\n")


"""Requisito 1 — Inicio del programa
•	Al iniciar, el programa debe mostrar el mensaje: ¡Bienvenido al sistema de gestión de localidades del Teatro Municipal!
•	El sistema parte con 200 localidades disponibles precargadas.
•	A continuación, debe mostrar el Menú Principal y mantenerse activo hasta que el usuario elija Salir.

Requisito 2 — Menú Principal
El menú principal debe mostrar las siguientes opciones:

Opción	Descripción
1	Localidades disponibles
2	Vender localidades
3	Devolver localidades
4	Historial de ventas
5	Salir

Si el usuario ingresa una opción no válida (letras u opción fuera de rango), el programa debe capturar el error con manejo de excepciones y mostrar un mensaje claro antes de volver a mostrar el menú.

Requisito 3 — Funcionalidades del sistema
Opción 1 — Localidades Disponibles
•	Muestra la cantidad actual de localidades disponibles en el teatro.
•	Este valor debe reflejar los cambios producidos por ventas y devoluciones.

Opción 2 — Vender Localidades
•	El sistema solicita la cantidad de localidades a vender.
•	Validaciones requeridas:
•	La cantidad debe ser mayor a 0.
•	No debe superar las localidades disponibles actuales.
•	Si la venta es exitosa: se descuenta del disponible y se suma al historial de ventas.

Opción 3 — Devolver Localidades
•	El sistema solicita la cantidad de localidades a devolver.
•	Validaciones requeridas:
•	La cantidad debe ser mayor a 0.
•	No puede exceder las 200 localidades (máximo del teatro).
•	Si la devolución es exitosa: se suma al disponible y se resta del historial.

Opción 4 — Historial de Ventas
•	Muestra el total de ventas netas realizadas durante la sesión (ventas menos devoluciones).

Opción 5 — Salir
•	Finaliza el programa mostrando el mensaje:

"Gracias por utilizar nuestro software, hasta la próxima."

"""

#----------------DECLARACION DE VARIABLES ------------------
max_localidades = 200 #NO SE MODIFICA
cant_disponibles = 200
count_ventas = 0

#INICIO EJERCICIO 2
print("------------------- INICIO EJERCICIO 2 ---------------------------")


#Bienvenida
print("**************************************************************************")
print("* ¡Bienvenido al sistema de gestión de localidades del Teatro Municipal! *")
print("**************************************************************************")

#---------------BLOQUE DE EJECUCION---------------------------


opcion = 984348924828432984993248932489329432.1

while opcion != 5:
    flag_1 = False
    print("1. Localidades Disponibles")
    print("2. Vender Localidades")
    print("3. Devolver Disponibles")
    print("4. Historial de Ventas")
    print("5. Salir")
    print("**************************************************")
    while not flag_1:
        try:
            opcion = int(input("Ingrese una opcion (1/5): "))
            if opcion < 1 or opcion > 5:
                raise ValueError
            else:
                flag_1 = True
        except ValueError:
            print("ERROR: - Debe ingresar un numero entero entre 1 y 5.")
            print("---------------------------------------------------------------------")
    
    if opcion == 1:
        print(f"Localidades disponibles: {cant_disponibles}")

    elif opcion == 2:
        if cant_disponibles == 0:
            print("ERROR: - No quedan localidades disponibles. Todas han sido vendidas.")
        else:
            flag_2 = False
            while not flag_2:
                errores1 = ""
                try:
                    cant_ventas = int(input("Cantidad de Localidades a comprar: "))
                    if cant_ventas < 1:
                        errores1 += "- Debe ingresar un numero entero mayor a cero. Ejemplo: 2.\n"
                        raise ValueError
                    if cant_ventas > cant_disponibles:
                        errores1 += f"- Excede la cantidad maxima de Localidades disponible: {cant_disponibles}"
                        raise ValueError
                    if cant_ventas >= 1 and cant_ventas <= cant_disponibles:
                        flag_2 = True
                        cant_disponibles -= cant_ventas
                        count_ventas += cant_ventas
                except ValueError as error:
                    if errores1 != "":
                        print(f"ERROR: {errores1}")
                    else:
                        print("ERROR: - Debe ingresar un numero entero mayor a cero.")
                    print("---------------------------------------------------------------------")

    

    elif opcion == 3:
        if cant_disponibles == max_localidades:
            print("ERROR: - Maximo de localidades disponibles, no se pueden realizar devoluciones.")
        else:
            flag_3 = False
            while not flag_3:
                errores2 = ""
                try:
                    devolucion = int(input("¿Cuantas Localidades devolverá?: "))
                    if devolucion + cant_disponibles > max_localidades:
                        errores2 += f"- No se pueden devolver {devolucion} entradas, excede el maximo de entradas totales."
                        raise ValueError
                    if devolucion < 1:
                        errores2 += f"- Debe ingresar un numero mayor a cero. Ejemplo: 2."
                        raise ValueError
                    else:
                        flag_3 = True
                    cant_disponibles += devolucion
                    count_ventas -= devolucion
                except ValueError:
                    if errores2 != "":
                        print(f"ERROR: {errores2}")
                    else:
                        print("ERROR: - Debe ingresar un numero entero mayor a cero. Ejemplo: 2.")
                    print("---------------------------------------------------------------------")
        

    elif opcion == 4:
        print(f"Cantidad de localidades vendidas hasta ahora: {count_ventas}")
        print("---------------------------------------------------------------------")
    
    elif opcion == 5:
        print("Gracias por usar nuestro software, hasta la proxima")
        print("---------------------------------------------------------------------")
    else: #Este else nunca se llega a ejecutar ya que el if opcion < 1 or opcion > 5: Raise ValueError del principio cubre este error antes :/
        print("ERROR: - Debe seleccionar una opcion del 1 al 5")
        print("---------------------------------------------------------------------")

print("------------------- FIN EJERCICIO 2 ---------------------------")