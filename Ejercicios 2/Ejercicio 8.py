try:
    
    a = int(input("Introduce un numero: "))
    b = int(input("Introduce otro numero: "))
    
    
    if a % 2 == 0:
        print(f"El numero {a} es par")
    else:
        print(f"El numero {a} es impar")
        
    if b % 2 == 0:
        print(f"El numero {b} es par")
    else:
        print(f"El numero {b} es impar")
        
except Exception as e:
    print(f"An error occurred: {e}")