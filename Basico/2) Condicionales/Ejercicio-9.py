
# Tarifa anual

opciones = int(input("Selecciona algunas de las opciones \n '1' Si es mayor de edad y esta trabajando \n '2' Si es menor de edad y esta trabajando \n '3' Si es mayor de edad y no esta trabajando \n '4' Si es menor de edad y no esta trabajando\nLa opcion es: "))

valorBoleta = float(input("Ingresa el valor de la boleta: "))

if (opciones == 1):
    print("El valor de la boleta es; ", valorBoleta)
elif (opciones == 2):
    valorBoleta = valorBoleta * 0.95
    print("El valor de la boleta es; ", valorBoleta)
elif (opciones == 3):
    valorBoleta = valorBoleta * 0.75
    print("El valor de la boleta es; ", valorBoleta)
elif (opciones == 4):
    valorBoleta = valorBoleta * 0.50
    print("El valor de la boleta es; ", valorBoleta)
else:
    print("Opcion no valida")