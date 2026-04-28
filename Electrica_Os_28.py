name = input("Ingrese su nombre\n")
kwh = int(input("Ingrese la cantidad kwh consumido: "))
type = input("Que tipo de residencia tiene (residencial o comercial)\n").lower()


if type != "residencial" and type != "comercial":
    print("Residencia invalida")
    total = 0
elif type == "residencial":
    if kwh < 150:
        total = kwh * 82
    else:
        total = 150 * 82 + (kwh-150) * 110
elif type == "comercial":
    total = kwh * 130

#te dice cosas
if total != 0:
    print(f"Su nombre es: {name.upper()}")
    print(f"El largo del nombre es: {len(name)}")
    print(f"Su consumo es de: {kwh}")
    print(f"El total a pagar es de: {total}")
