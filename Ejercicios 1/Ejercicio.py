# Pide al usuario el número total de goles en una temporada y el número de partidos. Calcula el promedio de goles por partido.

try:
    golesTotales = int(input("Introduce el número total de goles en una temporada: "))
    numPartidos = int(input("Introduce el número de partidos: "))

    print("El promedio de goles por partido es de", abs(golesTotales / numPartidos))
except ZeroDivisionError:
    print("No se puede dividir por 0")
except ValueError:
    print("Introduce un número válido")
    
    
#Dado un resultado final de un partido (goles a favor y en contra), calcula la diferencia de goles usando el valor absoluto
try:
    golesFavor =int(input("Introduce el numero de goles a favor: "))
    golesContra =int(input("Introduce el numero de goles en contra: "))
    
    print("La diferencia de goles es de", abs(golesFavor - golesContra))
except ValueError:
    print("Introduce un numero valido")