"""
Desarrolle un programa que simule un juego de adivinanza con sistema de puntaje. El programa solicita:
Limite inferior del rango, Limite superior del rango, Nombre del jugador
Si el numero generado es multiplo de 3, se ajusta al siguiente numero que NO sea multiplo de 3 dentro del rango, aplicando:
numero = numero + 1, si el resultado no se sale del rango
numero = numero - 1, si el numero se sale del rango
El juego tiene 3 intentos. El jugador comienza con 100 puntos. Cada intento fallado aplica una penalizacion segun que tan lejos estuvo
PENALIZACION POR INTENTO FALLIDO:
Si la diferencia entre el intento y el numero es > 20: pierde 30 puntos
Si la diferencia es entre 11 y 20: pierde 20 puntos
Si la diferencia es entre 1 y 10: pierde 10 puntos
Despues de cada intento fallido, indicar si el numero es mayor o menor y mostrar el puntaje actual. En el tercer intento fallido: revelar el numero y clasificar el puntaje final
80-100 puntos: "Excelente"
50-79 puntos: "Regular"
0-49 puntos: "Necesitas practicar"
Si adivina en cualquier intento no aplicar penalizacion de ese intento, mostrar "ADIVINASTE" y clasificar el puntaje. El nombre del jugador debe mostrarse siempre en mayusculas
"""

from random import randint    

#--- declaracion de variables ---
name = input("Ingrese su nombre: ")
lim_inf = int(input("Ingrese el número límite inferior: "))
lim_sup = int(input("Ingrese el número límite superior: "))
numero = randint(lim_inf, lim_sup)
puntaje= 100
resultado = ""

#--- bloque de ejecucion ---
if numero % 3 == 0 and (numero + 1 <= lim_sup):
    numero += 1
elif numero % 3 == 0 and numero > lim_sup:
    numero -= 1


print("--- PRIMER INTENTO ---") #iniciamos primer intento
#preguntamos numero al usuario
num_usuario = int(input("Ingrese su número: "))
#verificamos si el numero es correcto, sino, restamos puntaje
if num_usuario == numero:
    resultado = f"Felicidades, adivinaste\nPuntaje final: {puntaje}"
else:
    diferencia = num_usuario - numero
    if diferencia > 20:
        puntaje -= 30
    elif diferencia >= 11 and diferencia <= 20:
        puntaje -= 20
    else:
        puntaje -= 10
        
    if num_usuario > numero:
        print(f"El numero es menor que {num_usuario}")
    else:
        print(f"El numero es mayor que {num_usuario}")
    
    print(f"Puntaje actual: {puntaje}")
    
    
    print("--- SEGUNDO INTENTO ---")    #empezamos segundo intento
    #preguntamos numero al usuario
    num_usuario = int(input("Ingrese su número: "))
    #verificamos si el numero es correcto, sino, restamos puntaje
    if num_usuario == numero:
        resultado = f"Felicidades, adivinaste\nPuntaje final: {puntaje}"
    else:
        diferencia = num_usuario - numero
        if diferencia > 20:
            puntaje -= 30
        elif diferencia >= 11 and diferencia <= 20:
            puntaje -= 20
        else:
            puntaje -= 10
            
        if num_usuario > numero:
            print(f"El numero es menor que {num_usuario}")
        else:
            print(f"El numero es mayor que {num_usuario}")
        
        print(f"Puntaje actual: {puntaje}")
        
        print("--- TERCER INTENTO ---")    #empezamos tercer intento
        #preguntamos numero al usuario
        num_usuario = int(input("Ingrese su número: "))
        if num_usuario == numero:
            resultado = f"Felicidades, adivinaste\nPuntaje final: {puntaje}"
        else:
            diferencia = num_usuario - numero
            if diferencia > 20:
                puntaje -= 30
            elif diferencia >= 11 and diferencia <= 20:
                puntaje -= 20
            else:
                puntaje -= 10
                
            resultado = f"El numero era: {numero}\nPuntaje final: {puntaje}"
            
#--- prints finales ---
print("------------------------------------")
print(f"Nombre de jugador: {name.upper()}")
print(resultado)
if puntaje >= 80 and puntaje <= 100:
    print("Excelente")
elif puntaje >= 50 and puntaje <= 79:
    print("Regular")
else:
    print("Necesitas practicar")