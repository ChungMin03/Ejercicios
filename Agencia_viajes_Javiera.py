'''
Desafío 2: Agencia de Viajes a Medida
Crea un programa que calcule el costo de un paquete turístico. Solicite: 
-   Destino ("Caribe" o "Europa") .
-   Cantidad de personas. 
-   Si incluye "Todo Incluido" (si/no).

Precios Base:
-   Caribe: $800.000 por persona. Si son más de 4 personas, el precio baja a $720.000 por persona.
-   Europa: $1.200.000 por persona. (No hay descuento por grupo).
-   Servicios Extra: * Si elige "Todo Incluido" en el Caribe, sumar 15% al total.
-   Si elige "Todo Incluido" en Europa, sumar $250.000 fijos por persona.

Regla Especial: Si el destino es "Caribe" y el total supera los $3.000.000, aplicar un descuento final del 5% sobre el total 
acumulado.

Objetivo: Mostrar el desglose: Destino (mayúsculas), cantidad de letras del destino, precio por persona, costo total sin descuento
y costo total final con impuestos/descuentos aplicados.
'''
# ----------------- Bloque de variables -----------------
destino = input("Ingrese el destino (Caribe/Europa): ").lower()
cantidad_personas = int(input("Ingrese la cantidad de personas: "))
todo_incluido = input("¿Incluye Todo Incluido? (si/no): ").lower()

# ----------------- Bloque de ejecución -----------------


# Cálculo del costo total según si el destino es el caribe.
if destino == "caribe":
    if cantidad_personas > 4:
        precio_por_persona = 720000
    else:
        precio_por_persona = 800000
    
    costo_total = precio_por_persona * cantidad_personas

    # Cálculo del costo total con el servicio de todo incluido.
    if todo_incluido == "si":
        costo_total_todo_incluido = (costo_total * 0.15) + costo_total
    else: 
        costo_total_todo_incluido = costo_total

    # Cálculo del costo total final con el descuento especial.
    if costo_total_todo_incluido > 3000000:
        costo_total_final = costo_total_todo_incluido * 0.95
    else:
        costo_total_final = costo_total_todo_incluido


# Cálculo del costo total según si el destino es europa.
elif destino == "europa":
    precio_por_persona = 1200000
    costo_total = precio_por_persona * cantidad_personas

    # Cálculo del costo total con el servicio de todo incluido.
    if todo_incluido == "si":
        precio_por_persona = precio_por_persona + 250000
        costo_total_todo_incluido = precio_por_persona * cantidad_personas
    else:
        costo_total_todo_incluido = costo_total

else:
    print("Destino no válido")
    precio_por_persona = 0
    costo_total = 0
    costo_total_final = 0


# Desglose final de la información solicitada.
print("")
print("")
print(f"Destino: {destino.upper()}")
print(f"Cantidad de letras del destino: {len(destino)}")
print(f"Precio por persona: ${precio_por_persona:,}")
print(f"Costo total con todo incluido: ${costo_total_todo_incluido:,}")

if destino == "caribe" and costo_total_todo_incluido > 3000000:
    print(f"Costo total final con descuento aplicado: ${costo_total_final:,}")