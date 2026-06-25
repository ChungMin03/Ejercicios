"""
=====================================================================
EJERCICIO DE PRÁCTICA: SISTEMA DE GESTIÓN DE ALQUILER DE VEHÍCULOS
=====================================================================

CONTEXTO:
Una empresa de rentas de autos necesita un programa en Python para gestionar 
el alquiler diario de sus vehículos. Para almacenar la información se debe 
utilizar una LISTA DE DICCONARIOS, donde cada diccionario representará un 
vehículo alquilado con la siguiente estructura inicial:
    - patente: string (ej: "ABCD12")
    - modelo: string (ej: "Toyota Corolla")
    - dias: entero (cantidad de días por los que se alquila)
    - promocion: booleano (inicialmente se registra como None o vacío)

El programa debe contar con un menú interactivo de 6 opciones que se repita 
constantemente hasta que el usuario decida salir.

---------------------------------------------------------------------
REQUERIMIENTOS DE LAS OPCIONES DEL MENÚ
---------------------------------------------------------------------

Opción 1 - Registrar vehículo:
El sistema debe solicitar al usuario el ingreso de la patente, el modelo 
y la cantidad de días de alquiler. Los datos se guardan en un diccionario 
y este se agrega a la lista general. El programa comienza con la lista vacía.

Opción 2 - Buscar vehículo:
El sistema solicita al usuario el ingreso de la patente a buscar. Si el 
vehículo se encuentra en la lista, se muestran todos sus datos en pantalla. 
Si no se encuentra, se informa al usuario con un mensaje claro.

Opción 3 - Eliminar registro:
Para implementar esta opción DEBES DEFINIR UNA FUNCIÓN INDEPENDIENTE encargada 
de buscar un vehículo por su patente. Esta función debe:
    - Recibir como parámetros la lista y la patente buscada.
    - Retornar el ÍNDICE (posición) del registro dentro de la lista.
    - Retornar -1 si el vehículo no existe.

El programa principal llamará a esta función: si el valor devuelto es distinto 
de -1, elimina el registro en esa posición de la lista. Si retorna -1, 
informa al usuario con el siguiente mensaje exacto:
    "vehículo con patente '[patente_ingresada]' no se encuentra registrado."

Opción 4 - Aplicar promociones:
El sistema recorre la lista completa de vehículos y actualiza el campo 
"promocion" de cada registro según la cantidad de días de alquiler: 
    - Si los días son MAYORES O IGUALES A 5, el campo pasa a True.
    - Si es menor, queda en False.
Esta operación afecta a todos los registros de la lista sin excepción.
Para implementar esta opción DEBES DEFINIR UNA FUNCIÓN que reciba la lista 
como parámetro y aplique esa regla a cada elemento.

Opción 5 - Mostrar vehículos alquilados:
El sistema primero debe actualizar los estados de todas las promociones 
haciendo el llamado OBLIGATORIO a la función definida en la Opción 4. 
Luego, recorre la lista completa mostrando los datos organizados con el 
siguiente formato de salida exacto:

=== LISTA DE VEHÍCULOS ALQUILADOS ===
Patente: ABCD12
Modelo: Toyota Corolla
Días: 6
Promoción: APLICADA
********************************************
Patente: XY3456
Modelo: Suzuki Swift
Días: 3
Promoción: PENDIENTE/NO APLICA
*********************************************

Opción 6 - Salir:
El sistema termina su ejecución mostrando un mensaje de despedida.

=====================================================================
"""

def mostrar_menu():
    print("============== MENU PRINCIPAL ==============")
    print("1.- Registrar vehiculo.")
    print("2.- Buscar vehiculo.")
    print("3.- Eliminar registro.")
    print("4.- Aplicar promociones.")
    print("5.- Mostrar vehiculos alquilados.")
    print("6.- Salir.")

def pedir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 6:
                raise ValueError
            else:
                break
        except ValueError:
            print("Error: Debe ingresar un numero entre 1 y 6.")
    return opcion

def validar_patente(patente):
    if patente.isalnum() and len(patente) == 6:
        return True
    else:
        return False

def validar_modelo(modelo):
    if modelo.strip() != "" and len(modelo) > 1:
        return True
    else:
        return False

def validar_dias(dias_alquiler):
    if dias_alquiler > 0:
        return True
    else:
        return False

