"""
Un restaurante necesita un sistema que calcule el monto de propina según el porcentaje seleccionado
por el cliente (10%, 15% o 20%), y muestre el desglose: subtotal, propina y total a pagar.
🎯 Objetivo
Crear funciones para calcular y mostrar el desglose de una cuenta con propina,
usando return para comunicar resultados entre funciones.
💡 Concepto
Comunicación entre funciones mediante return
"""

#funcion propina
def desglose_propina():

    while True:
        try:
            subtotal = int(input("Ingrese subtotal a pagar: "))
            if subtotal <= 0:
                print("Ingrese un monto valido")
            else:
                break
        except ValueError:
            print("Ingrese valores numericos")

    print("Desea ingresar propina?")
    print("1.- 10%")
    print("2.- 15%")
    print("3.- 20%")
    print("4.- No")

    while True:
        try:
            opcion = int(input("Ingrese la opcion (1-4): "))
            if opcion > 4 or opcion < 1:
                print("Ingrese un valor dentro de las opciones")
            else:
                break
        except ValueError:
            print("Ingrese un valor numerico valido")
    
    total = 0
    if opcion == 1:
        total = 1.10*subtotal
    
    elif opcion == 2:
        total = 1.15*subtotal

    elif opcion == 3:
        total = 1.20*subtotal
    
    elif opcion == 4:
        total = subtotal

    propina = total - subtotal

    cuenta = {}
    cuenta["Subtotal"] = subtotal
    cuenta["Propina"] = propina
    cuenta["Total"] = total
    return cuenta 




#programa real

datos = desglose_propina()
for key, value in datos.items():
    print(f"{key} --------------> {value:.2f}")ß



