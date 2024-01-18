
# Encapsulamiento 
# Es una forma de ocultar los datos y los metodos de un objeto de manera que solo se pueda cambiar mediante los metodos del objeto

class Encapsulamiento:
    def __init__(self):
        self.__privado = "Soy privado"
        
encapsulamiento = Encapsulamiento()

print(encapsulamiento.__privado) # Esto no se puede hacer porque es privado