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

from random import randint
name = input ("Ingrese su nombre: ").upper()
a = int(input("Ingrese limite de rango inferior: "))
b = int(input("Ingrese limite de rango superior: "))
numero_aleatorio = randint(a,b)
residuo = numero_aleatorio % 3

if residuo == 0 and numero_aleatorio + 1 > b:
    numero_aleatorio = numero_aleatorio - 1
elif residuo == 0:
    numero_aleatorio = numero_aleatorio + 1

puntaje_inicial = 100
intento = 3

trys = int(input("Empieza el juego, ingrese un numero (Tiene 3 intentos): "))
resta = abs(trys - numero_aleatorio)

if trys == numero_aleatorio:
    print ("Adivinaste el número!!!")
    print (f"Tu puntaje es de: {puntaje_inicial}")
else:     
    if trys != numero_aleatorio and resta >20:
        puntaje_final = puntaje_inicial - 30
        intento = intento - 1

    elif trys != numero_aleatorio and resta >=11 and resta <=20:
        puntaje_final = puntaje_inicial - 20
        intento = intento - 1

    elif trys != numero_aleatorio and resta >=1 and resta <=10:
        puntaje_final = puntaje_inicial - 10
        intento = intento-1

    if trys > numero_aleatorio:
        print ("El numero es Mayor")
        print (f"Su puntaje es de : {puntaje_final}")
    elif trys < numero_aleatorio:
        print ("El numero es Menor")
        print (f"Su puntaje es de : {puntaje_final}")

#SEGUNDO INTENTO
        trys = int(input("Continua el juego, ingrese un numero (Tiene 2 intentos): "))
        resta = abs(trys - numero_aleatorio)

    if trys == numero_aleatorio:
        print ("Adivinaste el número!!!")
        print (f"Tu puntaje es de: {puntaje_inicial}")
    elif trys != numero_aleatorio and resta >20:
        puntaje_final = puntaje_inicial - 30
        intento = intento - 1

    elif trys != numero_aleatorio and resta >=11 and resta <=20:
        puntaje_final = puntaje_inicial - 20
        intento = intento - 1

    elif trys != numero_aleatorio and resta >=1 and resta <=10:
        puntaje_final = puntaje_inicial - 10
        intento = intento-1

    if trys > numero_aleatorio:
        print ("El numero es Mayor")
        print (f"Su puntaje es de : {puntaje_final}")
    elif trys < numero_aleatorio:
        print ("El numero es Menor")
        print (f"Su puntaje es de : {puntaje_final}")

    #ULTIMO INTENTO
    trys = int(input("Continua el juego, ingrese un numero (Tiene 1 intentos): "))
    resta = abs(trys - numero_aleatorio)

    if trys == numero_aleatorio:
        print ("Adivinaste el número!!!")
        print (f"Tu puntaje es de: {puntaje_inicial}")
        print (f"BIEN HECHO: {name}")
    elif trys != numero_aleatorio and resta >20:
        puntaje_final = puntaje_inicial - 30
        intento = intento - 1

    elif trys != numero_aleatorio and resta >=11 and resta <=20:
        puntaje_final = puntaje_inicial - 20
        intento = intento - 1

    elif trys != numero_aleatorio and resta >=1 and resta <=10:
        puntaje_final = puntaje_inicial - 10
        intento = intento-1

    if trys > numero_aleatorio:
        print ("El numero es Mayor")
        print (f"Su puntaje es de : {puntaje_final}")
    elif trys < numero_aleatorio:
        print ("El numero es Menor")
        print (f"Su puntaje es de : {puntaje_final}")

    if intento == 0:
        print ("No te quedan más intentos")
        print (f"Tu puntaje final es: {puntaje_final}")
        print (f"El numero era: {numero_aleatorio}")
    if puntaje_final > 80:
        print (f"Excelente, estuviste muy cerca! {name}")
    elif puntaje_final > 50 and puntaje_final <79:
        print (f"Regular, pudiste hacerlo mejor {name}")
    elif puntaje_final < 49:
        print (f"Necesitas practicar! {name}")




