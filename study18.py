#super : used to call the constructor of the parent class in the child class 
#           to call the methods of the parent class. alows to extend the functionality of the inherited methods
#           super().__init__(parameters)
#           super().method_name()
#           super().method_name(parameters)
#           super().method_name(*args, **kwargs)

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.color} color. {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        self.radius = radius
        #self.color = color
        #self.is_filled = is_filled instead we can call the constructor of the parent class by super keyword
        super().__init__(color,is_filled)
 
    def describe(self): #method overriding
        super().describe() #calling the method of the parent class
        print(f"this is a circle with an area of {3.14*self.radius**2}") #overriding the method of the parent class

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width

    def describe(self): #method overriding
        super().describe() #calling the method of the parent class
        print(f"this is a square with an area of {self.width**2}") #overriding the method of the parent class


class Triangle(Shape):
    def __init__(self,color,is_filled,base,height):
        super().__init__(color,is_filled)
        self.base = base
        self.height = height
    def describe(self): #method overriding
        super().describe() #calling the method of the parent class
        print(f"this is a Triangle with an area of {0.5*self.base*self.height}") #overriding the method of the parent class

circle = Circle(radius=5,color='red',is_filled=True)
print(circle.color)
print(circle.is_filled)
print(circle.radius)

square = Square(width=10,color='blue',is_filled=False)
print(square.color)
print(square.is_filled)
print(square.width)

triangle = Triangle(base=10,height=5,color='green',is_filled=True)
print(triangle.color)
print(triangle.is_filled)
print(triangle.base)
print(triangle.height)


#super().describe() #calling the method of the parent class
circle.describe() #calling the method and it'll only consider of child class / method overriding
square.describe()
triangle.describe()

