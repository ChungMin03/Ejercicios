'''
---------------------------------------------------------------------------------------------------------------------------------
Codigo para aprender a ocupar el Try y Except para validar los datos de ingreso. Ingnorar este comentario, no es parte del menu.
---------------------------------------------------------------------------------------------------------------------------------

correcto = False

while not correcto:
    try: 
        num = int(input("ingrese un numero: "))
        correcto = True
    except ValueError:
        print("Debe ingresar un numero. Error en el ingreso de dato")

par = 0

for i in range(1, num+1)
    if i % 2 == 0:
        print(f"numero: {i}")
        par = par + 1
    
print(f"Cantidad de numeros pares: {par}")
'''

'''
Una empresa realiza una encuesta de satisfaccion. El menu tiene opciones: 
1. Registrar respuesta: (1 = muy insatisfecho, 5 = muy satisfecho)
2. Ver estadisticas(promedio, mejor/peor puntacion, % de los que respondieron 4 o 5)
3. nueva encuesta
4. salir

La opcion 3 reinicia los contadores
'''
# ----------------- Bloque de variables -----------------
# Se definen las variables a trabajar para el menu, se inicializan en 0 o en un valor que no afecte los resultados.
suma_cantidad = 0
suma_elementos= 0
suma_porcentaje = 0
porcentaje = 0
mejor = 0
peor = 6 # Se inicializa en 6 para que cualquier valor ingresado sea menor y se actualice el peor resultado.

# ----------------- Bloque de menu -----------------
menu = False
while not menu:
    print("\n-------------<<< MENU >>>-------------")
    print("1.- Registrar respuesta")
    print("2.- Ver estadisticas")
    print("3.- Nueva encuesta")
    print("4.- Salir")

    # Validacion de ingreso de opcion del menu
    opc = False
    while not opc:
        try: 
            opcion = int(input("Ingrese la opción: "))
            opc = True
        except ValueError:
            print("No ingreso una opción")
    
    if opcion == 1:
        print("\n1.- Muy insatisfecho \n2.- Insatisfecho \n3.- Neutro \n4.- Satisfecho \n5.- Muy satisfecho")
        val = False
        while not val:
            try:
                valor = int(input("Ingrese su respuesta: "))

                # Se valida que el valor ingresado sea parte del rango permitido
                if (valor >= 1) and (valor <= 5):

                    # Valores que se registran para sacar el promedio
                    suma_cantidad = suma_cantidad + 1
                    suma_elementos = suma_elementos + valor

                    #Acumulador de totales de 4 y 5
                    if valor == 4 or valor == 5:
                        suma_porcentaje = suma_porcentaje + 1

                    # Logica para el mejor y el peor numero.
                    if valor > mejor:
                        mejor = valor

                    if valor < peor:
                        peor = valor
                    
                    # Si el valor es correcto, se sale del ciclo de validacion de ingreso de respuesta.
                    val = True
                else:
                    print("ingresa un numero de 1 al 5")
                
            except ValueError:
                print("Error en el ingreso de dato, ingresa un numero de 1 al 5")
                continue
                

    if opcion == 2:
        # Se crea un submenú para mostrar las estadisticas, se valida el ingreso de la opcion del submenú y se muestran los resultados.
        menu2 = False
        while not menu2:
            print("\n--- Submenú Estadísticas ---")
            print("1.- Promedio \n2.- Mejor y peor puntuacion \n3.- Porcentaje \n4.- Salir")
            
            # Validacion de ingreso de opcion del submenú
            opc = False
            while not opc:
                try: 
                    opcion2 = int(input("Ingrese la opción: "))
                    opc = True
                except ValueError:
                    print("No ingreso una opción")

            if opcion2 == 1:
                
                # Se valida que la cantidad de respuestas sea mayor a 0 para evitar una division por 0.
                if suma_cantidad > 0:
                    promedio = suma_elementos/suma_cantidad
                    print(f"\nEl promedio del la encuesta es: {promedio:.1f}")
                else:
                    promedio = 0
                    print(f"\nEl promedio del la encuesta es: {promedio}")
                    print("No se han registrado respuestas aún.")
            
            elif opcion2 == 2:
                
                # Para no mostrar valores erroneos, se valida que el mejor y el peor resultado hayan sido actualizados.
                if mejor == 0 and peor == 6:
                    print("\nNo se han registrado respuestas aún.")
                else:
                    print(f"\nLa mejor nota fue: {mejor}")
                    print(f"La peor nota fue: {peor}")

            elif opcion2 == 3:

                # Se valida que la cantidad de respuestas sea mayor a 0 para evitar una division por 0.
                if suma_cantidad != 0:
                    porcentaje = (suma_porcentaje/suma_cantidad)*100
                    print(f"\nEl porcentaje de 4 y 5 es: {porcentaje:.1f}%")

                else:
                    porcentaje = 0
                    print(f"\nEl porcentaje de 4 y 5 es: {porcentaje}%")
                    print("No se han registrado respuestas aún.")

            elif opcion2 == 4:
                print("\nSaliendo del submenú de estadísticas...")
                menu2 = True

    if opcion == 3:

        suma_cantidad = 0
        suma_elementos= 0
        suma_porcentaje = 0
        porcentaje = 0
        mejor = 0
        peor = 6
        promedio = 0
        print("\nDatos reiniciados")
    
    if opcion == 4:
        print("\nGracias por ocupar el menu")
        menu = True