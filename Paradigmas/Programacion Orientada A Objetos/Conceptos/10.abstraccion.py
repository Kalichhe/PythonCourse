
# Abstraccion
# Es un proceso mental que consiste en aislar los aspectos relevantes de un objeto

class Auto:
    def __init__(self):
        self.estado = "Apagado"
        
    def encender(self):
        self.estado = "Encendido"
        print("El auto esta encendido")
    
    def conducir(self):
        if (self.estado == "Encendido"):
            print("Estoy conduciendo")
        else:
            print("El auto esta apagado, primero hay que encenderlo")
            
mi_auto = Auto()

mi_auto.encender()
mi_auto.conducir()