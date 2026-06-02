
#Definicion de variables-----------------------------------------------------------------------------
name = input("Ingrese su nombre\n")
kwh = float(input("Ingrese la cantidad kwh consumido: "))
type = input("Que tipo de residencia tiene (residencial o comercial)\n").lower()


#Bloque de ejecucion--------------------------------------------------------------------------------
#validacion de que tipo de residencia tiene y el valor que le genera
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

#Este if es para que no se tire el valor cuando el tipo de recidencia es invalido------------------
if total != 0:
    print(f"Su nombre es: {name.upper()}")
    print(f"El largo del nombre es: {len(name)}")
    print(f"Su consumo es de: {kwh}")
    print(f"El total a pagar es de: {total}")
