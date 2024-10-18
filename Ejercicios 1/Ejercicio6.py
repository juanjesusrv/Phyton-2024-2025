try:
    
    hojas = int(input("Introduce el numero de hojas: "))
    rojas = 0;
    verdes = 0
    azul = 0
    
    if hojas % 3 == 0:
        rojas = hojas // 3
        verdes = hojas // 3
        azul = hojas // 3
    elif hojas % 3 == 1:
        rojas = (hojas // 3) + 1
        verdes = hojas // 3
        azul = hojas // 3
    else:
        rojas = (hojas // 3) + 1
        verdes = (hojas // 3) + 1
        azul = hojas // 3
        
        
    print("El numero de hojas totales es: " , hojas)
    print("El numero de hojas rojas es:", rojas)
    print("El numero de hojas verdes es:", verdes)
    print("El numero de hojas azules es:", azul)

    
    
    
except:
    print("Eso ta mal manito")