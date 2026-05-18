"""Practica de definicion de funciones
 y dejar funcione definidas por si acaso
   o para practicar con ellas :)"""


def sum_arg(a,b):
    result1 = a + b
    return result1

def suma():
    a = int("Ingrese un numero a")
    b = int("Ingrese un numero b")
    result2 = a + b
    return result2

def suma_indef():
    flag1 = False
    while not flag1:
        try:
            num = float(input("Ingrese numeros a sumar, para detener ingrese alo gue no sean numeros: "))
            result3 += num
        except ValueError:
            return result3

def res_targ(a,b):
    result4 = a - b
    return result4

def resta():
    a = int("Ingrese un numero a")
    b = int("Ingrese un numero b")
    result5 = a - b
    return result5

def multipic_arg(a,b):
    result6 = a * b
    return result6 

def multipicacion():
    a = int("Ingrese un numero a")
    b = int("Ingrese un numero b")
    result7 = a * b
    return result7

def divid_irg(a,b):
    result8 = a / b
    return result8

def division():
    a = int("Ingrese un numero a")
    b = int("Ingrese un numero b")
    result9 = a / b
    return result9

def promedio():
    flag = False
    count = 0
    total = 0
    while not flag:
        try:
            value = float(input("Ingrese valores a promediar, para detener ingrese algo que no sean numeros: "))
            count += 1
            total += value
            result10 = total/count
        except ValueError:
            return result10, count


