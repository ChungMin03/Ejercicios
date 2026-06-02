"""
3. Control de Gasto Mensual (Ciclo while SIN break/continue)
Crea un programa que ayude a una persona a no pasarse de su presupuesto.

Solicita el presupuesto máximo del mes.

Pide el nombre del gasto y su valor de forma sucesiva.

Condición: El ciclo debe detenerse únicamente cuando la suma de los gastos sea mayor o igual al presupuesto máximo, usando solo la condición del while.

Muestra cuánto se pasó del presupuesto original.
"""

print("**** Control de Gasto Mensual ****")
presupuesto_mensual = int(input("Ingrese su presupuesto maximo del mes: "))
count_gastos = 0

while count_gastos <= presupuesto_mensual:
    nombre_gasto = input("Ingrese el nombre del gasto: ")
    gasto = int(input("Ingrese el monto del gasto: "))
    count_gastos += gasto

print(f"Hey, te pasaste por ${count_gastos - presupuesto_mensual}")