#-------------------------------- BLOQUE DE FUNCIONES -------------------------------------------

#funcion que muestra el menu solicitado
def mostrarMenu():
    print("-------------------- MENU PRINCIPAL ---------------------")
    print("1. Agregar mascota.")
    print("2. Buscar mascota.")
    print("3. Eliminar mascota.")
    print("4. Marcar como vacunada.")
    print("5. Mostrar mascotas.")
    print("6. Salir.")
    print("---------------------------------------------------------")

#funcion que solicita la opcion
def solicitarOpcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 0 or opcion > 6:
                print("Debe seleccionar una opcion del 1 al 6.")
            else:
                break
        except ValueError:
            print("Debe ingresar un numero.")
    return opcion

#funcion que crea diccionario pedido
def crearDiccionario(nombre, especie, edad):
    diccionario_mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad,
        "vacunado": False
    }
    return diccionario_mascota

#funcion que valida el nombre entregado por el usuario, retorna True o False para evaluar en el llamado
def validarNombre(nombre_mascota):
    if nombre_mascota.strip() != "":
        return True
    else:
        return False

#funcion que valida la especie entregada por el usuario, retorna True o False para evaluar en el llamado
def validarEspecie(especie_mascota):
    if especie_mascota not in ["perro", "gato", "ave"]:
        return False
    else:
        return True

#funcion que valida la edad entregada por el usuario, retorna True o False para evaluar en el llamado
def validarEdad(edad_mascota):
    if edad_mascota < 0:
        return False
    else:
        return True

#funcion que agrega el diccionario con las entradas del usuario a la lista de diccionarios
def agregarMascota(listaMascotas, nombre_mascota, especie_mascota, edad_mascota):
    listaMascotas.append(crearDiccionario(nombre_mascota, especie_mascota, edad_mascota))

#funcion que busca el nombre que busca el usuario y retorna el indice de la lista donde se encuentra el diccionario
def buscarMascota(listaMascotas, nombre_buscado):
    indice = 0
    for datos_mascota in listaMascotas:
        if datos_mascota["nombre"].lower() == nombre_buscado.lower():
            return indice
        indice += 1
    return -1

#funcion que asigna las vacunas dependiendo de la edad de las mascotas
def asignarVacunas(listaMascotas):
    for datos_mascota in listaMascotas:
        if datos_mascota["edad"] >= 1:
            datos_mascota["vacunado"] = True

#funcion que muestra los datos de las mascotas en los dicciconarios de la lista
def mostrarMascotas(listaMascotas):
    for datos_mascota in listaMascotas:
        print(f"---------------------- DATOS PACIENTE ----------------------")
        print(f"Nombre: {datos_mascota["nombre"]}")
        print(f"Especie: {datos_mascota["especie"]}")
        print(f"Edad: {datos_mascota["edad"]}")
        if not datos_mascota["vacunado"]:
            print(f"Estado Vacuna: PENDIENTE")
        else:
            print(f"Estado Vacuna: AL DIA")


#-------------------------------- CODIGO PRINCIPAL -------------------------------------------
#declarar lista de mascotas
lista_mascotas = []

#inicializamos opcion en un numero != 6
opcion = 999999999999999999999999999999999999
while opcion != 6:
    mostrarMenu() #muestra menu
    opcion = solicitarOpcion() #solicita opcion al usuario
    
    if opcion == 1:
        while True: 
            nombre_mascota = input("Ingrese el nombre de su mascota: ").strip()
            if not validarNombre(nombre_mascota): #validamos el nombre ingresado por el usuario
                print("Error: El nombre no puede estar vacio o contener solo espacios.") 
            else:
                break
    
        while True:
            especie_mascota = input("Ingrese la especie de su mascota: ")
            if not validarEspecie(especie_mascota): #validamos la especie ingresada por el usuario
                print("Error: Solo atendemos perros, gatos y aves.")
            else:
                break
        
        while True:
            try:
                edad_mascota = int(input("Ingrese la edad de su mascota (en años): "))
                if not validarEdad(edad_mascota): #validamos la edad ingresada por el usuario
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Error: La edad de la mascota debe ser un numero mayor o igual a cero.")
        #creamos y agregamos diccionario a la lista
        lista_mascotas.append(crearDiccionario(nombre_mascota, especie_mascota, edad_mascota))

    elif opcion == 2:
        nombre_buscado = input("Ingrese el nombre de su mascota: ")
        indice_mascota = buscarMascota(lista_mascotas, nombre_buscado) #guardamos el indice de la lista donde fue encontrado el nombre de la mascota
        if indice_mascota != -1: #si encuentra el nombre, muestra los datos de la mascota
            print(f"---------------------- DATOS PACIENTE ----------------------")
            print(f"Nombre: {lista_mascotas[indice_mascota]["nombre"]}")
            print(f"Especie: {lista_mascotas[indice_mascota]["especie"]}")
            print(f"Edad: {lista_mascotas[indice_mascota]["edad"]}")
            if not lista_mascotas[indice_mascota]["vacunado"]: #si no esta vacunado muestra pendiente
                print(f"Estado Vacuna: PENDIENTE")
            else: #si esta vacunado muestra al dia
                print(f"Estado Vacuna: AL DIA")
        else: #si no encuentra el nombre muestra mensaje solicitado
            print(f"La mascota {nombre_buscado} no se encuentra registrada.")

    elif opcion == 3:
        nombre_buscado = input("Ingrese el nombre de su mascota: ")
        indice_mascota = buscarMascota(lista_mascotas, nombre_buscado) #guardamos el indice de la lista donde fue encontrado el nombre de la mascota
        if indice_mascota != -1: #si encuentra el nombre, usamos pop para eliminar el elemento de la lista
            lista_mascotas.pop(indice_mascota)
            print(f"La mascota {nombre_buscado} ha sido eliminada del registro.")
        else: #si no encuentra el nombre, mostramos mensaje solicitado
            print(f"La mascota {nombre_buscado} no se encuentra registrada.")
    
    elif opcion == 4:
        asignarVacunas(lista_mascotas)
        print("Vacunas actualizadas.")
        
    elif opcion == 5:
        if lista_mascotas == []:
            print("No hay mascotas en el sistema.")
        else:
            asignarVacunas(lista_mascotas)
            mostrarMascotas(lista_mascotas)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")