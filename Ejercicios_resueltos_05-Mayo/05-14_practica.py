"""Una empresa realiza una encusta de satisfaccion. el menú tiene opcines.
1 registrar respuesta (1 = muy insatisfecho 5 = muy satisfecho)
2 ves estadisticas (promedio, Mejor puntuacion, % respondieron 4 o 5), 
3 nueva encuesta 
4 salir. 
la opcion 3 reinicia los contadores"""

opcion = 10000000000000000000000000000000000000000000000000000000
count = 0
acum = 0

while opcion != 4:
    print("******* MENU PRINCIPAL *********")
    print("1.- Registrar respuestas")
    print("2.- Ver estadisticas")
    print("3.- Nueva encuesta")
    print("4.- Salir")
    print("----------------------------------")
    
    try:
        opcion = int(input("Ingrese una opcion: ")) #ocho
    except ValueError:
        print("ERROR: Debe ingresar una opcion entre 1 y 4")
        continue
    
    if opcion == 1:
        print("---- Nivel de satisfacción ----")
        print("(1) Muy insatisfecho\n(2) Insatisfecho\n(3) Medianamente satisfecho\n(4) Satisfecho\n(5) Muy satisfecho\n")
        
        try:
            satis_nivel = int(input("Ingrese su nivel de satisfaccion (1-5): "))
            if satis_nivel < 1 or satis_nivel > 5:
                raise ValueError("Debe ingresar un numero entre 1 y 5")
        except ValueError as Error: 
            print(f"ERROR: {Error}")

        #aumentamos variables
        count += 1
