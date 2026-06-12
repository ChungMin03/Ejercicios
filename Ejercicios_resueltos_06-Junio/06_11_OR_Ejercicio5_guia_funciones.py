"""
Una plataforma educativa requiere un mini sistema de presentación que primero muestre un encabezado,
luego solicite los datos del estudiante y finalmente muestre su ficha completa.
🎯 Objetivo
Combinar 3 tipos de funciones: una sin args/sin return para el encabezado,
una sin args/con return para leer datos, y una con args/sin return para mostrar la ficha.
"""

#-----------------bloque de funciones-----------------

def encabezado():
    print("Ficha de estudiante")

def ingreso_datos():
    datos = []
    nombre = input("Ingrese su nombre: ")
    while True:
        try:
            semestre = int(input("Ingrese su semestre actual: "))
            if semestre < 1 or semestre > 5:
                print("Ingrese un valor valido")
            else:
                break
        except ValueError:
            print("Ingrese un valor numerico")
    carrera = input("Ingrese su carrera: ")
    rut = input("Ingrese su rut: ")
    datos.append(nombre)
    datos.append(semestre)
    datos.append(carrera)
    datos.append(rut)
    return datos

def mostrar_datos(name,semester,carrier,rut):
    print(f"Estudiante: {name}")
    print(f"Carrera: {carrier}")
    print(f"Semestre actual: {semester}")
    print(f"RUT del estudiante: {rut}")

#-----------------bloque de ejecucion-------------------


info = ingreso_datos()
nombre = info[0]
semestre = info[1]
carrera = info[2]
rut = info[3]

encabezado()
mostrar_datos(nombre,semestre,carrera,rut)