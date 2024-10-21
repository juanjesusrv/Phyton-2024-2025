try:
    hora = int(input("Introduce la hora: "))
    
    while hora < 0 or hora > 23:
        hora = int(input("Error. Introduce la hora: "))
        
    if hora >= 6 and hora <= 12:
        print("Buenos dias")
    elif hora >= 13 and hora <= 20:
        print("Buenas tardes")
    else:
        print("Buenas noches")
    
except Exception as e:
    print(f"An error occurred: {e}")