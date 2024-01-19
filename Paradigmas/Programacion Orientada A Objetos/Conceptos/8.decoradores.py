# Decoradores 
# Son funciones que envuelven a otras funciones y permiten ejecutar código antes y después de la función envuelta sin modificarla.

# Decoradores de clases es este

def userDecorator():
    def superUser(cls):
        
        class SuperUser(cls):
            def get_fullName(self):
                return f"{self.get_name()} {self.get_lastName()}"
            
            def __str__(self):
                return f"My full name is {self.get_name()} {self.get_lastName()}"
        return SuperUser
    return superUser

@userDecorator()
class User:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName
        
    def get_name(self):
        return self.name
    
    def get_lastName(self):
        return self.lastName
    
user = User("Carlos", "Lopez")
print(user.get_fullName())
print(user)
print(type(user))