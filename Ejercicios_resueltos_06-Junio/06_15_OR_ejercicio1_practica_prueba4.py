



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



def name_validator(name):
    if name.strip() == "":
        return False
    else:
        return True

def  specie_validator(specie):
    if specie.lower() == "perro" or specie.lower() == "gato" or specie.lower() == "ave":
        return True
    else:
        return False

def age_validator(age):
    if age >= 0:
        return True
    else:
        return False


#forma que pide el ejercicio
def add_pet(pet_list):
    while True:
        name = input("Ingrese el nombre de su mascota: ")
        if not name_validator(name):
            print("El nombre no puede estar vacio ni ser solo epacio en blanco")
        else:
            break
    while True:
        specie = input("Ingrese la especie de su mascota: ")
        if not specie_validator(specie):
            print("La especie solo puede ser 'perro', 'gato', 'ave' ")
        else:
            break
    while True:
        try:
            age = int(input("Ingrese la edad de su mascota: "))
            if not age_validator(age):
                raise ValueError
            else:
                break
        except ValueError:
            print("La edad debe ser un numero entero mayor o igual a 0")

    pet_info = {
        "Nombre" : name,
        "Especie" : specie,
        "Edad" : age,
        "Vacuna" : False
    }        
    pet_list.append(pet_info)

def find_pet(pet_list, finded_pet):
    for pet in pet_list:
        if pet["Nombre"] == finded_pet:
           index = pet_list.index(pet)
        else:
            index = -1
    return index


#funcion para agregar mascotas
#forma wena wena
"""def search_pet():
    pet_name = input("Ingrese el nombre de la mascota a buscar")
    for pet in pet_list:
        if pet["name"] == pet_name:
            print("Mascota encontrada")
        else:
            print("Mascota no encontrada")

def delete_pet():
    pet_name = input("Ingrese el nombre de la mascota a eliminar del registro")
    for pet in pet_list:
        if pet["name"] == pet_name:
            pet_list.remove(pet["name"])
        else:
            print("Mascota no encontrada")"""









#-----------------bloque de variables-----------------

pet_list = []


#-----------------bloque de ejecucion-----------------
opcion = 0
while opcion != 6:
    display_menu()
    opcion = select_option()
 
    if opcion == 1:
        add_pet(pet_list)

    elif opcion == 2:
        while True:
            finded_pet = input("Ingrese el nombre de la mascota a buscar: ")
            name_validator(finded_pet)
            if not name_validator:
                print("El nombre no puede estar vacio ni ser solo epacio en blanco")
            else:
                break
            
        indice = find_pet(pet_list, finded_pet)
        if indice >= 0:
            print(f"Mascota Nº{indice}")
            print(pet_list[indice])
        else:
            print("No existe")

    elif opcion == 3:
        eliminate_pet = input("Ingrese el nombre de la mascota a eliminar del registro: ")
        index = find_pet(pet_list, eliminate_pet)
        if index >= 0:
            pet_list.pop(index)
        else:
            print("No existe")




            