try:
    
    num = int(input("Ingrese un número entero: "))
    
    while num < 1:
        num = int(input("Ingrese un número entero: "))
    
    if num == 1:
        print("El número 1 no es primo")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(f"El número {num} no es primo")
                break
        else:
            print(f"El número {num} es primo")
    
    
except Exception as e:
    print(f"An error occurred: {e}")