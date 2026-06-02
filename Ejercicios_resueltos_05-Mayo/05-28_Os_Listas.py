"""listas de elementos"""
'''numeros = [0,1,2,3,4,5]
print(numeros[2])
Las listas empiezan el conteo por 0'''

"""diccionarios
user = {"nombre":"Victor" , "nombre":"Joel"}

"""

"""
user = {"nombre":"Victor" , "nombre2":"Joel"}
print(user["nombre"], user["nombre2"])"""

"""
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
                valor = int(input("Ingrese el valor del producto: "))
                valorSuper.append(valor)




            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")

    print("-----Detalle Boleta-----")
    print(f"Productos:\n{listaSuper}")
    print(f"Cantidad de productos: {len(listaSuper)}")
    print(f"Valor total: {sum(valorSuper)}")
else:
    print("Adiós")
"""

#clase 29/05



