# ----------------- Bloque variables -----------------
contador_vehiculos = 0
cantidad = 0
capacidad = 0
pesado = 0
ligero = 0

# ----------------- Bloque de ejecución -----------------

menu = True

while menu:
    print("\n-------------<<< MENU >>>-------------")
    print("1.- Datos vehiculos")
    print("2.- Capacidad de carga")
    print("3.- Clasificación de vehículos")
    print("4.- Resetear vehículos")
    print("5.- Salir")
    print("------------------------------------\n")
    
    try: 
        opcion = int(input("Ingrese la opción: "))
    except ValueError:
         print("ingrese un numero entero")

    if opcion == 1:
        opc = False
        while not opc:
            try: 
                cantidad = int(input("Ingrese la cantidad de vehículos a registrar: "))
                opc = True
            except ValueError:
                print("Ingrese un número entero válido para la cantidad de vehículos.")

        i = 1
        while i <= cantidad:
            if cantidad <= 0:
                    print("La cantidad debe ser un número positivo. Por favor, ingrese una cantidad válida.")
            else:
                placa_vehicular = input("Ingrese la placa del vehículo: ")
                if len(placa_vehicular) >= 6 and (" ") not in placa_vehicular:
                    placa_vehicular = placa_vehicular.upper()
                    contador_vehiculos = contador_vehiculos + 1
                    i = i + 1

                elif len(placa_vehicular) < 6:
                    print("La placa debe tener al menos 6 caracteres. Por favor, ingrese una placa válida.")

                elif (" ") in placa_vehicular:
                    print("La placa no debe contener espacios. Por favor, ingrese una placa válida.")
        
        print(cantidad)
                
    
    if opcion == 2:
        pesado = 0
        ligero = 0
        if cantidad <= 0:
            print("No se han registrado vehículos. Por favor, registre vehículos antes de ingresar sus capacidades de carga.")
        else:
            i = 0
            while i < cantidad:
                opc = False
                while not opc:
                    try:
                        capacidad = int(input("Ingrese la capacidad de carga del vehículo: "))
                        opc = True
                    except ValueError:
                        print("Ingrese un número entero")
                        continue

                    if capacidad > 55:
                        pesado = pesado + 1
                        i = i + 1

                    elif capacidad <= 55 and capacidad > 0:
                        ligero = ligero + 1
                        i = i + 1

                    elif capacidad <= 0:
                        print("La capacidad no puede ser negativa o cero.")


    if opcion == 3:
        print("Cantidad de vehículos registrados: ", contador_vehiculos)
        print("Cantidad de vehículos pesados: ", pesado)
        print("Cantidad de vehículos ligeros: ", ligero)
        
    if opcion == 4:
        contador_vehiculos = 0
        cantidad = 0
        capacidad = 0
        pesado = 0
        ligero = 0
        print("Vehículos reseteados exitosamente.")

    if opcion == 5:
        print("Saliendo del programa...")
        menu = False