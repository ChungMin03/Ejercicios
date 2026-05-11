"""ejercicio 1:
Escriba un programa que pida al usuario un numero entero positivo N y muestre en pantalla todos los numeros
desde 1 hasta N, uno por linea
"""

print("***** EJERCICIO 1 ******")
n = int(input("Ingrese un numero N: "))

for num in range(1, n + 1):
    print(f"Numero: {num}")

"""ejercicio 2:
Pida al usuario un numero N y calcula la suma de todos los enteros desde 1 hasta N.
Muestra el resultado final
"""
print("***** EJERCICIO 2 ******")
n2 = int(input("Ingrese un numero N: "))
acum = 0

for num in range (1, n2 +1):
    acum += num

print(f"Resultado final de la suma desde 1 hasta N: {acum}")

"""ejercicio 3:
Pide un numero entero al usuario y muestra su tabla de multiplicar del 1 al 10
"""
print("***** EJERCICIO 3 ******")
n3 = int(input("Ingrese un numero N: "))
for num in range(1, 11):
    print(f"{n3} x {num} = {num * n3}")


print("***** EJERCICIO 1 con while ******")
n = int(input("Ingrese un numero N: "))
count = 1
while count <= n:
    print(count)
    count += 1


print("***** EJERCICIO 2 con while ******")
n2 = int(input("Ingrese un valor N: "))
count = 1
acum = 0
while count <= n2:
    acum += count
    count += 1
print(f"Resultado final de la suma desde 1 hasta N: {acum}")


print("***** EJERCICIO 3 con while ******")
n3 = int(input("Ingrese un numero N: "))
count = 1
while count <= 10:
    if count < 10:
        print(f"{n3} * 0{count} = {n3 * count}")
    else:
        print(f"{n3} * {count} = {n3 * count}")
    count += 1