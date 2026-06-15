def mostrarMenu():
    print("-------------------- MENU PRINCIPAL ---------------------")
    print("1. Agregar mascota.")
    print("2. Buscar mascota.")
    print("3. Eliminar mascota.")
    print("4. Marcar como vacunada.")
    print("5. Mostrar mascotas.")
    print("6. Salir.")
    print("---------------------------------------------------------")

def solicitarOpcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opcion del 1 al 6.")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero.")
    return opcion

def agregarMascota(listaMascotas):
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    listaMascotas.append(nombre_mascota)
    return listaMascotas

#codigo principal
#declarar lista de mascotas
lista_mascotas = []

opcion = 999999999999999999999999999999999999
while opcion != 6:
    lista_mascotas = []
    mostrarMenu()
    opcion = solicitarOpcion()
    if opcion == 1:
        lista_mascotas = agregarMascota(lista_mascotas)
        print(lista_mascotas)
