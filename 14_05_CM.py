#ejercicio ejemplo (mio)
#1. Pedir la cantidad de socios con validacion (Try-Except)
cant_valida = False
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
