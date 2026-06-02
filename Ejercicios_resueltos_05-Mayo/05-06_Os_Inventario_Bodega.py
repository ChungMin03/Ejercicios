'''Inventario de Bodega (Ciclo while con continue)
Un bodeguero está contando cajas de productos.

Solicita la cantidad total de cajas que espera contar.

Usa un ciclo while para pedir el peso de cada caja.

Regla: Si el peso ingresado es menor a 1kg,
 muestra un mensaje "Caja demasiado liviana, descartada" y usa continue para pedir 
la siguiente sin descontarla del total esperado.

Al final, muestra el peso total acumulado.
'''



#Forma mia-----------------------------------------------------------------------------------------------------------------------------------
'''#------------------------------BLoque de variables-----------------------------------------------------

box_cant = int(input("Ingrese la cantidad de cajs que ingresara: "))
total_weight = 0

#------------------------------Bloque de ejecucion-----------------------------------------------------

while box_cant > 0:
    box_cant -= 1
    weight = int(input("Ingrese el peso de la caja en kg: "))
    if weight < 1:
        print("Caja demasiado liviana, descartada")
        box_cant += 1
        continue
    else:
        total_weight += weight
        


#-------------------------Bloque de prints--------------------------------------------------------------
print(f"El peso total acumulado es de : {total_weight}")
print(f"El total de cajas fue de {box_cant}")'''



#Forma anotacion de carlos
#------------------------------BLoque de variables-----------------------------------------------------

box_cant = int(input("Ingrese la cantidad de cajs que ingresara: "))
total_weight = 0
count = 0
total_cajas = 0

#------------------------------Bloque de ejecucion-----------------------------------------------------

while count < box_cant:
    count += 1
    weight = int(input("Ingrese el peso de la caja en kg: "))
    if weight < 1:
        print("Caja demasiado liviana, descartada")
        count -= 1
        continue
    else:
        total_weight += weight
        


#-------------------------Bloque de prints--------------------------------------------------------------
print(f"El peso total acumulado es de : {total_weight}")
print(f"El total de cajas fue de {box_cant}")