
# Carne que se puede pagar por puntos

puntos = int(input("Ingrese la cantidad de puntos que tienes: "))
precioCarne = 15000

if (puntos < 100):
    descuento = precioCarne * 0.1
    precioFinalCompra = precioCarne - descuento
    print("Tu precio final es de: " + str(precioFinalCompra))
elif (puntos >= 100 and puntos < 150):
    descuento = precioCarne * 0.12
    precioFinalCompra = precioCarne - descuento
    print("Tu precio final es de: " + str(precioFinalCompra))
elif (puntos == 150):
    descuento = precioCarne * 0.15
    precioFinalCompra = precioCarne - descuento
    print("Tu precio final es de: " + str(precioFinalCompra))
else:
    descuento = precioCarne * 0.2
    precioFinalCompra = precioCarne - descuento
    print("Tu precio final es de: " + str(precioFinalCompra))