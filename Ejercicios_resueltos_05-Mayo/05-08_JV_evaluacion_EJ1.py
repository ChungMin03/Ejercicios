

# Bloque de variables ---------------------------------
integrantes =int(input("Ingrese integrantes del hogar: "))
quintil = int(input("Ingrese su quintil: "))

cuota_mensual = 12000
kit = 15000
descuento = 0

# Bloque de ejecucion ---------------------------------

# Bloque de ejecución en base a la cuota mensual:

if integrantes >= 5 and (quintil == 1 or quintil == 2):
    descuento = 0.25 * cuota_mensual
    nueva_cuota_mensual = cuota_mensual - descuento

elif integrantes >= 5 and (quintil == 3 or quintil == 4):
    descuento = 0.18 * cuota_mensual
    nueva_cuota_mensual = cuota_mensual - descuento

elif integrantes < 5 or integrantes >= 2 and (quintil == 1 or quintil == 2):
    descuento = 0.15 * cuota_mensual
    nueva_cuota_mensual = cuota_mensual - descuento

elif integrantes < 5 or integrantes >= 2 and (quintil == 3 or quintil == 4):
    descuento = 0.10
    nueva_cuota_mensual = cuota_mensual - descuento

elif integrantes < 2 or quintil == 5:
    descuento = 0
    nueva_cuota_mensual = cuota_mensual - descuento

else:
    nueva_cuota_mensual = cuota_mensual

# Bloque de ejecución en base a los descuento del kit

    
if integrantes >= 4 and (quintil == 1 or quintil == 2 or quintil == 3):
    descuento = 0.17 * kit
    nuevo_kit = kit - descuento

elif quintil == 1 or quintil == 2 or quintil == 3:
    descuento_kit = 0.12 * kit
    nuevo_kit = kit - descuento
    
else:
    nuevo_kit = kit
    


      
    


