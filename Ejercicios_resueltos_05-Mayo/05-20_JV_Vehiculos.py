# ----- Bloque funciones -----

# Requisito 1:
# - Cantidad de vehiculos a registrar
def cantidad_vehiculos():
    flag = False
    while not flag:
        try:
            cantidad = int(input("Cantidad: "))

            # Se verifica que la cantidad de vehiculos ingresados sea mayor a 0
            if cantidad > 0:
                flag = True
                return cantidad
            
            else: 
                print("Debe ingresar un valor mayor a 0")
                
        except ValueError:
            print("No ingreso un numero entero")


# Requisito 2:
# - Placa vehicular
def placa_vehicular():
    flag2 = False
    while not flag2:
        matricula = input("Ingresar matricula: ").upper()
        if len(matricula) == 6 and " " not in matricula:
            flag2 = True
            return matricula
        else:
            print("No debe escribir espacios y la placa debe tener 6 caracteres")

# - Cantidad de carga:

def cantidad_cargada():
    flag3 = False
    while not flag3:
        try:
            capacidad_carga = float(input("Ingresar carga: "))

            if capacidad_carga <= 0:
                print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga")
            
            else:
                flag3 = True
                return capacidad_carga

        except ValueError:
            print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga")

# Clasificacion del vehiculo

def calificacion_vehiculo():
    calificacion= cantidad_cargada()

    if calificacion > 55:
        peso = "PESADO"
    elif calificacion <= 55 and calificacion > 0:
        peso = "LIGERO"

    return [calificacion, peso]

 
# ----- Bloque ejecución -----

total_vehiculos = cantidad_vehiculos()

total_pesados = 0
total_ligeros = 0
historial_vehiculos = []

for i in range (total_vehiculos):

    solicitud_matricula = placa_vehicular()
    dato_peso = calificacion_vehiculo()

    if dato_peso[1] == "PESADO":
        total_pesados = total_pesados + 1
    else:
        total_ligeros = total_ligeros + 1
        
    info_vehiculo = [solicitud_matricula, dato_peso]
    historial_vehiculos.append(info_vehiculo)

print(f"\n¡La flota cuenta con un total de {total_vehiculos} vehiculos donde {total_pesados} son vehículos Pesados y {total_ligeros} son vehículos Ligeros! ¡Rutas asignadas!")
print(" ---- Historial de vehiculos ---- ")
print(historial_vehiculos)