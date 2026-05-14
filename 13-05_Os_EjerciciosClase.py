"""Ingresar un numero n. el programa tiene que contar cuantos pares hay desde 1 hasta ese numero n"""

"""
#ejercicio con "for"
#----------------Bloque de inputs y variables------------------------------------------
num = int(input("Ingrese el Numero hasta el que quiere contar los pares: "))
par = 0

#-----------------Bloque de ejecutables------------------------------------------------

for contador in range(1,(num + 1)):
    resto = contador % 2                #Revisando que numeros son pares
    if resto == 0:
        par += 1

#----------------Bloque de prints----------------------------------------------------

print(f"La cantidad de pares hasta {num} es {par}")"""



#ejercicio con while
#------------------------------Bloque de variables----------------------------------

"""num = int(input("Ingrese el Numero hasta el que quiere contar los pares: "))
even = 0
count = 0

#------------------------------Bloque de ejecutables

while count != num:
    count += 1
    resto = count % 2
    if resto == 0:
        even += 1



print(f"La cantidad de pares es de {even} hasta numero {num}")"""


"""crear un programa con un menu con 4 opciones. 1 sumar 2 restar 3 multiplicar 4 salir,
el programa muestra el menu, el usuario elige, ingresa 2 numerps y se muestra el resultado.
el ciclo se repite hasta que se elija salir"""


resta = 0
suma = 0
mult = 1
option = 0
while option != 5:

    #Menu
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Division")
    print("5.- Salir")

#opciones del menu
    option = int(input("Ingrese a opcion que desea usar: "))

    #suma
    if option == 1:

        cant1 = int(input("Ingrese la cantidad de numeros que desea sumar: "))

        for i in range(1,(cant1+1)):
            num1 = float(input("Ingrese el valor a sumar"))
            suma += num1

        print(f"El total de los {cant1} numeros sumados fue: {suma}")

    #resta
    elif option == 2:

        cant2 = int(input("Ingrese la cantidad de numeros que desea restar: "))

        for i in range(1,((cant2+1))):
            num2 = float(input("Ingrese el valor a restar"))
            abs.resta -= num2
            
        print(f"El total de los {cant2} numeros restados fue: {resta}")

    #Multiplicacion
    elif option == 3:

        cant3 = int(input("Ingrese la cantidad de numeros que desea multiplicar: "))

        for i in range(1,(cant3+1)):
            num3 = float(input("Ingrese el valor a restar"))
            mult *= num3
            
        print(f"El total de los {cant3} numeros multiplcados fue: {mult}")
    

    #Division
    elif option == 4:

        num4 = float(input("Ingrese el dividendo: "))
        num5 = float(input("Ingrese el divisor: "))

        if num5 == 0:
            print("Divisor invalido")

        else:
            div = num4/num5
            print(f"El resultado de la division es: {div}")


    #opcion final
    elif option == 5:

        print("Gragias por usar nuestra calculadora")

    #Opcion en caso de error
    else:
        print("Opcion invalida, vuelva a tratar con alguno de las opciones")