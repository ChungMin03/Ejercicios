"""Una empresa electrica calcula el cobro mensual segun el consumo de kWh y el tipo de tarifa del cliente ("residencial" o "comercial"). SOlicita los datos y aplica:
- residencial, consumo <= 150 kWh: $82 por kWh
- residencial, consumo > 150 kWh: primeros 150 kWh a $82 y el exceso a $110
- Comercial (cualquier consumo): $130 por kWh
Mostrar el nombre del cliente en Mayusculas, su largo, tipo de tarifa, consumo y monto a pagar
"""

name = input("Ingrese su nombre: ")
consumo = float(input("Ingrese su consumo en kWh: "))
tarifa = input("Ingrese tipo de cliente (residencial/comercial): ").lower()

if consumo > 150 and tarifa == "residencial":
    consumo_exceso = consumo - 150
    cobro = 150 * 82 + consumo_exceso * 110
elif consumo <= 150 and tarifa == "residencial":
    cobro = consumo * 82
elif tarifa == "comercial":
    cobro = consumo * 130
else:
    cobro = -1
    

print(f"Nombre: {name.upper()}")
print(f"Largo del nombre: {len(name)}")
if cobro != -1:
    print(f"Tipo de tarifa: {tarifa}")
    print(f"Consumo: {consumo}")
    print(f"Monto a pagar: {cobro}")
else:
    print(f"Tipo de tarifa: Incorrecta")
    print(f"Consumo: {consumo}")
    print(f"Monto a pagar: ----------- ")

