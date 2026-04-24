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
