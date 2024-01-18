
# años raros

añoActual = int(input("Ingrese el año actual: "))

if (añoActual % 4 == 0):
    if (añoActual % 100 == 0):
        if (añoActual % 400 == 0):
            print("Este es un años bisiesto (Tiene 366 dias)")
        else:
            print("Este no es un años bisiesto (Tiene 365 dias)")
    else:
        print("Este es un años bisiesto (Tiene 366 dias)")            
else:
    print("Este no es un años bisiesto (Tiene 365 dias)")