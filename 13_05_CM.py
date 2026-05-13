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
while opcion != 4:
    print("**** CALCULADORA ****")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Salir")
    print("----------------------------------")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        num1 = int(input("Ingrese el primer numero a sumar: "))
        num2 = int(input("Ingrese el segundo numero a sumar: "))
        print(f"{num1} + {num2} = {num1 + num2}")
        print("----------------------------------")
    elif opcion == 2:
        num1 = int(input("Ingrese el primer numero a restar: "))
        num2 = int(input("Ingrese el segundo numero a restar: "))
        print(f"{num1} - {num2} = {num1 - num2}")
        print("----------------------------------")
    elif opcion == 3:
        num1 = int(input("Ingrese el primer numero a multiplicar: "))
        num2 = int(input("Ingrese el segundo numero a multiplicar: "))
        print(f"{num1} * {num2} = {num1 * num2}")
        print("----------------------------------")
    elif opcion == 4:
        print("Gracias por usar nuestra calculadora")
        print("----------------------------------")
    else:
        print("Opción ingresada no válida")
        print("----------------------------------")