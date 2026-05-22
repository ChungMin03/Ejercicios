"""
Registro 1
El programa debe preguntar al usuario cuántos vehículos desea registrar en esta sesión.
•	Este valor debe ser un número entero positivo (mayor a 0).
•	Si el usuario ingresa un valor inválido (letras, cero o negativo),
se debe mostrar el siguiente mensaje y volver a pedir el dato:

"¡Cantidad inválida! Ingresa un entero positivo para continuar."

Registro 2
Para cada vehículo, el programa debe solicitar los siguientes datos:

a) Placa Vehicular (texto - String)
•	Debe tener al menos 6 caracteres.
•	No debe contener espacios.
•	Si no cumple alguna condición, se debe volver a pedir la placa.
Ejemplos válidos: TRK001HD, VANMAX6, CARLITE2

b) Capacidad de Carga (número entero positivo)
•	El usuario ingresa la capacidad de carga en toneladas.
•	Si se ingresa un valor inválido (letras, cero o negativo), se muestra
el siguiente mensaje y se repite la solicitud:

"¡Error logístico! Ingresa un número entero positivo para la capacidad de carga."

Registro 3
Una vez ingresada la capacidad de carga, el programa debe clasificar automáticamente el vehículo:

Condición	Clasificación
Capacidad > 55 toneladas	PESADO
Capacidad ≤ 55 toneladas	LIGERO

El programa debe mantener contadores separados para vehículos Pesados y Ligeros durante todo el proceso.


"""
'''
#-----------------bloque de ejecucion-------------------
try:
    flag = False
    while not flag:
        quant = int(input("Ingrese la cantidad de vehiculos a registrar: "))
        flag = True
        if quant < 1:
            raise ValueError
        
except ValueError:
    print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

error = ""
peso = ""
heavy = 0
light = 0

for i in range(1,(quant+1)):
    flag1 = False
    while not flag1:
        plate = input("Ingrese la placa del auto: ")
        if len(plate) < 6:
            error += ("Cantidad de caracteres incorrectos\n")

        if " " in plate:
            error += ("No debe contener espacios vacios\n")

        if error != "":
            print(error)
        
        else:
            flag1 = True
    try: 
        flag2 = False 
        while not flag2:
            weight = int(input("Ingrese la capacidad de carga del vehiculo: "))
            flag2 = True

            if weight < 1:
                raise ValueError
            
    except ValueError:
        print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga.")
        
        if weight > 55:
            peso = "pesado"
            heavy += 1

        elif weight <= 55:
            peso = "Ligero"
            light += 1

print(f"{heavy} Pesado y {light} Ligero")

'''


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

Si el usuario ingresa una opción no válida (letras u opción fuera de rango), el programa debe capturar el error
con manejo de excepciones y mostrar un mensaje claro antes de volver a mostrar el menú.

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

#requisito 1
print("¡Bienvenido al sistema de gestión de localidades del Teatro Municipal!")
cant_localidades = 200
max_locaidades = 200


#requisito 2 (Menú)
opcion = 0
while opcion != 5:
    error_menu = ""
    print("1.- Localidades disponibles")
    print("2.- Vender localidades")
    print("3.- Devolver localidades")
    print("4.- Historial de ventas")
    print("5.- Salir")
    
    try:
        flag1 = False
        while not flag1:
            opcion = int(input("Ingrese la opcion que desea usar: "))
            flag1 = True
            if opcion<1 or opcion>5:
                raise ValueError
    except ValueError as error:
        print("Ingrese un valor numerico entero y entre 1 y 5")

    if opcion == 1:
        print(f"Quedan un total de {cant_localidades} de localidades")

    elif opcion == 2:
        if cant_localidades == 0:
            print("No hay localidades disponibles")

        elif cant_localidades != 0:
            flag2 = False
            while not flag2:
                error = ""
                try: 
                    venta = int(input("Ingrese la cantidad de localidades que desea comprar: "))
                    if venta < 1:
                        error += "La cantidad a comprar no puede ser menor a 1\n"
                        raise ValueError
                    
                    if venta > cant_localidades:
                        error += "No puede comprar mas localidades de las que hay"
                        raise ValueError
                    
                    else:
                        flag2 = True
                        cant_localidades -= venta

                except ValueError:
                    if error != "":
                        print(error)

                    else:
                        print(f"Ingrese valores numericos")

    elif opcion == 3:
                if cant_localidades == max_locaidades:
                    print("Cantidad de localidades al maximo, no se pueden hacer devoluciones")

                elif cant_localidades != max_locaidades:
                    flag_devolucion = False

                    while not flag_devolucion:
                        error_devolucion = ""
                        try: 
                            devolucion = int(input("Ingrese la cantidad de localidades que desea devolver: "))
                            if devolucion < 1:
                                error_devolucion += "La cantidad a devolver no puede ser menor a 1\n"
                                raise ValueError
                            
                            if devolucion + cant_localidades > max_locaidades:
                                error_devolucion += "No pueden devolverse mas localidades del maximo disponible a la venta"
                                raise ValueError

                            else:
                                cant_localidades += devolucion
                                flag_devolucion = True

                        except ValueError:
                            if error_devolucion != "":
                                print(error_devolucion)

                            else:
                                print("Ingrese valores numericos")

                '''
    elif opcion == 4:
    '''
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
