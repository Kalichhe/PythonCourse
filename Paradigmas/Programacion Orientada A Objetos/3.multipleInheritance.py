
# Multiple Inheritance

class Person:
    def __init__(self, name, age, nacionality):
        self.name = name
        self.age = age
        self.nacionality = nacionality
        
    def speak(self):
        print("I can speak")

class Artist:
    def __init__(self, hability):
        self.hability = hability
        
    def hability(self):
        print(f"My hability is {self.hability}")
        
class Employee(Person, Artist):
    def __init__(self, name, age, nacionality, hability, salary):
        Person.__init__(self, name, age, nacionality)
        Artist.__init__(self, hability)
        self.salary = salary
        
    def presentation(self):
        return f"{super().hability()}"
    
Employee1 = Employee("John", 25, "American", "Singing", "$5000")
Employee1.presentation()   