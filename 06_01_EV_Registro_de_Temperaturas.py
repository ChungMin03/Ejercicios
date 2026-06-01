##Desarrolle un programa que almacene las temperaturas durante 7 días 
##Muestra: Todas las temperaturas ingresadas (con sus días correspondientes)
##La temp máx ingresada
##La temp mín ingresada

##-------------------------DECLARAMOS LISTA----------------------------##

temperaturas=[]

print("------------------------------------------------------------")
print("############# REGISTRO DE TEMPERATURA ######################")
print("------------------------------------------------------------")

##----------------------DECLARAMOS VARIABLES------------------------------##

flag1=True
temp_max=0
temp_min=0

##----------------------CICLO------------------------------##

##Implementamos un ciclo para preguntar por cada temperatura

for dia in range(7):
    flag1=True

    while flag1==True:   
        flag1=True

        try:
            temp=float(input(f"Ingrese la temperatura del día {dia+1} \n"))
            temperaturas.append(temp)
            flag1=False
        except ValueError:

            print("Error. Ingrese un número real")

print(f"Temperatura del día lunes: {temperaturas[0]}")
print(f"Temperatura del día martes: {temperaturas[1]}")
print(f"Temperatura del día miércoles: {temperaturas[2]}")
print(f"Temperatura del día jueves: {temperaturas[3]}")
print(f"Temperatura del día viernes: {temperaturas[4]}")
print(f"Temperatura del día sábado: {temperaturas[5]}")
print(f"Temperatura del día domingo: {temperaturas[6]}")

temperaturas.sort()
print(f"La temperatura mas baja es: {temperaturas[0]}")
print(f"La temperatura mas alta es: {temperaturas[6]}")