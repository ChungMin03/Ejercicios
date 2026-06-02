"""
1. Registro de Donaciones (Ciclo for con break)
Una fundación necesita recaudar fondos para una meta específica.

Solicita al usuario cuántas donaciones se ingresarán.

Usa un ciclo for para pedir cada monto.

Regla: Si se ingresa un monto negativo, el programa debe mostrar un mensaje de "Error: Donación fraudulenta detected" y salir del bucle inmediatamente usando break.

Al final, muestra el monto total recaudado.
"""

cant_donaciones = int(input("Ingrese la cantidad de donaciones que ingresara: "))
monto_total = 0

for donacion in range(cant_donaciones):
    valor_donacion = int(input("Ingrese el valor de la donacion: "))
    if valor_donacion < 0:
        print("Error: Donación fraudulenta detected")
        break
    else:
        
        monto_total += valor_donacion

print(f"Monto total recaudado: {monto_total}")