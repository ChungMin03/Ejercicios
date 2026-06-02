vehiculo = input("Ingrese su tipo de vehiculo (auto/moto/camioneta): ").lower()
horas = int(input("Ingrese las horas que estuvo estacionado: "))

if vehiculo == "auto":
    if horas <= 2:
        pago = horas * 1500
    elif horas >= 3:
        horas_adicionales = horas - 2
        pago = (horas_adicionales * 800) + (2 * 1500)
elif vehiculo == "moto":
    if horas <= 2:
        pago = horas * 800
    elif horas >= 3:
        horas_adicionales = horas - 2
        pago = (horas_adicionales * 400) + (2 * 800)
elif vehiculo == "camioneta":
    if horas <= 2:
        pago = horas * 2500
    elif horas >= 3:
        horas_adicionales = horas - 2
        pago = (horas_adicionales * 1200) + (2 * 2500)

if horas >= 8 and (vehiculo == "auto" or vehiculo == "camioneta"):
    total_final = pago * 0.8
    descuento = 20
else:
    descuento = 0

print(f"El total sin descuento es: {pago}")
if descuento != 0:
    print (f"Su descuento es: {descuento}%")
    print(f"El total después del descuento es: {total_final}")
else:
    print("No tiene descuento D:")