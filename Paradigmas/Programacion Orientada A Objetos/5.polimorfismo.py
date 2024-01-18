
# Polimorfismo: Es la habilidad de tomar varias formas, en este caso, un objeto puede tomar varias formas, por ejemplo, un objeto de la clase perro puede ser un perro salchicha, un perro labrador, un perro pastor aleman, etc.

class Perro:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        
    def mostrarCaracteristicas(self):
        print(f"Nombre:  {self.nombre}\n Tipo:  {self.tipo}")
        
    def sonido(self):
        print("Guau")
        
class PastorAleman(Perro):
    def sonido(self):
        print("Woof")
       
class Pitbull(Perro):
    def sonido(self):
        print("Grrr") 
    
pastorAleman = PastorAleman("Pastor", "Pastor Aleman")
pastorAleman.mostrarCaracteristicas()
pastorAleman.sonido()

print("")

pitbull = Pitbull("PitbullBueno", "Pitbull")
pitbull.mostrarCaracteristicas(pitbull)
pitbull.sonido()