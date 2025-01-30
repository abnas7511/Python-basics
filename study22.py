#Decorator : a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
#               pass the base function as an argument to the decorator function.
#               the decorator function returns a new function that extends the behavior of the original function.
#               the new function calls the original function and modifies its behavior.
#               the new function is returned as the result of the decorator function.


#               @add_sprinkles
#               get_icecream('vanilla'):    #output: vanilla icecream with sprinkles # here we ``decorated'' the get_icecream function with add_sprinkles function 

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you have added sprinkles")
        func(*args, **kwargs)
    return wrapper

# we want the above code to be executed only when we call the get_icecream function that's why we are using the wrapper function
# the wrapper function is the one that is going to be executed when we call the get_icecream function

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("you have added fudge")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_icecream(flavor):
    print(f"here's your {flavor} icecream")

get_icecream('vanilla')    #output: you have added sprinkles you have added fudge here's your icecream


print("-----------------")
print()

#excepction handling = An event that interrupts the normal flow of the program's execution
#                       when an exception occurs, the program terminates abnormally
#                       (zero division error, value error, type error, index error, key error, file not found error, etc)
#                       we can handle these exceptions using try, except, else, finally block

try:
    num = int(input("enter a number: "))
    print(1/num)

#except ZeroDivisionError:
    #print("cannot divide by zero")

except ValueError:
    print("invalid, only valid input ")

except Exception as e:
    print(e)

finally:
    print("do some cleanup here")

print("-----------------")
print()

#file handling = a file is a collection of data stored in a disk with a specific name and a directory path

import os

file_path  = "stuff/test.txt"
#file_path = "templates"

if os.path.exists(file_path):
    print("file path exists")

    if os.path.isfile(file_path):
        print("it is a file")
    elif os.path.isdir(file_path):
        print("it is a directory")
else:
    print("file does not exist")