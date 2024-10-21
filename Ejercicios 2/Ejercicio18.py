try:
    const_iva = { "general": 21, "reducido": 10, "superreducido": 4 }
    const_promo = { "nopro": 0, "mitad": 50, "meno5": 5, "5porc": 5 }
    
    base_imponible = float(input("Introduce la base imponible: "))
    
    while base_imponible < 0:
        print("La base imponible introducida no es valida.")
        base_imponible = float(input("Introduce la base imponible: "))
        
    iva = input("Introduce el tipo de IVA (general, reducido o superreducido): ")
    
    while iva not in const_iva:
        print("El tipo de IVA introducido no es valido.")
        iva = input("Introduce el tipo de IVA (general, reducido o superreducido): ")
        
    promo = input("Introduce el codigo promocional (nopro, mitad, meno5 o 5porc): ")
    
    while promo not in const_promo:
        print("El codigo promocional introducido no es valido.")
        promo = input("Introduce el codigo promocional (nopro, mitad, meno5 o 5porc): ")
        
    if promo == "5porc":
        precio_final = base_imponible + (base_imponible * (const_iva[iva] / 100)) - (base_imponible * (const_promo[promo] / 100))
    elif promo == "mitad":
        precio_final = base_imponible + (base_imponible * const_iva[iva] / 100) - (base_imponible / 2)
    else:
        precio_final = base_imponible + (base_imponible * const_iva[iva] / 100) - const_promo[promo];
    
    print(f"La base imponible del producto es: {base_imponible}")
    print(f"El precio final del producto es: {precio_final}")
    
    
    
    
except Exception as e:
    print(f"An error occurred: {e}")



#Escribe un programa que calcule el precio final de un producto según su base
#imponible (precio antes de impuestos), el tipo de IVA aplicado (general, reducido o
#superreducido) y el código promocional. Los tipos de IVA general, reducido y superreducido son
#del 21%, 10% y 4% respectivamente. Los códigos promocionales pueden ser nopro, mitad,
#meno5 o 5porc que significan respectivamente que no se aplica promoción, el precio se reduce
#a la mitad, se descuentan 5 euros o se descuenta el 5%.