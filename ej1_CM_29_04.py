name = input("Ingrese su nombre: ")
experiencia = int(input("Ingrese sus años de experiencia: "))
ingles = input("Ingrese su nivel de ingles (basico/intermedio/avanzado): ").lower()
viaja = input("¿Posee disponibilidad para viajar? (si/no) ").lower()
resultado = ""

if experiencia >= 5 and ingles == "avanzado":
    resultado =  "Postulante DESTACADO - pasa a entrevista final\n"
elif experiencia >= 3 and (ingles == ("intermedio" or "avanzado")):
    resultado = "Postulante APTO - pasa a 2da fase\n"
elif viaja == "si" and experiencia >= 1:
    resultado = "Postulante EN REVISION\n"
else:
    resultado = "Postulante NO CUMPLE requisitos\n"

print(f"Nombre: {name.upper()}")
print(f"Largo de nombre: {len(name)}")
print(resultado)