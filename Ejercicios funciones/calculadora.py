def calculadora():
    mostrar_menu()
    opcion = int(input("Introduce una opción: "))
    while opcion < 1 or opcion > 5:
        print("  ")
        print("Opción incorrecta")
        opcion = int(input("Introduce una opción válida: "))
        
    
    while opcion != 5:
        print("  ")
        num1 = input("Introduce el primer número: ")
        num2 = input("Introduce el segundo número: ")
        
        if num1.isdigit() and num2.isdigit():
            num1 = float(num1)
            num2 = float(num2)
        
        if opcion == 1:
            sumar(num1, num2)
        elif opcion == 2:
            restar(num1, num2)
        elif opcion == 3:
            multiplicar(num1, num2)
        elif opcion == 4:
            dividir(num1, num2)
        
        print("  ")
        
        mostrar_menu()
        opcion = int(input("Introduce una opción: "))
        while opcion < 1 or opcion > 5:
            print("  ")
            print("Opción incorrecta")
            opcion = int(input("Introduce una opción válida: "))
    
    
    print("Fin de la calculadora")
    
    

def mostrar_menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
def sumar(num1, num2):
    print("Resultado: ", num1 + num2)
def restar(num1, num2):
    print("Resultado: ", num1 - num2)
def multiplicar(num1, num2):
    print("Resultado: ", num1 * num2)
def dividir(num1, num2):
    if num2 == 0:
        print("No se puede dividir por 0")
    else:
        print("Resultado: ", num1 / num2)
try:
    calculadora()
except:
    print("Error. La calculadora se ha cerrado")