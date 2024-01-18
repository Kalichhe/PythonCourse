# lista = [1, 2, [3, 4, [5, 6]]]

# print(lista[2][2][1])


# Codigo del juego
# Lo que toca hacer es configurar los ataques de los jugadores en una lista

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

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

# Lista con los ataques que van a tener los jugadores
ataqueA = []
ataqueB = []

# Ciclos for para poder llenar las listas con los ataques y no ataques de forma aleatoria
for i in range(1, 51):
    ataque = random.randint(0,1)
    ataqueA.append(ataque)
    
for i in range(1, 51):
    ataque = random.randint(0,1)
    ataqueB.append(ataque)

iPlayerA = 0
iPlayerB = 0

while estado:    
    
    if (desicion == 0):
        print(f"\nInicia atacando el jugador '{nombreJugadorA}'")
        if (ataqueA[iPlayerA] == 0):
            iPlayerA += 1
            print(f"El jugador '{nombreJugadorA}' no decide atacar")
            desicion = 1
            print(f"Vida del jugador '{nombreJugadorB}' es {b}")
            print(iPlayerA)
        else:
            iPlayerA += 1
            b -= 10
            print(f"El jugador '{nombreJugadorA}' le quita 10 de vida al jugador '{nombreJugadorB}'")
            desicion = 1
            print(f"Vida del jugador '{nombreJugadorB}' es {b}")
            print(iPlayerA)
            
    else:
        print(f"\nInicia atacando el jugador '{nombreJugadorB}'")
        if (ataqueB[iPlayerB] == 0):
            iPlayerB += 1
            print(f"El jugador '{nombreJugadorB}' no decide atacar")
            desicion = 0
            print(f"Vida del jugador '{nombreJugadorA}' es {a}")
            print(iPlayerB)
        else:
            iPlayerB += 1
            a -= 10
            print(f"El jugador '{nombreJugadorB}' le quita 10 de vida al jugador '{nombreJugadorA}'")
            desicion = 0
            print(f"Vida del jugador '{nombreJugadorA}' es {a}")
            print(iPlayerB)
            
            
    if (a == 0):
        print(f"\nEl jugador '{nombreJugadorA}' ha muerto, por loka")
        estado = False
    elif (b == 0):
        print(f"\nEl jugador '{nombreJugadorB}' ha muerto, por loka")
        estado = False

input("\nPresiona cualquier tecla para salir")    