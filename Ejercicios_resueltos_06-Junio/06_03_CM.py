"""lista_num = []
cant_pares = 0
cant_impares = 0
suma_pares = 0
suma_impares = 0

for i in range(10):
    flag = False
    while not flag:
        try:
            num = int(input(f"Ingrese un número entero: "))
            lista_num.append(num)
            flag = True
        except:
            print("Error: Ingrese un numero entero.")
            
for n in lista_num:
    if n % 2 == 0:
        cant_pares += 1
        suma_pares += n
    else:
        cant_impares += 1
        suma_impares += n

print(f"Cantidad de pares: {cant_pares} y cantidad de impares: {cant_impares}")
print(f"Suma de todos los numeros pares: {suma_pares}")
print(f"Suma de todos los numeros impares: {suma_impares}")"""

lista_numeros = []

for i in range(8):
    flag = False
    while not flag:
        try:
            num = int(input(f"Ingrese un número entero: "))
            lista_numeros.append(num)
            flag = True
        except:
            print("Error: Ingrese un numero entero.")

flag2 = False
while not flag2:
    try:
        buscar = int(input("Ingrese el numero a buscar: "))
        flag2 = True
    except:
        print("ERROR: Ingrese un numero entero. ")
            
if buscar in lista_numeros:
    coincidencias = lista_numeros.count(buscar)
    if coincidencias > 1:
        indices = []
        for i in range(len(lista_numeros)):
            if lista_numeros[i] == buscar:
                indices.append(i)
        print(f"El numero {buscar} se encuentra {coincidencias} veces, en las posiciones: ")
        for indice in indices:
            print(f"{indice + 1}")
    else:
        print(f"El numero {buscar} se encuentra {coincidencias} vez, en la posicion {lista_numeros.index(buscar) + 1}: ")
else:
    print(f"El numero {buscar} no se encuentra en la lista.")