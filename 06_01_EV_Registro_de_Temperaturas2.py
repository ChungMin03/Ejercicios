##Desarrolle un programa que almacene las temperaturas durante 7 días 
##Muestra: Todas las temperaturas ingresadas (con sus días correspondientes)
##La temp máx ingresada
##La temp mín ingresada

##-------------------------DECLARAMOS LISTA----------------------------##

temperaturas=[]
dias=["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

##----------------------DECLARAMOS VARIABLES------------------------------##

flag1=True

##----------------------ENTRADA------------------------------##

print("------------------------------------------------------------")
print("############# REGISTRO DE TEMPERATURA ######################")
print("------------------------------------------------------------")

##----------------------CICLO------------------------------##

for i in range(7):
    flag1=True

    while flag1==True:   
        try:
            temp=float(input(f"Ingrese la temperatura del {dias[i]}: \n"))
            temperaturas.append(temp)
            flag1=False
            print("")
        except ValueError:
            print("Error. Ingrese un número real")

##---------------------------PROCESO-------------------------##

temp_min=min(temperaturas)
pos_min=temperaturas.index(temp_min)
dia_min=dias[pos_min]

temp_max=max(temperaturas)
pos_max=temperaturas.index(temp_max)
dia_max=dias[pos_max]

##---------------------------SALIDA-------------------------##

for j in range(7):
    print(f"La temperatura del {dias[j]} fue de: {temperaturas[j]}°C")

print("")
print(f"La temperatura mas baja fué de {temp_min}°C , el día {dia_min}")
print(f"La temperatura mas alta fué de {temp_max}°C , el día {dia_max}")