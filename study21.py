#magic methods/dunder methods:  double underscore methods egs: __init__, __str__, __add__, __sub__ etc
#                               which are automatically called by python built-in functions
#                               they allow developers to define or customize the behavior of the objects

class Student():

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"{self.name} has {self.gpa} GPA"
    
    def __eq__(self,other):
        return self.name == other.name
    
    def __gt__(self,other):
        return self.gpa > other.gpa
    

s1 = Student("John",3.5)
s2 = Student("John",3.5)
s3 = Student("John",3.5)

print(s1)
print(s1==s2)
print(s1==s3)
print(s1>s2)

print("-----------------")

class Book():

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self): #overriding the __str__ method of the object class
        return f"{self.title} by {self.author} has {self.num_pages} pages"
    
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author and self.num_pages == other.num_pages

    def __lt__(self,other):
        return self.num_pages < other.num_pages

    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __le__(self,other):
        return self.num_pages <= other.num_pages
    
    def __contains__(self,other):
        return other in self.title or other in self.author

    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return "Invalid key"

book1 = Book("Python", "John", 200)
book2 = Book("Python", "John", 310)
book3 = Book("Java mayhem", "John", 300)
        
print(book1)
print(book1==book2)
print(book1<book3)
print(book1>book3)
print(book1<=book3)
print("mayhem" in book3)
print(book1["title"]) 
print(book1["author"])
print(book1["num_pages"])
print(book1["price"]) #invalid key

print("-----------------")
print()
  
#property: decorator used to define a method as an property (can be accessed as an attribute)
#           benifits: add additional logic to the attribute when read, write or delete attributes
#           gives you getter, setter and deleter methods

class Rectangle():
    def __init__(self, width, height):
        self._width = width #private variable by adding _ before the variable name  
        self._height = height # it is a convention to tell the developer that this variable should not be accessed directly

    @property
    def width(self):
        return f"Width is {self._width:.1f}cm"

    @property
    def height(self):
        return f"Height is {self._height:.1f}cm"

    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width should be greater than 0")
    
    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height should be greater than 0")
        
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rectangle = Rectangle(10,20)

#rectangle.width = -1 #this will give an error message as the width should be greater than 0
#rectangle.height = 0

rectangle.width = 15
rectangle.height = 25

print(rectangle._width) #this will give an error value without the .2f as it is a private variable
print(rectangle._height) 

print(rectangle.width) #this will give the width of the rectangle
print(rectangle.height) #this will give the height of the rectangle

del rectangle.width
del rectangle.height
