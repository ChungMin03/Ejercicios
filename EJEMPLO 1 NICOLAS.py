#Declaramos variables
cantidad_vehiculos = 0 
placa = ""
capacidad = 0
pesados = 0
ligeros = 0

#ciclo para repetir la pregunta hasta que genere el numero positivo
while cantidad_vehiculos <= 0:
    try:
        cantidad_vehiculos = int(input("Ingrese cantidad de vehiculos a registrar: "))
#Verificar con un if
        if cantidad_vehiculos <= 0:
            raise ValueError 

    except ValueError:
        print ("¡Cantidad inválida! Ingresa un entero positivo para continuar.")


#Ahora registramos cantidad de vehiculos indicadas por el usuario
for z in range(1, cantidad_vehiculos + 1):
    #imprimir un titulo para saber que vehiculo estoy registrando del total
    #no es parte del ejercicio
    print(f"\n------ Vehiculo {z} de {cantidad_vehiculos} -----") 
    #solicitar la placa del vehiculo
cumple = False
while not cumple:    
    placa = input("Ingrese la patente del vehiculo: ").upper()
#verificamos si cumple los requisitos de aceptación (longitud y espacios)
    if len(placa) >= 6 and " " not in placa:
        print ("Patente Registrada correctamente!")
        cumple = True
    else: 
        print ("La patente no cumple con los siguientes requisitos:\n - No debe contener espacios\n -Debe tener al menos 6 caracteres ")


#Solicitamos la capcacidad 
capacidad = 0

while capacidad <= 0: 
    try:
        capacidad = int(input("Ingrese Capacidad de carga del vehiculo (Tonteladas)"))
        if capacidad <= 0:
            raise ValueError
    except ValueError:
        print ("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga.")


#Verificamos la capacidad para la clasificacion
if capacidad > 55:
    pesados +=1
else: 
    ligeros = ligeros + 1

#Mostrar mensaje solicitado (resumen)
print(f"La flota cuenta con {pesados} Vehiculos pesados\n Y {ligeros} Vehiculos Ligeros.\n Rutas asignadas correctamente!!") 