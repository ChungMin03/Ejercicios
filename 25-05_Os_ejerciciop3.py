"""
Prueba 3 Osvaldo Ruiz
requisito 1:
el sistema deberá:
- calsificar ingenieros según su nivel tecnico
- contabilizar caintos ingenieros son Senior y cuantos son junior
- mostrar un resumen al finalizar
Requisisto 2
el programa deberá preguntar cuantos ingenieros desea ingresar
- este valor debe ser un numero entero positivo
- si el ususario ingresa un valor invalido debe mostrar el siguiente mensaje hasta recicir una entrada incorrecta:
"¡dato inválido! Ingresa un entero positivo para continuar con el registro"
Requisito 3
nombre tecnico
- Debe tener al menos 6 caracteres
No debe incluir espacios
nivel tecnico
- el usuario debe ingresar el nivel del ingeniero(entero positivo)
- si si engresa un valor incorrecto, se mostrará el siguiente mensaje:
"¡Error de validacion! Ingresa un número entero positivo para el nivel tecnico"
Requisito 4
dependiendo del nivel ingresado:
- si el nivel es mayor a 45, el ingeniero será un ingeniero Senior
- si el nivel es menor o igual a 45, será un ingeniero junior
Requisito 5
el programa debe llevar un conteo durante el registro de:
-numero total de ingenieros junior
-numero total de ingenieros senio
Requisito 6
Al finalizar el registro, el programa mostrará un resumen con el total de ingenieros registrados
por ejemplo:
¡El instituto cuenta con x ingenieros Senior y z ingenieros Junior! ¡Registro completado satisfactoriamente! """
#requisito 1
junior = 0
senior = 0
#requisito 2
flag_cant = False
while not flag_cant:
    try:
#-----------------bloque de inputs y variables----------------------
        cant = int(input("Ingrese la cantidad de registros que se harán: "))
        if cant < 1:
            raise ValueError
        else:
            flag_cant = True
    except ValueError:
        print("¡dato inválido! Ingresa un entero positivo para continuar con el registro")
#-----------
#requisito 3
for i in range(1,(cant+1)):
    flag_tecnico = False
    while not flag_tecnico:
        try:
            nombre = input(f"Ingrese el nombre tecnico N°{i}: ")
            if len(nombre) < 6 or " " in nombre:
                print("El nombre debe tener al menos 6 caracteres, sin espacios")
                continue
            nivel = int(input(f"Ingrese el nivel tecnico del ingeniero N°{i}: "))
            if nivel < 1:
                raise ValueError
            else:
            #Requisitos 4 y 5
                if nivel <= 45:
                    junior += 1
                elif nivel > 45:
                    senior += 1
                flag_tecnico = True
        except ValueError:
            print("¡Error de validacion! Ingresa un número entero positivo para el nivel tecnico")
#Requisito 6
print(f"¡El instituto cuenta con {senior} ingenieros Senior y {junior} ingenieros Junior! ¡Registro completado satisfactoriamente!")