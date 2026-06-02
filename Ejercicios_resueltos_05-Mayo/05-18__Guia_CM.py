"""Ejercicio 1:
Escribe un programa que pida al usuario un número entero positivo N y muestre en pantalla todos los
números desde 1 hasta N, uno por línea.

flag_1 = False
while not flag_1:
    try:
        numero_ej1 = int(input("Ingrese un numero N: "))
        flag_1 = True
        for i in range(1, numero_ej1 + 1):
            print(f"Numero: {i}")
    except ValueError:
        print("ERROR: Ingrese un numero entero positivo: ")
        
"""

"""Ejercicio 2
Pide un número entero al usuario y muestra su tabla de multiplicar del 1 al 10


flag_2 = False
while not flag_2:
    try:
        numero_ej2 = int(input("Ingrese un numero N: "))
        flag_2 = True
        for i in range(1, 11):
            print(f"{numero_ej2} x {i} = {numero_ej2 * i}")
    except ValueError:
        print("ERROR: Ingrese un numero entero positivo: ")
"""

"""Ejercicio 3
El usuario ingresa un número N. El programa cuenta cuántos números pares existen entre 1 y N
(inclusive) y los muestra junto con el total.

flag_3 = False
count_pares = 0
while not flag_3:
    try:
        numero_ej3 = int(input("Ingrese un numero N: "))
        flag_3 = True
        for i in range(1, numero_ej3 + 1):
            if i % 2 == 0:
                count_pares += 1
                print(f"El numero {i} es par.")
        print(f"En el rango entre 1 y {numero_ej3} hay {count_pares} numero pares")
    except ValueError:
        print("ERROR: Ingrese un numero entero positivo: ")
"""

"""Ejercicio 4
El programa pide al usuario que ingrese notas (entre 1.0 y 7.0) una a una. El ciclo termina cuando el
usuario ingrese -1 como señal de fin. Al finalizar muestra cuántas notas ingresó.


flag_4 = False
count_notas = 0
while not flag_4:
    try:
        nota_ej4 = float(input("Ingrese una nota (1.0/7.0), para terminar ingrese (-1): "))
        if nota_ej4 == -1:
            flag_4 = True
        elif nota_ej4 < 1.0 or nota_ej4 > 7.0:
            raise ValueError
        else:
            count_notas += 1
        
    except ValueError:
        print("ERROR: Ingrese una nota entre 1.0 y 7.0")
        
print(f"La cantidad de notas ingresadas fue: {count_notas}")
"""

"""Ejercicio 5
Pide al usuario cuántas notas desea ingresar (N). Luego solicita cada nota y al final muestra el
promedio con dos decimales. Las notas están en escala 1.0 a 7.0.


flag_5_1 = False
flag_5_2 = False
acum_notas = 0
count_notas = 0
while not flag_5_1:
    try:
        cant_notas = int(input("Ingrese la cantidad de notas que deses ingresar: "))
        if cant_notas < 1:
            raise ValueError
        else:
            flag_5_1 = True
    except ValueError:
        print("ERROR: Ingrese un numero entero mayor a cero.")
        
for i in range(1, cant_notas + 1):
    flag_5_2 = False
    while not flag_5_2:
        try:
            nota = float(input(f"Ingrese la nota {i}: "))
            if nota < 1 or nota > 7:
                raise ValueError
            else:
                acum_notas += nota
                count_notas += 1
                flag_5_2 = True
        
        except ValueError:
            print("ERROR: Ingrese una nota entre 1.0 y 7.0")
print(f"Promedio final: {(acum_notas/count_notas):.2f}")
"""

"""Ejercicio 6
Pide al usuario un número entero N ≥ 0 y calcula su factorial (N!). Muestra el resultado.

flag6 = False
acum = 1
while not flag6:
    try:
        numero_6 = int(input("Ingrese un numero N mayor o igual a cero: "))
        if numero_6 < 0:
            raise ValueError
        else:
            flag6 = True
            numero_6_copia = numero_6
            while numero_6_copia >= 1:
                acum *= numero_6_copia
                numero_6_copia -= 1
    except ValueError:
        print("ERROR: Debe ingresar un numero entero mayor o igual a cero.")
print(f"El valor del factorial de {numero_6} es: {acum}")
"""

