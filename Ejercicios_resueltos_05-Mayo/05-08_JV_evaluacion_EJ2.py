# Bloque de librerias --------------------------
from random import randint

# Bloque de variables --------------------------

num1 = int(input("Ingresar primer numero: "))
num2 = int(input("Ingresar segundo numero: "))

# Bloque de ejecución --------------------------

# Se confirma que el primer numero a ingresar sea menor.
if num1 < num2:
    numero = randint(num1, num2)

    if numero % 2 != 0:
        if (numero + 1) >= num1 and (numero + 1) <= num2:
            numero = numero + 1
        else:
            numero = numero - 1 
else: 
    print("El primer numero a ingresar, debe ser menor que el segundo.")


# Si lo anterior esta bien, el jugador empieza con su primer intento.
jugador = int(input("Ingresa tu primer intento (1/3): "))
if jugador == numero:
    print("Felicidades! Adivinaste en el primer intento")
    print(f"El numero adivinar era: {numero}")
else: 
    if jugador > numero:
        print("El numero es más pequeño")

    elif jugador < numero:
        print("El numero es más grande")

    jugador2 = int(input("Ingresa tu segundo intento (2/3): "))
    if jugador == numero:
        print("Felicidades! Adivinaste en el segundo intento")
        print(f"El numero adivinar era: {numero}")
    else: 
        # Se comprueba si el segundo numero era más cercano o mas lejano
        # que en su primer intento.
        if jugador > numero: #numero: 10, jugador1: 4 y jugador2: 14
            print("El numero es más pequeño")
            diferencia1 = abs(numero - jugador) # 10 - 4 = 6, 10 - 14 = 4
            diferencia2 = abs(numero - jugador2)

            if diferencia1 > diferencia2:
                print("En el segundo intento estuvo más cerca")
            else: 
                print("En su primer intento estuvo más cerca")

        elif jugador < numero:
            print("El numero es más grande")
            
            diferencia1 = abs(numero - jugador) # 10 - 4 = 6, 10 - 14 = 4
            diferencia2 = abs(numero - jugador2)

            if diferencia1 > diferencia2:
                print("En el segundo intento estuvo más cerca")
            else: 
                print("En su primer intento estuvo más cerca")

        # Se llega al tercer intento del jugador.
        jugador = int(input("Ingresa tu tercer intento (3/3): "))
        if jugador == numero:
            print("Felicidades! Adivinaste en el tercer intento")
            print(f"El numero adivinar era: {numero}")
        else: 
            if jugador > numero:
                print("El numero es más pequeño")
                print("PERDISTE!")
                print(f"El numero adivinar era: {numero}")

            elif jugador < numero:
                print("El numero es más grande")
                print("PERDISTE!")
                print(f"El numero adivinar era: {numero}")



