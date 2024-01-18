
# Modelando animales de un zoologico

class Animal:
    def comer(self):
        print("Comiendo...")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando...")

class Ave(Animal):
    def volar(self):
        print("Volando...")

class Murcielago(Mamifero, Ave):
    def __init__(self):
        super().__init__()
    
murcielago1 = Murcielago()

murcielago1.comer()
murcielago1.amamantar()
murcielago1.volar()

print(Murcielago.mro())