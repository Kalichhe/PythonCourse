
# Open Close Principle

from abc import ABC, abstractmethod
from random import randint

class Usuario(ABC):
    def __init__(self, nombre,):
        self.nombre = nombre
        
    @abstractmethod
    def metodoComunicacion(self):
        raise NotImplementedError("metodoComunicacion no esta implementado")

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    @abstractmethod
    def notificar(self):
        raise NotImplementedError("Notificar no esta implementado")
    
# Estas clases no tenemos que tocarlas 

    
class UsuarioSMS(Usuario):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.sms = f"+57 {randint(3000000000, 3999999999)}"
        
    def metodoComunicacion(self):
        return self.sms

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando notificacion a {self.usuario.nombre} a traves del metodo de comunicacion SMS a {self.usuario.metodoComunicacion()} con el mensaje: {self.mensaje}")

carlosSMS = UsuarioSMS("Carlos")
mensaje = NotificadorSMS(carlosSMS, "Hola Carlos, todo bien?")
mensaje.notificar()

# Este principio nos dice que una clase debe estar abierta para extensión pero cerrada para modificación. Es decir, que una clase debe poder extenderse para agregar nuevas funcionalidades pero sin necesidad de modificar el código ya existente.