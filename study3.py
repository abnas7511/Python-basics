#arithmetic operators

friends = 5

#friends = friends + 1
friends += 1
#friends = friends - 1
friends -= 1
#friends = friends * 6
friends *= 6
#fireds = friends/ 2
friends /= 2
#friends = friends ** 2
friends **=2
#friends = friends % 3
friends %= 2

print(friends)


#functions

x = 3.14
y = 5
z = 9
a = -7

print(round(x))
print(pow(y,z))
print(abs(a))
print(max(x,y,z))
print(min(x,y,z))

#math module

import math

print(math.pi)
print(math.e)
print(math.sqrt(z))
print(math.ceil(x)) 
print(math.floor(x))

r = float(input("enter the radius of the circle: "))
crcmfrnc = 2 * math.pi * r
print(round(crcmfrnc,2))

#if = do something only if the condition is true
#       else do something
#       elif another condition

age = int(input("enter the age: "))
if age >= 100:
    print("too old grandpa")
elif age >= 18:
    print("Sign up")
elif age < 0:
    print("not a human")

elif age:
    print(f"you are {age } years old")

elif not age: 
    print(f"go and get a life")

else:
    print("not for kids bruh")



