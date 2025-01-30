#function  =  a reusuable block of code that does a specific task

def greet(name,age):
    print(f"Hello {name}")
    print(f"Good Morning. You are {age} years old")

name = input("Enter your name: ")
age = input("Enter your age: ")
greet(name,age)

#function with return statement

def add(a,b):
    return a+b
print(add(5,6))

#function with multiple return statement
def add(a,b):
    return a+b, a-b
print(add(5,6))

#function with default argument
def greet(name="John",age=30):
    print(f"Hello {name}")
    print(f"Good Morning. You are {age} years old")
greet()

#default arguments = a default value is assigned to the parameter
#non-default arguments = a value is assigned to the parameter
#keyword arguments = a value is assigned to the parameter using the parameter name
#variable arguments = a value is assigned to the parameter using the parameter name and the value is passed as a dictionary


def net_salary(basic,da,hra):
    return basic+da+hra
print(net_salary(10000,2000,3000))
print(net_salary(10000,da=2800,hra=3400))
print(net_salary(10000,hra=3000,da=2000))

#*args = variable length arguments = a value is assigned to the parameter using the parameter name and the value is passed as a tuple

#**kwargs = variable length keyword arguments = a value is assigned to the parameter using the parameter name and the value is passed as a dictionary

def add(*args): #*nums can also be used as unpacking character is the only requirement
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5)) # we pass in a tuple

def add(**kwargs):
    return sum(kwargs.values())
print(add(a=1,b=2,c=3,d=4,e=5)) # we pass in a dictionary

def printaddress(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

printaddress(name="John",age=30,city="New York",country="USA")


def shippinglabel(*args, **kwargs):
    print("Shipping Label:")
    print("---------------")
    for arg in args:
        print(arg)
    print("---------------")
    for key,value in kwargs.items():
        print(f"{key} : {value}")

shippinglabel("John Doe","123 Main St","New York","NY",10001,weight=10,fragile=True)