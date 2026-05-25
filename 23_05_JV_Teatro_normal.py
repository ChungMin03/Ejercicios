# ----------------- Bloque variables -----------------
asiento = 200
historial_ventas = 0


# ----------------- Bloque de ejecución -----------------
print("##############################################################################")
print("#                                                                            #")
print("#   ¡Bienvenido al sistema de gestión de localidades del Teatro Municipal!   #")
print("#                                                                            #")
print("##############################################################################")

menu = True
while menu:
    print("\n-------------<<< MENU >>>-------------")
    print("1.- Localidades disponibles")
    print("2.- Vender localidades")
    print("3.- Devolver localidades")
    print("4.- Historial de ventas")
    print("5.- Salir\n")

    opc = True
    while opc:
        try: 
            opcion = int(input("Ingrese la opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
            else:
                opc = False
        except ValueError:
            print("Ingrese un número entero válido para la opción del menú.")
    
    if opcion == 1:
        print(f"\nActualmente, hay {asiento} localidades disponibles para el evento.")
    
    if opcion == 2:
        if asiento <= 0:
            print("\nNo hay localidades disponibles")
        
        else:
            opc = False
            while not opc:
                try: 
                    venta = int(input("\nIngrese la cantidad de localidades a vender: "))
                    
                    if venta <= 0:
                        print("La cantidad de localidades a vender debe ser un número positivo. Por favor, ingrese una cantidad válida.")


                    elif venta > asiento:
                        print(f"No hay suficientes localidades disponibles para vender {venta} localidades. Actualmente, hay {asiento} localidades disponibles.")


                    elif venta <= asiento:
                        asiento = asiento - venta
                        historial_ventas = historial_ventas + venta
                        print(f"Venta exitosa. Quedan {asiento} localidades disponibles.")
                        opc = True

                except ValueError:
                    print("Ingrese un número entero válido para la cantidad de localidades a vender.")
                        

        
    if opcion == 3:

        if historial_ventas <= 0:
            print("\nNo hay localidades vendidas para devolver.")

        else:

            opc = False
            while not opc:
                try:
                    devolucion = int(input("\nIngrese la cantidad de localidades a devolver: "))

                    if devolucion <= 0:
                        print("La cantidad de localidades a devolver debe ser un número positivo. Por favor, ingrese una cantidad válida.")
                    
                    elif devolucion > historial_ventas:
                        print(f"No se pueden devolver más localidades de las que se han vendido. Actualmente, hay {historial_ventas} localidades vendidas.")

                    elif devolucion <= historial_ventas:
                        asiento = asiento + devolucion
                        historial_ventas = historial_ventas - devolucion
                        print(f"Devolución exitosa. Ahora hay {asiento} localidades disponibles.")
                        opc = True
                except ValueError:
                    print("Ingrese un número entero válido para la cantidad de localidades a devolver.")

    if opcion == 4:
        print(f"\nEl historial de ventas actual es de {historial_ventas} localidades vendidas.")
    
    if opcion == 5:
        print("\nGracias por utilizar nuestro software, hasta la próxima.")
        menu = False