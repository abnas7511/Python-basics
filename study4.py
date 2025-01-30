# == operator

name = input("enter your name: ")

if name == "":
    print("you did not type anything niggar")
else:
    print(f"hello {name}!!")

# logical operators (and,not,or,xor)
#   and = only if 2 conditions are true
#   or = only if any one of conditions are true
#   not = invert the condition

temp = 30
is_raining = False
is_sunny = True


if temp < 0 or temp > 35 or is_raining: # 
    print("match cancelled")
else:
    print("match is onn")

if temp >= 28 and is_sunny:
    print("sunny day")
else:
    print("not a sunny day")

#conditional operation = one-shot condition checking for the if-else statement(ternary operator)
# X if condition else Y

x = -5
print("Positive" if x > 0 else "Negative")

#odd even
num = int(input("enter the number: "))
print("EVEN" if num % 2 == 0 else "ODD")

# or you can do this way 
num2 = int(input("enter the number: "))
if num2 % 2 == 0:
    print("EVEN")
else:
    print("ODD")