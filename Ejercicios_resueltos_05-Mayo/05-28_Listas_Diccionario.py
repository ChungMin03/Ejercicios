#TIPOS DE DATOS COMPUESTOS
#Listas y Diccionarios

#Para declarar una lista usaremos la siguiente sentencia:
nombrelista = [] #Los brackets indican que es de tipo lista

milista = [1,2,3,4,5] #Lista con 5 elementos separados por comas
lista_nombres = ["carlos", "nico", "Javi", "Oswald"] #Strings deben estar entre comillas

#PAra consultar elementos de una lista, podemos utilizar sentencias print, o sentencia For o While

#Bucle for para mostrar cada elemento de la lista
for elemento in milista:
    print(elemento)

#Usando print para mostrar solo un elemento de la lista -> nombreLista[posicionElemento]
print(lista_nombres[0])

#Insertar elementos 
#Para ingresar elementos a una lista, debemos utilizar funciones de lista, por ahora usaremos append()
milista.append(6)
for elemento in milista:
    print(elemento)

#Para ingresar un elemento en una posicion exacta, debemos utilizar la funcion insert(posicion, elemento)
milista.insert(2, 10)
print(milista)

#La funcion remove, elimina un elemento, como argumento requiere que se indique el elemento que desea eliminar.
#Busca y elimina la coincidencia del elemento ingresado, en caso de no encontrar coincidencia emite un mensaje de error
milista.remove(10)
print(milista)

#Funcion sort ordena los elementos de una lista
lista_desordenada = [53,4354,1,43,87,2,99,984389432]
print(lista_desordenada)
lista_desordenada.sort()
print(lista_desordenada)

#Eliminar todas las coincidencias de una lista
lista_repeticion = [1,2,1,1,1,1]
while 1 in lista_repeticion:
    lista_repeticion.remove(1)
print(lista_repeticion)

#Diccionarios

diccionario = {
    "nombre" : "Cesar Huispe",
    "fonos" : [987654321,
               987123456
               ],
    "activo" : True
}

#mostrar elemento del diccionario
print(diccionario["nombre"])
print(f"Segundo fono: {diccionario['fonos'][1]}")

#Insertar elemento a un diccionario
diccionario["email"] = "cesar.huispe@gmail.com"
diccionario["fonos"].append(123456789)

#actualizar elementos del diccionario
diccionario["activo"] = False
diccionario["fonos"][1] = 999999999999

#eliminar elementos del diccionario
del diccionario["activo"]
print(diccionario["fonos"])
diccionario["fonos"].pop(1)
print(diccionario["fonos"])
diccionario["fonos"].remove(987654321)

print(diccionario)