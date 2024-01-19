
# Inheritance: Is a way of creating a new class for using details of an existing class without modifying it.

class Person:
    def __init__(self, name, age, nacionality):
        self.name = name
        self.age = age
        self.nacionality = nacionality
        
    def speak(self):
        print("I can speak")

# Here inheritance is applied,the Employee class inherits the attributes of the Person class

class Employee(Person):
    def __init__(self, name, age, nacionality, salary, job):
        
        # super() function that will make the child class inherit all the methods and properties from its parent
        super().__init__(name, age, nacionality)
        self.salary = salary
        self.job = job

Employee1 = Employee("John", 25, "American", "$5000", "Software Engineer")

# print(Employee1.name)
print(Employee1.job)
Employee1.speak()