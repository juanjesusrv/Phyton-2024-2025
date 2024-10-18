try:
    
    a = int(input("¿Cuanto has gastado en la compra?: "))
    
    if a > 300:
        print("Tienes un descuento del 20%")
        print(f"El total de la compra es: {a - (a * 0.20)}")
    else:
        print("No tienes descuento")
        print(f"El total de la compra es: {a}")
    
except Exception as e:
    print(f"An error occurred: {e}")