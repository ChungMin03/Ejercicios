#---------- BLOQUE DE VARIABLES --------------

from random import randint #importamos funcion desde libreria random
lim_inferior = int(input("Ingrese límite inferior: "))
lim_superior = int(input("Ingrese límite superior: "))
numero = randint(lim_inferior, lim_superior)


#--------- BLOQUE DE EJECUCION ----------------
if numero % 2 != 0:
    if numero + 1 <= lim_superior:
        numero += 1
    else:
        numero -= 1

print("******** ADIVINA EL NÚMERO ********")
#PRIMER INTENTO
print("******** PRIMER INTENTO ********")
intento_1 = int(input("Intente adivinar: "))
if intento_1 == numero:
    print("Felicitaciones, adivinó en el primer intento")
else:
    if intento_1 > numero:
        print("El número es menor")
    else:
        print("El número es mayor")
    
    #SEGUNDO INTENTO
    print("******** SEGUNDO INTENTO ********")
    intento_2 = int(input("Intente de nuevo: "))
    if intento_2 == numero:
        print("Felicitaciones, adivinó en su segundo intento")
    else:
        if intento_2 > numero:
            print("El número es menor")
        else:
            print("El número es mayor")
        print("Te daré una pista:")
        if abs(numero - intento_1) > abs(numero - intento_2):
            print(f"El número que buscas está más cerca de {intento_2} que de {intento_1}")
        else:
            print(f"El número que buscas está más cerca de {intento_1} que de {intento_2}")
    
            #INTENTO 3
        print("******** TERCER INTENTO ********")
        intento_3 = int(input("Intente la última vez: "))
        if intento_3 == numero:
            print("Felicitaciones, pudiste adivinar")
        else:
            print(f"Perdiste.\nEl número era: {numero}")                        