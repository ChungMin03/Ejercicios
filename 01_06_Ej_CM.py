#------------------ BLOQUE DE VARIABLES ----------------------
lista_temp = []
lista_dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

#----------------- BLOQUE DE EJECUCION -----------------------

#pedimos las temperaturas de cada dia
for i in range(7):
    flag = False
    while not flag:
        try:
            temp = float(input(f"Ingrese la temperatura del dia {lista_dias[i]}: "))
            lista_temp.append(temp)
            flag = True
        except:
            print("Ingrese una temperatura válida")

#variables para almacenar temperatura maxima y minima
temp_max = lista_temp[0]
temp_min = lista_temp[0]

i = 0
#recorremos con while para guardar temperaturas e indice a la vez
while i <= len(lista_temp) - 1:
    if lista_temp[i] > temp_max:
        temp_max = lista_temp[i]
        index_top = i
    else:
        temp_min = lista_temp[i]
        index_min = i
    i += 1
    
#--------------------- PRINTS FINALES ----------------------------
for i in range(7):
    print(f"Temperatura día {lista_dias[i]}: {lista_temp[i]}")

print(f"Temperatura máxima de la semana: {temp_max}, el día {lista_dias[index_top]}")
print(f"Temperatura mínima de la semana: {temp_min}, el día {lista_dias[index_min]}")