vehicle = input("Ingrese el tipo de vehiculo (Auto, Moto, Camioneta)\n").lower()
time = int(input("Ingrese las horas que estuvo: "))
if vehicle != ("auto" or "moto" or "camioneta"):
    print("Vehiculo invalido")
elif time <= 2 and vehicle == "auto":
    price = time * 1500
    print(f"El monto total es: {price}")
elif time <= 2 and vehicle == "moto":
    price = time * 800
    print(f"El monto total es: {price}")
elif time <= 2 and vehicle == "camioneta":
    price = time * 2500
    print(f"El monto total es: {price}")
elif time > 2 and time < 8 and vehicle == "auto":
    price = (2 * 1500) + ((time-2) * 800)
    print(f"El monto total es: {price}")
elif time > 2 and time < 8 and vehicle == "moto":
    price = (2 * 800) + ((time-2) * 400)
    print(f"El monto total es: {price}")
elif time > 2 and time < 8 and vehicle == "auto":
    price = (2 * 2500) + ((time-2) * 1200)
    print(f"El monto total es: {price}")
elif time >= 8 and vehicle == "auto":
    price = ((time - 2) * 800) + (2 * 1500)
    dprice = price * 0.8
    print(f"El total sin descuento es: {price}")
    print(f"El total con descuento es: {dprice}")
elif time >= 8 and vehicle == "camioneta":
    price = ((time - 2) * 1200) + (2 * 2500)
    dprice = price * 0.8
    print(f"El total sin descuento es: {price}")
    print(f"El total con descuento es: {dprice}")
