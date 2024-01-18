
# Pizzeria 

opcion = int(input("Escoge una opcion \n '1' Pizzas vegetarianas \n '2' Pizzas no veganas \nLa opcion es: "))

if (opcion == 1):
    print("\nPizzas vegetarianas")
    
    print("Todas las pizzas llevan Mozzarella y Tomate\n")
    
    ingredienteElegir = int(input("Los ingredientes son:\n '1' Pimenton\n '2' Tofu \nLa opcion es: "))
    
    if (ingredienteElegir == 1):
        print("\nLos ingredientes que lleva tu pizza vegana son\n '1' Pimenton\n '2' Mozzarella\n '3' Tomate")
    elif (ingredienteElegir == 2):
        print("\nLos ingredientes que lleva tu pizza vegana son\n '1' Tofu\n '2' Mozzarella\n '3' Tomate")
    else:
        print("Esos HP ingredientes no estan, asi que no se los vamos a echar")
elif (opcion == 2):
    print("\nPizzas no veganas\n")
    
    print("Todas las pizzas llevan Mozzarella y Tomate")
    
    ingredienteElegir = int(input("Los ingredientes son:\n '1' Peperoni\n '2' Jamon\n '3' Salmon \nLa opcion es: "))
    
    if (ingredienteElegir == 1):
        print("\nLos ingredientes que lleva tu pizza no vegana son\n '1' Peperoni\n '2' Mozzarella\n '3' Tomate")
    elif (ingredienteElegir == 2):
        print("\nLos ingredientes que lleva tu pizza vegana son\n '1' Jamon\n '2' Mozzarella\n '3' Tomate")
    elif (ingredienteElegir == 3):
        print("\nLos ingredientes que lleva tu pizza vegana son\n '1' Salmon\n '2' Mozzarella\n '3' Tomate")
    else:
        print("Esos HP ingredientes no estan, asi que no se los vamos a echar")
else:
    print("Opcion no valida")