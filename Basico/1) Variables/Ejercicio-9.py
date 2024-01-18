
# Calcular el factorial

numero = int(input("Ingresa un numero: "))

# Funcion 

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    

print(factorial(numero))
    