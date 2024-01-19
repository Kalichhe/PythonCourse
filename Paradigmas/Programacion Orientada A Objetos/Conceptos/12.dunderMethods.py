
# Comienzan y finalizan con doble guión bajo

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # __str__ devuelve un string con la representación del objeto, no la dirección de memoria sino el contenido que queremos mostrar
    def __str__(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}"
    
persona1 = Persona("Juan", 28)
print(persona1) # Nombre: Juan, edad: 28


# Sobrecarga de operadores
# Investigar 