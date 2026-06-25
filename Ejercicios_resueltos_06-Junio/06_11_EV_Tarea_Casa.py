"""Un restaurante necesita un sistema que calcule el monto de propina según el
porcentaje seleccionado por el cliente (10%, 15% o 20%), y muestre el desglose:
subtotal, propina y total a paga

Crear funciones para calcular y mostrar el desglose de una cuenta con propina,
usando return para comunicar resultados entre funciones.

Comunicación entre funciones mediante return
"""
error="Error. Caracter inválido, intente nuevamente"
#---------------------------------------------ENTRADA----------------------------------------------#

def calcular_propina(subtotal, porcentaje):
    propina = subtotal * (porcentaje / 100)
    return propina

def calcular_total(subtotal, propina):
    total = subtotal + propina
    return total

def mostrar_desglose(subtotal, porcentaje, propina, total):
    print("***** DESGLOSE DE LA CUENTA *****")
    print(f"Subtotal: ${subtotal}")
    print(f"Propina ({porcentaje}%): ${propina:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print("*********************************")


def main():
    while True:
        try:
            subtotal = float(input("Ingrese el subtotal de la cuenta: $"))

        print("Seleccione el porcentaje de propina:")
        print("1. 10%")
        print("2. 15%")
        print("3. 20%")
        
        if subtotal<1:
            print("Error. La cuenta no puede ser menor a 1")
            
        else:
            break        
        
        except ValueError:
            print(error)


while True:
    try:
        subtotal = float(input("Ingrese el subtotal de la cuenta: $"))

        print("Seleccione el porcentaje de propina:")
        print("1. 10%")
        print("2. 15%")
        print("3. 20%")
        
        if subtotal<1:
            print("Error. La cuenta no puede ser menor a 1")
            
        else:
            break        
        
    except ValueError:
        print(error)
    propina = calcular_propina(subtotal, porcentaje)
    total = calcular_total(subtotal, propina)

    mostrar_desglose(subtotal, porcentaje, propina, total)


main()
        
    
                                                                                                               
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  
                                                                                                                  





















































































