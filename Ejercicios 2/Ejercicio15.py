try:
    
    operacion = input("Ingrese la operación a realizar (S, R, D, M): ")
  
    while operacion != "S" and operacion != "s" and operacion != "R" and operacion != "r" and operacion != "D" and operacion != "d" and operacion != "M" and operacion != "m":
      print("La operación introducida no es valida.")
      operacion = input("Ingrese la operación a realizar (S, R, D, M): ")  
    
    
    num1 = int(input("Introduce el primer número: "))
    
    while num1 < 0:
        print("El número introducido no es valido.")
        num1 = int(input("Introduce el primer número: "))
        
    num2 = int(input("Introduce el segundo número: "))
    
    while num2 < 0:
        print("El número introducido no es valido.")
        num2 = int(input("Introduce el segundo número: "))
        
    if operacion == "S" or operacion == "s":
        resultado = num1 + num2
        print(f"El resultado de la suma es {resultado}")
    elif operacion == "R" or operacion == "r":
        resultado = num1 - num2
        print(f"El resultado de la resta es {resultado}")
    elif operacion == "D" or operacion == "d":
        resultado = num1 / num2
        print(f"El resultado de la división es {resultado}")
    else:
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es {resultado}")
    
    
except Exception as e:
    print(f"An error occurred: {e}")



#Construir un programa que simule el funcionamiento de una calculadora que
#puede realizar las cuatro operaciones aritméticas básicas (suma, resta, producto y división) con
#valores numéricos enteros. El usuario debe especificar la operación con el primer carácter del
#primer parámetro de la línea de comandos: S o s para la suma, R o r para la resta, D o d para la
#división y M o m para la multiplicación.