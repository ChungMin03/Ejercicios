"""
2. Inventario de Bodega (Ciclo while con continue)
Un bodeguero está contando cajas de productos.

Solicita la cantidad total de cajas que espera contar.

Usa un ciclo while para pedir el peso de cada caja.

Regla: Si el peso ingresado es menor a 1kg, muestra un mensaje "Caja demasiado liviana, descartada" y usa continue para pedir 
la siguiente sin descontarla del total esperado (tal como hiciste con cant_pasajes_alt += 1 en tu ejemplo).  

Al final, muestra el peso total acumulado.
"""
cant_cajas = int(input("Ingrese la cantidad de cajas: "))
count = 1
total_acum = 0

while count <= cant_cajas:
    count += 1
    peso_caja = float(input("Ingrese el peso de la caja en kg: "))
    if peso_caja < 1:
        print("Caja demasiado liviana, descartada")
        count -= 1
        continue
    else:
        total_acum += peso_caja
        
print(f"El peso total acumulado de las {cant_cajas} cajas es: {total_acum} kg")