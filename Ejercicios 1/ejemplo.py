var = input("Introduce un número: ")

try:
    var = int(var)
except ValueError:
    print("El valor introducido no es un número válido.")
    var = 0

while var < 5:
    print("El número es",var ," y es menor que 5.")
    var = var + 1