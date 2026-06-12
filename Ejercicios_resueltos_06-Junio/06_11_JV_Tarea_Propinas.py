'''
Un restaurante necesita un sistema que calcule el monto de propina según el porcentaje seleccionado por el cliente (10%, 15% o 20%), y 
muestre el desglose: subtotal, propina y total a pagar.

Crear funciones para calcular y mostrar el desglose de una cuenta con propina, usando return para comunicar resultados entre funciones.

Comunicación entre funciones mediante return

Cuando una función llama a otra y usa su return como parte de su propio cálculo, estamos componiendo funciones. Es un patrón clave en 
programación modular.

'''
#----------------- bloque funciones ----------------

def calcular_propina(subtotal, porcentaje):
    propina = subtotal * (porcentaje / 100)
    return propina


def calcular_total_cuenta(subtotal, porcentaje):
    propina = calcular_propina(subtotal, porcentaje)
    total = subtotal + propina
    return {'subtotal': subtotal, 'propina': propina, 'total': total}

def mostrar_desglose_cuenta(desglose):
    print("\n--- Desglose de la cuenta ---")
    print(f"Subtotal:           ${desglose['subtotal']:.2f}")
    print(f"Propina:            ${desglose['propina']:.2f}")
    print(f"Total a pagar:      ${desglose['total']:.2f}")

#----------------- bloque de ejecucion -----------------
def main():
    print("Bienvenido al sistema de cálculo de propinas del restaurante.")

    while True:
        try:
            subtotal = float(input("Ingrese el subtotal de la cuenta: $"))
            if subtotal < 0:
                print("El subtotal no puede ser negativo. Intente nuevamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido para el subtotal.")
        
    while True:
        try:
            porcentaje = int(input("Seleccione el porcentaje de propina (10, 15, 20): "))
            if porcentaje not in [10, 15, 20]:
                print("Porcentaje no válido. Por favor, seleccione 10, 15 o 20.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido para el porcentaje.")

    desglose_cuenta = calcular_total_cuenta(subtotal, porcentaje)
    mostrar_desglose_cuenta(desglose_cuenta)

if __name__ == "__main__":
    main()