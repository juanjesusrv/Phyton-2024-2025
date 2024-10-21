try:
    
    horas = int(input("Introduce las horas trabajadas: "))
    
    if horas <= 40:
        salario = horas * 16
    else:
        salario = 40 * 16 + (horas - 40) * 20
        
    print(f"El salario es de {salario} euros")
    
    
except Exception as e:
    print(f"An error occurred: {e}")