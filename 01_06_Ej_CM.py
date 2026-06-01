lista_temp = []
lista_dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
for i in range(7):
    flag = False
    while not flag:
        try:
            temp = float(input("Ingrese la temperatura del dia: "))
            lista_temp.append(temp)
            flag = True
        except:
            print("Ingrese una temperatura válida")

for i in range(7):
    print(f"Temperatura día {lista_dias[i]}: {lista_temp[i]}")

print(f"Temperatura máxima de la semana: {max(lista_temp)}, el día {(max(lista_temp)).index()}")
print(f"Temperatura mínima de la semana: {min(lista_temp)}, el día {(min(lista_temp)).index()}")