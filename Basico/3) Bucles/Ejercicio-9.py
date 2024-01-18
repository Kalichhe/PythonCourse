
# Calculadora que se enciende y se apaga
from math import sqrt 
estado = "Enciende"

while estado != "SAL":
    
    a = float(input("\nIngresa el dato 'A': "))
    b = float(input("Ingresa el dato 'B': "))
    
    opcion = int(input("\nElige la opcion:\n '1' Raiz cuadrada de la suma\n '2' A / B\n '3' (A * B) / 2.5 \nOpcion: "))
    
    if (opcion == 1):
        raiz = sqrt(a + b)
        print(raiz)
    elif (opcion == 2):
        division = a / b
        print(division)
    elif (opcion == 3):
        varios = (a * b) / 2.5
        print(varios)
    else:
        print("Esa opcion no se encuentra disponible")
            
    estado = str(input("\nSi deseas seguir, presiona escribe otra cosa y si deseas salir escribe 'SAL': ")).upper()
    if (estado == "sal" or estado == "SAL"):
        print("Todo bien")