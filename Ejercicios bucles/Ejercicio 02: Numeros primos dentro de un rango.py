try:
    
    print("Introduce un rango de números para saber cuáles son primos")
    num_inferior = int(input("Introduce el número inferior del rango: "))
    
    while num_inferior < 1:
        num_inferior = int(input("Introduce el número inferior del rango: "))
    
    num_superior = int(input("Introduce el número superior del rango: "))
    
    while num_superior < num_inferior:
        num_superior = int(input("Introduce el número superior del rango: "))
        
    numeros = []
        
        
    for num in range(num_inferior, num_superior + 1):
        if num == 1:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            numeros.append(num)
    
    print(f"Los números primos en el rango de {num_inferior} a {num_superior} son: {numeros}")
    
    
except Exception as e:
    print(f"An error occurred: {e}")