
# Factorial de un numero 

print("For")

number = int(input("Ingresa un numero: "))
resultado = 1
for i in range(1, number + 1):
    resultado *= i
print(resultado)

print("\nWhile")

number = int(input("Ingresa un numero: "))
resultado = 1
while number > 0:
    resultado *= number
    number -= 1
print(resultado)