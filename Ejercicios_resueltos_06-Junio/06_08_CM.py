"""ficha_alumno = {}

while True:
    try:
        ficha_alumno["nombre"] = input("Ingrese su nombre: ")
        break
    except ValueError:
        print("Error: Caracter inválido.")

while True:
    try:
        ficha_alumno["edad"] = int(input("Ingrese su edad: "))
        
        if ficha_alumno["edad"] < 1:
            raise ValueError
        else:
            break
    except ValueError:
        print("Error: Edad ingresada no es valida.")

while True:
    try:
        ficha_alumno["carrera"] = input("Ingrese su carrera: ")
        break

    except ValueError:
        print("Error: Carrera no válida.")

while True:
    try:
        ficha_alumno["correo"] = input("Ingrese su correo electronico: ")
        break
    except:
        print("Error. Correo ingresado no valido")

while True:
    try:
        ficha_alumno["edad"] = int(input("Ingrese su edad: "))
        if ficha_alumno["edad"] < 1:
            raise ValueError
        else:
            break
    except ValueError:
        print("Error: Edad ingresada no valida.")

del(ficha_alumno["carrera"])

for llave, valor in ficha_alumno.items():
    print(f"{llave} <----> {valor}")"""


def solicitar_nombre():
    nombre = input("Ingrese su nombre: ")
    mensaje = f"Nombre ingresado: {nombre}"
    return nombre, mensaje

nombre, mensaje = solicitar_nombre()

print(f"Nombre ingresado: {nombre}")
print(mensaje)