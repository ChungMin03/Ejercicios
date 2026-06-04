#caracterizticas de los diccionarios:

#definimos un diccionario ejemplo, en este caso personal es nuestro diccionario ejemplo
#donde nombre = clave y victor el valor
personal={
    "nombre" : "victor"
}


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
    print(f"{llave} <--> {valor}")