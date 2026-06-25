

#Ejercicio 1
"""
Una clínica veterinaria desea que su sistema de atención
muestre siempre el mismo mensaje de bienvenida al inicio de cada turno.
El mensaje incluye el nombre de la clínica, el horario de atención y un saludo estándar.

Crear una función sin argumentos y sin retorno que imprima un mensaje de bienvenida fijo.
Tipo 1 — Sin argumentos / Sin return


def funcion_saludo():
    print("<><><>Veterinaria perritos felices<><><>")
    print("Horario de atencion: 09:00 - 21:00 ")
    print("Sea Bienvenido a la veterinaria mas acojedora que existe en el mundo mundial")

"""


#Ejercicio 2
"""
Un sistema de registro de gimnasio necesita capturar el nombre del cliente para personalizar su sesión.
La lectura del dato debe estar encapsulada en una función que retorne el valor al código principal.

Crear una función sin argumentos que capture un dato del usuario mediante input() y lo devuelva con return.

def ingreso_usuario():
    name = input("Ingrese su nombre: )
    return name

"""


#Ejercicio 3
"""
Una tienda de electrónica necesita mostrar la ficha de cada producto con su nombre, precio y stock disponible.
Los datos cambian para cada producto, pero el formato de presentación es siempre el mismo.

Crear una función con argumentos que reciba los datos del producto y los muestre formateados, sin retornar nada.

def data_products(name,price,stock):
    print("producto----------precio------------cantidad")
    print(f"{name}-----------{price}------------{stock}")

"""


#Ejercicio 4
"""
El sistema de notas de una institución educativa necesita convertir
el puntaje obtenido por un estudiante a la escala chilena (1.0 a 7.0).
La fórmula es: nota = (puntaje × 6 / puntaje_total) + 1.

Crear una función con argumentos que calcule y retorne la nota según la fórmula chilena.

def transformador_de_notas(puntaje,puntaje_total)
    nota = (puntaje * 6 / puntaje_total) + 1
    return nota

"""


#Ejercicio 5
"""
Una plataforma educativa requiere un mini sistema de presentación que primero muestre un encabezado,
luego solicite los datos del estudiante y finalmente muestre su ficha completa.

Combinar 3 tipos de funciones: una sin args/sin return para el encabezado,
una sin args/con return para leer datos, y una con args/sin return para mostrar la ficha.

def motrar_encabezado():
    print("---------DuocUc----------")
    print("---ficha de estudiante---")

def ingreso_info_ficha():
    ficha_estudiante = {}
    ficha_estudiante["Nombre"] = input("Ingrese nombre del estudiante: ")
    ficha_estudiante["Rut"] = input("Ingrese rut del estudiante: ")
    ficha_estudiante["Carrera"] = input("Ingrese la carrera del estudiante: ")
    while True:
        try:
            ficha_estudiante["Semestre"] = int(input("Ingrese semestre actual del estudiante: "))
            if ficha_estudiante["Semestre"] < 1:
                print("ERROR: ingrese un valor mayor a 0")
            else:
                break
        except ValueError:
            print("Ingrese valores numericos validos")
    return ficha_estudiante
    
def mostrar_info_ficha(datos_estudiante):
    for key, value in datos_estudiante.items():
        print(f"{key} ---- {value}")

"""

#Ejercicio 6
"""
Un sistema de autenticación necesita validar que la contraseña ingresada cumpla tres condiciones:
    -tener al menos 8 caracteres
    -contener al menos un dígito numérico 
    -contener al menos una letra mayúscula.

Crear funciones que validen condiciones individuales además una función principal que combine los resultados
y retorne un mensaje de validación.
Funciones que retornan booleanos — Descomposición del problema

def validar_cantidad_caracteres(contraseña):
    if len(contraseña) > 7:
        return True
    return False

def validar_digito_numerico(contraseña):
    contador = 0
    for i in contraseña:
        if i.isnumeric():
            return True
    return False

def validar_mayuscula(contraseña):
    for letra in contraseña:
        for mayuscula in contraseña.upper():
            if letra == mayuscula:
                return True
    return False

def validacion_definitiva(validacion_cantidad,validacion_numero,validacion_mayuscula):
    if not validacion_mayuscula:
        print("Ingrese al menos una mayuscula")
    if not validacion_cantidad:
        print("Debe tener al menos 8 caracteres")
    if not validacion_numero:
        print("Debe tener al menos un numero")
    elif validacion_cantidad and validacion_numero  and validacion_mayuscula:
        print("Contraseña valida, ¡Muchas Gracias!")
                
"""