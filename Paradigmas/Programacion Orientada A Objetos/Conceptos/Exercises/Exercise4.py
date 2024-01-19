
# Game

class Personaje:
    def __init__(self, nombre, poder, velocidad):
        self.nombre = nombre
        self.poder = poder
        self.velocidad = velocidad
    
    def __str__(self):
        return f"Nombre: {self.nombre}, poder: {self.poder}, velocidad: {self.velocidad}"
    
    def __add__(self, otro):
        nuevoNombre = self.nombre + otro.nombre
        nuevaPoder = ((self.poder + otro.poder)/2)**2
        nuevaVelocidad = ((self.velocidad + otro.velocidad)/2)**2
        return Personaje(nuevoNombre, nuevaPoder, nuevaVelocidad)
    
goku = Personaje("Goku", 100, 50)
vegeta = Personaje("Vegeta", 80, 70)
gojan = Personaje("Gojan", 90, 60)
print(goku)
print(vegeta)
gogeta = goku + vegeta
print(gogeta)