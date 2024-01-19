
# Single Responsability Principle

class Tanque:
    def __init__(self):
        self.combustible = 0
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        print(f"El combustible actual es: {self.combustible}")
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad
        
class Auto:
    def __init__(self, tanque):
        self.tanque = tanque
        self.posicion = 0
        
    def avanzar(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Avanzando...")
        else:
            print("No hay combustible suficiente")
            
    def obtener_posicion(self):
        print(f"La posicion actual es: {self.posicion}")
        return self.posicion
    
tanqueCarro = Tanque()
tanqueCarro.agregar_combustible(100)

carroMio = Auto(tanqueCarro)
carroMio.avanzar(100)
carroMio.avanzar(100)
carroMio.avanzar(1)
carroMio.obtener_posicion()
tanqueCarro.obtener_combustible()


# Este primer principio nos dice que una clase debe tener una sola responsabilidad, es decir, una sola razón para cambiar.