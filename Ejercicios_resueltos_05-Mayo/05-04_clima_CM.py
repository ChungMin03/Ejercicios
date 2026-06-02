temperatura = int(input('Temperatura (°C): '))
lluvia      = int(input('Lluvia (mm): '))
viento      = int(input('Viento (km/h): '))
humedad     = int(input('Humedad (%): '))

# ERROR 1 — ¿Está bien el orden aquí?
#if temperatura <= 0:   #ERROR
    #clima = 'Frío extremo'
if temperatura <= 0 and lluvia > 0: #CORRECCION
    clima = 'Tormenta de nieve'
elif temperatura <= 0:   
    clima = 'Frío extremo'

# ERROR 2 — ¿El operador lógico es correcto?
#elif viento >= 80 or lluvia > 30:  #ERROR
elif viento >= 80 and lluvia > 30:  #CORRECCION
    clima = 'Tormenta severa'
elif lluvia > 30:
    clima = 'Lluvia intensa'

# ERROR 3 — ¿El umbral está bien definido?
elif temperatura >= 35 and humedad >= 70:
    clima = 'Bochorno'
#elif temperatura > 35: #ERROR
elif temperatura >= 35: #CORRECCION
    clima = 'Ola de calor'
elif lluvia > 5:
    clima = 'Lluvioso'
elif viento >= 50:
    clima = 'Ventoso'
else:
    clima = 'Despejado'

print('Clima:', clima)
