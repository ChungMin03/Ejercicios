'''
Desarrolle un programa que simule un juego de adivinanza con sistema de puntaje. El programa solicita:
-   Limite inferior del rango (entero).
-   Limite superior del rango (entero).
-   Nombre del jugador.

El programa genera un numero aleatorio dentro del rango:

|   from random import randint                                              |
|   numero_aleatorio = randint(limite_inferior, limite_superior)            |

Si el numero generado es multiplo de 3, se ajusta al siguiente numero que NO sea multiplo de 3 dentro del rango, aplicando:
    -   numero = numero + 1, si el resultado no sale del rango.
    -   numero = numero - 1, si numero + 1 se sale del rango.

El jugador tiene 3 intentos. El juego comienza con 100 puntos. Cada intento fallido aplica una penalizacion segun que tan
lejos estuvo:

|PENALIZACION POR INTENTO FALLIDO
|   - Si la diferencia entre el intento y el numero es > 20: pierdes 30 puntos.     |
|   - Si la diferencia es entre 11 y 20: pierdes 20 puntos.                         |
|   - Si la diferencia es entre 1 y 10: pierdes 10 puntos.                          |

Después de cada intento fallido. Indicar si el número es mayor o menor y mostrar el puntaje actual. En el tercer intento
fallido: Revelar el numero y clasificar el puntaje final del jugador:
|   PUNTAJE FINAL       |   CLASIFICACION       |
|   80 - 100            |   Excelente           |
|   50 - 79             |   Regular             |
|   0 - 49              |   Necesita Mejorar    |

Adivinar en cualquier intento: no aplicar penalización de ese intento, mostrar mensaje de "Adivinaste el numero!" y clasificar
el puntaje. El nombre del jugador debe mostrarse en mayúsculas en el resultado final.
'''


#----------Bloque de variables-------------------------------------------------------------------

from random import randint
name = input("Ingrese su nombre\n")
sub = int(input("Ingrese limite inferior: "))
top = int(input("Ingrese limite superior: "))

aleatorio = randint(sub, top)
puntos = 100
resto = aleatorio % 3



#------------------------Bloque de ejecucucion---------------------------------------------------
if resto == 0:
    if (aleatorio + 1) > top:
        aleatorio = aleatorio - 1
    else:
        aleatorio = aleatorio + 1
intento = int(input("Ingrese el numero que cree que sea: ")) 
diff = abs(intento - aleatorio)
if intento == aleatorio:
    print("Ganaste :D")
    print(f"El numero era {aleatorio}")
    print(name.upper())
elif intento != aleatorio:

    #Caso es muy alto
    if intento > aleatorio and diff > 20:
        print("Muy alto")
        puntos = puntos - 30
    elif intento > aleatorio and diff <= 20 and diff >= 11:
        print("Medio alto")
        puntos = puntos - 20
    elif intento > aleatorio and diff < 11:
        print("Un poco alto")
        puntos = puntos - 10


        #Caso es muy bajo
    elif intento < aleatorio and diff > 20:
        print("Muy bajo")
        puntos = puntos - 30
    elif intento < aleatorio and diff <= 20 and diff >= 11:
        print("Medio bajo")
        puntos = puntos - 20
    elif intento < aleatorio and diff < 11:
        print("Un poco bajo")
        puntos = puntos - 10
        
    print("Segundo Intento") 

    intento = int(input("Ingrese el numero que cree que sea: ")) 
    diff = abs(intento - aleatorio)
    if intento == aleatorio:
        print(f"Ganaste con {puntos} puntos")
    elif intento != aleatorio:

        #------------------------------------Caso es muy alto------------------------------

        if intento > aleatorio and diff > 20:
            print("Muy alto")
            puntos = puntos - 30
        elif intento > aleatorio and diff <= 20 and diff >= 11:
            print("Medio alto")
            puntos = puntos - 20
        elif intento > aleatorio and diff < 11:
            print("Un poco alto")
            puntos = puntos - 10


            #--------------------------------Caso es muy bajo--------------------------------

        elif intento < aleatorio and diff > 20:
            print("Muy bajo")
            puntos = puntos - 30
        elif intento < aleatorio and diff <= 20 and diff >= 11:
            print("Medio bajo")
            puntos = puntos - 20
        elif intento < aleatorio and diff < 11:
            print("Un poco bajo")
            puntos = puntos - 10

        print("Tercer Intento") 


        intento = int(input("Ingrese el numero que cree que sea: ")) 
        diff = abs(intento - aleatorio)
        if intento == aleatorio:
            print(f"Ganaste con {puntos} puntos")
        elif intento != aleatorio:

            #Caso es muy alto
            if intento > aleatorio and diff > 20:
                print("Muy alto")
                puntos = puntos - 30
            elif intento > aleatorio and diff <= 20 and diff >= 11:
                print("Medio alto")
                puntos = puntos - 20
            elif intento > aleatorio and diff < 11:
                print("Un poco alto")
                puntos = puntos - 10


                #Caso es muy bajo
            elif intento < aleatorio and diff > 20:
                print("Muy bajo")
                puntos = puntos - 30
            elif intento < aleatorio and diff <= 20 and diff >= 11:
                print("Medio bajo")
                puntos = puntos - 20
            elif intento < aleatorio and diff < 11:
                print("Un poco bajo")
                puntos = puntos - 10

print(f"El numero era {aleatorio}")
print(name.upper())
print(f"Terminaste con {puntos} puntos")
if puntos <= 100 and puntos >= 80:
    print("Excelente")
elif puntos <= 79 and puntos >= 50:
    print("Regular")
elif puntos <= 49 and puntos >= 0:
    print("Necesita Mejorar")