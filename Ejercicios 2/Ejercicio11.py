try:
    
    euros = float(input("Introduce la cantidad de euros que quieres convertir: "))
    
    while euros < 0:
        print("El numero introducido no es valido.")
        euros = float(input("Introduce la cantidad de euros que quieres convertir: "))
        
    moneda = input("Introduce la moneda a la que quieres convertir (libras, dolares, yenes o bolivares): ")
    
    while moneda != "libras" and moneda != "dolares" and moneda != "yenes" and moneda != "bolivares":
        print("La moneda introducida no es valida.")
        moneda = input("Introduce la moneda a la que quieres convertir (libras, dolares, yenes o bolivares): ")
        
    if moneda == "libras":
        conversion = euros * 0.86
    elif moneda == "dolares":
        conversion = euros * 1.21
    elif moneda == "yenes":
        conversion = euros * 129.852
    else:
        conversion = euros * 1000000
        
        
    print(f"La cantidad {euros}€ pasada a {moneda} es {conversion}")
    
    
except Exception as e:
    print(f"An error occurred: {e}")
    
    
    
# Realiza un conversor de euros a libras, dólares, yenes o bolívares. La cantidad de
# euros que se quiere convertir debe ser introducida por teclado, así como la moneda a la que
# debo realizar el cambio.