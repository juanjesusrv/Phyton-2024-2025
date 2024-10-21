try:
    dia = int(input("Introduce un día: "))
    
    while dia < 1 or dia > 31:
        dia = int(input("Error. Introduce un día: "))
        
    mes = int(input("Introduce un mes: "))
    
    while mes < 1 or mes > 12:
        mes = int(input("Error. Introduce un mes: "))
        
    if (mes == 3 and dia >= 21) or (mes == 4  and dia <= 19):
        print("Eres Aries")
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        print("Eres Tauro")
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        print("Eres Géminis")
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        print("Eres Cáncer")
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        print("Eres Leo")
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        print("Eres Virgo")
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        print("Eres Libra")
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        print("Eres Escorpio")
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        print("Eres Sagitario")
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        print("Eres Capricornio")
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        print("Eres Acuario")
    else:
        print("Eres Piscis")
    
except Exception as e:
    print(f"An error occurred: {e}")