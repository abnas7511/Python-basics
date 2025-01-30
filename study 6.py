#validate username excercise
# username must not exceed 12 characters
# it shouldn't have spaces
# it shouldn't include digits

username = input("enter the username: ")


if len(username) > 12:
    print("your username can only have upto 12 characters")
elif not username.find(" ") == -1:
    print("you can't have spaces in your username.")
elif not username.isalpha():
    print("you can't have numbers in your username.")
else:
    print(f"welcome {username}!!")

#indexing = accessing elements of a string using [] (indexing operator)
#       [start : end : step]

cred_card = "12245-5646-6421-4658"

print(cred_card[0])
print(cred_card[0:5])
print(cred_card[:4])
print(cred_card[6:])
print(cred_card[-1])
print(cred_card[::2]) #skip 2 steps

last_digits = cred_card[-4:]
print(f"XXXX-XXXX-XXX-{last_digits}")

#to reverse the string
print(cred_card[::-1])