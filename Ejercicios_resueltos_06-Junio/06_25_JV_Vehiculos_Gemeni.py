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

#----------------- bloque variables ----------------

lista_vehiculos = []

#----------------- bloque funciones validacion ----------------

def validar_patente(patente):
    if patente.strip() != "" and patente.replace(" ", "").isalnum() and len(patente) == 6:
        return True
    else:
        return False
    
def validar_modelo(modelo):
    if modelo.strip() != "" and modelo.replace(" ", "").isalpha():
        return True
    else:
        return False

def validar_numero(dias):
    if isinstance(dias, int) and dias > 0:
        return True
    else:
        return False

def validar_opcion(opcion):
    if isinstance(opcion,int) and (opcion >= 1 and opcion <= 6):
        return True
    else:
        return False
    
#----------------- bloque funciones Menu ----------------

def menu():
    print("\n======== MENÚ PRINCIPAL ========")
    print("1.- Registrar vehiculo")
    print("2.- Buscar vehiculo")
    print("3.- Eliminar vehiculo")
    print("4.- Aplicar promocion")
    print("5.- Mostrar vehiculos")
    print("6.- Salir")
    print("================================")

def opcion_escogida():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if validar_opcion(opcion):
                return opcion
            else:
                print("Debe escoger una opción del 1 al 6")
        except ValueError:
            print("Debe ingresar un valor numerico")

def crear_vehiculo(patente: str, modelo: str, dias: int) -> dict:
    vehiculo = {
        "Patente": patente,
        "Modelo": modelo,
        "Dias": dias,
        "Promocion": False 
    }
    return vehiculo


def registrar_vehiculo():
    #Se registra la patente:
    while True:
        patente = input("Ingrese su patente: ").upper().strip()
        if validar_patente(patente):
            break
        else:
            print("Debe ingresar solo letras y numeros")
    
    #Se registra el modelo:
    while True:
        modelo = input("Ingrese el modelo de su auto: ").capitalize().strip()
        if validar_modelo(modelo):
            break
        else:
            print("No debe ingresar caracteres especiales y tampoco debe estar el campo vacio")

    #Se registra los dias de arrendamiento:
    while True:
        dias = int(input("Ingresa la cantidad de dias para arrendar: "))
        try:
            if validar_numero(dias):
                break
            else:
                print("Debe ingresar al menos un dia de arrendamiento")
        except ValueError:
            print("Debe ingresar solo numeros")
    
    lista_vehiculos.append(crear_vehiculo(patente, modelo, dias))
    print(f"Se ha registrado correctamente el vehiculo con patente {patente}, de modelo {modelo} con un total de {dias} dias arrendando.")

def buscar_vehiculo(patente_buscar, lista_vehiculos):
    for i in range(len(lista_vehiculos)):
        if lista_vehiculos[i]["Patente"].upper() == patente_buscar.upper():
            return i
        else:
            print(f"No se ha encontrado del vehiculo de pantente {patente_buscar}")
    return -1

def eliminar_vehiculo(posicion):
    if posicion != -1:
        posicion = lista_vehiculos[i]["Patente"]
        lista_vehiculos.pop(posicion)
        return True
    return False
    
def aplicar_promocion1(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        if vehiculo['Dias'] >= 5 and vehiculo['Promocion'] == False:
            vehiculo['Promocion'] = True
            print(f"El vehiculo con pantente: {vehiculo['Patente']} se le aplico promocion")
        elif vehiculo['Promocion'] == True:
            print(f"El vehiculo con patente {vehiculo['Patente']} ya tiene propoción aplicada")
        else:
            print(f"{vehiculo['Patente']} no cumple con los requisitos para la promoción.")

def aplicar_promocion2(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        if vehiculo['Dias'] >= 5 and vehiculo['Promocion'] == False:
            vehiculo['Promocion'] = True

def mostrar_vehiculos():
    if not lista_vehiculos:
        print("No hay vehiculos registrados")
    
    for vehiculo in lista_vehiculos:
        print(f"Patente: {vehiculo['Patente']}")
        print(f"Modelo: {vehiculo['Modelo']}")
        print(f"Dias de arrendamiento: {vehiculo['Dias']}")
        print(f"Promoción: {'APLICADA' if vehiculo['Promocion'] else 'PENDIENTE'}")

    print("Proceso completado")

#----------------- bloque funcion principal ----------------

def main():
    while True:
        menu()
        opcion = opcion_escogida()

        if opcion == 1:
            registrar_vehiculo()
        
        elif opcion == 2:
            patente_buscar = input("Ingrese patente: ").strip().upper()
            posicion = buscar_vehiculo(patente_buscar, lista_vehiculos)

            if posicion != -1:
                vehiculo = lista_vehiculos[posicion]
                print(f"\n--- Reserva encontrada ---")
                print(f"Patente: {vehiculo['Patente']}")
                print(f"Modelo: {vehiculo['Modelo']}")
                print(f"Dias arrendado: {vehiculo['Dias']}")
                print(f"Promocion: {'APLICADA' if vehiculo['Promocion'] == True else 'PENDIENTE'}")
            else:
                print(f"No se encontro vehiculo con la patente {patente_buscar}")
       
        elif opcion == 3:
            patente_eliminar = input("Ingrese patente: ").strip().upper()
            posicion = buscar_vehiculo(patente_eliminar, lista_vehiculos)

            if eliminar_vehiculo(posicion):
                print(f"Se elimino el vehiculo de pantete {patente_eliminar}")
            else:
                print(f"No se pudo eliminar el vehiculo de pantente {patente_eliminar}")
        
        elif opcion == 4:
            aplicar_promocion1(lista_vehiculos)            
        
        elif opcion == 5:
            if not lista_vehiculos:
                print("No se han ingresado vehiculos")
            else:
                aplicar_promocion2(lista_vehiculos)
                mostrar_vehiculos()
        
        elif opcion == 6:
            print("Gracias por usar el sistema")
            break

#----------------- Bloque de ejecucion ----------------

if __name__ == "__main__":
    main()