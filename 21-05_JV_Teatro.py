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
matriz_asientos = [["*"] * 20 for _ in range(10)]

# ----------------- Bloque funciones -----------------


def asiento_ocupado():
    ocupar_asiento = False
    while not ocupar_asiento:
        try:
            fila = int(input("Ingrese la fila (1-10): "))
            columna = int(input("Ingrese la columna (1-20): "))

            if fila < 1 or fila > 10 or columna < 1 or columna > 20:
                print("Número de fila o columna fuera de rango. Por favor, ingrese valores válidos.")
            else:
                if 0 <= (fila - 1) <= 9 and 0 <= (columna - 1) <= 19:
                    if matriz_asientos[(fila - 1)][(columna - 1)] == "X":
                        print("El asiento ya está ocupado.")
                    else:
                        matriz_asientos[(fila - 1)][(columna - 1)] = "X"
                        print("Asiento reservado exitosamente.")
                        ocupar_asiento = True

        except ValueError:
            print("No ingreso un numero entero")



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
                        print("El asiento ya está disponible.")
                    else:
                        matriz_asientos[(fila - 1)][(columna - 1)] = "*"
                        print("Asiento devuelto exitosamente.")
                        devolver_asiento = True
            
        except ValueError:
            print("No ingreso un numero entero")


# ----------------- Bloque de ejecución -----------------

menu = False

while not menu:
    print("\n-------------<<< MENU >>>-------------")
    print("1.- Localidades disponibles")
    print("2.- Vender localidades")
    print("3.- Devolver localidades")
    print("4.- Historial de ventas")
    print("5.- Salir")

    # Validacion de ingreso de opcion del menu
    opc = False
    while not opc:
        try: 
            opcion = int(input("Ingrese la opción: "))
            opc = True
        except ValueError:
            print("No ingreso una opción válida.")
        
    if opcion == 1:
        print("Localidades disponibles:\n")
        for fila in matriz_asientos:
            print(" ".join(fila))

    
    elif opcion == 2:
        ciclo = False
        while not ciclo:
            print("Ingrese el asiento que desea reservar")
            ocupadas = sum(fila.count("X") for fila in matriz_asientos)

            if ocupadas >= 200:
                print("No hay localidades disponibles.")
                ciclo = True
            else:
                if asiento_ocupado():
                    historial_ventas = historial_ventas + 1
                
                decision = input("¿Desea reservar otro asiento? (s/n): ").lower()
                if decision != "s" or decision != "si":
                    ciclo = True

    elif opcion == 3:
        ciclo2 = False
        while not ciclo2:
            print("Ingrese el asiento que desea devolver")
            ocupados = sum(fila.count("X") for fila in matriz_asientos)

            if ocupados <= 0:
                print("No hay localidades ocupadas para devolver.")
                ciclo2 = True

            else:
                if devolver_asiento():
                    devoluciones = devoluciones + 1
                    historial_ventas = historial_ventas - 1

                decision = input("¿Desea devolver otro asiento? (s/n): ").lower()
                if decision != "s" or decision != "si":
                    ciclo2 = True
    
    elif opcion == 4:
        print(f"Total de ventas netas realizadas durante la sesión: {historial_ventas}")
        print(f"Total de devoluciones realizadas durante la sesión: {devoluciones}")
    
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        menu = True

    else:
        print("Opción no válida. Por favor, ingrese una opción del 1 al 5.")