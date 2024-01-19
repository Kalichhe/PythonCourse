
# Student

class Student:
    
    # Constructor method
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    # Class method
    def study(self):
        print(f"\nThe student {self.name} is studying")
    

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
course = str(input("Enter your course: "))

student1 = Student(name, age, course)

student1.study()
