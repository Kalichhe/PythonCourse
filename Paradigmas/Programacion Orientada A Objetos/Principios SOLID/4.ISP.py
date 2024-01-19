
# Interface Segregation Principle 

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        raise NotImplementedError("trabajar no esta implementado")

class Cobrador(ABC):
    @abstractmethod
    def cobrar(self):
        raise NotImplementedError("cobrar no esta implementado")

class Comensal(ABC):
    @abstractmethod
    def comer(self):
        raise NotImplementedError("comer no esta implementado")
    
class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        raise NotImplementedError("dormir no esta implementado")
    
# No hay necesidad de tocar lo de arriba

class Humano(Trabajador, Cobrador, Comensal, Durmiente):
    def trabajar(self):
        print("El humano esta trabajando...")
    
    def cobrar(self):
        print("El humano esta cobrando...")
    
    def comer(self):
        print("El humano esta comiendo...")
    
    def dormir(self):
        print("El humano esta durmiendo...")
        
class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando...")
        
carlos = Humano()
carlos.trabajar()
carlos.cobrar()
carlos.comer()
carlos.dormir()

robot = Robot()
robot.trabajar()        

# Este principio nos dice que una clase no debe implementar interfaces que no va a usar. Es decir, que una clase no debe implementar métodos que no va a usar.
# Y cadad interface debe tener una sola responsabilidad, es decir, una sola razón para cambiar entre comillas.