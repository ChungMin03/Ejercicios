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

# ----------------- Bloque de bibliotecas -----------------
from random import randint


# ----------------- Bloque de variables -----------------

# Solicitud de datos al usuario.
nombre_jugador = input("Ingrese el nombre del jugador: ").upper()
limite_inferior = int(input("Ingrese el limite inferior del rango: "))
limite_superior = int(input("Ingrese el limite superior del rango: "))
numero_jugador = int(input("Ingrese el numero que crees que es: "))

# Asignación de puntaje inicial
puntaje = 100

# ----------------- Bloque de ejecución -----------------
# Generación del numero aleatorio dentro del rango.
numero_aleatorio = randint(limite_inferior, limite_superior)

# Ajuste del numero aleatorio si es multiplo de 3.
if numero_aleatorio % 3 == 0:
    if (numero_aleatorio + 1) <= limite_superior:
        numero_aleatorio = numero_aleatorio + 1
    else:
        numero_aleatorio = numero_aleatorio - 1

# Ciclo de intentos del jugador.
if numero_jugador == numero_aleatorio:
    print("Adivinaste el numero!")
else:
    if numero_jugador > numero_aleatorio:
        print("El numero es menor.")
    else:
        print("El numero es mayor.")

    diferencia = abs(numero_jugador - numero_aleatorio)
    if diferencia > 20:
        puntaje = puntaje - 30
    elif diferencia >= 11 and diferencia <= 20:
        puntaje = puntaje - 20
    elif diferencia >= 1 and diferencia <= 10:
        puntaje = puntaje - 10
    print(f"Puntaje actual: {puntaje}")

    # Segundo intento del jugador. Intentos = 2
    print("Segundo intento:")
    numero_jugador = int(input("Ingrese el numero que crees que es: "))
    if numero_jugador == numero_aleatorio:
        print("Adivinaste el numero!")
    else:
        if numero_jugador > numero_aleatorio:
            print("El numero es menor.")
        else:
            print("El numero es mayor.")

        diferencia = abs(numero_jugador - numero_aleatorio)
        if diferencia > 20:
            puntaje = puntaje - 30
        elif diferencia >= 11 and diferencia <= 20:
            puntaje = puntaje - 20
        elif diferencia >= 1 and diferencia <= 10:
            puntaje = puntaje - 10
        print(f"Puntaje actual: {puntaje}")

        # Tercer intento del jugador. Intentos = 1
        print("Tercer intento:")
        numero_jugador = int(input("Ingrese el numero que crees que es: "))
        if numero_jugador == numero_aleatorio:
            print("Adivinaste el numero!")
        else:
            print(f"El numero era: {numero_aleatorio}")

            diferencia = abs(numero_jugador - numero_aleatorio)
            if diferencia > 20:
                puntaje = puntaje - 30
            elif diferencia >= 11 and diferencia <= 20:
                puntaje = puntaje - 20
            elif diferencia >= 1 and diferencia <= 10:
                puntaje = puntaje - 10
            print(f"Puntaje final: {puntaje}")

# Clasificación del puntaje final del jugador.
if puntaje >= 80 and puntaje <= 100:
    print(f"{nombre_jugador} tu clasificación es: Excelente")
elif puntaje >= 50 and puntaje <= 79:
    print(f"{nombre_jugador} tu clasificación es: Regular")
elif puntaje >= 0 and puntaje <= 49:
    print(f"{nombre_jugador} tu clasificación es: Necesita Mejorar")


    

    





