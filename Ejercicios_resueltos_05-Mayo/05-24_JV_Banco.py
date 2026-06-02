"""
Sistema de Registro de Clientes — Banco Digital

Contexto: Eres desarrollador en un banco digital. Tu jefa te pide crear un programa que registre nuevos clientes, valide sus datos y clasifique sus cuentas según el saldo inicial.

    - Requisito 1: Cantidad de clientes a registrar
        -> El programa debe preguntar cuántos clientes se registrarán en la sesión. Debe ser un número entero positivo (mayor a 0). Si el usuario ingresa un valor inválido 
        (letras, cero o negativo), mostrar el siguiente mensaje y volver a pedir:
        "¡Cantidad inválida! Ingresa un entero positivo para continuar."
    
    - Requisito 2: Datos de cada cliente
        -> RUT (texto - String): debe tener al menos 8 caracteres y no debe contener espacios. Si no cumple, volver a pedir. Ejemplos válidos:
        EJ: 12345678-K, 9876543-2, 11111111-1
        -> Saldo inicial (entero positivo): si el usuario ingresa letras, cero o un valor negativo, mostrar el siguiente mensaje y repetir la solicitud:
        "¡Error bancario! Ingresa un saldo inicial válido (entero positivo)."
    
    - Requisito 3: Clasificación de la cuenta
        -> Según el saldo inicial ingresado, clasificar automáticamente:
         _________________________________________________
        | Saldo Inicial (CLP)   | Clasificación de Cuenta |
        |-----------------------|-------------------------|
        | Saldo > 1.000.000     | CUENTA PREMIUM          |
        | Saldo ≤ 1.000.000     | CUENTA ESTÁNDAR         |
        |_______________________|_________________________|

        -> Mantener contadores separados durante todo el proceso.
    
    - Requisito 4: Resumen final
        -> Al finalizar, mostrar:
        "¡Registro completado! X clientes Premium y Y clientes Estándar incorporados al sistema."
        -> Donde X e Y corresponden a los contadores acumulados.
"""

# ----------------- Bloque variables -----------------

premium = 0
estandar = 0
i = 0

# ----------------- Bloque ejecución -----------------

# Registro de clientes:
opc = False
while not opc:
    try:
        cantidad_clientes = int(input("Ingrese la cantidad de clientes a registrar: "))

        if cantidad_clientes <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        else:
            opc = True
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    

# Procesamiento de cada cliente:
while i < cantidad_clientes:
    rut = input("\nIngrese su RUT (sin espacios y con guion): ")

    if len(rut) < 8 or " " in rut or "-" not in rut:
        print("¡RUT inválido! Asegúrate de ingresar un RUT con al menos 8 caracteres, sin espacios y con guion.")

    else:
        partes_rut = rut.split("-")

        if len(partes_rut) != 2:
            print("¡RUT inválido! Debe contener solo un guion.")
            continue

        else:    
            numero = partes_rut[0]
            digito_verificador = partes_rut[1]

            if numero.isdigit() and len(digito_verificador) == 1 and (digito_verificador in "123456789" or digito_verificador.upper() == "K"):
                
                opc2 = False
                while not opc2:
                        try: 
                            saldo = int(input("\nIngrese su saldo inicial en CLP: "))

                            if saldo <= 0:
                                print("¡Error bancario! Ingresa un saldo inicial válido (entero positivo).")
                            
                            elif saldo > 1000000:
                                premium = premium + 1
                                i = i + 1
                                opc2 = True
                            
                            elif saldo <= 1000000:
                                estandar = estandar + 1
                                i = i + 1
                                opc2 = True
                            
                        except ValueError:
                            print("¡Error bancario! Ingresa un saldo inicial válido (entero positivo).")
            else:
                print("RUT INVALIDO")


    

# Resumen final:
print(f"\n ¡Registro completado! Del total de {cantidad_clientes} clientes registrados, {premium} son Premium y {estandar} son Estándar. ¡Bienvenidos al sistema del Banco Digital!")
