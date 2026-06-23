def menu():
    print("1. Agregar reserva")
    print("2. Buscar reserva")
    print("3. Eliminar reserva")
    print("4. Confirmar reservas")
    print("5. Mostrar reservas")
    print("6. Salir")

def opction_selector():
    while True:
        try:
            option = int(input("Ingrese la opcion que desea usar: "))
            if option < 1 or option > 6:
                print("Ingreses una opcion dentro del rango de valores (1-6)")
        except ValueError:
            print("Ingrese un valor numerico")
        return option

def name_validator(name):
    if name.strip() == "":
        return False
    return True

def room_validator(room):
    if room < 1 or room > 200:
        return False
    return True

def night_validator(night):
    if night < 1:
        return False
    return True

def booking(list):
    while True:
            name = input("Ingrese su nombre: ")
            if not name_validator(name):
                print("No puede dejar este espacio en blanco")
            else:
                break
    while True:
        try:
            room = int(input("Ingrese el numero de habitacion: "))
            if not room_validator(room):
                print("Ingrese un numero de habitacion valido")
            else:
                break
        except ValueError:
            print("Ingrese un valur numerico valido")
    while True:
        try:
            night = int(input("Ingrese la cantidad de noches que se hospedará: "))
            if not night_validator(night):
                print("Ingrese una cantidad de noches valida")
            else:
                break
        except ValueError:
            print("Ingrese un valor numerico válido")
    
    guest = {
        'Nombre': name,
        'Habitación': room,
        'Noches': night
    }
    list.append(guest)

def search_booking(list,name):
    












#-----------------bloque de variables---------------
rooms = []
booking = []
#---------------------------------------------------


#-----------------bloque de ejecucion-------------------