def registrar_vehiculo(lista_v):
    while True:
        patente = input("Ingrese la patente del vehiculo a alquilar: ").upper()
        if validar_patente(patente):
            break
        else:
            print("Error: La patente ingresada no es correcta.")
    
    while True:
        modelo = input("Ingrese el modelo del vehiculo a alquilar: ").title()
        if validar_modelo(modelo):
            break
        else:
            print("Error: El modelo de vehiculo no es correcto.")
    
    while True:
        try:
            dias = int(input("Ingrese la cantidad de dias a alquilar: "))
            if validar_dias(dias):
                break
            else:
                print("Error: Debe alquilar al menos 1 dia.")
        except ValueError:
            print("Error: Debe ingresar un numero entero.")
    
    #una vez pasadas las 3 validaciones, creamos diccionario
    diccionario = {
        "patente": patente,
        "modelo": modelo,
        "dias": dias,
        "promocion": False
    }
    
    lista_v.append(diccionario)

def buscar_vehiculo(lista_v, patente_v):
    for i in range(len(lista_v)):
        if lista_v[i]["patente"] == patente_v:
            return i
    return -1

def aplicar_promocion(lista_v):
    for vehiculo in lista_v:
        vehiculo["promocion"] = True if vehiculo["dias"] >= 5 else False
        

def mostrar_vehiculos(lista_v):
    for vehiculo in lista_v:
        print(f"Patente: {vehiculo["patente"]}")
        print(f"Modelo: {vehiculo["modelo"]}")
        print(f"Dias: {vehiculo["dias"]}")
        print(f"Promocion: {"APLICADA" if vehiculo["promocion"] else "PENDIENTE/NO APLICA"}")
        print("*****************************************************")

#======================================= CODIGO PRINCIPAL =====================================================
#DECLARACION DE VARIABLES
lista_vehiculos = list()
opcion = 9999999999999999999999999

while opcion != 6:
    mostrar_menu()
    opcion = pedir_opcion()
    
    if opcion == 1:
        registrar_vehiculo(lista_vehiculos)
    
    elif opcion == 2:
        if not lista_vehiculos:
            print("No hay registros en el sistema para buscar.")
        else:
            patente_buscar = input("Ingrese la patente del vehiculo a buscar: ").upper()
            if validar_patente(patente_buscar):
                indice = buscar_vehiculo(lista_vehiculos, patente_buscar)
                if indice != -1:
                    print(f"Patente: {lista_vehiculos[indice]["patente"]}")
                    print(f"Modelo: {lista_vehiculos[indice]["modelo"]}")
                    print(f"Dias: {lista_vehiculos[indice]["dias"]}")
                    print(f"Promocion: {"APLICADA" if lista_vehiculos[indice]["dias"] >= 5 else "PENDIENTE/NO APLICA"}")
                else:
                    print(f"Error: El vehiculo con patente {patente_buscar} no se encuentra en el registro.")
            else:
                print(f"Error: La patente ingresada ({patente_buscar}) no es valida.")
    
    elif opcion == 3:
        if not lista_vehiculos:
            print("No hay registros en el sistema para eliminar.")
        else:
            patente_buscar = input("Ingrese la patente del vehiculo a buscar: ").upper()
            if validar_patente(patente_buscar):
                indice = buscar_vehiculo(lista_vehiculos, patente_buscar)
                if indice != -1:
                    lista_vehiculos.pop(indice)
                    print(f"Vehiculo con patente {patente_buscar} eliminado del registro.")
                else:
                    print(f"vehículo con patente {patente_buscar} no se encuentra en el registro.")
            else:
                print(f"Error: La patente ingresada ({patente_buscar}) no es valida.")
    
    elif opcion == 4:
        if not lista_vehiculos:
            print("Promocion no aplicada, no hay registros en el sistema.")
        else:
            aplicar_promocion(lista_vehiculos)
            print("Promociones aplicadas.")
    
    elif opcion == 5:
        if not lista_vehiculos:
            print("No hay registros en el sistema para mostrar.")
        else:
            aplicar_promocion(lista_vehiculos)
            print("================= LISTA DE VEHICULOS ALQUILADOS ====================")
            mostrar_vehiculos(lista_vehiculos)
    
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto")