
# Hipotenusa
import math
        
numeroCatetos = 0
sumCatetos = 0

while numeroCatetos != 2:
    cateto = float(input("\nIngresa el valor del cateto, mano que sea mayor de 0 grados: "))
    
    if (cateto == 0):
        print("Pendejo que sea mayor a 0 grados")
        print(f"Numero del cateto actual {numeroCatetos}")
        
    else:
        numeroCatetos += 1
        print(f"Numero del cateto actual {numeroCatetos}")
    suma = cateto ** 2
    sumCatetos += suma
    
print(f"\nLa suma de los catetos nos da la hipotenusa de: {math.sqrt(sumCatetos)}")