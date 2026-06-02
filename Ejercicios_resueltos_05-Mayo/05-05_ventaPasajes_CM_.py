"""
Deberás construir un programa que esta diseñado para ayudar en la venta
de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
utiliza un proceso organizado (llamado bucle for) para pedirte el precio de
cada pasaje por separado. Si ingresas un valor que no es un número, te
indica que necesitas proporcionar un valor numérico válido. Al final, muestra
el monto total que se ha obtenido por la venta de todos los pasajes
• Solicita al usuario la cantidad de pasajes a vender.
• Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
• Dentro del bucle, se solicita al usuario el precio de cada pasaje y se
acumula en la variable totalIngresos.
• Si el usuario ingresa un valor no numérico para el precio del pasaje,
el programa muestra un mensaje y sale del bucle usando break.
• Finalmente, se imprime el total de ingresos por la venta de pasajes
"""

cant_pasajes = int(input("Ingrese la cantidad de pasajes que comprara: "))
totalIngresos = 0

"""for pasaje in range(cant_pasajes):
    price = input("Ingrese el valor del pasaje: ")
    if not price.isnumeric():
        break
    price = int(price)
    totalIngresos += price #totalIngresos = totalIngresos + price


if totalIngresos != 0:
    print(f"El total de los {cant_pasajes} pasajes es: ${totalIngresos}")
else:
    print("Ingrese un valor valido")
    
"""

cant_pasajes_alt = cant_pasajes
while cant_pasajes_alt != 0:
    price = input("Ingrese el valor del pasaje: ")
    cant_pasajes_alt -= 1
    if not price.isnumeric():
        print("Se ha equivocado, ingrese un valor valido")
        cant_pasajes_alt += 1
        continue
    price = int(price)
    totalIngresos += price #totalIngresos = totalIngresos + price



if totalIngresos != 0:
    print(f"El total de los {cant_pasajes} pasajes es: ${totalIngresos}")
else:
    print("Ingrese un valor valido")
    

