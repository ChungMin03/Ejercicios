"""
Desarrolle un programa que calcule el costo mensual de un plan de salud
similar al nivel del parcial. El programa debe solicitar:
-Edad del afiliado (Entero)
-Tramo de ingreso: A,B,C,D
-Tiene carga familiar? (si/no)
El precio base del plan es de $45.000. Aplique las siguientes reglas
Edad            |Tramo       |Descuento Plan
<= 30           | A o B      |  20%
<= 30           | C o D      |  10%
31-60           | A o B      |  10%
31-60           | C o D      |  5%
Mayor de 60     |Cualquiera  |  0%

Carga familiar: Si tiene carga familiar Y el tramo es A o B, agregar
$8.000 al plan. Si tiene carga familiar Y el tramo es C o D, agregar
$5.000. Si no tiene carga, no se agrega nada.
Mostrar: precio base, descuento, costo del plan con descuento,
costo de carga (si aplica) y total mensual final.
"""

#--------- VARIABLES ----------
edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo de ingresos (A,B,C o D): ").upper()
carga = input("Posee carga familiar? ").lower()
precio_base = 45000
errores = ""

#--------- BLOQUE DE EJECUCION ----------

if tramo != ("A" and "B" and "C" and "D"):
    errores += "Tramo de ingreso invalido\n"
    precio_descuento = 0
    descuento = 0
if carga != "si" and carga != "no":
    errores += "Carga familiar invalida"
    precio_descuento = 0
    descuento = 0

if errores == "":
    if edad <= 30 and (tramo == ("A" or "B")):
        descuento = 20
        precio_descuento = precio_base * 0.8
    elif edad <= 30 and (tramo == ("C" or "D")):
        descuento = 10
        precio_descuento = precio_base * 0.9
    elif edad <= 61 and (tramo == ("A" or "B")):
        descuento = 10
        precio_descuento = precio_base * 0.9
    elif edad <= 61 and (tramo == ("C" or "D")):
        descuento = 5
        precio_descuento = precio_base * 0.95
    else:
        descuento = 0
        precio_descuento = precio_base
        
    if carga == "si" and (tramo == ("A" or "B")):
        costo_carga = 8000
        precio_final = precio_descuento + costo_carga
    elif carga == "si" and (tramo == ("C" or "D")):
        costo_carga = 5000
        precio_final = precio_descuento + costo_carga
    else:
        costo_carga = 0
        precio_final = precio_descuento
        
#----------- PRINTS FINALES ------------------
    print(f"Precio base: ${precio_base}\nDescuento: {descuento}%\nCosto plan con descuento: ${precio_descuento}")
    if costo_carga != 0:
        print(f"Costo de carga: ${costo_carga}")
    print(f"Total mensual final: ${precio_final}")
else:
    print(errores)