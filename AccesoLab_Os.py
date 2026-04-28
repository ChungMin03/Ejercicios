year = int(input("Año de estudios: "))

if year < 2:
    print("Acceso denegado por año cursado")
else:
    payment = input("Indique si tiene el pago al día (Si/No)\n").lower()
    if payment != "si":
        print("Acceso denegado por falta de pago")
    else:
        sus = input("Indique si se encuantra o no suspendido (Si/No)\n")
        if sus != "no":
            print("Acceso denegado por suspencion")
        else:
            print("Acceso permitido")