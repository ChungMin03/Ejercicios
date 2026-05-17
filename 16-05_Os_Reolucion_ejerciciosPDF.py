
#Ejercicios para practicar programacion enviados por el profe y divididios en niveles

#------------------------nivel 1--------------------------------------

#ejercicio 1
"""Un programa que pida al usuario un numero 
y muestre en pantalla todos los numeros hassta el numero que indico"""

'''
#-----------------bloque de input---------------------------
n1 = int(input("Ingrese numero hasta el que quiere contar: "))

#-----------------bloquye de ejecucion----------------------
for i in range(1,(n1+1)):
    print(i)
'''

#ejercicio 2
"""Pide al usuario un numero n y calcula la suma hasta ese numero"""
'''
#-----------------bloque de input y variables---------------------------
n2 = int(input("Ingrese numero hasta el que desea hacer la sumatoria: "))
suma = 0

#-----------------bloque de ejecutables---------------------

for i in range(1, (n2+1)):
    suma += i
print(suma)
'''

#ejercicio 4
"""mostrar la tabla hasta el 10 del numero que ingrese el usuario"""
'''
#-----------------bloque de input---------------------------
n3 = int(input("Ingrese el numero del cual quiere la tabla: "))

#-----------------bloque de ejecutables---------------------
for i in range(1,11):
    resultado = i * n3
    print(f"{i} * {n3} = {resultado}")

#ejercicio 4
"""contar cunatos pares existen desde 1 hasta el numero que ingresa el usuario"""
'''


#ejercicio 5
'''
#-----------------bloque de input y variables---------------------------
n4 = int(input("Ingrese un numero hasta el que quiere contar pares: "))
count = 0
#-----------------bloque de ejecutables---------------------------------
for i in range(1, (n4+1)):
    if i % 2 == 0:
        count += 1
if count != 0:
    print(count)
'''


#------------------------nivel 2--------------------------------------

#ejercicio 1
"""pida al usuario cuantas notas ingresara, luego calcule el promedio.
las notas estan en una escala del 1 al 7"""
#-----------------bloque de input y variables---------------------------
'''
#-----------------bloque de input y variables---------------------------
try:
    quantity = int(input("Ingrese la cantidad de notas que desea ingresar: "))
except ValueError:
   print("ingrese valores numericos")
count2 = 0

#-----------------bloque de ejecucion----------------------------------
for i in range(1,(quantity + 1 )):
    grades = float(input("Ingrese las calificaciones a promediar: "))
    count2 += grades
print(f"El promedio es {(count2/quantity):.2f}")'''


#ejercicio 2
"""pide al usuario un numero n >= 0 y calcula su factorial, muestra el resultado"""

'''
#-----------------bloque de inputs----------------------------
try:
    quantity = int(input("Ingrese el factorial mayor a 0 que desea calcular: "))
    if quantity < 0:
        raise ValueError("El numero debe ser mayor a 0")
except ValueError:
   print("ingrese valores numericos")
total = 1
#-----------------bloque de ejecucion-------------------------
for i in range(1,(quantity+1)):
    total *= i
print(f"el factorial de {quantity} es: {total}")
'''


#Ejercicio 3
"""El ususario ingresa N numeros enteros, al final el programa muestra cual fue el mayor y el menor"""

'''
#-----------------bloque de input y variables---------------------------

n = int(input("Ingrese cuantos enteros va a ingresar al programa: "))

mayor = 0               #se elije un numero bajo para que cualquier numero que elija se mayor que el que elija el usuario

menor = 10000000000000000000000000000000000000000000000000000000000000000 #se define un numero grande para que 
                                                                          #cualquier primer numero que elija el usuario sea menor

#-----------------bloque de ejecucion-------------------------
for i in range(1,(n+1)):
    num = int(input("Ingrese numeros enteros: "))
    if num > mayor:         #guardamos el mayor numero
        mayor = num
    if num < menor:         #guardamos el menor numero
        menor = num

#-----------------bloque de prints----------------------------
print(f"El numero mayor fue: {mayor}")
print(f"El menor numero fue: {menor}")
'''


#Ejercicio 4
"""pide el usuario una edad, debe estar entre 0 y 120,
si no, envia un mensaje y repite hasta recibir un valor valido.
muestra las categorias menor edad < 18, adulto edad entre 18 y 64 o adulto mayor edad >=65"""

'''
#-----------------bloque de variables-------------------------------
flag = False

#-----------------bloque de ejecucion-------------------------------
while not flag:
    try:
        age = int(input("Ingrese edad: "))
        flag = True

        if age > 120 or age < 0:
            raise ValueError("Edad invalida, debe estar entre los 0 y 120")
        
    except ValueError as error:
        print(f"ERROR: {error}")

#-----------------bloque de prints----------------------------------
if age < 18:
    print("Usted es menor")

elif age >= 18 and age <= 64:
    print("Usted es adulto")

elif age > 64:
    print("Usted es adulto mayor")

 '''           


#ejercicio 5
"""El usuario ingresa n, con n siendo el numero de temperatutas que desea ingresar en celsius,
para cada temperatura que ingresa se muestra la temperatura en fahreheint y kelvin """
'''
#-----------------bloque de inputs y variables------------------------
total = int(input("Ingrese la cantidad de temperaturas que desea calcular en farenheint y kelvin: "))

#-----------------bloque de ejecucion---------------------------------
for i in range(total):
    c = float(input("Ingrese la temperatura en Celsius: "))
    f = c * 9/5 + 32
    k = c + 273.15
    print(f"Fahreinheint: {f}\nKelvin: {k}")
'''


#------------------------nivel 3--------------------------------------


#ejercicio 1
"""calculadora de suma, resta, multiplicacion, de dos numeros"""

'''
#-----------------bloque de menu--------------------------------------
option = 0
while option != 4:
    print("***CALCULADORA***")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicacion")
    print("4.- Salir")

    try:
        option = int(input("Ingrese Opcion (1-4): "))

        if option < 1 or option > 4:
            raise ValueError("La opcion debe estar entre 1 y 4")
        
    except ValueError as error:
        print(f"ERROR: {error}")

#-----------------bloque de ejecucion---------------------------------
    if option == 1:
        try:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            resultado = a + b

            print(f"El resultado es: {resultado}")

        except ValueError:
                print("Ingrese un numero valido")

    elif option == 2:
        try:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            resultado = a - b

            print(f"El resultado es: {resultado}")

        except ValueError:
                print("Ingrese un numero valido")

    elif option == 3:
        try:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            resultado = a * b

            print(f"El resultado es: {resultado}")

        except ValueError:
                print("Ingrese un numero valido")

    elif option == 4:
        print("Gracias por usar nuestra calculadora")
'''


#Ejercicio 2
