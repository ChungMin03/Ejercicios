



#variables-----------------------------------------------------------------------------------------------
name = input("Ingrese su nombre\n")
lvl = input("Nivel de inglés que posee: (Avanzado, Intermedio, Basico)\n").lower()
years = int(input("Ingrese los años que tiene de experiencia: "))
disp = input("Posee disponbilidad para viajar? (Si/No)\n").lower()

#Ejecicion-----------------------------------------------------------------------------------------------
postulante = ""
if lvl != "avanzado" or lvl != "intermedio" or lvl != "basico":
    print("Nivel de inglés indeterminado")
    postulante = ""
    if disp != "si" and disp != "no":
        print("Disponibilidad para viajar indeterminada")
        postulante = ""
    elif years >= 5 and lvl == "avanzado":
        postulante = "Postulante destacado - pasa a segunda fase"
    elif years < 5 and years >= 3 and lvl == ("avanzado" or "intermedio"):
        postulante = "Postulante APTO - Pasa a 2da fase"
    elif disp == "si" and years >= 1:
        postulante = "Postulante EN REVISION"
    else:
        postulante = "Postulante NO CUMPLE los requisitos"


#Prints de la ejecucion---------------------------------------------------------------------------------
if postulante != "":
    print(f"Nombre: {name.upper()}")
    print(f"Largo de nombre: {len(name)}")
    print(postulante)


