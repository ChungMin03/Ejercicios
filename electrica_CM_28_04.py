"""Una empresa electrica calcula el cobro mensual segun el consumo de kWh y el tipo de tarifa del cliente ("residencial" o "comercial"). SOlicita los datos y aplica:
- residencial, consumo <= 150 kWh: $82 por kWh
- residencial, consumo > 150 kWh: primeros 150 kWh a $82 y el exceso a $110
- Comercial (cualquier consumo): $130 por kWh
"""

consumo = float(input("Ingrese su consumo en kWh: "))
tarifa = input("Ingrese tipo de cliente (residencial/comercial): ").lower()

if consumo > 150 and tarifa == "residencial":
    consumo_exceso = consumo - 150
    cobro = 150 * 82 + consumo_exceso * 110
elif consumo <= 150 and tarifa == "residencial":
    cobro = consumo * 82
else:
    cobro = consumo * 130

print(f"Su factura es de: ${cobro}, ya que consumio {consumo} kWh")

