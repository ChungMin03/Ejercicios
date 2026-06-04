##Una tienda necesita registrar datos de un producto indicado por el usuario.
##El programa debe solicitar el nombre del producto, su precio y su stock disponible y mostrar un 
##resumen con todos sus datos.


##----------------------------INICIALIZACIÓN DE LISTAS/DICCIONARIOS/VARIABLES--------------------------##

producto={}

##---------------------------------------------ENTRADA------------------------------------##

while True:
    try:
        producto["nombre"]=input("Ingrese el nombre del producto: \n").title()
        print("")
        break

    except ValueError:
        print("Error. Caracter inválido")

while True:
    try:
        producto["precio"]=int(input("Ingrese el valor del producto: \n"))
        print("")
        
        if producto["precio"]<=0:
            print("Error. El precio no puede ser negativo")

        else:
            break
    
    except ValueError:
        print("Error. Ingrese un número entero")

while True:
    try:
        producto["stock"]=int(input("Ingrese el stock disponible para el producto \n"))
        print("")
        
        if producto["stock"]<0:
            print("Error. El precio no puede ser negativo")

        else:
            break

    except ValueError:
        print("Error. Ingrese un número entero")

##--------------------------------PROCESO----------------------------------##

producto["estado"]="Disponible" if producto["stock"]>0 else "Agotado"

##--------------------------------------SALIDA------------------------------------##

print("**********************************")
print("-------RESUMEN DEL PRODUCTO-------")
print("**********************************")
print("")
for llave, valor in producto.items(): 
    
    print(f"{llave.title()}: {valor}")


