try:
    
    num = int(input("Entroduce un numero entre 0 y 99999: "))
    
    while num < 0 or num > 99999:
        print("El numero introducido no es valido.")
        num = int(input("Entroduce un numero entre 0 y 99999: "))
        
        
    print(f"El numero {num} tiene {len(str(num))} digitos")
    
except Exception as e:
    print(f"An error occurred: {e}")