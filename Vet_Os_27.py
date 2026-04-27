name = input("Ingrese el nombre de du mascota:\n").upper()
specie = input("Ingrese que especie es su mascota:\n").lower()
weight = float(input("Iingrese el peso de su mascota en kg: "))

if specie != ("perro" or "gato"):                   #Descate de mascotas invalidas
    print("Especie no atendida en esta clinica")
elif specie == "perro" and weight < 10:
    consulta = "Consulta pequeña"
elif specie == "perro" and weight >= 10:
    consulta = "Consulta grande"
else:
    consulta = "Consulta felina"


print(f"Nombre: {name}")
print((f"Cantidad de caracteres: {len(name)}"))
print(consulta)