#mensaje de bienvenida
print("Bienvenido al registro de cleintes")

#-----------------bloque de inpits y variables-------------------
#requisito 1
#varificador de cantidad de cuantas a registrar
flag_register = True
while flag_register:
    try:
        quant = int(input("Ingrese la cantidad de cuentas a registrar: "))
        if quant < 1:
            raise ValueError
        else:
            flag_register = False
    except ValueError:
        print("ERROR: Ingrese un numero entero positivo")
#----------------------------------------------

#requisito 2
#verificador de datos de cliente
#variables contadoras del tipo de usuario
premiun = 0
standar = 0
#varable contadora del while
n = 0
#---------------------------
while n != quant:
    n += 1
    error_data = ""
    try:
        data = input(f"Ingrese el rut N°{n} con digito verificador y sin puntos ni guión:\n").replace(" ","")
        if len(data) < 8 or len(data) > 9:
            error_data = "RUT INVALIDO: ingrese nuevamente el rut sin puntos ni gión, y con digito verificador\n"
            n -= 1
            raise ValueError
        balance = int(input("Ingrese el saldo inicial de la cuenta:\n"))

        if balance < 0:
            error_data += "¡Error bancario! Ingresa un saldo inicial valido, entero positivo"
            n -= 1
            raise ValueError
        else:
            flag_data = False
            if balance <= 1000000:
                premiun += 1
            elif balance > 10000000:
                standar += 1
    except ValueError: 
        if error_data == "":
            print("")
        elif error_data != "":
            print(error_data)
 #------------------------------       

print(f"¡registro completado! {premiun} clientes premiun y {standar} cleintes estandar incorporados al sistema")

