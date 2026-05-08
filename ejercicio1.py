#------- BLOQUE DE VARIABLES ---------
edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A/B/C/D): ").upper()
#valores base
base_medicamentos = 60000
base_despacho = 8000

#------- BLOQUE DE EJECUCION --------------

#aplicamos descuento al precio de los medicamentos
if edad <= 30 and (tramo == "A" or tramo == "B"):
    medicamentos_descuento = base_medicamentos * 0.82
elif edad <= 30 and (tramo =="C" or tramo == "D"):
    medicamentos_descuento = base_medicamentos * 0.88
elif edad <= 60 and (tramo == "A" or tramo == "B"):
    medicamentos_descuento = base_medicamentos * 0.88
elif edad <= 60 and (tramo == "C" or tramo == "D"):
    medicamentos_descuento = base_medicamentos * 0.92
else:
    medicamentos_descuento = base_medicamentos

#aplicamos descuento al precio del despacho
if tramo == "A" or tramo == "B":
    despacho_descuento = base_despacho * 0.9 
    if edad >= 55: #si es tramo A o B y además tiene 55 años o mas, se le hace un descuento sobre descuento del 5%
        despacho_descuento = despacho_descuento * 0.95
else:
    despacho_descuento = base_despacho


#--------- PRINTS FINALES ----------------

print(f"El valor de medicamentos es: {medicamentos_descuento}\nEl valor del despacho es: {despacho_descuento}")