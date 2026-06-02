
"""sw = 1
listaNotas = []
print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción: "))
2
if(op == 1):
    while sw==1:
        try:
            print("----------------------------------------------------------")
            nota=float(input("Incorpore su nota, si desea salir, presione 0: "))
            if(nota != 0):
                listaNotas.append(nota)

            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")
    print("========== Notas Ingresadas ============")
    print(listaNotas)
    #mostrar cantidad de notas
    print("========= Cantidad de notas ingresadas ===========")
    print(len(listaNotas))
    #Promedio de notas
    suma_total = 0
    for calif in listaNotas:
        suma_total += calif
    print("========= Promedio de Notas ==========")
    print(f"{suma_total / len(listaNotas)}")

else:
    print("Adiós")"""


#listaSuper
sw = 1
listaSuper = []
valorSuper = []
print("Presione 1 para ingresar los productos del súper")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción "))
if(op == 1):
    while sw==1:
        try:
            print("----------------------------------------------------------")
            producto=input("Incorpore su producto, para salir, presione 0: ")
            if(producto != "0"):
                listaSuper.append(producto)
                valor_producto = int(input(f"Ingrese el valor de {producto}: "))
                valorSuper.append(valor_producto)
            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")

    print("======== DETALLE BOLETA ===========")
    for i in range(len(listaSuper)):
        print(f"{listaSuper[i]} ----------- ${valorSuper[i]}")
    print("---------------------------------------------------")
    print(f"Cantidad de productos comprados: {len(listaSuper)}")
    suma_productos = sum(valorSuper)
    print("---------------------------------------------------")
    print(f"TOTAL: ${suma_productos}")
else:
    print("Adiós")