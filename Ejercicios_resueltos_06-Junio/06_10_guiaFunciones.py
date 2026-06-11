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
    flag_nombre = False
    while not flag_nombre:
        name = input("Ingrese su nombre: ")
        if name.replace(" ","").isalpha():
            flag_nombre = True
        else:
            print("Error: Contiene numeros o caracteres invalidos.")
    
    flag_rut = False
    while not flag_rut:
        rut = input("Ingrese su rut (sin puntos y con guion): ")
        if "-" in rut:
            lista_rut = rut.split("-")
            if lista_rut[0].isnumeric() and lista_rut[1]!= "0" and (lista_rut[1].isnumeric() or lista_rut[1].upper() == "K"):
                flag_rut = True
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
        except ValueError:
            print("Error: Ingrese una edad valida.")
            
    return name, rut, edad

def mostrarFicha(nombre, rut, edad):
    print("================= FICHA DEL ESTUDIANTE =================")
    print(f"Nombre: {nombre}\nRut: {rut}\nEdad: {edad}")
    
"""encabezado()
nombre, rut, edad = solicitarDatos()
mostrarFicha(nombre, rut, edad)"""