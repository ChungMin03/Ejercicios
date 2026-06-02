#----------------------------------Bloque de ejercicio------------------------------------

'''Registro de Donaciones (Ciclo for con break)
Una fundación necesita recaudar fondos para una meta específica.

Solicita al usuario cuántas donaciones se ingresarán.

Usa un ciclo for para pedir cada monto.

Regla: Si se ingresa un monto negativo, el programa debe mostrar un mensaje de
"Error: Donación fraudulenta detected" y salir del bucle inmediatamente usando break.

Al final, muestra el monto total recaudado.'''

#--------------------------------Bloque de declaracion de variables--------------------------------------------

cant_donations = int(input("Ingrese la cantidad de donaciones: "))
monto_total = 0
#--------------------------------Bloque de ejecucion------------------------------------------

for donaciones in range(cant_donations):
    donacion = int(input("Ingrese el valor de la donacion: "))
    if donacion < 0:
        print("ERROR: Donación fraudulenta detected")
        break
    else:
        monto_total += donacion


#------------------------------------------------Bloque de print--------------------------------------
'''if cant_donations > 0:'''
print(f"La donacion total es de: {monto_total}")