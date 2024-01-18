
# Fibonacci

numero = int(input("Ingresa un numero: "))
serie = [0, 1]
for i in range(2, numero):
    serie.append(serie[i - 1] + serie[i - 2])
print(serie)