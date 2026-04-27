"""
Enunciado
Una empresa importadora necesita clasificar sus productos. Solicite el nombre del producto (string), 
su precio en dólares (float) y el país de origen. El programa debe:
-Mostrar el nombre del producto en mayúsculas y sin espacios extremos.

-Calcular el precio en pesos chilenos. Si el país de origen es "USA" o "Canada", el tipo de cambio es 
$980 por dólar; si es "Europa" el tipo de cambio es $1050; para cualquier otro país, el tipo de cambio es $920.

-Clasificar el producto por precio en dólares: si es < 50 -> "Económico"; si está entre 50 y 200 -> "Estándar"; 
si es $> 200$ -> "Premium".

-Si el producto es "Premium" y el país es "USA" o "Canada", agregar un recargo de 5% por arancel. Mostrar el precio final en pesos con y sin arancel si corresponde.

"""
product = input("Ingrese el nombre del producto: ")
usd_price = float(input("Ingrese el valor del producto en dolares: "))
country = input("Ingrese el país de origen del procutos: ").lower()

if country == "usa" or country == "canada":
    cl_price = 980 * usd_price
elif country == "europa":
    cl_price = 1050 * usd_price
else:
    cl_price = 920 * usd_price

if usd_price < 50:
    product_type = "economico"
elif usd_price >= 50 and usd_price <= 200:
    product_type = "estandar"
else: product_type = "premium"

if product_type == "premium" and (country == "usa" or country == "canada"):
    arancel = 5

print(product.upper().strip())
if arancel == 5:
    print(f"El precio de su producto sin arancel es: {cl_price}")
    print(f"El precio de su producto con arancel es: {cl_price * 1.05}")
elif arancel != 5:
    print(f"El precio de su producto es: {cl_price}")