# format specifiers
#   {value:flags} format a value based on   flags

# flags
#   <   left align
#   >   right align
#   ^   center align
#   :   zero pad
#   #   alternate form
#   +   sign
#   -   sign only negative
#   space   space if positive
#   ,   thousand separator
#   _   use underscore for space
#   b   binary
#   c   character
#   d   decimal
#   e   scientific
#   E   scientific
#   f   fixed point
#   F   fixed point
#   g   general
#   G   general
#   n   number
#   o   octal
#   x   hex lower
#   X   hex upper
#   %   percentage
#   r   raw string
#and many moree


price1 = 3094.844444
price2 = -9803.443
price3 = 0.873

print(f'{price1:,.2f}')
print(f'{price2:,.2f}')
print(f'{price3:,.2f}')

#WHILE LOOP : excecuting a block of code as long as a condition is true

age = int(input("enter your age: "))
while age<0:
    print("age cannot be negative")
    age = int(input("enter your age: "))
print(f"your age is {age}")

food = input("enter your favorite food (q to quit) : ")
while not food == 'q':
    print(f"your favorite food is {food}")
    food = input("enter your favorite food (q to quit) : ")
print("goodbye")


principle = 0
rate = 0
time = 0


while True:
    principle = float(input("enter principle amount: "))
    if principle < 0:
        print("principle amount cannot be negative")
    else:
        break

while True:
    rate = float(input("enter rate of interest: "))
    if rate < 0:
        print("rate of interest cannot be negative")
    else:
        break

while True:
    time = int(input("enter time in years: "))
    if time < 0:
        print("time cannot be negative")
    else:
        break
amount = principle * (1 + rate/100) ** time
print(f"amount after {time} years is {amount:.2f}")




