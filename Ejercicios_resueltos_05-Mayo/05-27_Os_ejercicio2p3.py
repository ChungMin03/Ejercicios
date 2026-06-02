#Ejercicio 2 prueba 3
#Osvaldo Ruiz
#introduccion del programa
print("¡Bienvenido al sistema de gestion de habitaciones de Hotel Estelar!")
#-----------------bloque de variables e inputs----------------
habitaciones = 50
habitaciones_max = 50
total_habitaciones = 0
opcion = 0
#-----------------bloque de menú-------------------
while opcion != 5:
    print("---------------------------------------")
    print("1.- Visualizar habitaciones disponibles")
    print("2.- Realizar check-in")
    print("3.- Realizar check-out")
    print("4.- Historial de ocupaciones")
    print("5.- Salir")
    print("---------------------------------------")
    try:
        opcion = int(input("Ingrese la opcion que desea usar: "))
        if opcion > 5 or opcion < 1:
            raise ValueError
    except:
        print("Ingrese un valor nuemrico entre 1 y 5")
    #-----------------bloque de ejecucion------------------
    if opcion == 1:
        print(f"La cantidad de habitaciones disponibles es de: {habitaciones}")
    #check-in
    elif opcion == 2:
        if habitaciones < 1:
            print("No hay habitaciones disponibles")
        else:
            flag_in = False
            while not flag_in:
                try:
                    cant_reserva = int(input("Ingrese la cantidad de habitaciones a reservar: "))
                    if cant_reserva == 0:
                        print("No se ha reservado ninguna habitacion")
                        flag_in = True
                    if cant_reserva < 1 or cant_reserva > habitaciones:
                        raise ValueError
                    else:
                        habitaciones -= cant_reserva
                        total_habitaciones += cant_reserva
                        flag_in = True
                except:
                    print("La cantidad de habitaciones a reservar tiene que ser un numero menor a la cantidad restante y mayor a 0")
    #check-out
    elif opcion == 3:
        if habitaciones == habitaciones_max:
            print("No existen habitaciones reservadas")
        else:
            flag_out = False
            while not flag_out:
                try:
                    cant_liberar = int(input("Ingrese la cantidad de habitaciones que desea cancelar: "))
                    if (cant_liberar + habitaciones) > habitaciones_max or cant_liberar < 1:
                        raise ValueError
                    else:
                        habitaciones += cant_liberar
                        total_habitaciones -= cant_liberar
                        flag_out = True
                except ValueError:
                    print("La cantidad de habitaciones a cancelar tiene que ser un numero menor al total de habitaciones restantes y mayor a 0")
    elif opcion == 4:
        print(f"El total de las habitaciones reservadas es: {total_habitaciones}")
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima")
