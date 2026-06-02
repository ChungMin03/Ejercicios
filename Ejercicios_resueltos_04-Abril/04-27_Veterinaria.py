name = input("Ingrese el nombre de su mascota: ")
especie = input(f"Ingrese la especie de {name} (perro/gato): ").lower()
peso = float(input(f"Ingrese el peso de {name}: "))

if especie == "perro" and peso < 10:
    consulta = "Consulta pequeña - $15.000\n"
elif especie == "perro" and peso >= 10:
    consulta = "Consulta grande - $22.000\n"
elif especie == "gato":
    consulta = "Consulta felina - $12.000\n"
else:
    consulta = "Especie no atendida en esta clínica\n"

print(f"Nombre paciente: {name.upper()}")
print(f"Cantidad de letras: {len(name)}")
print(consulta)