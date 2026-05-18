"""
Registro 1
El programa debe preguntar al usuario cuántos vehículos desea registrar en esta sesión.
•	Este valor debe ser un número entero positivo (mayor a 0).
•	Si el usuario ingresa un valor inválido (letras, cero o negativo),
 se debe mostrar el siguiente mensaje y volver a pedir el dato:

"¡Cantidad inválida! Ingresa un entero positivo para continuar."

Registro 2
Para cada vehículo, el programa debe solicitar los siguientes datos:

a) Placa Vehicular (texto - String)
•	Debe tener al menos 6 caracteres.
•	No debe contener espacios.
•	Si no cumple alguna condición, se debe volver a pedir la placa.
Ejemplos válidos: TRK001HD, VANMAX6, CARLITE2

b) Capacidad de Carga (número entero positivo)
•	El usuario ingresa la capacidad de carga en toneladas.
•	Si se ingresa un valor inválido (letras, cero o negativo), se muestra
 el siguiente mensaje y se repite la solicitud:
 
"¡Error logístico! Ingresa un número entero positivo para la capacidad de carga."

Registro 3
Una vez ingresada la capacidad de carga, el programa debe clasificar automáticamente el vehículo:

Condición	Clasificación
Capacidad > 55 toneladas	PESADO
Capacidad ≤ 55 toneladas	LIGERO

El programa debe mantener contadores separados para vehículos Pesados y Ligeros durante todo el proceso.


"""
#-----------------bloque de ejecucion-------------------
try:
    flag = False
    while not flag:
        quant = int(input("Ingrese la cantidad de vehiculos a registrar: "))
        flag = True
        if quant < 1:
            raise ValueError("la cantidad debe ser positiva")
        
except ValueError as error1:
    print(f"ERROR: {error1}")

error = ""

for i in range(1,(quant+1)):
    flag1 = False
    while not flag1:
        plate = input("Ingrese la placa del auto")
        if len(plate) < 6:
            error += ("Cantidad de caracteres incorrectos\n")

        if " " in plate:
            error += ("No debe contener espacios vacios\n")

        if error != "":
            print(error)
        
        else:
            flag1 = True

    







