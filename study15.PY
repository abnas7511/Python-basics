#oop
# object = a bundle of related attributes and methods 
# class = a blueprint or template for creating objects
# instance = a specific object created from a particular class

# attribute = a characteristic or property of an object
# method = a function that is associated

#from car import Car  can be used for classess by defining in another pages

class Car:
    def __init__(self,model,color,make,year,price): #constructor
        self.color = color #attributes
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    
    def display_details(self): #methods
        print(f"Color: {self.color}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")

    def stop(self):
        print(f"{self.make} {self.model} has stopped")
    
    def drive(self):
        print(f"{self.make} {self.model} is driving")

car1 = Car('toyota','red','corolla','2019','2000000')
car1.display_details()
print()
car2 = Car('honda','blue','civic','2020','2500000')
car2.display_details()

print(car1.color) #accessing attributes of an object by using dot operator
print(car2.color)

car1.stop()
car2.drive()

car1.drive()
car2.stop()

#class variables : variables that are shared among all instances of a class
# defined outside the constructor
# allow to share data among all objects

class Student:

    grad_year = 2024 #class variable
    number_of_students = 0

    def __init__(self,name,age):
        self.name = name #instance variables : variables that are unique to each instance
        self.age = age
        Student.number_of_students += 1

student1 = Student('Ali',20)
student2 = Student('Ahmed',22)
student3 = Student('Asad',21)
student4 = Student('Ahsan',23)

print(student1.name) #accessing instance variables using dot operator
print(student2.name)


print(student1.grad_year)
print(student2.grad_year) #class variables can be accessed by all instances of a class
print(Student.grad_year) # accessing class variable using class name is the best way to access class variables



print(Student.number_of_students)
print(f"my class of {Student.number_of_students} students will graduate in {Student.grad_year}")

