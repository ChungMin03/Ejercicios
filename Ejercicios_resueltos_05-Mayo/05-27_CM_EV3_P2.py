#---------------- BLOQUE DE VARIABLES -----------------
stock_maximo = 50 #no se modifica
stock_actual = 50
count_reservas = 0

#---------------- BLQOUE DE EJECUCION -----------------

print("¡Bienvenido al sistema de gestión de habitaciones del Hotel Estelar!") #Bienvenida

#Menú Principal
opcion = 0
while opcion != 5:
    print("========= MENÚ PRINCIPAL =========")
    print("1. Habitaciones disponibles.")
    print("2. Realizar check-in.")
    print("3. Realizar check-out.")
    print("4. Historial de ocupaciones.")
    print("5. Salir.")

    flag_opcion = False
    while not flag_opcion:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion < 1 or opcion > 5:
                raise ValueError
            else:
                flag_opcion = True
        except ValueError:
            print("Opción inválida, ingrese un numero entero entre 1 y 5.")
    #1. Habitaciones disponibles
    if opcion == 1:
        print(f"Cantidad de habitaciones libres: {stock_actual}")
    #2. Realizar Check-in
    elif opcion == 2:
        if stock_actual == 0:
            print("No hay habitaciones disponibles.")
        else:
            flag_checkin = False
            while not flag_checkin:
                try:
                    reserva = int(input("¿Cuántas habitaciones desea reservar? "))
                    if reserva < 1:
                        print("Cantidad inválida, debe ingresar un número mayor a cero.")
                    if reserva > stock_actual:
                        print(f"Cantidad inválida, supera el stock disponible de {stock_actual} habitaciones.")
                    if reserva >= 1 and reserva <= stock_actual:
                        flag_checkin = True
                        stock_actual -= reserva
                        count_reservas += reserva
                except ValueError:
                    print("Reserva inválida, ingrese un número entero mayor a cero.")
    #3. Realizar Check-out
    elif opcion == 3:
        if stock_actual == stock_maximo:
            print("No se pueden realizar devoluciones, todas las habitaciones están disponibles.")
        else:
            flag_checkout = False
            while not flag_checkout:
                try:
                    devolucion = int(input("Ingrese la cantidad de habitaciones que liberará: "))
                    if devolucion < 1:
                        print("Cantidad inválida, debe ingresar un número mayor a cero.")
                    if devolucion + stock_actual > stock_maximo:
                        cantidad_devolucion = stock_maximo - stock_actual
                        print(f"Cantidad inválida, supera el stock máximo de habitaciones.")
                        print(f"Puede liberar hasta {cantidad_devolucion} habitaciones.")
                    if devolucion >= 1 and devolucion + stock_actual <= stock_maximo:
                        flag_checkout = True
                        stock_actual += devolucion
                        count_reservas -= devolucion
                except ValueError:
                    print("Devolución inválida, ingrese un numero mayor a cero.")
    #4. Historial de ocupaciones                
    elif opcion == 4:
        print("======= HISTORIAL DE MOVIMIENTO =======")
        print(f"Habitaciones ocupadas : {count_reservas}.")
        print(f"Habitaciones libres: {stock_actual}.")
    #5. Salir del sistema
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")