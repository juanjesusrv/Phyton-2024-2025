try:
    nombre = input("Introduce el nombre: ")

    primerAp = input("Introduce el primer apellido: ")

    segundoAp = input("Introduce el segundo apellido: ")

    if ("ñ" in nombre.lower() or "ñ" in primerAp.lower() or "ñ" in segundoAp.lower() or
        "á" in nombre.lower() or "á" in primerAp.lower() or "á" in segundoAp.lower() or
        "é" in nombre.lower() or "é" in primerAp.lower() or "é" in segundoAp.lower() or
        "í" in nombre.lower() or "í" in primerAp.lower() or "í" in segundoAp.lower() or
        "ó" in nombre.lower() or "ó" in primerAp.lower() or "ó" in segundoAp.lower() or
        "ú" in nombre.lower() or "ú" in primerAp.lower() or "ú" in segundoAp.lower()):
                            valido = False  
    else :
        valido = True
         
    if valido:
        if (len(primerAp) != len(segundoAp) or 
           nombre[0].lower() != nombre[-1].lower() or 
           nombre[0].upper() != nombre[0] or 
           primerAp[0].upper() != primerAp[0] or 
           segundoAp[0].upper() != segundoAp[0] or 
           any(char.isdigit() for char in nombre) or 
           any(char.isdigit() for char in primerAp) or 
           any(char.isdigit() for char in segundoAp)):  
            valido = False
        else:
            valido = True

              
    if valido:
        print(nombre, primerAp, segundoAp, ". La persona es APTA para el concurso")
    else:
        print(nombre, primerAp, segundoAp, ". La persona NO es APTA para el concurso")
        
except:
    print("Eso ta mal manito")
    

