
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property    
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def get_name(self, newName):
        self.__name = f"The new name is {newName}"

    @property    
    def get_age(self):
        return self.__age
    
    @get_age.setter
    def get_age(self, newAge):
        self.__age = f"The new age is {newAge}"
    
carlos = Person("Carlos", 20)
print(carlos.get_name)
# print(carlos.__name) # Esto no se puede hacer porque es privado

carlos.get_name = "Kalichhe"
print(carlos.get_name)

# print("")

print(carlos.get_age)

carlos.get_age = 21
print(carlos.get_age)