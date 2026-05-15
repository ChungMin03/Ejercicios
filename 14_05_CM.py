#ejercicio ejemplo (mio)
#1. Pedir la cantidad de socios con validacion (Try-Except)
"""cant_valida = False
while not cant_valida:
    try:
        cant_socios = int(input("Ingrese la cantidad de socios que desea inscribir: "))
        if cant_socios > 0:
            cant_valida = True
        else:
            print("Ingrese un numero mayor a 0.")
    except ValueError:
        print("ERROR: Edad debe ser un número entero.")

#2. ciclo for para procesar cada socio
for i in range(1, cant_socios+1):
    print(f"----- Datos del socio {i} -----")
    nombre = input("Ingrese el nombre del socio: ").strip().upper()
    #validacion de edad con (Try-Except)
    edad_valida = False
    while not edad_valida:
        try:
            edad = int(input(f"Ingrese la edad de {nombre}: "))
            edad_valida = True
        except ValueError:
            print("ERROR: Edad ingresada no válida.")
    
    recom_medica = input("¿Posee recomendación médica? (si/no) ").lower()


    #3. Validacion de requisitos
    motivos_rechazo = ""
    if edad < 15:
        motivos_rechazo += "Motivo: Edad insuficiente\n"
    if edad > 60 and recom_medica == "no":
        motivos_rechazo += "Motivo: Tiene mas de 60 años y no posee recomendación médica\n"

#Prints finales
    if motivos_rechazo == "":
        print(f"Socio {nombre} aceptado")
    else:
        print(f"Socio {nombre} rechazado\n{motivos_rechazo}")
"""

#ejercicio encuesta satisfaccion
opcion = 0
count = 0
acum = 0
promedio = 0
mejor = 0
peor  = 6
nivel_4_5 = 0
porcent_45 = 0
opcion_valida = False

while opcion != 4:
    print("**** ENCUESTA SATISFACCIÓN ****")
    print("1.- Registrar respuestas")
    print("2.- Ver estadisticas")
    print("3.- Nueva encuesta")
    print("4.- Salir")
    print("----------------------------------")
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("ERROR: Opción debe ser un numero (1-4).")
        print("----------------------------------")
        continue
    
    if opcion == 1:
        print("---- Nivel de satisfacción ----")
        print("(1) Muy insatisfecho\n(2) Insatisfecho\n(3) Medianamente satisfecho\n(4) Satisfecho\n(5) Muy satisfecho\n")
        
        try:
            nivel_sat = int(input("Ingrese su nivel de satisfacción (1/5): "))
            if nivel_sat < 1 or nivel_sat > 5:
                raise ValueError("El nivel de satisfacción debe estar entre 1 y 5")
        except ValueError as error:
            print(f"ERROR: {error}")
            print("----------------------------------")
            continue
        
        if nivel_sat < peor:
            peor = nivel_sat

        if nivel_sat > mejor:
            mejor = nivel_sat
        
        if nivel_sat >= 4:
            nivel_4_5 += 1

        count += 1
        acum += nivel_sat
        print("----------------------------------")
    elif opcion == 2:
        try:
            #promedio
            promedio = acum / count
            #porcentaje que respondieron 4 o 5
            porcent_45 = nivel_4_5 / count * 100
            
            #prints
            print("********* Estadisticas ***********")
            print(f"Promedio de satisfacción: {promedio}")
            print(f"Mejor puntuación: {mejor}")
            print(f"Peor puntuación: {peor}")
            print(f"Porcentaje de satisfacción 4 o 5: {porcent_45}%")
            print("----------------------------------")

        except ZeroDivisionError:
            print("No ha respondido la encuesta de satisfacción")
            print("----------------------------------")


    elif opcion == 3:
        count = 0
        acum = 0
        promedio = 0
        mejor = 0
        peor  = 6
        nivel_4_5 = 0
        porcent_45 = 0
        print("Contadores reiniciados")
        print("----------------------------------")

    elif opcion == 4:
        print("Gracias por responder nuestra encuesta")
        print("----------------------------------")
    else:
        print("Opción ingresada no válida")
        print("----------------------------------")
        
        
        
        