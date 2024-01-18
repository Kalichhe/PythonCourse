
# Setters y Getters

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def set_name(self, newName):
        self.__name = f"The new name is {newName}"
        
    def get_age(self):
        return self.__age
    
    def set_age(self, newAge):
        self.__age = f"The new age is {newAge}"
    
carlos = Person("Carlos", 20)
print(carlos.get_name())
# print(carlos.__name) # Esto no se puede hacer porque es privado

carlos.set_name("Kalichhe")
print(carlos.get_name())

print("")

print(carlos.get_age())

carlos.set_age(21)
print(carlos.get_age())