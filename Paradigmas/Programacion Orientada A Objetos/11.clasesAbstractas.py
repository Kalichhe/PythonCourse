
# Abstract classes

# Todo esto es una plantilla, con las cual podemos crear mas clases

from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def __init__(self, name, age, sex, activity):
        self.name = name
        self.age = age
        self.sex = sex
        self.activity = activity
        
    @abstractmethod
    def doActivity(self):
        pass
    
class Student(Person):
    def __init__(self, name, age, sex, activity):
        super().__init__(name, age, sex, activity)
    
    def doActivity(self):
        print(f"{self.name}: I'm studying: {self.activity}")

class worker(Person):
    def __init__(self, name, age, sex, activity):
        super().__init__(name, age, sex, activity)
    
    def doActivity(self):
        print(f"{self.name}: I'm working as a: {self.activity}")
    
carlos = Student("Carlos", 20, "M", "Programming")    
carlos.doActivity()

kalichhe = worker("Kalichhe", 20, "M", "Programmer")
kalichhe.doActivity()