"""Ejercicio 7
El usuario ingresa N números enteros. Al final el programa muestra cuál fue el mayor y cuál fue el
menor ingresado.


flag_7 = False
flag_7_2 = False
mayor = 0
menor = 7
while not flag_7:
    try:
        numero_7 = int(input("Ingrese la cantidad de numeros que ingresara: "))
        if numero_7 < 1:
            raise ValueError
        else:
            flag_7 = True
    except ValueError:
        print("ERROR: Debe ingresar un numero entero mayor a cero. ")
        
for i in range(1, numero_7 + 1):
    flag_7_2 = False
    while not flag_7_2:
        try:
            num = int(input(f"Ingrese el numero {i}: "))
            if num > mayor:
                mayor = num
            if num < menor:
                menor = num
            flag_7_2 = True
        except ValueError:
            print("ERROR: Debe ingresar numeros enteros.")
print(f"El numero mayor es: {mayor} y el menor es: {menor}")
"""

"""Ejercicio 8
Pide al usuario una edad. Si es inválida (< 0 o > 120), muestra un mensaje de error y vuelve a pedir.
Repite hasta recibir un valor válido. Muestra la categoría: menor (< 18), adulto (18-64) o adulto mayor
(≥ 65).


flag_8 = False
while not flag_8:
    try:
        edad = int(input("Ingrese una edad: "))
        if edad < 0 or edad > 120:
            raise ValueError
        else:
            if edad < 18:
                print("Menor de edad.")
            elif edad >= 18 and edad <= 64:
                print("Adulto.")
            else:
                print("Adulto Mayor.")
            flag_8 = True
    except ValueError:
        print("ERROR: Debe ingresar un numero entero entre 1 y 120.")
"""

"""Ejercicio 9
El usuario ingresa cuántas temperaturas desea convertir (N). Para cada una ingresa el valor en Celsius
y el programa muestra su equivalente en Fahrenheit (F = C × 9/5 + 32) y Kelvin (K = C + 273.15)


flag_9 = False
while not flag_9:
    try:
        cant_temp = int(input("Ingrese cuantas temperaturas desea convertir: "))
        if cant_temp < 1:
            raise ValueError
        else:
            flag_9 = True
    except ValueError:
        print("ERROR: Debe ingresar valores enteros mayores a cero.")
        
flag_9_1 = False
for i in range(1, cant_temp + 1):
    flag_9_1 = False
    while not flag_9_1:
        try:
            temp = float(input("Ingrese la temperatura en grados Celsius: "))
            print(f"Grados Celsius: {temp} - Grados Farenheit: {(temp * 9 / 5) + 32}")
            flag_9_1 = True
        except:
            print("ERROR: Debe ingresar un numero.")
"""

"""Ejercicio 10
Crea un menú con 4 opciones: (1) Sumar, (2) Restar, (3) Multiplicar, (4) Salir. El programa muestra el
menú, el usuario elige, ingresa dos números y se muestra el resultado. El ciclo repite hasta que se elija
Salir.
"""
opcion = 10000000000000000000000.000000414124124141
flag_10 = False
while opcion != 4:
    print("----------------------------")
    print("|        CALCULADORA        |")
    print("----------------------------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Salir")
    #pedimos opcion
    flag_10 = False
    while not flag_10:
        try:
            opcion = int(input("Ingrese una opcion (1/4): "))
            flag_10 = True
        except ValueError:
            print("ERROR: Debe ingresar un numero entre 1 y 4.")
    #opcion 1
    if opcion == 1:
        flag_10_1 = False
        while not flag_10_1:
            try:
                num1 = float(input("Ingrese el primer numero a sumar: "))
                num2 = float(input("Ingrese el segundo numero a sumar: "))
                flag_10_1 = True
            except ValueError:
                print("ERROR: Debe ingresar un numero.")
        print(f"{num1} + {num2} = {num1 + num2}")
    
    #opcion 2
    elif opcion == 2:
        flag_10_1 = False
        while not flag_10_1:
            try:
                num1 = float(input("Ingrese el primer numero a restar: "))
                num2 = float(input("Ingrese el segundo numero a restar: "))
                flag_10_1 = True
            except ValueError:
                print("ERROR: Debe ingresar un numero.")
        print(f"{num1} - {num2} = {num1 - num2}")
    
    #opcion 3
    elif opcion == 3:
        flag_10_1 = False
        while not flag_10_1:
            try:
                num1 = float(input("Ingrese el primer numero a multiplicar: "))
                num2 = float(input("Ingrese el segundo numero a multiplicar: "))
                flag_10_1 = True
            except ValueError:
                print("ERROR: Debe ingresar un numero.")
        print(f"{num1} * {num2} = {num1 * num2}")
        
    elif opcion == 4:
        print("Gracias por usar nuestra calculadora.")
    
    else:
        print("Ingrese una opcion valida (1/4)")