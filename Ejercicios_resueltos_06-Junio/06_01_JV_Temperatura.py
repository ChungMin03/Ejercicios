"""
Registros de temperatura semanales:

- Desarrolle un programa que almacene las temperaturass registradas durante 7 días consecutivos en una lista. Al finalizar el ingreso, el programa debe mostrar:
    1. Todas las temperaturas ingresadas (con su día correspondiente).
    2. La temperatura máxima registrada durante la semana con su día.
    3. La temperatura mínima registrada durante la semana con su día.
"""
#----------------- bloque funciones ----------------
#Esta funcion nos permite mostrar las temperaturas con sus dias correspondientes
def mostrar_temperaturas(temperatura,dias):
    for n in range(7):
        print(f"La temperatura del día {dias[n]} fue {temperatura[n]}")

#Esta función nos permite mostrar la temperatura máxima con su día correspondiente
def mostrar_temp_max(temperatura,dias):
    temp_maxima = temperatura[0]
    dia_maximo = dias[0]

    for i in range(1, len(temperatura)):
        if temperatura[i] > temp_maxima:
            temp_maxima = temperatura[i]
            dia_maximo = dias[i]
    
    print(f"El día con mayor temperatura fue el {dia_maximo} con {temp_maxima} grados")

#Esta función nos permite mostrar la temperatura mínima con su día correspondiente
def mostrar_temp_min(temperatura,dias):
    temp_minima = temperatura[0]
    dia_minimo = dias[0]

    for i in range(1, len(temperatura)):
        if temperatura[i] < temp_minima:
            temp_minima = temperatura[i]
            dia_minimo = dias[i]
    
    print(f"El día con menor temperatura fue el {dia_minimo} con {temp_minima} grados")


#----------------- bloque de variables ----------------
temperatura = []
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

#----------------- bloque de ejecucion -----------------

for dia in range(7):
    #solicitar temperatura
    opc = False
    while not opc:
        try:
            temp = float(input(f"Ingrese la temperatura del día {dia+1}: "))

            # agregar temperatura a la lista
            temperatura.append(temp)

            opc = True
        except ValueError:
            print("Debe ingresar un numero valido")


#----------------- bloque de prints ----------------
print("") #salto de linea para mejor lectura
#mostrar temperaturas con sus dias correspondientes
mostrar_temperaturas(temperatura,dias)

#mostrar temperatura máxima con su día correspondiente
mostrar_temp_max(temperatura,dias)

#mostrar temperatura mínima con su día correspondiente
mostrar_temp_min(temperatura,dias)