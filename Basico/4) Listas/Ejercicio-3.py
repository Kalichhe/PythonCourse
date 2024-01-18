
# Nombres

# Lista con los nombres 

nombres = []

contadorNombres = 0

while True:
    
    nombre = str(input("Ingrese los nombres, escribe '-1' para poder terminar: "))
    
    if nombre == "" or nombre == "-1":
        break

    nombres.append(nombre)


for i in nombres:
    print("1", i)
    for j in nombres:
        print("2", j)
        if (i == j):
            contadorNombres += 1
            print(contadorNombres)