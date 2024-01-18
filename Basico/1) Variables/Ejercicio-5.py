# Calculo de intereses

# Formula del interes compuesto

capitalInicial = float(input("Ingresa el capital inicial: "))
tasaInteres = float(input("Ingresa la tasa de interes: "))
tiempo = float(input("Ingresa el tiempo que va a durar: "))

capitalFinal = capitalInicial * (1 + tasaInteres) ** tiempo
print(capitalFinal)