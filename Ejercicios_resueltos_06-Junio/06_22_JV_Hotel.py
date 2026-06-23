"""
EJERCICIO DE PRÁCTICA - SISTEMA DE RESERVAS DE HOTEL
"""
#----------------- bloque variables ----------------
lista_huespedes = []
lista_habitaciones_ocupadas = []

#----------------- bloque funciones validacion ----------------

def validar_nombre(nombre):
    if nombre.strip() != "" and nombre.replace(" ", "").isalpha():
        return True
    else:
        return False

def validar_habitacion(habitacion):
    if isinstance(habitacion, int) and 1 <= habitacion <= 200:
        return True
    else:
        return False

def validar_noches_reservadas(noches):
    if isinstance(noches, int) and noches > 0:
        return True
    else:
        return False

def validar_confirmacion(noches):
    if isinstance(noches, int) and noches >= 2:
        return True
    else:
        return False

#----------------- bloque funciones Menu ----------------

def mostrar_menu():
    print("\n======== MENÚ PRINCIPAL ========")
    print("1.- Agregar reserva")
    print("2.- Buscar reserva")
    print("3.- Eliminar reserva")
    print("4.- Confirmar reservas")
    print("5.- Mostrar reservas")
    print("6.- Modificar reserva")
    print("7.- Salir")
    print("================================")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Seleccionar una opción: "))
            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Debe seleccionar una opción del 1 al 7.")
        except ValueError:
            print("Debe ingresar un número.")

def crear_reserva(nombre: str, habitacion: int, noches: int) -> dict:
    reserva = {
        "nombre": nombre,
        "habitacion": habitacion,
        "noches": noches,
        "confirmacion": False
    }
    return reserva

def agregar_reserva():
    while True:
        nombre = input("Ingrese su nombre: ").strip().capitalize()
        if validar_nombre(nombre):
            break
        else:
            print("Nombre inválido. Debe contener solo letras y no estar vacío.")
    
    while True:
        try:
            habitacion = int(input("Ingrese el número de habitación (1-200): "))
            if validar_habitacion(habitacion):
                if habitacion not in lista_habitaciones_ocupadas:
                    break
                else:
                    print("La habitación ya está ocupada. Por favor, elija otra.")
            else:
                print("Número de habitación inválido. Debe estar entre 1 y 200.")
        except ValueError:
            print("Debe ingresar un número válido para la habitación.")
        
    while True:
        try:
            noches = int(input("Ingrese la cantidad de noches a reservar: "))
            if validar_noches_reservadas(noches):
                break
            else:
                print("Debe ingresar un número válido de noches (mayor a 0).")
        except ValueError:
            print("Debe ingresar un número válido para las noches.")
    
    lista_huespedes.append(crear_reserva(nombre, habitacion, noches))
    lista_habitaciones_ocupadas.append(habitacion)
    print(f"Reserva agregada exitosamente para {nombre} en la habitación {habitacion} por {noches} noches.")

def buscar_reserva(nombre_buscar, lista_huespedes):
    for i in range(len(lista_huespedes)):
        if lista_huespedes[i]["nombre"].lower() == nombre_buscar.lower():
            return i
    return -1

def eliminar_reserva(posicion):
    if posicion != -1:
        habitacion = lista_huespedes[posicion]["habitacion"]
        lista_habitaciones_ocupadas.remove(habitacion)
        lista_huespedes.pop(posicion)
        return True
    return False

def confirmar_reservas(lista_huespedes):
    for huesped in lista_huespedes:
        if huesped["noches"] >= 2 and huesped["confirmacion"] == False:
            huesped["confirmacion"] = True
            print(f"Reserva confirmada para {huesped['nombre']}.")
        elif huesped["confirmacion"] == True:
            print(f"La reserva de {huesped['nombre']} ya está confirmada.")
        else:
            huesped["confirmacion"] = False
            print(f"{huesped['nombre']} no cumple con los requisitos para confirmar la reserva.")
    
    print("Proceso de confirmación de reservas completado.")

def mostrar_reservas():
    if not lista_huespedes:
        print("No hay reservas registradas.")

    for huesped in lista_huespedes:
        print(f"\nNombre: {huesped['nombre']}")
        print(f"Habitación: {huesped['habitacion']}")
        print(f"Noches reservadas: {huesped['noches']}")
        print(f"Confirmación: {'CONFIRMADA' if huesped['confirmacion'] == True else 'PENDIENTE  '}")

def modificar_reserva(posicion):
    if posicion != -1:
        huesped = lista_huespedes[posicion]
        while True:
            try:
                nueva_cantidad_noches = int(input(f"Ingrese la nueva cantidad de noches para {huesped['nombre']} (actual: {huesped['noches']}): "))
                if validar_noches_reservadas(nueva_cantidad_noches):
                    if validar_confirmacion(nueva_cantidad_noches):
                        huesped["noches"] = nueva_cantidad_noches
                        print(f"Cantidad de noches actualizada exitosamente para {huesped['nombre']}.")
                        break
                    else:
                        print(f"{huesped['nombre']} no cumple con los requisitos para confirmar la reserva.")
                else:
                    print("Debe ingresar un número válido de noches (mayor a 0).")
            except ValueError:
                print("Debe ingresar un número válido para las noches.")
            

#----------------- bloque funcion principal ----------------

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == 1:
            agregar_reserva()
        
        elif opcion == 2:
            nombre = input("Ingrese el nombre del huésped a buscar: ").strip().capitalize()
            posicion = buscar_reserva(nombre, lista_huespedes)

            if posicion != -1:
                huesped = lista_huespedes[posicion]
                print(f"\n--- Reserva encontrada ---")
                print(f"Nombre: {huesped['nombre']}")
                print(f"Habitación: {huesped['habitacion']}")
                print(f"Noches reservadas: {huesped['noches']}")
                print(f"Confirmación: {'CONFIRMADA' if huesped['confirmacion'] == True else 'PENDIENTE'}")
            else:
                print(f"No se encontró ninguna reserva para el huésped {nombre}.")
        
        elif opcion == 3:
            nombre = input("Ingrese el nombre del huésped cuya reserva desea eliminar: ").strip().capitalize()
            posicion = buscar_reserva(nombre, lista_huespedes)

            if eliminar_reserva(posicion):
                print(f"Reserva eliminada exitosamente para {nombre}.")
            else:
                print(f"No se encontró ninguna reserva para el huésped {nombre}.")
        
        elif opcion == 4:
            confirmar_reservas(lista_huespedes)
        
        elif opcion == 5:
            mostrar_reservas()

        elif opcion == 6:
            nombre = input("Ingrese el nombre del huésped cuya reserva desea modificar: ").strip().capitalize()
            posicion = buscar_reserva(nombre, lista_huespedes)

            if posicion != -1:
                modificar_reserva(posicion)
            else:
                print(f"No se encontró ninguna reserva para el huésped {nombre}.")
        
        elif opcion == 7:
            print("Saliendo del sistema de reservas. ¡Hasta luego!")
            break

#----------------- Bloque de ejecucion ----------------

if __name__ == "__main__":
    main()