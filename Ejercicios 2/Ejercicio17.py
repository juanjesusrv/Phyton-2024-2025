try:

    peso = int(input("Introduce un peso en kg: "))
    
    while peso < 0:
        print("El peso introducido no es valido.")
        peso = int(input("Introduce un peso en kg: "))
        
    print(f"1. Hectogramos: {peso * 10}")
    print(f"2. Decagramos: {peso * 100}")
    print(f"3. Gramos: {peso * 1000}")
    print(f"4. Decigramos: {peso * 10000}")
    print(f"5. Centigramos: {peso * 100000}")
    print(f"6. Miligramos: {peso * 1000000}")
    

    


except Exception as e:
    print(f"An error occurred: {e}")


#Hacer un programa que pase de kg a otra unidad de medida de masa. Mostrar en
#pantalla un menú con las opciones posibles (hectogramos, decagramos…miligramos).