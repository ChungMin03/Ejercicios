#FUNCION PARA SUMAR
def suma(num1, num2):
    resultado = num1 + num2
    return resultado
#FUNCION PARA RESTAR
def resta():
    a = int(input("Ingrese el numero a"))
    b = int(input("Ingrese el numero b"))
    resultado = a - b
    return resultado
#FUNCION PARA SUMAR INDEFINIDAMENTE
def suma_indefinida():
    flag = False
    acum = 0
    count = 0
    while not flag:
        try:
            num = int(input("Ingrese un numero culiao (para detenerse escriba):"))
            acum += num
            count += 1
        except ValueError:
            print("Suma indefinida terminada")
            flag = True
    return acum, count

def mult():
    a = float(input("Ingrese el numero a:"))
    b = float(input("Ingrese el numero b:"))
    resultado = a * b
    return resultado

"""
opcion = 0
opcion_valida = False
while opcion != 4:
    print("**** CALCULADORA ****")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Salir")
    print("----------------------------------")
    
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        num1 = float(input("Ingrese un numero 1: "))
        num2 = float(input("Ingrese un numero 2: "))
        sumasion = suma(num1,num2)
        print(f"El resultado de la suma es: {sumasion}")
        
    elif opcion == 2:
        restasion = resta()
        print(f"El resultado de la resta es: {restasion}")
        
    elif opcion == 3:
        multiplicasion = mult()
        print(f"El resultado de la multiplicacion es: {multiplicasion}")
        
    elif opcion == 4:
        print("Gracias por usar esta calculadora con funciones hechas por mis amigos xd")
        
    else:
        print("Ingresasteuna wea na q ver sipoe")
"""

lista_notas = []
flag = False

"""while not flag:
    try:
        num = float(input("Ingrese una nota culia (para detenerse escriba):"))
        lista_notas.append(num)
    except ValueError:
        print("Lista terminada")
        flag = True
        
#print(max(lista_notas))
"""

lista = [2,4,5,1,2,3,4,5]
lst = [i for i in lista if i%2==0 and i > 2]
print(lst)

lst2 = []
for i in lista:
    if i % 2 == 0:
        lst2.append(i)
print(lst2)