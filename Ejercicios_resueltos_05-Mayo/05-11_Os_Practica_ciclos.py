


#Practica con for
"""valor = int(input("Ingrese el numero: "))
for numero in range(1,(valor + 1)):
    print(numero)



total = 0
ingreso = int(input("ingrese el numero que desea sumar hasta: "))
for num in range(1, (ingreso+1)):
    total += num
print(total)



mult = int(input("ingrese el numero del que quiera la tabla de multiplicar: "))
for multiplo in range(1, 11):
    print(f"{mult} * {multiplo} = {multiplo * mult}")"""

#practica con while

                        #ejercicio 1
"""valor = int(input("Ingrese el numero: "))
max = 0
while max != valor:
    max += 1
    print(max)


                        #Ejercicio2
ingreso = int(input("ingrese el numero que desea sumar hasta: "))
tope = 0
sumatoria = 0
while tope != ingreso:
    tope += 1
    sumatoria += tope
print(sumatoria)"""


                        #Ejercicio 3

mult = int(input("ingrese el numero del que quiera la tabla de multiplicar: "))
tabla = 0
while tabla != 10:
    tabla += 1
    if tabla < 10:
        print(f"0{tabla} * {mult} = {tabla*mult}")
    else:
        print(f"{tabla} * {mult} = {tabla*mult}")