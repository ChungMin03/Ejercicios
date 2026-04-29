#Definicion del problema----------------------------------------------------------------------------------

'''
Suscripción a Gimnasio
Un gimnasio ofrece planes según la edad del socio y la jornada ("mañana" o "completa").
Jornada Mañana: $20.000 para cualquier edad.
Jornada Completa:
Menores de 18 años: $25.000.
Entre 18 y 60 años: $35.000.
Mayores de 60 años: $28.000.
Salida: Nombre del socio (sin espacios extras y en mayúsculas), jornada elegida y el valor de la mensualidad.
'''


#Definicion de variables--------------------------------------------------------------------------------
name = input("Ingrese su nombre\n")
age = int(input("Ingrese su edad: "))
type = input("Ingrese el tipo de jornada que contratara (Manana/completa)\n").lower()



#Bloque de ejecucion------------------------------------------------------------------------------------
if type != "manana" and type != "completa":
    print("Jornada invalida")
    jornada = 0                            #Se le otorga un valor para que el programa no se rompa al tratar de escribir un valor no definido
elif type == "manana":
    jornada = "Jornada matutina"
    valor = 20000
elif type == "completa":
    if age < 18:
        jornada = "Jornada completa"
        valor = 25000
    elif age >= 18 and age <= 60:
        jornada = "Jornada completa"
        valor = 35000
    elif age > 60:
        jornada = "Jornada completa"
        valor = 28000



#Prints de la ejecucion-------------------------------------------------------------------------------
if jornada != 0:                #if para que no se rompa el programa si el type no existe
    print(f"Su nombre es: {name.upper().replace(" ","")}")       #El nombre en mayusculas y sin los espacios(remplazando los espacios por vacio)
    print(jornada)
    print(f"El valor de su mensualidad es de:{valor}")