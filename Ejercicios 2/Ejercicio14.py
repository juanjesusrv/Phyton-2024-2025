try:
    
    dia = int(input("Introduce el dia: "))
    
    while dia < 1 or dia > 31:
        print("El dia introducido no es valido.")
        dia = int(input("Introduce el dia: "))
        
    mes = int(input("Introduce el mes: "))
    
    while mes < 1 or mes > 12:
        print("El mes introducido no es valido.")
        mes = int(input("Introduce el mes: "))
        
    anio = int(input("Introduce el año: "))
    
    while anio < 1:
        print("El año introducido no es valido.")
        anio = int(input("Introduce el año: "))
        
        
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0 and anio % 100 == 0 and anio % 4 == 0): 
            if dia > 29:
                print("La fecha introducida no es valida.")
            else:
                print("La fecha introducida es valida.")
        else:
            if dia > 28:
                print("La fecha introducida no es valida.")
            else:
                print("La fecha introducida es valida.")
    
    
except Exception as e:
    print(f"An error occurred: {e}")
    
    
#Hacer lo mismo que el ejercicio anterior pero teniendo en cuenta los años
#bisiestos (dónde febrero tiene 29 días).    