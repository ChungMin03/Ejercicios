"""
Requisito 1 — Inicio del programa
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
# ----------------- Bloque de variables -----------------
historial_ventas = 0
devoluciones = 0
historial_total_ventas = 0

# Esta variable global representa la matriz de asientos del teatro.
matriz_asientos = [["*"] * 20 for _ in range(10)]

# ----------------- Bloque funciones -----------------

# Esta función permite reservar un asiento, seleccionando la fila y columna, remplazando el valor "*" por "X" en la matriz de asientos.
# Si el asiento ya está ocupado, se muestra un mensaje indicando que no se puede reservar ese asiento.
# La funcion retorna True si se utiliza. Esto debido a que al no retornar nada, el valor por defecto es None, lo que no permite incrementar el historial de ventas.
def asiento_ocupado():
    ocupar_asiento = False
    while not ocupar_asiento:
        try:
            fila = int(input("Ingrese la fila (1-10): "))
            columna = int(input("Ingrese la columna (1-20): "))
            
            # Se valida que la fila y columna ingresada estén dentro del rango permitido (1-10 para filas y 1-20 para columnas)
            if fila < 1 or fila > 10 or columna < 1 or columna > 20:
                print("Número de fila o columna fuera de rango. Por favor, ingrese valores válidos.")
            else:
                # Se resta 1 a la fila y columna para ajustar a los índices de la matriz (que comienzan en 0)
                if 0 <= (fila - 1) <= 9 and 0 <= (columna - 1) <= 19:
                    if matriz_asientos[(fila - 1)][(columna - 1)] == "X":
                        print("El asiento ya está ocupado.\n")
                        ocupar_asiento = False
                        # Se retorna False para indicar que no se pudo reservar el asiento, lo que evita incrementar el historial de ventas.
                        return False
                    else:
                        matriz_asientos[(fila - 1)][(columna - 1)] = "X"
                        print("Asiento reservado exitosamente.\n")
                        ocupar_asiento = True

        except ValueError:
            print("No ingreso un numero entero")
    return True


# Esta función permite devolver un asiento, seleccionando la fila y columna, remplazando el valor "X" por "*" en la matriz de asientos.
# Si el asiento ya está disponible, se muestra un mensaje indicando que no se puede devolver ese asiento.
# La funcion retorna True si se utiliza.
# Esta función es similar a la función de reservar asiento, pero en lugar de marcar el asiento como ocupado ("X"), lo marca como disponible ("*").
def devolver_asiento():
    devolver_asiento = False
    while not devolver_asiento:
        try:
            fila = int(input("Ingrese la fila (1-10): "))
            columna = int(input("Ingrese la columna (1-20): "))
            
            if fila < 1 or fila > 10 or columna < 1 or columna > 20:
                print("Número de fila o columna fuera de rango. Por favor, ingrese valores válidos.")
            else:
                if 0 <= (fila - 1) <= 9 and 0 <= (columna - 1) <= 19:
                    if matriz_asientos[(fila - 1)][(columna - 1)] == "*":
                        print("El asiento ya está disponible.\n")
                        devolver_asiento = False
                        return False
                    else:
                        matriz_asientos[(fila - 1)][(columna - 1)] = "*"
                        print("Asiento devuelto exitosamente.\n")
                        devolver_asiento = True
            
        except ValueError:
            print("No ingreso un numero entero")
    return True


# ----------------- Bloque de ejecución -----------------
menu = False

while not menu:
    print("\n-------------<<< MENU >>>-------------")
    print("1.- Localidades disponibles")
    print("2.- Vender localidades")
    print("3.- Devolver localidades")
    print("4.- Historial de ventas")
    print("5.- Salir")
    print("------------------------------------\n")

    # Validacion de ingreso de opcion del menu
    opc = False
    while not opc:
        try: 
            opcion = int(input("Ingrese la opción: "))
            opc = True
        except ValueError:
            print("No ingreso una opción válida.")
        
    if opcion == 1:
        
        print("\nLocalidades disponibles:")
        print("|                                                        |")
        print("|                 ESCENARIO PRINCIPAL                    |")
        print("|________________________________________________________|")
        print("                                                          ")
        for fila in matriz_asientos:
            # Se utiliza el método join para convertir cada fila de la matriz de asientos en una cadena de texto, separando los elementos con dos espacios ("  ").
            print("  ".join(fila))

    
    elif opcion == 2:
        ciclo = False
        while not ciclo:
            print("Ingrese el asiento que desea reservar:")
            # Se utiliza una comprensión de listas para contar el número de asientos ocupados ("X") en la matriz de asientos. 
            # La función sum() se encarga de sumar los conteos de cada fila para obtener el total de asientos ocupados.
            # La veriable fila no es la misma que se utiliza en la función de reservar asiento, ya que esta variable solo existe dentro del bloque de código de esa función.
            ocupadas = sum(fila.count("X") for fila in matriz_asientos)

            # Para evitar errores, se valida que existan asientos disponibles antes de intentar reservar un asiento. Si no hay asientos disponibles, el programa termina el ciclo.
            if ocupadas >= 200:
                print("No hay localidades disponibles.")
                print("Volviendo al menú principal...")
                ciclo = True
            else:
                # 
                if asiento_ocupado():
                    historial_ventas = historial_ventas + 1
                    historial_total_ventas = historial_total_ventas + 1
                
                decision = input("¿Desea reservar otro asiento? (s/n): ").lower()
                if decision != "s" and decision != "si":
                    print("Volviendo al menú principal...")
                    ciclo = True

    elif opcion == 3:
        ciclo2 = False
        while not ciclo2:
            print("Ingrese el asiento que desea devolver")
            ocupados = sum(fila.count("X") for fila in matriz_asientos)

            # Para evitar errores, se valida que existan asientos ocupados antes de intentar devolver un asiento. Si no hay asientos ocupados, el programa termina el ciclo.
            if ocupados <= 0:
                print("No hay localidades ocupadas para devolver.")
                print("Volviendo al menú principal...")
                ciclo2 = True

            else:
                if devolver_asiento():
                    devoluciones = devoluciones + 1
                    historial_ventas = historial_ventas - 1

                decision = input("¿Desea devolver otro asiento? (s/n): ").lower()
                if decision != "s" and decision != "si":
                    print("Volviendo al menú principal...")
                    ciclo2 = True
    
    elif opcion == 4:
        print(f"Total de ventas netas realizadas durante la sesión: {historial_ventas}")
        print(f"Total de devoluciones realizadas durante la sesión: {devoluciones}")
        print(f"Total de ventas realizadas, sin descontar por devoluciones: {historial_total_ventas}")
    
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        menu = True

    else:
        print("Opción no válida. Por favor, ingrese una opción del 1 al 5.")