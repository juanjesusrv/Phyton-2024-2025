try:
    
    figura = input("Introduce la figura geométrica (cuadrado, rectangulo, circulo o triangulo): ")
    
    while figura != "cuadrado" and figura != "rectángulo" and figura != "círculo" and figura != "triangulo":
        print("La figura introducida no es valida.")
        figura = input("Introduce la figura geométrica (cuadrado, rectangulo, circulo o triangulo): ")
        
    if figura == "cuadrado":
        
        lado = float(input("Introduce el lado del cuadrado: "))
        
        while lado < 0:
            print("El lado introducido no es valido.")
            lado = float(input("Introduce el lado del cuadrado: "))
                        
        area = lado * lado
        print(f"El área del cuadrado es {area}")
        
    elif figura == "rectángulo":
        
        base = float(input("Introduce la base del rectángulo: "))
        
        while base < 0:
            print("La base introducida no es valida.")
            base = float(input("Introduce la base del rectángulo: "))
        
        altura = float(input("Introduce la altura del rectángulo: "))
        
        while altura < 0:
            print("La altura introducida no es valida.")
            altura = float(input("Introduce la altura del rectángulo: "))
            
        area = base * altura
        print(f"El área del rectángulo es {area}")
        
    elif figura == "círculo":
        
        radio = float(input("Introduce el radio del círculo: "))
        
        while radio < 0:
            print("El radio introducido no es valido.")
            radio = float(input("Introduce el radio del círculo: "))
        
        
        area = 3.1416 * radio * radio
        print(f"El área del círculo es {area}")
        
    else:
        
        base = float(input("Introduce la base del triángulo: "))
        
        while base < 0:
            print("La base introducida no es valida.")
            base = float(input("Introduce la base del triángulo: "))
        
        
        altura = float(input("Introduce la altura del triángulo: "))
        
        while altura < 0:
            print("La altura introducida no es valida.")
            altura = float(input("Introduce la altura del triángulo: "))
        
        area = base * altura / 2
        print(f"El área del triángulo es {area}")
    
except Exception as e:
    print(f"An error occurred: {e}")


#Escribir un programa que sea capaz de calcular el área de un cuadrado,
#rectángulo, círculo o triángulo. Primero debemos pedir qué figura geométrica usaremos y, en
#función de la figura, pediremos los datos necesarios para calcular su área