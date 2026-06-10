"""
Una clinica veterinaria desea que su sistema de atencion siempre muestra el mismo mensaje de bienvenida
"""

def saludo():
    print("-----------Perritos bonitos--------------")
    print("Atención 09:00 - 21:00")
    print("Bienvenido a nuestra clinica veterinaria")



def gym_nombre():
    a = input("Ingrese su nombre: ")
    return a

nombre = gym_nombre()

print(f"Hola {nombre}")


