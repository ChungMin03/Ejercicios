



#-----------------bloque de funciones-----------------
#funcion para mostrar el menu de opciones
def display_menu():
    print("---------------------------")
    print("1.- Agregar mascota")
    print("2.- Buscar mascota")
    print("3.- Eliminar mascota")
    print("4.- Marcar como vacunada")
    print("5.- Mostrar mascotas")
    print("6.- Salir")
    print("---------------------------")

#seleccion de la opcion a usar
def select_option():
    while True:
        try:
            option = int(input("Ingrese la opcion que desea usar: "))
            if option < 1 or option > 6:
                print("Ingrese un valor dentro de las opciones (1-6)")
            else:
                break
        except ValueError:
            print("Ingrese un valor numerico válido")
    return option

#funcion para agregar mascotas
def add_pet():
    pet_info = {
        "name" : input("Ingrese el nombre de la mascota: "),
        "specie" : input("Ingrese la especie de su mascora: ")

    }
    pet_list.append(pet_info)

def search_pet():
    pet_name = input("Ingrese el nombre de la mascota a buscar")
    for pet in pet_list:
        if pet["name"] == pet_name:
            print("Mascota encontrada")
        else:
            print("Mascota no encontrada")

def delete_pet():
    pet_name = input("Ingrese el nombre de la mascota a buscar")
    for pet in pet_list:
        if pet["name"] == pet_name:
            pet_list.pop[]
        else:
            print("Mascota no encontrada")




#-----------------bloque de variables-----------------

pet_list = []


#-----------------bloque de ejecucion-----------------
display_menu()
opcion = select_option()
if opcion == 1:
    add_pet()
if opcion == 2:
    search_pet()





            