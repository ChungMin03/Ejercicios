# ------ Bloque variables ------

senior = 0
junior = 0
i = 0

# ------ Bloque ejecución ------

opc = False
while not opc:
    try: 
        cantidad_ing = int(input("Ingrese la cantidad de ingenieros a registrar: "))
        if cantidad_ing <= 0:
            print("¡Dato invalido! Ingresa un entero positivo mayor a 0 para continuar el registro.")
        else:
            opc = True
    except ValueError:
        print("¡Dato invalido! Ingresa un entero positivo para continuar el registro.")


while i < cantidad_ing:
    registro = input("\nIngrese su nombre tecnico: ")

    if len(registro) < 6 or " " in registro:
        print("¡Dato invalido! Su registro debe tener al menos 6 caracteres y no incluir espacios.")
    else:
        opc2 = False
        while not opc2:
            try: 
                nivel = int(input("\nIngrese su nivel: "))
                
                if nivel <= 0:
                    print("¡Error de validacion! Ingresa un número entero positivo para el nivel técnico.")

                elif nivel <= 45:
                    junior = junior + 1
                    i = i + 1
                    opc2 = True
                
                elif nivel > 45:
                    senior = senior + 1
                    i = i + 1
                    opc2 = True


            except ValueError:
                print("¡Error de validacion! Ingresa un número entero positivo para el nivel técnico.")

print(f"\n¡Del total {cantidad_ing} ingenieros registrados, el instituto cuenta con {senior} ingenieros senior y {junior} ingenieros junior!")
print("¡Registro completado satisfactoriamente!")
