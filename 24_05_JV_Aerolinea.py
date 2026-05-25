"""
Sistema de Control de Equipaje
------------------------------

Contexto: Eres desarrollador en una aerolínea comercial. Tu jefe te solicita crear un programa en Python que registre de manera ordenada el equipaje de bodega 
para los pasajeros de un vuelo, valide estrictamente los datos de las maletas y genere un resumen de carga crítico antes del despegue.

    - Requisito 1:  
        Cantidad de maletas a registrar
            -> El programa debe preguntar al usuario cuántas maletas desea registrar en el counter para este vuelo.
            -> Este valor debe ser obligatoriamente un número entero positivo (mayor a 0).
            -> Si el usuario ingresa un valor inválido (letras, símbolos, cero o números negativos), el programa debe capturar el error con manejo de excepciones, 
                mostrar el siguiente mensaje exacto y repetir la solicitud hasta que el dato sea correcto: 
                "¡Cantidad inválida! Ingresa un entero positivo para continuar."

    - Requisito 2:  
        Datos de cada maleta
            -> Para cada maleta, el programa debe solicitar de forma sucesiva e independiente los siguientes datos:
                a) Código de Etiqueta (texto - String): Debe tener una longitud de al menos 5 caracteres y no debe contener espacios en blanco. 
                Si no cumple con alguna de estas dos condiciones lógicas, se debe repetir la solicitud de la etiqueta sin alterar los datos previos. 
                (Ejemplos válidos: LAT99, SKY001, VLUX8)

                b) Peso de la Maleta (número entero positivo): El usuario ingresa el peso estimado en kilogramos. Si se ingresa un valor no numérico o menor/igual a cero,
                se debe capturar el error, mostrar el siguiente mensaje exacto y repetir la solicitud:
                "¡Error de pesaje! Ingresa un número entero positivo para el peso de la maleta."

    - Requisito 3: 
        Clasificación automática del equipaje
            -> Una vez ingresado y validado el peso de la maleta en curso, el sistema debe determinar su categoría de forma interna:

            |               Condición de Carga            |       Clasificación       |
            |Peso estrictamente mayor a 23 kilogramos     |        SOBREPESO          |
            |Peso menor o igual a 23 kilogramos           |        ESTÁNDAR           |

            -> El programa debe mantener contadores numéricos separados para maletas con Sobrepeso y maletas Estándar, incrementándose dinámicamente.

    - Requisito 4: 
        Resumen final de la flota
            -> Al finalizar por completo el registro de la cantidad de maletas indicada en el Requisito 1, el programa debe desplegar en pantalla el siguiente 
            mensaje de cierre con los contadores correspondientes:
            "¡El vuelo cuenta con X maletas con Sobrepeso y Y maletas Estándar! ¡Carga distribuida con éxito!"
            (Donde X e Y corresponden a los contadores acumulados durante el procesamiento).
"""

# ----------------- Bloque variables -----------------
i = 0
pesado = 0
ligero = 0

# ----------------- Bloque ejecución -----------------

# Registro de maletas:
opc = False
while not opc:
    try: 
        cantidad_maletas = int(input("Ingrese la cantidad de maletas a registrar: "))

        if cantidad_maletas <= 0:
            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        
        else:
            opc = True

    except ValueError:
        print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
        

# Datos de cada maleta y clasificación automática del equipaje:
while i < cantidad_maletas:

    etiqueta_maleta = input("\nIngrese el código de etiqueta de la maleta: ")

    if len(etiqueta_maleta) >= 5 and (" ") not in etiqueta_maleta:
        etiqueta_maleta = etiqueta_maleta.upper()

        opc2 = False
        while not opc2:
            try:
                peso_maleta = int(input("Ingrese el peso de la maleta en kilogramos: "))

                if peso_maleta <= 0:
                    print("¡Error de pesaje! Ingresa un número entero positivo para el peso de la maleta.")

                elif peso_maleta > 23:
                    pesado = pesado + 1
                    i = i + 1
                    opc2 = True
                
                elif peso_maleta <= 23:
                    ligero = ligero + 1
                    i = i + 1
                    opc2 = True

            except ValueError:
                print("¡Error de pesaje! Ingresa un número entero positivo para el peso de la maleta.")

    else:
        print("¡Código de etiqueta inválido! Debe tener al menos 5 caracteres y no contener espacios. Por favor, ingrese un código válido.")


# Resumen final de la flota:
print(f"\n¡El vuelo cuenta con un total de {cantidad_maletas} maletas, de las cuales {pesado} tienen Sobrepeso y {ligero} son Estándar! ¡Carga distribuida con éxito!")
    
