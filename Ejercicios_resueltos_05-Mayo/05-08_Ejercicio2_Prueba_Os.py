from random import randint
#--------------------------Bloque de imputs y variables--------------------------------------------------

name = input("Ingrese su Username: ")
sub = int(input("Ingrese el límite inferior: "))
top = int(input("Ingrese el límite superior: "))

number = randint(sub, top)
resto = number % 2
if resto != 0:
    if (number + 1) > top:
        number -= 1
    else:
        number += 1
print(number)

#----------------------------------Bloque de ejecución---------------------------------------------------

cry1 = int(input("---COMIENZA EL JUEGO---\nIngrese un número para intentar adivinar el número RANDOM\n"))
if cry1 == number:
    print("Felicidades atinaste")
elif cry1 > number:
    posicion = "Muy Alto"
else:
    posicion = "Muy bajo"
    print(f"Estás {posicion}")
    #Comienza el segundo intento------------------------------------------------------------
    cry2 = int(input("SEGUNDO INTENTO!!!\nIngrese otro numero para adivinar el número RANDOM\n"))
    if cry2 == number:
        print("Que grande, le atinaste")
    elif cry2 > number:
        posicion = "Muy alto"
    else:
        posicion = "Muy Bajo"
        diff1 = abs(cry1 - number)
        diff2 = abs(cry2 - number)
        print(f"Estas {posicion}")
        if diff1 > diff2:
            print(f"{cry2} está mas cerca")
        else:
            print(f"{cry1} está mas cerca")
        cry3 = int(input("ULTIMO INTENTO!!!\n Ingrese su ultima oportunidad para adivinar el numero RANDOM\n"))
        if cry3 == number:
            print("SAFASTE AL ULTIMO\nFELICIDADES!!!")
        else:
            print("PERDISTE!!!! >:D")
            
print(f"EL numero era: {number}")



