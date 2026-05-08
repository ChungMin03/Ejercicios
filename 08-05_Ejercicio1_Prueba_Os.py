#---------------------Datos del problema----------------------------------------

'''Medicamentos mensual = 60000
    Despacho a domicilio = 8000
    edad < 30
    tramo A o B = 18%
          C o D = 12%
    edad entre 31 y 60 
    tramo A o B = 12%
          C o D = 8%
    '''
#-----------------------Bloque de inputs y variables----------------------------------------------

age = int(input("Ingrese su edad: "))
income = input("Ingrese su tramo de ingresos (A/B/C/D) : ").lower()
descuento_despacho = 0
descuento = 0
medicamentos = 60000
despacho = 8000

#----------------------Bloque de ejecucion-------------------------------------------------

if age < 30 and income == ("a" or "b"):
    descuento = 18
    descuento_despacho = 10
elif age < 30 and income == ("c" or "d"):
    descuento = 12
    descuento_despacho = 0
elif age >= 30 and age <= 60 and income == ("a" or "b"):
    descuento = 12
    descuento_despacho = 10
elif age >= 30 and age <= 60 and income == ("c" or "d"):
    descuento = 8
    descuento_despacho = 0
elif age >= 55:
    descuento_despacho += 5
else:
    descuento = 0
    descuento_despacho = 0

#------------------------------------Bloque de prints--------------------------------------

print(f"El valor de los medicamentos es: {medicamentos - (medicamentos * descuento/100)}")
print(f"El valor del despacho es: {despacho - (despacho * descuento_despacho/100)}")