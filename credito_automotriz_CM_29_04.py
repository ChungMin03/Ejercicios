""" Validador de Crédito Automotriz
Una automotriz otorga créditos según el sueldo del cliente, su edad y el valor del auto.

Condiciones para aprobar:

El cliente debe tener entre 21 y 65 años.

El sueldo debe ser al menos 1/10 del valor total del auto.

Si el auto es de origen "China", el sueldo debe ser superior a $800.000 (por políticas de repuestos).

Cálculo adicional: Si el crédito es aprobado y el cliente tiene menos de 30 años, se agrega un "Seguro Joven" de $15.000 al costo mensual.

Objetivo: Mostrar si el crédito fue APROBADO o RECHAZADO. Si fue rechazado, indicar todos los motivos (edad fuera de rango, sueldo insuficiente, etc.)."""

#variables
edad = int(input("Ingrese su edad: "))
sueldo = int(input("Ingrese su sueldo: "))
valor_auto = int(input("Ingrese el valor del auto: "))
origen = input("Ingrese el origen del auto: ").lower()
motivos = ""

#ejecucion
if edad < 21 or edad > 65:
    motivos += 'Motivo: Edad fuera de rango\n'
if sueldo < valor_auto * 0.1:
    motivos += 'Motivo: Sueldo insuficiente\n'
if origen == 'china' and sueldo < 800000:
    motivos += 'Motivo: Sueldo menor a 800.000 (politica de repuesto para auto de origen Chino)\n'
    

#prints finales
if motivos == '':
    print('Credito aprobado')
    if edad < 30:
        print('Se agrega un "Seguro Joven" de $15.000 al costo mensual.')
else:
    print(f'Credito rechazado\n{motivos}')


