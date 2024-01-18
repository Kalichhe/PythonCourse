
# Calculos de la hipotenusa

import math

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))

if a and b >= 0:
    c = math.sqrt((a**2) + (b**2))
    print("La hipotenusa es: ", c)
else:
    print("Parcero, no se pueden ingresar catetos iguales a cero")
    