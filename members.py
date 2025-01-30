# __members__ and __methods__ are attributes, not keywords
class MyClass:
    def __init__(self):
        pass

    def my_method(self):
        pass

print(MyClass.__members__)  # Output: ['__module__', '__doc__', '__init__', 'my_method', '__dict__', '__weakref__']
print(MyClass.__methods__)  # Output: ['__init__', 'my_method'