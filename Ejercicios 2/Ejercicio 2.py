try:
    a = int(input("Introduce un numero: "))
    b = int(input("Introduce otro numero: "))
    
    
    
    if a == b:
        print("Los numeros son iguales")
    elif a > b:
        print(f"El numero {a} es mayor que el numero {b}")
    else:
        print(f"El numero {b} es mayor que el numero {a}")
        
except Exception as e:
    print(f"An error occurred: {e}")