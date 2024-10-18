try:
    
    largos = int(input("Introduce la cantidad de largos: "))
    metros = int(input("Introduce el numero de metros de la piscina: "))
    
    crol = 0
    espalda = 0
    
    if largos % 2 == 0:
        crol = largos // 2
        espalda = largos // 2
    else: 
        crol = (largos // 2) + 1
        espalda = largos // 2
    
    print("Se han nadado" , largos , "largos en una piscina de" , metros , "metros")
    print("El total de metros recorridos en crol es: " , crol * metros)
    print("El total de metros recorridos en espalda es: " , espalda * metros)
    print("El total de metros recorridos es: " , largos * metros)
    
    
    
except:
    print("Eso ta mal manito")