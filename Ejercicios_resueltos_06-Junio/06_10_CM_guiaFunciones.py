#Ejercicio 1
#Una clínica veterinaria desea que su sistema de atención muestre siempre el mismo mensaje de bienvenida al inicio de cada turno. El mensaje incluye el nombre de la clínica, el 
#horario de atención y un saludo estándar.
#Crear una función sin argumentos y sin retorno que imprima un mensaje de bienvenida fijo.
#Tipo 1 — Sin argumentos / Sin return

def saludoVet():
    print("==========================================")
    print("|       Clinica veterinaria Cholito      |")
    print("==========================================")
    print("\nHorario de atencion:")
    print("Lunes a Domingo de 08:00 a 24:00")
    
#Ejercicio 2
#Un sistema de registro de gimnasio necesita capturar el nombre del cliente para personalizar su sesión. La lectura del dato debe estar encapsulada en una función que 
#retorne el valor al código principal.
#Crear una función sin argumentos que capture un dato del usuario mediante input() y lo devuelva con return.
#Tipo 2 — Sin argumentos / Con return

def registroGym():
    name = input("Ingrese su nombre: ")
    return name

"""name = registroGym()
print(f"Bienvenido/a al gimnasio {name}")"""

#Ejercicio 3
#Una tienda de electrónica necesita mostrar la ficha de cada producto con su nombre, precio y stock disponible. Los datos cambian para cada producto, 
#pero el formato de presentación es siempre el mismo.
#Crear una función con argumentos que reciba los datos del producto y los muestre formateados, sin retornar nada.
#Tipo 3 — Con argumentos / Sin return

def fichaProducto(producto, precio, stockProducto):
    print(f"Producto: {producto}\nPrecio: ${precio}\nStock Disponible: {stockProducto}")

"""producto = "PC Gamer"
precio = 990990
stock = 7
fichaProducto(producto, precio, stock)"""

#Ejercicio 4
#El sistema de notas de una institución educativa necesita convertir el puntaje obtenido por un estudiante a la escala chilena (1.0 a 7.0). 
#La fórmula es: nota = (puntaje × 6 / puntaje_total) + 1.
#Crear una función con argumentos que calcule y retorne la nota según la fórmula chilena.
#Tipo 4 — Con argumentos / Con return

def puntajeNota(puntaje, puntaje_total):
    nota = (puntaje * 6 / puntaje_total) + 1
    return nota

"""puntaje=90
puntaje_total=100
nota_final = puntajeNota(puntaje, puntaje_total)
print(f"Puntaje obtenido: {puntaje}\nNota final: {nota_final}")"""

#Ejercicio 5
#Una plataforma educativa requiere un mini sistema de presentación que primero muestre un encabezado, luego solicite los datos del estudiante y finalmente muestre su ficha completa.
#Combinar 3 tipos de funciones: una sin args/sin return para el encabezado, una sin args/con return para leer datos, y una con args/sin return para mostrar la ficha.
#Composición de funciones — Tipos 1, 2 y 3

def encabezado():
    print("==========================================")
    print("|               DUOC UC                  |")
    print("==========================================")
    
def solicitarDatos():
    #creamos diccionario para guardar los datos
    diccionario_datos = {
        "Nombre" : "",
        "Semestre" : "",
        "Carrera" : "",
        "Rut" : "",
        "Edad" : ""
    }
    flag_nombre = False
    while not flag_nombre:
        name = input("Ingrese su nombre: ")
        if name.replace(" ","").isalpha():
            flag_nombre = True
            diccionario_datos["Nombre"] = name
        else:
            print("Error: Contiene numeros o caracteres invalidos.")
    
    flag_rut = False
    while not flag_rut:
        rut = input("Ingrese su rut (sin puntos y con guion): ")
        if "-" in rut:
            lista_rut = rut.split("-")
            if lista_rut[0].isnumeric() and lista_rut[1]!= "0" and (lista_rut[1].isnumeric() or lista_rut[1].upper() == "K"):
                flag_rut = True
                diccionario_datos["Rut"] = rut
            else:
                print("Error: Rut ingresado no es valido")
        else:
            print("Error: Debe tener guion (-).")
            
    flag_edad = False
    while not flag_edad:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 1:
                raise ValueError
            else:
                flag_edad = True
                diccionario_datos["Edad"] = edad
        except ValueError:
            print("Error: Ingrese una edad valida.")

    flag_semestre = False
    while not flag_semestre:
        try:
            semestre = int(input("Ingrese el semestre que cursa: "))
            if semestre < 1:
                raise ValueError
            else:
                flag_semestre = True
                diccionario_datos["Semestre"] = semestre
        except ValueError:
            print("Error: Ingrese un semestre valido.")

    flag_carrera = False
    while not flag_carrera:
        carrera = input("Ingrese su carrera: ")
        flag_carrera = True
        diccionario_datos["Carrera"] = carrera
            
    return diccionario_datos

def mostrarFicha(diccionario_datos):
    print("================= FICHA DEL ESTUDIANTE =================")
    for llave, valor in diccionario_datos.items():
        print(f"{llave}: {valor}")
    
"""encabezado()
diccionario = solicitarDatos()
mostrarFicha(diccionario)"""


#Ejercicio 7
#Un restaurante necesita un sistema que calcule el monto de propina según el
#porcentaje seleccionado por el cliente (10%, 15% o 20%), y muestre el desglose:
#subtotal, propina y total a pagar.
#🎯 Objetivo Crear funciones para calcular y mostrar el desglose de una cuenta con propina,
#usando return para comunicar resultados entre funciones.
#💡 Concepto Comunicación entre funciones mediante return

def calcularPropina(subtotal):
    boleta = {}
    flag_propina = False
    while not flag_propina:
        print("-------------------- PROPINA --------------------")
        try:
            opcion_propina = int(input("Ingrese una opcion:\n1) 10%\n2) 15%\n3) 20%\n"))
            if opcion_propina < 1 or opcion_propina > 3:
                raise ValueError
            else:
                flag_propina = True
        except ValueError:
            print("Ingrese una opcion valida (1,2,3).")
    
    if opcion_propina == 1:
        propina = 1.1
        valor_propina = subtotal * 0.1
        total = subtotal * propina
    elif opcion_propina == 2:
        propina = 1.15
        valor_propina = subtotal * 0.15
        total = subtotal * propina
    else:
        propina = 1.2
        valor_propina = subtotal * 0.2
        total = subtotal * propina
    
    boleta["subtotal"] = subtotal
    boleta["propina"] = valor_propina
    boleta["total"] = total
    
    return boleta

def mostrarBoleta(boleta):
    print(f"----------------------- BOLETA -----------------------")
    print(f"Monto neto ---------------------- ${boleta["subtotal"]}")
    print(f"Propina ------------------------- ${boleta["propina"]:.2f}")
    print(f"Monto total --------------------- ${boleta["total"]:.2f}")
    

#codigo principal
flag_subtotal = False
while not flag_subtotal:
    try:
        subtotal = float(input("Ingrese el valor de la cuenta: "))
        if subtotal < 1:
            raise ValueError
        else:
            flag_subtotal = True
    except ValueError:
        print("Ingrese un monto valido.")

boleta = calcularPropina(subtotal)
mostrarBoleta(boleta)