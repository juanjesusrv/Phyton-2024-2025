try:
    a = int(input("Introduce un numero entero: "))
    
    if a % 10 ==  0:
        print("El numero es multiplo de 10")  
    else: 
        print("El numero no es multiplo de 10")     
        
except Exception as e:
    print(f"An error occurred: {e}")