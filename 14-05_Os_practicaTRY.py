"""Una empresa realiza una encusta de satisfaccion. el menú tiene opcines.
 1 registrar respuesta (1 = muy insatisfecho 5 = muy satisfecho)
 2 ves estadisticas (promedio, Mejor puntuacion, % respondieron 4 o 5), 
 3 nueva encuesta 
 4 salir. 
 la opcion 3 reinicia los contadores"""



#-------------------Bloque de variables---------------------------------------------------------

opcion = 0
total_respuestas = 0
total_nivel = 0
puntaje = 0
#valores de satisfaccion
muy_satisfecho = 0
satisfecho = 0
neutro = 0
insatisfecho = 0
muy_insatisfecho = 0
#----------------

#-------------------Bloque del menú----------------------------------------------------------------
while opcion != 4:

    print("***Menu de Encuesta***")
    print("1.- Ingrese su nivel de satisfaccion (1-5)")
    print("2.- Ver estadisticas")
    print("3.- Nueva encuesta (Reinicia informacion anterior)")
    print("4.- Salir")



#-------------------Bloque de ejecución-------------------------------------------------------------
    try:
        opcion = int(input("Ingrese una de las opciones(1-4): "))

    except ValueError:
        print("Ingrese un valor numerico del 1 al 4")

    if opcion == 1:
        flag1 = False
        while not flag1:
            try:
                nivel = int(input("Ingrese Su nivel de satisfacción\n5 = Muy satisfecho\n4 = Satisfecho\n3 = Neutral\n2 = Insatisfecho\n1 = Muy insatisfecho\n "))
                flag1 = True

            except ValueError:
                print("Ingrese un valor numerico")

        #Sumando los niveles de satisfaccion
        total_respuestas += 1
        total_nivel += nivel
        if nivel == 5:
            muy_satisfecho += 1

        elif nivel == 4:
            satisfecho += 1

        elif nivel == 3:
            neutro += 1

        elif nivel == 2:
            insatisfecho += 1

        elif nivel == 6:
            muy_insatisfecho += 1
            
        else:
            print("Valor invalido")
            total_respuestas -= 1

        #Verificar cual e la mejor nota
        if muy_satisfecho != 0:
            puntaje = 5

        elif satisfecho != 0:
            puntaje = 4

        elif neutro != 0:
            puntaje = 3

        elif insatisfecho != 0:
            puntaje = 2

        elif muy_insatisfecho != 0:
            puntaje = 1

            
    elif opcion == 2:
        if total_respuestas == 0:
            print("Aun no hay encuestas")

        else:
            print(f"La nota mas alta es {puntaje}/5")
            print(f"El total de encuestados es de {total_respuestas}")
            print(f"El promedio de puntaje es de {total_nivel/total_respuestas}")
            print(f"En promedio de pesrsonas satifechas y muy satisfechas es de {(muy_satisfecho+satisfecho)/total_respuestas}")

    elif opcion == 3:
        print("Encuestas reiniciadas")
        total_respuestas = 0
        puntaje = 0

        #valores de satisfaccion

        muy_satisfecho = 0
        satisfecho = 0
        neutro = 0
        insatisfecho = 0    
        muy_insatisfecho = 0
    elif opcion == 4:

        print("Gracias por usar nuestro programa de encuestas")


"""
#--------------intento con lista ---------------------
#definimos variables
lista_nivel = []
flag1 = False

#while para que no se apage la encuesta hasta que ingrese una respeusta valida
while not flag1:
    try:
        nivel = int(input("Ingrese Su nivel de satisfacción\n5 = Muy satisfecho\n4 = Satisfecho\n3 = Neutral\n2 = Insatisfecho\n1 = Muy insatisfecho\n "))
        if nivel > 5 or nivel < 1:      #verificacion de que la nota este entre 1 y 5
            raise ValueError("El nivel de satisfaccion debe estar entre 1 y 5")
    
    except ValueError as error:
        print(f"Error: {error}")
        flag1 = True
        top_nivel = lista_nivel.count(5) + lista_nivel.count(4)
        
    lista_nivel.append(nivel)
#Prints de la lista
print(len(lista_nivel)-1)       #cantidad de numeros en la lista
print(max(lista_nivel))         #la nota mas alta
print(min(lista_nivel))         #La nota mas baja
print(f"{(top_nivel/(len(lista_nivel)-1))*100}%")         #porcentaje de 4 y 5 en la lista
"""