def agregar_reserva(lista_hotel):
    while True:
        nombre_huesped = input("Ingrese su nombre: ")
        if validar_huesped(nombre_huesped):
            break

    while True:
        habitacion = input("Ingrese la habitacion que desea reservar: ")
        if validar_habitacion(habitacion):
            # Guardamos como entero para cumplir la restricción
            habitacion = int(habitacion)
            break

    while True:
        noches = input("¿Por cuantas noches desea reservar?: ")
        if validar_noches(noches):
            # Guardamos como entero para cumplir la restricción
            noches = int(noches)
            break

    # La guía pide que la llave se llame "confirmada" y comience en False
    confirmada = False

    dicc_reserva = {
        "huesped": nombre_huesped,
        "habitacion": habitacion,
        "noches": noches,
        "confirmada": confirmada
    }

    lista_hotel.append(dicc_reserva)

#Funcion para validar huesped
def validar_huesped(name):
    if not name == "":
        u = 0
        for i in range(len(name)):
            if name[i] == " ":
                u += 0
            else:
                u += 1    
    else:
        print("Error: El nombre del huesped no puede ser vacío ")
        return False
    if u != 0:
        return True
    else:
        print("Error: El nombre del huesped no pueden ser solo espacios en blanco ")
        return False
    
#Funcion para validar la habitacion
def validar_habitacion(room):
    try:
        room = int(room)
    except ValueError:
        print("Error: Dato invalido")
        return False
    if room >= 1 and room <= 200:
        return True
    else: 
        print("Error: dato ingresado fuera de rangos")
        return False    

#Funcion para validar las noches
def validar_noches(night):
    try:
        night = int(night)
    except ValueError:
        print("Debe ingresar un numero entero mayor a 0") 
        return False 
    if int(night) > 0:
        return True   
    else: 
        print("Error: Dato fuera de rango")
        return False
    
#Funcion para buscar es de la opcion 2  
def buscar(lista_hotel, buscar_name=None):
    p = 0
    if buscar_name == None:
        buscar_name = input("Ingrese el nombre que desea Buscar: ")
        p = 1

    for i in range(len(lista_hotel)):
        if buscar_name == lista_hotel[i]["huesped"]:
            # Dejamos que devuelva la posición encontrada
            return i
    return -1
            
        
def eliminar(lista_hotel):
    eliminar_name = input("Ingrese el nombre que desea eliminar: ")
    b = buscar(lista_hotel, buscar_name=eliminar_name)
    if b == -1:
        # Formato de mensaje con comillas simples solicitado por la guía
        print(f"La reserva del huésped '{eliminar_name}' no se encuentra registrada. ")
    else:
        lista_hotel.pop(b)
        print(f"La reserva del huésped '{eliminar_name}' ha sido eliminada con exito. ")


def estado_reserva(lista_hotel):
    for i in range(len(lista_hotel)):
        # Al ser un entero, ya no necesitamos usar int() aquí
        if lista_hotel[i]["noches"] >= 2:
            lista_hotel[i]["confirmada"] = True
        else:
            lista_hotel[i]["confirmada"] = False
            

def mostrar_reservas(lista_hotel):
    estado_reserva(lista_hotel)
    print("\n=== LISTA DE RESERVAS ===") # Formato de la guía
    for i in range(len(lista_hotel)):
        print("____________________________________________")
        print(f"Huésped: {lista_hotel[i]['huesped']}")
        print(f"Habitación: {lista_hotel[i]['habitacion']}")
        print(f"Noches: {lista_hotel[i]['noches']}")
        
        # Leemos la llave "confirmada"
        if lista_hotel[i]["confirmada"] == True:
            p = "CONFIRMADA"      
        else:
            p = "PENDIENTE"

        print(f"Estado: {p}")


def opciones(lista_hotel): 
    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            agregar_reserva(lista_hotel)

        elif opcion == 2:
            # SOLUCIÓN AL PROBLEMA: Capturamos la posición que retorna la función buscar
            pos = buscar(lista_hotel)  
            
            # Evaluamos el resultado aquí, tal como exige la guía
            if pos != -1:
                reserva = lista_hotel[pos]
                # Traducimos el estado booleano a texto para mostrarlo
                est_texto = "CONFIRMADA" if reserva["confirmada"] else "PENDIENTE"
                
                print(f"\nReserva encontrada en la posición {pos}:")
                print(f"Huésped: {reserva['huesped']}")
                print(f"Habitación: {reserva['habitacion']}")
                print(f"Noches: {reserva['noches']}")
                print(f"Estado: {est_texto}")
            else:
                print("El huésped no tiene ninguna reserva registrada.")

        elif opcion == 3: 
            eliminar(lista_hotel)
        
        elif opcion == 4: 
            estado_reserva(lista_hotel)
            print("Estados de reservas actualizados con éxito.")
            
        elif opcion == 5:
            mostrar_reservas(lista_hotel)

        elif opcion == 6:
            # Mensaje de despedida exacto que pide la guía
            print("Gracias por usar el sistema. Vuelva Pronto") 
        else: 
            print("Error: Seleccione una opción válida. ")
        return opcion 
    except ValueError:
        print("Ingrese una opción válida")
    

def mostrar_menu(): 
    print("======== MENÚ PRINCIPAL ========")
    print("1. Agregar reserva")
    print("2. Buscar reserva")
    print("3. Eliminar reserva")
    print("4. Confirmar reservas")
    print("5. Mostrar reservas")
    print("6. Salir")   
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#Bloque de ejecucion
lista_hotel = []
while True:
    mostrar_menu()
    opc = opciones(lista_hotel)
    if opc == 6:
        break