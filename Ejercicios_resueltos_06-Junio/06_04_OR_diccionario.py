#caracterizticas de los diccionarios:

#definimos un diccionario ejemplo, en este caso personal es nuestro diccionario ejemplo
#donde nombre = clave y victor el valor
"""personal={
    "nombre" : "victor"
}

#agregar valores al diccionario
personal["edad"] = 28
#definimos la clave en este caso edad y le agregamos el input que en este caso el 28

#Modificar
personal["nombre"] = "Joel"


#eliminar 
del personal["nombre"]


#recorrer los diccionarios
#mostrar solo las claves del diccionario
for llave in personal.keys():
    print(llave)
    #esto imprime solo las llaves del diccionario

#mostrar solo los valores del diccionario
for valor in personal.value():
    print(valor)
    #con esto imprimimos solo los valores

#mostrar ambos datos tanto claves como valores
#aplicar ambos valores dontro del for
for llave, valor in personal.items():
    print(f"{llave} <--> {valor}")"""



#Ejercicio 1
"""
Una tienda necesita registrar datos de un producto indicado por el usuario.
El programa debe solicitar el nombre del producto, su precio y su stock disponible,
almacenar los en un diccionario y luego mostrar un resumen de sus datos
ademas debe indicar si el producto tiene o no stock disponible
"""

#resolucion del profe

#declarar diccionario vacio para rellenarlo posteriormente
producto = {}

#solicitud de datos
#solicitud del producto especifico
producto["nombre"] = input("Ingrese el nombre del producto: ")

#solicitud del valor del producto especifico
flag_valor = True
while flag_valor:
    try:
        producto["valor"] = int(input("Ingrese el precio del producto: "))
        if producto["valor"] <= 0:
            raise ValueError
        else:
            flag_valor = False

    except ValueError:
        print("Ingrese valores numericos positivos")

#solicitud del stock del producto especifico
flag_stock = True
while flag_stock:
    try:
        producto["stock"] = int("Ingrese el stock del producto: ")
        if producto["stock"] < 0:
            raise ValueError
        else:
            flag_stock = False
    except ValueError:
        print("Ingrese valores numericos positivos")
        if producto["stock"] == 0:
                producto["disponibilidad"] = "No"
        else:
                producto["disponibilidad"] = "Si"
        #forma "mas corta" para agregar valores directos a un diccionario o se aplica una "misma" consecuencia
        """producto["disponibilidad"]="No disponible" if producto["stock"] < 0 else producto["disponibilidad"] = "Disponible"""" 

#forma generica
        

for llave, value in producto.items():
    print(f"{llave.capitalize()}: {value}")
    