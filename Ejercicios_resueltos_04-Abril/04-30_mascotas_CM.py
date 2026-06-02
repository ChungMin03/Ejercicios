horas_libre  = int(input('Horas libres por dia (0-24): '))
espacio      = input('Tienes espacio exterior? (si/no): ')
experiencia  = input('Tienes experiencia con mascotas? (si/no): ')
presupuesto  = int(input('Presupuesto mensual en USD (0-500): '))

# ── BLOQUE 1: ¿Es apta para adoptar? ──────────────────────
# ERROR 1 — revisa el operador lógico
#if horas_libre < 2 or presupuesto < 50: #ERROR
if horas_libre < 2 and presupuesto < 30: #CORRECCION
    apta = False
    mascota = 'No apta para adoptar'

# ── BLOQUE 2: ¿Qué mascota le conviene? ───────────────────
# ERROR 2 — revisa el orden de las condiciones
#elif horas_libre >= 4: #ERROR
elif horas_libre >= 4 and espacio == 'si' and experiencia == 'si': #CORRECCION
    mascota = 'Perro grande'

elif horas_libre >= 4: #CORRECCION
    mascota = 'Perro'


elif horas_libre >= 3 and espacio == 'si':
    mascota = 'Perro mediano'

# ERROR 3 — revisa el umbral
#elif horas_libre > 2: #ERROR
elif horas_libre >= 2: #CORRECCION
    mascota = 'Gato'

elif presupuesto >= 30:
    mascota = 'Pez o hamster'

else:
    mascota = 'No apta para adoptar'

print('Resultado:', mascota)

