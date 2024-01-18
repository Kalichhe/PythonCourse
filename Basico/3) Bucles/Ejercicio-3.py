
# Frase 

frase = str(input("Ingresa una frase: "))
contadorPalabras = 0

for i in range(len(frase)):
    print(frase[i])
    contadorPalabras += 1
    
print(contadorPalabras)