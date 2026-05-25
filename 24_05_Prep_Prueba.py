"""#EJERCICIO 1
#--------------- BLOQUE DE VARIABLES ---------------------
premium = 0
estandar = 0

#-------------- BLOQUE DE EJECUCION --------------------
#requisito 1
flag = False
while not flag:
    try:
        cant_registros = int(input("Ingrese la cantidad de clientes que registrara: "))
        if cant_registros <= 0:
            raise ValueError
        else:
            flag = True
    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        

#requisito 2
for i in range(1, cant_registros + 1):
    flag2 = False
    while not flag2:
        errores = ""
        print(f"-------------- Registro usuario {i} --------------------")
        try:
            rut = input(f"Ingrese su rut, sin guion ni puntos: ")
            if len(rut) < 8:
                print("\n - Debe tener al menos 8 caracteres.")
                if " " in rut:
                    print("\n - No debe contener espacios.")
                    continue
                continue
            if " " in rut:
                print("\n - No debe contener espacios.")
                if len(rut) < 8:
                    print("\n - Debe tener al menos 8 caracteres.")
                    continue
                continue

            if len(rut) >= 8 and " " not in rut:
                flag2 = True
                flag3 = False
                while not flag3:
                    try:
                        saldo_inicial = int(input("Ingrese su saldo: "))
                        if saldo_inicial <= 0:
                            raise ValueError
                        else:
                            flag3 = True
                            #requisito 3
                            if saldo_inicial > 1000000:
                                premium += 1
                            else:
                                estandar += 1
                    except ValueError:
                        print("¡Error bancario! Ingresa un saldo inicial válido (entero positivo).")
        except ValueError:
            print(f"ERRORES: {errores}")
        
        
                
#requisito 4
print(f"¡Registro completado! {premium} clientes Premium y {estandar} clientes Estándar incorporados al sistema.")

"""