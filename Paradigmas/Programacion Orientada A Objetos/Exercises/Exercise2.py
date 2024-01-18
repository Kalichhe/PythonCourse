
# Sistema para una escuela

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Metodo para mostrar el nombre y la edad
    def mostrarNombreEdad(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}")
    
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    # Metodo para mostrar el grado
    def mostrarGrado(self):
        print(f"Grado: {self.grado}")
        
estudiante1 = Estudiante("Carlos", 20, "7 semestre")

estudiante1.mostrarNombreEdad()
estudiante1.mostrarGrado()