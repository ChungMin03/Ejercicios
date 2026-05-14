"""num = int(input("Ingrese un numero N: "))
count = 0
pares = ""
for i in range(1, num+1):
    if i % 2 == 0:
        count += 1
        #pares += str(i) + ", "
        print(f"El numero {i} es Par")
print(f"El total de numeros pares entre 1 y {num} es: {count}")
#print(f"Los numeros pares son: {pares}")      
"""

#EJERCICIO MENU
opcion = 0
opcion_valida = False
while opcion != 4:
    print("**** CALCULADORA ****")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Salir")
    print("----------------------------------")
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("ERROR: Opción debe ser un numero (1-4).")
        print("----------------------------------")
        continue

    if opcion == 1:
        try:
            num1 = int(input("Ingrese el primer numero a sumar: "))
            num2 = int(input("Ingrese el segundo numero a sumar: "))
        except ValueError:
            print("ERROR: Ingrese numeros enteros.")
            print("----------------------------------")
            continue

        print(f"{num1} + {num2} = {num1 + num2}")
        print("----------------------------------")
    elif opcion == 2:
        try:
            num1 = int(input("Ingrese el primer numero a restar: "))
            num2 = int(input("Ingrese el segundo numero a restar: "))
        except ValueError:
            print("ERROR: Ingrese numeros enteros.")
            print("----------------------------------")
            continue
        print(f"{num1} - {num2} = {num1 - num2}")
        print("----------------------------------")
    elif opcion == 3:
        opcion_valida = False
        while not opcion_valida:
            try:
                num1 = int(input("Ingrese el primer numero a multiplicar: "))
                num2 = int(input("Ingrese el segundo numero a multiplicar: "))
                opcion_valida = True
            except ValueError:
                print("ERROR: Ingrese numeros enteros.")
                print("----------------------------------")

        print(f"{num1} * {num2} = {num1 * num2}")
        print("----------------------------------")
    elif opcion == 4:
        print("Gracias por usar nuestra calculadora")
        print("----------------------------------")
    else:
        print("Opción ingresada no válida")
        print("----------------------------------")