#-------------------------------- BLOQUE DE FUNCIONES -------------------------------------------
def menu():
    print("=========== MENÚ PRINCIPAL ===========")
    print("1. Agregar reserva")
    print("2. Buscar reserva")
    print("3. Eliminar reserva")
    print("4. Confirmar reservas")
    print("5. Mostrar reservas")
    print("6. Salir")
    print("**************************************")
    
def pedir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 6:
                raise ValueError
            else:
                break
        except ValueError:
            print("Error: Debes ingresar un numero entre 1 y 6.")
    return opcion

def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    else:
        return True

def validar_habitacion(num_habitacion):
    if num_habitacion < 1 or num_habitacion > 200:
        return False
    else:
        return True

def validar_cant_noches(cant_noches):
    if cant_noches < 1:
        return False
    else:
        return True

def agregar_reserva(lista_reservas):
    while True:
        nombre_huesped = input("Ingrese su nombre: ")
        if validar_nombre(nombre_huesped):
            break
        else:
            print("Error: Que cojones tio, no puedes ingresar solo espacios.")
    while True:
        try:
            num_habitacion = int(input("Ingrese el numero de habitacion que reservara: "))
            if validar_habitacion(num_habitacion):
                break
            else:
                raise ValueError
        except ValueError:
            print("Error: Que cojones ingresas tio, debe ser una habitacion entre 1 y 200.")
    while True:
        try:
            cant_noches = int(input("Ingrese la cantidad de noches que se hospedara: "))
            if validar_cant_noches(cant_noches):
                break
            else:
                raise ValueError
        except ValueError:
            print("Error: Que cojones haces tio, no puedes reservar menos de una noche.")
    
    reserva_persona = {
        "nombre": nombre_huesped,
        "habitacion": num_habitacion,
        "noches": cant_noches,
        "confirmada": False
    }
    lista_reservas.append(reserva_persona)

def buscar_reserva(lista_reservas, nombre_buscar):
    for i in range(len(lista_reservas)):
        if lista_reservas[i]["nombre"].lower() == nombre_buscar.lower():
            return i
    return -1

def actualizar_reservas(lista_reservas):
    for reserva in lista_reservas:
        if reserva["noches"] >= 2:
            reserva["confirmada"] = True


#-------------------------------- CODIGO PRINCIPAL -------------------------------------------
lista_reservas = []
opcion = 99999999999999999999.1
while opcion != 6:
    menu()
    opcion = pedir_opcion()
    
    if opcion == 1:
        agregar_reserva(lista_reservas)

    if opcion == 2:
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        indice = buscar_reserva(lista_reservas, nombre_buscar)
        
        if indice != -1:
            print(f"Nombre: {lista_reservas[indice]["nombre"]}")
            print(f"Habitacion reservada: {lista_reservas[indice]["habitacion"]}")
            print(f"Noches reservadas: {lista_reservas[indice]["noches"]}")
        else:
            print("No hay reservas a este nombre.")

    if opcion == 3:
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        indice = buscar_reserva(lista_reservas, nombre_buscar)
        
        if indice != -1:
            lista_reservas.pop(indice)
            print(f"Huesped {nombre_buscar} eliminado del registro.")
        else:
            print(f"La reserva del huésped {nombre_buscar} no se encuentra registrada.")
    
    if opcion == 4:
        actualizar_reservas(lista_reservas)
    
    if opcion == 5:
        actualizar_reservas(lista_reservas)
        
        if not lista_reservas:
            print("No hay reservas. ")
        else:
            print("============ LISTA DE RESERVAS =============")
            for reserva in lista_reservas:
                print("\n")
                print(f"Huesped: {reserva["nombre"]}")
                print(f"Habitacion: {reserva["habitacion"]}")
                print(f"Noches: {reserva["noches"]}")
                print(f"Estado: {"CONFIRMADA" if reserva["confirmada"] else "PENDIENTE"}")

                print("\n")
                print("********************************************")
    
    if opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")