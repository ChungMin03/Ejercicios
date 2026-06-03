##El usuario ingresa 10 números enteros que se almacenan en una lista.
##Al finalizar el programa debe mostrar:
##Cuántos números pares contiene la lista
##Cuántos números impares contiene la lista
##La suma total de los pares
##La suma total de los impares

##--------------------------INICIALIZACIÓN DE LISTAS/VARIABLES----------------------------------##

numeros=[]
flag1=False
cant_pares=0
cant_impares=0
suma_pares=0
suma_impares=0

##----------------------------------ENTRADA-----------------------------------##

for i in range(10):
    flag1=False
    while not flag1:
        
        try:
            num=int(input("Ingrese el número \n"))
            print("")
            numeros.append(num)
            flag1=True

        except ValueError:
            print("Error. Dijite un número entero")

##-----------------------------PROECESO------------------------------##

for i in range(10):
    if numeros[i]%2==0:
        cant_pares+=1
        suma_pares+=numeros[i]
    
    else:
        cant_impares+=1
        suma_impares+=numeros[i]

##----------------------------------SALIDA----------------------------##

print(f"La cantidad de números pares es: {cant_pares}")
print(f"La cantidad de números impares es: {cant_impares}")
print(f"La suma de los números pares es: {suma_pares}")
print(f"La suma de los números impares es: {suma_impares}")


