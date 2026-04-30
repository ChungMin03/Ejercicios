from random import randint

name = input("Ingrese su nombre: ")
lim_inf = int(input("Ingrese el número límite inferior: "))
lim_sup = int(input("Ingrese el número límite superior: "))
numero = randint(lim_inf, lim_sup)
vida= 100

if numero % 3 == 0 and (numero + 1 <= lim_sup):
    numero += 1
else:
    numero -= 1

#preguntamos numero al usuario
num_usuario = int(input("Ingrese su número: "))

if num_usuario - numero > 20:
    vida -= 30
elif num_usuario - numero >= 11 and num_usuario - numero <= 20:
    vida -= 20
elif num_usuario - numero >= 1 and num_usuario - numero <= 10:
    vida -= 10
    