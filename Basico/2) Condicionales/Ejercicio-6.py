
# IVA

ivaOtroLugar = 0.21
ivaRestaurante = 0.1

tipoFactura = int(input("Si es una factura de un restaurante selecciona '1' y si no selecciona '2': "))

valorFactura = int(input("Ingresa el valor de la factura: "))

if (tipoFactura == 1):
    iva = valorFactura * ivaRestaurante
    valorFinal = valorFactura + iva
    print("Tu valor final es de: " + str(valorFinal))
else:
    iva = valorFactura * ivaOtroLugar
    valorFinal = valorFactura + iva
    print("Tu valor final es de: " + str(valorFinal))