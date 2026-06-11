"""
Una clinica veterinaria desea que su sistema de atencion siempre muestra el mismo mensaje de bienvenida
"""
"""
def saludo():
    print("-----------Perritos bonitos--------------")
    print("Atención 09:00 - 21:00")
    print("Bienvenido a nuestra clinica veterinaria")



def gym_nombre():
    a = input("Ingrese su nombre: ")
    return a

nombre = gym_nombre()

print(f"Hola {nombre}")"""

#Ejercicio 2

"""
Una tienda de electrónica necesita mostrar la ficha de cada producto con su nombre, precio y stock disponible.}
 Los datos cambian para cada producto, pero el formato de presentación es siempre el mismo.
🎯 Objetivo
Crear una función con argumentos que reciba los datos del producto y los muestre formateados, sin retornar nada
"""
def display_products(name, stock, price):
    print("-----------------------------------")
    print(f"Nombre del producto: {name}")
    print(f"Cantidad de {name}: {stock}")
    print(f"Precio de {name}: {price}")
    print("-----------------------------------")


producto = input("Ingrese el nombre del producto: ")
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de producto: "))
        if cantidad < 0:
            print("Debe ingresar valores numericos positivos")
        else:
            break
    except ValueError:
        print("Ingrese valores numericos")
    try:
        precio = int("Ingrese el precio del producto: ")
        if precio < 0:
            print("Debe ingresar valores numericos positivos")
        else:
            break
    except ValueError:
        print("Ingrese valores numericos")

display_products(producto, cantidad, precio)