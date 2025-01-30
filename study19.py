#polymorphism: many forms of a single object or method or function or operator or etc. 
#two methods to achieve polymorphism: Duck typing and inheritance
#inheritance: an object could be treated of the same type as its parent class
#Duck typing: object must have attributes and methods

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod # to make the class Shape an abstract class so that it can't be instantiated and the child classes must implement the abstract methods of the parent class. 
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height
    

class Pizza(Circle): #pizza have many forms like circle, shape and pizza
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

#circle = Circle() #object of the class Circle has two forms one is Circle and the other is Shape
shapes = [Circle(4),Square(10),Triangle(3,6),Pizza("chicken",7)] #list of objects of different classes
for shape in shapes:
    print(shape.area()) #calling the method of the parent class
