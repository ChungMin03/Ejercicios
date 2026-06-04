#ejercicio 2
"""
El ususario ingresa 10 numeros enteros que se almacenan un una lista,
al finalizar el programa debe mostrar:
-Cuantos pares contiene la lista
-Cuantos impares contiene la lista 
-La suma total de pares
-La suma total de impares
"""

"""
contador_pares = 0
total_pares = 0
contador_impares = 0
total_impares = 0
cont_numeros = 1
lista_numeros = []

while cont_numeros != 10:
    try: 
        numeros = int(input("Ingrese los numeros que desea ingresar: "))
    except ValueError:
        print("Debe ingresar valores númericos")
    lista_numeros.append(numeros)
    cont_numeros += 1

for i in lista_numeros:
    if (i % 2) == 0:
        contador_pares += 1
        total_pares += i
    else:
        contador_impares += 1
        total_impares += i
print(cont_numeros)
print(f"La cantidad de par es: {contador_pares}")
print(f"La cantidad de impar es: {contador_impares}")
print(f"La suma de pares es: {total_pares}")
print(f"La suma de impares es : {total_impares}")"""

#ejercicio 3
"""
el usuario ingresa números enteros almacenados en una lista.
luego ingresa un numero a buscar. El programa debe indicar:
-Si el numero existe en la lista
-En que posicion está 
-Cauntas veces se repite
"""
lista_numeros = []
contador_numeros = 0
contador_find = 0
posicion_find = []
existe = ""
find = 0
while contador_numeros != 8:
    contador_numeros += 1
    try:
        numeros = int(input("Ingrese los numeros que desea agregar: "))
    except ValueError:
        contador_numeros -= 1
        print("Debe ingresar valores numericos enteros")

        lista_numeros.append(numeros)

flag_numero = False
while not flag_numero:
    try:
        find = int(input("Agregue el numero a buscar: "))
        flag_numero = True
    except ValueError:
        print("Ingrese un valor numerico entero")

for i in lista_numeros:
    if find == i:
        contador_find += 1
        posicion_find.append(lista_numeros.index(i))
        existe += "SI"
    elif find not in lista_numeros:
        existe += "NO"

if existe == "NO":
    print("El numero no existe en la lista")
else:
    print(f"{find} Existe en la lista")
    print(f"{find} Está en las posiciones {posicion_find}")
    print(f"{find} Se repite {contador_find} en la lista")


