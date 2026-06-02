

#ejercicio 1
"""
Desarrolla un programa que alamacene las temperatusar registradas durante 7 días
consecutivos en una lista. Al finaliar el ingreso, el programa debe mostrar.
- Todas las temperaturas ingresadas (con su día corriespondeinte)
- La temperatura máxima registrada durante la semana con su día
- La temperatura mínima registrada durante la semana con su día
"""

#-----------------bloque de variables----------------
temp_diaria = []
lista_dias = ["Lunes","Martes","miercoles","Jueves","Viernes","Sabado","Domingo"]
dia = 0
#----------------------------------------------------

#-----------------bloque de ejecucion-----------------


while dia != 7:
    dia += 1
    try:
        #preguntamos por la temperatura del día 
        temp = float(input(f"Ingrese la temperatura del día N°{dia}: "))
    
    except ValueError:
        dia -= 1
        print("Ingrese valores numericos")
    
    #se agrega la temperatura a la lista
    temp_diaria.append(temp)

top = max(temp_diaria)
low = min(temp_diaria)
day_max = temp_diaria.index(top)
day_min = temp_diaria.index(low)
#------------------------------------------------------


#-----------------bloque de prints----------------------
for n in range(7):
    print(f"La temperatura del día {lista_dias[n]} fue {temp_diaria[n]}")
print(f"El día con mayor temperatura fue el {lista_dias[day_max]} con {max(temp_diaria)} grados")
print(f"El día con menor temperatura fue el {lista_dias[day_min]} con {min(temp_diaria)} grados")
#-------------------------------------------------------