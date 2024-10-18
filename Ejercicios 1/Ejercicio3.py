h = input("Introduce la altura: ")
L = input("Introduce el tamaño del lado de la base: ")

h = float(h)
L = float(L)

B = float(L ** 2)

formula = 1/3 * B * h
piscinas = int (formula / 2500)

print("El volumen de la piramide: ", formula)
print("Equivale aproximadamente a: ", piscinas)