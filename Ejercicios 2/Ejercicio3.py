try:
    a = str(input("Introduce un caracter: "))
    
    while len(a) < 1 or len(a) > 1 or not a.isalpha():
        a = str(input("Introduce un caracter: "))
    
    if a.lower() != a:
        print("El caracter introducido es una letra mayuscula")
    else:
        print("El caracter introducido es una letra minuscula")
        
        
except Exception as e:
    print(f"An error occurred: {e}")