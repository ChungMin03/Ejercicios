#Ejercicio 7
#Un restaurante necesita un sistema que calcule el monto de propina según el
#porcentaje seleccionado por el cliente (10%, 15% o 20%), y muestre el desglose:
#subtotal, propina y total a pagar.
#🎯 Objetivo Crear funciones para calcular y mostrar el desglose de una cuenta con propina,
#usando return para comunicar resultados entre funciones.
#💡 Concepto Comunicación entre funciones mediante return

"""def calcularPropina(subtotal):
    boleta = {}
    flag_propina = False
    while not flag_propina:
        print("-------------------- PROPINA --------------------")
        try:
            opcion_propina = int(input("Ingrese una opcion:\n1) 10%\n2) 15%\n3) 20%\n"))
            if opcion_propina < 1 or opcion_propina > 3:
                raise ValueError
            else:
                flag_propina = True
        except ValueError:
            print("Ingrese una opcion valida (1,2,3).")
    
    if opcion_propina == 1:
        propina = 1.1
        valor_propina = subtotal * 0.1
        total = subtotal * propina
    elif opcion_propina == 2:
        propina = 1.15
        valor_propina = subtotal * 0.15
        total = subtotal * propina
    else:
        propina = 1.2
        valor_propina = subtotal * 0.2
        total = subtotal * propina
    
    boleta["subtotal"] = subtotal
    boleta["propina"] = valor_propina
    boleta["total"] = total
    
    return boleta"""
    
def calcularTotal(subtotal, opcion_propina):
    if opcion_propina == 1:
        propina = 1.1
        valor_propina = subtotal * 0.1
        total = subtotal * propina
    elif opcion_propina == 2:
        propina = 1.15
        valor_propina = subtotal * 0.15
        total = subtotal * propina
    else:
        propina = 1.2
        valor_propina = subtotal * 0.2
        total = subtotal * propina
    return {"subtotal": subtotal,
            "propina" : valor_propina,
            "total" : total
    }

def mostrarBoleta(boleta):
    print(f"----------------------- BOLETA -----------------------")
    print(f"Monto neto ---------------------- ${boleta["subtotal"]}")
    print(f"Propina ------------------------- ${boleta["propina"]:.2f}")
    print(f"Monto total --------------------- ${boleta["total"]:.2f}")
    

#codigo principal
flag_subtotal = False
while not flag_subtotal:
    try:
        subtotal = float(input("Ingrese el valor de la cuenta: "))
        if subtotal < 1:
            raise ValueError
        else:
            flag_subtotal = True
    except ValueError:
        print("Ingrese un monto valido.")
        
flag_propina = False
while not flag_propina:
    print("-------------------- PROPINA --------------------")
    try:
        opcion_propina = int(input("Ingrese una opcion:\n1) 10%\n2) 15%\n3) 20%\n"))
        if opcion_propina < 1 or opcion_propina > 3:
            raise ValueError
        else:
            flag_propina = True
    except ValueError:
        print("Ingrese una opcion valida (1,2,3).")

boleta = calcularTotal(subtotal, opcion_propina)
mostrarBoleta(boleta)