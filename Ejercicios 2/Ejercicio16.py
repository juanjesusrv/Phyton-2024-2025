try:
    
    nota = int(input("Introduce una nota de 0 a 10: "))
    
    if nota < 5:
        print("Insuficiente")
    elif nota < 6:
        print("Suficiente")
    elif nota < 7:
        print("Bien")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")
    
except Exception as e:
    print(f"An error occurred: {e}")



#Pedir una nota de 0 a 10 y mostrar su equivalente alfabético: Insuficiente,
#Suficiente, etc…