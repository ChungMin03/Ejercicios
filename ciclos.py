"""nombres = input("Ingrese nombres separados por coma: ").replace(" ","").split(",")
for nombre in nombres:
    print(f"Hola {nombre}")

nombre = "carlos"
for letra in nombre:
    print(letra)"""

opcion = 0
while opcion != 3:
    print(f"1- Escribir saludo:\n2- Escribir despedida\n3-Salir")
    opcion = int(input("Ingrese una opción"))
    if opcion == 1:
        print("Hola")
    elif opcion == 2:
        print("Adios")
    elif opcion == 3:
        print("Gracias por usar esto")
    else:
        print("Que ingresaste bobo")