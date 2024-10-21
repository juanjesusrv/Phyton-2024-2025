try:
    
    numeros = int(input("Cuantos numeros de Fibonacci quieres sacar: "))
    
    while numeros < 1:
        numeros = int(input("Error. Cuantos numeros de Fibonacci quieres sacar: "))
        
        
    auxA = 0
    auxB = 1
    serie = []
        
    for i in range(numeros):
        serie.append(auxA)
        auxA, auxB = auxB, auxA + auxB 
        
    print(f"Serie de Fibonacci: {serie}")
    
except Exception as e:
    print(f"An error occurred: {e}")
    