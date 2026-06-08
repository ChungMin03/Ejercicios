#Estructura:
#1. Palabra reservada: def inicia siempre la definicion de una funcion
#2. Nombre de la funcion: Descriptivo, en snake_case
#3. Parámetros: Variables locales que reciben los valores
#4. Salida: Return devuelve el resultado al código principal

#Estructura de una funcion sin parametros y sin retorno:
def suma():
    a = int(input("Ingrese su primer numero: "))
    b = int(input("Ingrese su segundo numero: "))
    sumatoria = a + b
    print(f"{a} + {b} = {sumatoria}")

#Estructura de una funcion con parametros y sin retorno
def resta(a,b):
    restaa = a - b
    print(f"{a} - {b} = {restaa}")

#Estructura de una funcion sin parametros y con retorno
def multiplicacion():
    a = int(input("Ingrese su primer numero: "))
    b = int(input("Ingrese su segundo numero: "))
    mult = a * b
    print(f"{a} * {b} = {mult}")

#Estructura de una funcion con parametros y con retorno
def calcular_promedio(notas, alumno):
    total = sum(notas)
    promedio = total / len(notas)
    print(f"Promedio de {alumno}: {promedio:.2f}")
    return promedio



#Variables Globales: Estan declaradas en el programa principal y se pueden usar en cualquier lado
#Variables Locales: Estan declaradas solamente en las funciones y solo se pueden usar dentro de la funcion


#MENU APLICADO CON FUNCIONES
opcion = 21921094124211
while opcion != 5:
    print("--------------- [MENU PRINCIPAL] ---------------")
    print("1.- Suma.")
    print("2.- Resta.")
    print("3.- Multiplicacion.")
    print("4.- Promedio.")
    print("5.- Salir.")
    print("------------------------------------------------")
    
    flag_menu = False
    while not flag_menu:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion < 1 or opcion > 5:
                raise ValueError
            else:
                flag_menu = True
        except ValueError:
            print("Opcion invalida, ingrese un numero entre 1 y 5.")
            print("-----------------------------------------------")
            
    if opcion == 1:
        valor_suma = suma()
        print("--------------------------------------")
    elif opcion == 2:
        a = int(input("Ingrese su primer numero: "))
        b = int(input("Ingrese su segundo numero: "))
        resta = resta(a,b)
    elif opcion == 3:
        multiplicacion = multiplicacion()
                    
    elif opcion == 4:
        notas = [4.1, 2.3, 5.6, 7.0]
        nombre_alumno = input("Ingrese su nombre: ")
        prom = calcular_promedio(notas, nombre_alumno)
        
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")
        print("--------------------------------------------------------")