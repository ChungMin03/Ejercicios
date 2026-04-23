grade1 = float(input("Ingrese su primera nota: "))
grade2 = float(input("Ingrese su segunda nota: "))
grade3 = float(input("Ingrese su tercera nota: "))

ntotal = (grade1 * 0.3) + (grade2 * 0.3) + (grade3 * 0.4)
if ntotal >=6.0:
    print(f"Aprobó con distincioón, su nota es: {ntotal:.2f}")
elif ntotal < 6.0 and ntotal >= 4.0:
    print(f"Aprobó, su nota es: {ntotal:.2f}")
elif ntotal < 4.0:
    print(f"Reprobó, su nota es: {ntotal:.2f}")
else:
    print("Valor invalido") 