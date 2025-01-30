# variables = A container for a value(strings, integer, float, boolean)
#             variables behave as it contain a value

#strings
first_name = "john"
last_name = "doe"

#integers
age = 25
quantity = 9

#float
price = 5.9
gpa = 8.9

#boolean
is_Sale = True
is_alive = False


#Typecasting : process of converting a variable from one datatype to another
#               str(), int() , bool(), float()
name = "john doe"
gname = ""
years = 19
cgpa = 9.8
is_student = True

print(type(name))
#output: <class 'str'>

print(int(cgpa))
print(float(years))
print(str(years))
print(type(str(years)))
print(bool(name))
print(bool(gname))


#input() : return a string that user entered (prompt the user to enter the data)
hname = input("what is your name: ")
hage = int(input("how old are you: "))

hage += 1  #hage = hage+1 

print(f"hello {hname} ")
print("Happy bday!!")
print(f"you are {hage} years old now")

#excercise
#rectangle area

length = int(input("length: "))
breadth = int(input("breadth: "))
area = length * breadth
print(f"the area of given rectangle is {area} cm²")
print("the area is",area)

