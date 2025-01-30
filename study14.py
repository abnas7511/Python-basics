#iterables = [1, 2, 3, 4, 5] #list, tuple, set, dictionary, string


nums = [1, 2, 3, 4, 5]

for num in reversed(nums):
    print(num, end= " ")

print()
string = "Hello"
for char in reversed(string):
    print(char, end= " ")#prints the string in reverse order


def pal(word):
    rev = ""
    for char in reversed(word):
        rev += char     
    print(rev)
    return word == rev
    #checks if a word is a palindrome
    #a palindrome is a word that reads the same forwards and backwards
    

# or i could do with slicing by using [::-1]
# def pal(word):
#     return word == word[::-1]


#prints True
print()
print(pal("radar")) #returns true if the word is a palindrome, false otherwise
print(pal("hello")) #returns false if the word is a palindrome, false otherwise
print(pal("level")) #returns true if the word is a palindrome, false otherwise


dictionary = {"name":"John","age":30,"city":"New York","country":"USA"}

for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

for key,value in dictionary.items():
    print(f"{key} : {value}")
    # prints the keys, values and key-value pairs of the dictionary


#membership operators
#in and not in
#checks if a value is in a sequence or not
#returns True if the value is in the sequence, False otherwise

nums = [1, 2, 3, 4, 5]
print(3 in nums) #prints True
print(6 in nums) #prints False

#list comprehension
#allows you to create a list based on an existing list
#syntax: [expression for item in iterable if condition]

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
new_list = [fruit for fruit in fruits if 'a' in fruit]
print(new_list) #prints ['apple', 'banana', 'mango']


#match-case statement or switch-case statement

def day_of_week(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _: #default case
            print("Invalid day")
    
day_of_week(3) #prints Wednesday
day_of_week(8) #prints Invalid day
day_of_week(1) #prints Monday

#modules

