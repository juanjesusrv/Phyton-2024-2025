try:
    
    a = int(input("Introduce el primer numero: "))
    b = int(input("Introduce el segundo numero: "))
    c = int(input("Introduce el tercer numero: "))
    
    
    if a > b and a > c:
        primero = a
        if b > c:
            segundo = b
            tercero = c
        else:
            segundo = c
            tercero = b
            
    elif b > a and b > c:
        primero = b
        if a > c:
            segundo = a
            tercero = c
        else:
            segundo = c
            tercero = a
            
    else:
        primero = c
        if a > b:
            segundo = a
            tercero = b
        else:
            segundo = b
            tercero = a
    
    
    print(f"{primero},{segundo},{tercero}")
    
except Exception as e:
    print(f"An error occurred: {e}")