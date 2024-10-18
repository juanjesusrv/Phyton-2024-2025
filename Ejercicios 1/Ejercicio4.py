try:
    print("ANÁLISIS DE UN NÚMERO")
    print("---------------------")
    num = input("Introduce un numero entero: ")
    print("RESULTADO")
    print("---------")
    
    num = int(num)

    print("El numero es par:", num % 2 == 0)
    print("El numero es menor que 100:", num < 100)
    print("El numero es positivo:", num > 0)
    print("El numero es cero:", num ==0)

except:
    print("Eso ta mal manito")