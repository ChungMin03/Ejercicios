def agregar_reserva(lista_hotel):
    while True:
        nombre_huesped = input("Ingrese su nombre: ")
        if validar_huesped(nombre_huesped):
            break

    while True:
        habitacion = input("Ingrese la habitacion que desea reservar: ")
        if validar_habitacion(habitacion):
            break

    while True:
        noches = input("¿Por cuantas noches desea reservar?: ")
        if validar_noches(noches):
            break


    estado = False

    dicc_reserva = {
        "huesped":nombre_huesped,
        "habitacion":habitacion,
        "noches":noches,
        "estado": estado
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
            if p == 1:
                print("Su reserva ha sido encontrada")
            return i
    return -1
            
        

def eliminar(lista_hotel):
    eliminar_name = input("Ingrese el nombre que desea eliminar: ")
    b = buscar(lista_hotel, buscar_name=eliminar_name)
    if b == -1:
        print(f"La reserva del huésped {eliminar_name} no se encuentra registrada. ")
    else:
        lista_hotel.pop(b)
        print(f"La reserva del huésped {eliminar_name} ha sido eliminada con exito. ")


def estado_reserva(lista_hotel):

    for i in range(len(lista_hotel)):
        #print(lista_hotel[i]["noches"][0])
        if int(lista_hotel[i]["noches"])>= 2:
            lista_hotel[i]["estado"] = True
        else:
            lista_hotel[i]["estado"] = False
            

             

def mostrar_reservas(lista_hotel):

    estado_reserva(lista_hotel)
    for i in range(len(lista_hotel)):
        print("____________________________________________")
        print(f"Huesped: {lista_hotel[i]["huesped"][0]}")
        print(f"Habitacion: {lista_hotel[i]["habitacion"][0]}")
        print(f"Noches:         {lista_hotel[i]["noches"][0] }")
        if lista_hotel[i]["estado"][0] == True:
            p = "Confirmado"      
        else:
            p = "Pendiente"

        print(f"Estado:   {p}")

def opciones(lista_hotel): 
    
    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            agregar_reserva(lista_hotel)

        elif opcion == 2:
            buscar(lista_hotel)  

        elif opcion == 3: 
            eliminar(lista_hotel)
        
        elif opcion == 4: 
            estado_reserva(lista_hotel)
        elif opcion == 5:
            mostrar_reservas(lista_hotel)

        elif opcion == 6:
            print("Gracias por usar el sistema!!!") 
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











                   
