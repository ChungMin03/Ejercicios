import prueba2 as p
#Código Principal

#Declarar la lista vacia
lista_reservas = []
opcion = 0
while opcion != 6:
    #mostrar mi menú
    p.mostrar_menu()
    #preguntar al usuario por la opcion del menu
    opcion = p.ingresar_opcion()
    #validamos la opcion seleccionada
    if opcion == 1:
        #llamar a la funcion que agregar las reservas
        p.agregar_reserva(lista_reservas)
    elif opcion == 2:
        #solicitar el nombre a buscar
        nombre = input("Ingrese el nombre del huésped a buscar: ")
        pos = p.buscar_reserva(lista_reservas, nombre)
        #validar si lo encontro o no
        if pos != -1:
            #mostrar los datos
            print("**** Reserva ******")
            print(f"Nombre del Huésped: {lista_reservas[pos]["huesped"]}")
            print(f"Número de Habitación: {lista_reservas[pos]["habitacion"]}")
            print(f"Cantidad de noches: {lista_reservas[pos]["noches"]}")
            estado = "CONFIRMADA" if lista_reservas[pos]["confirmada"] else "PENDIENTE"  
            print(f"Estado: {estado}")
            print("*******************")
        else:
            print(f"El huésped '{nombre}' no ha sido encontrado")
    elif opcion == 3:
        #solicitar el nombre a buscar
        nombre = input("Ingrese el nombre del huésped a eliminar la reserva: ")
        pos = p.buscar_reserva(lista_reservas, nombre)
        #validar si lo encontro o no
        if pos != -1:
            #elimino el elemento de la lista
            lista_reservas.pop(pos)
            print("Reserva eliminada")
        else:
            print(f"El huésped '{nombre}' no ha sido encontrado")

    elif opcion == 4:
        #llamar a la funcion que actualiza la confirmada
        p.confirmar_reservas(lista_reservas)
        print("Reservas actualizadas")
    elif opcion == 5:
        p.confirmar_reservas(lista_reservas)
        p.mostrar_reservas(lista_reservas)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto")

