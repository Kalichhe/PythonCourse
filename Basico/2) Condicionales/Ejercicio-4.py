
# Calculadora basica

a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))

opciones = int(input("Elige alguna de las opciones disponibles: "))
if (opciones == 1):
    print(a + b)
elif (opciones == 2):
    print(a - b)
elif (opciones == 3):
    print(a * b)
elif (opciones == 4):
    print(a / b)
    