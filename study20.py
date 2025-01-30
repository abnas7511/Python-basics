#Duck typing: Another way to achieve polymorphism other than inheritance
#Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
#                       object must have minimum required methods/attributes
#                       'If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.'

class Animal():
    alive = True

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car():  #the car looks like an animal object with all methods/attributes required so it can be used in the list of animals
    alive = False
    def speak(self):
    #def drive(self):
        print("Vroom")

#animals = [Dog(), Cat(), Car()] # car has no minimum required methods/attributes
animals = [Dog(), Cat(),Car()] 
for animal in animals:
    animal.speak()
    print(animal.alive)


print('---------------------------------')
print()
#static methods: methods that do not require an instance of the class to be created
#               instance methods: methods that require an instance of the class to be created
#               static methods are created using the @staticmethod decorator and best for utility functions that do not require an instance of the class to be created


class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_pos(position):
        return position in ['Manager','Developer','Intern']
    

print(Employee.is_valid_pos('Manager')) # calling static method without creating an instance of the class
print(Employee.is_valid_pos('CEO'))

employee1 = Employee('John','Manager')
employee2 = Employee('Jane','Developer')
employee3 = Employee('Jack','CEO')

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info()) # calling instance method

print('---------------------------------')
print()


#class methods: methods that are bound to the class and not the instance of the class
#              class methods are created using the @classmethod decorator and allow operations on the class itself, take cls as the first argument instead of self

class Student():
    count = 0
    tot_gpa = 0


    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.tot_gpa += gpa
    
    #instance method
    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"
    
    #class method
    @classmethod
    def get_count(cls): #cls is the class itself
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        return f"Average GPA: {cls.tot_gpa/cls.count:.2f}"

print(Student.get_count())

student1 = Student('John',3.5)
student2 = Student('Jane',3.7)
student3 = Student('Jack',3.9)

print(Student.get_count()) #calling class method without creating an instance of the class

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print(Student.get_avg_gpa()) #calling class method without creating an instance of the class

#instance methods: best for operations on instance of the class
#class methods: best for class-level data or operations on the class itself
#static methods: best for operations that don't depend on the class or instance of the class
print('---------------------------------')



