try:
    var = input("Ingrese un número o una letra: ")
    var2 = input("Ingrese otro número o letra: ")

    var = float(var)
    var2 = float(var2)

    print("El doble del segundo numero: ", var2 * 2)
    print("La tercera parte del primer numero: ", var / 3)
    print("El cuadrado de la suma de ambos: ", (var + var2) ** 2)
    print("La décima parte de la suma de los cuadrados de ambos numeros: ", ((var ** 2) + (var2 ** 2)) / 10)

except:
    print("No valido")