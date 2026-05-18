#---------------- DEFINICION DE VARIABLES --------------
vehiculo_flag = False
errores = ""
pesado = 0
ligero = 0

#--------------- BLOQUE DE EJECUCION ------------------

#REQUISITO 1
while not vehiculo_flag:
    try:
        cant_vehi = int(input("Ingrese la cantidad de vehículos que desea registrar: "))
        vehiculo_flag = True
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        print("---------------------------------------------------------------------")

#REQUISITO 2
count_vehi = 1
while count_vehi <= cant_vehi:
    print(f"--------- Vehículo {count_vehi} de {cant_vehi} -------------")
    placa = input("Ingrese la placa vehicular: ")
    if len(placa) < 6 or (" " in placa):
        count_vehi = count_vehi
        print("¡Placa inválida! Ingrese una placa con al menos 6 caracteres y sin espacios. ")
        continue
    


    capacidad_flag = False
    while not capacidad_flag:
        try:
            capacidad_carga = int(input("Ingrese la capacidad de carga del vehículo (toneladas): "))
            
            if capacidad_carga <= 0:
                print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga.")
                capacidad_flag = False
            else:
                capacidad_flag = True
                #REQUISITO 3
                if capacidad_carga > 55:
                    pesado += 1
                else:
                    ligero += 1

            
        except ValueError:
            print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga.")


    count_vehi += 1

#REQUISITO 4
print(f"¡La flota cuenta con {pesado} vehículos Pesados y {ligero} vehículos Ligeros! ¡Rutas asignadas!")