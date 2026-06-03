#ejercicio 2
"""
El ususario ingresa 10 numeros enteros que se almacenan un una lista,
al finalizar el programa debe mostrar:
-Cuantos pares contiene la lista
-Cuantos impares contiene la lista 
-La suma total de pares
-La suma total de impares
"""
contador_pares = 0
total_pares = 0
contador_impares = 0
total_impares = 0
cont_numeros = 0
lista_numeros = []

while cont_numeros != 10:
    cont_numeros += 1
    try: 
        numeros = int(input("Ingrese los numeros que desea ingresar: "))
    except ValueError:
        cont_numeros -= 1
        print("Debe ingresar valores númericos")
    lista_numeros.append(numeros)

for i in lista_numeros:
    if (i % 2) == 0:
        contador_pares += 1
        total_pares += i
    else:
        contador_impares += 1
        total_impares += i

print(f"La cantidad de par es: {contador_pares}")
print(f"La cantidad de impar es: {contador_impares}")
print(f"La suma de pares es: {total_pares}")
print(f"La suma de impares es : {total_impares}")