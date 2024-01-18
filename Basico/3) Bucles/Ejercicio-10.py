
# Motor de videojuego

import random

# Vida de los jugadores
a = 100
b = 100

nombreJugadorA = str(input("Ingresa el nombre del jugador 'A': "))

nombreJugadorB = str(input("Ingresa el nombre del jugador 'B': "))

print(f"\nEl jugador '{nombreJugadorA}' es 0 y el jugador '{nombreJugadorB}' es 1\n")
print("Las reglas son las siguientes:\n '1' La maquina decide quien inicia\n '2' Cada golpe equivale a 10 puntos de daño y cada jugador tiene 100 puntos de vida\n")

estado = True

desicion = random.randint(0,1)
print(f"La desicion de quien inicia el combate lo decide la maquina:\n La opcion es: {desicion}")


while estado:
    
    ataque = random.randint(0,1)
    
    if (desicion == 0):
        print(f"\nInicia atacando el jugador '{nombreJugadorA}'")
        if (ataque == 0):
            print(f"El jugador '{nombreJugadorA}' no decide atacar")
            desicion = 1
            print(f"Vida del jugador '{nombreJugadorB}' es {b}")
        else:
            b -= 10
            print(f"El jugador '{nombreJugadorA}' le quita 10 de vida al jugador '{nombreJugadorB}'")
            desicion = 1
            print(f"Vida del jugador '{nombreJugadorB}' es {b}")
    else:
        print(f"\nInicia atacando el jugador '{nombreJugadorB}'")
        if (ataque == 0):
            print(f"El jugador '{nombreJugadorB}' no decide atacar")
            desicion = 0
            print(f"Vida del jugador '{nombreJugadorA}' es {a}")
        else:
            a -= 10
            print(f"El jugador '{nombreJugadorB}' le quita 10 de vida al jugador '{nombreJugadorA}'")
            desicion = 0
            print(f"Vida del jugador '{nombreJugadorA}' es {a}")
            
    if (a == 0):
        print(f"\nEl jugador '{nombreJugadorA}' ha muerto, por loka")
        estado = False
    elif (b == 0):
        print(f"\nEl jugador '{nombreJugadorB}' ha muerto, por loka")
        estado = False

input("\nPresiona cualquier tecla para salir")    