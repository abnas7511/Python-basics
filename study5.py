#string methods

#len method
name = input("enter the name: ")
print(len(name))

#find method
occurance = name.find(" ") # To find the occurence of first space character
print(occurance)

#rfind
occ = name.rfind("a") # to find the last occurence of a character
print(occ)

#capitalize
cap = name.capitalize() # to capitalize first letter only
print(cap)

#upper
capi = name.upper() # whole word capitalization
print(capi)

#lower
low = name.lower() # whole word lower
print(low)

#isdigit
print(name.isdigit()) # to check whether all are digits 

#isalpha
print(name.isalpha()) #to check whether all are albhabets

#count
phn = input("enter the phone number: ")
print(phn.count("-")) # to get the count of a char

#replace
print(phn.replace("-","")) # replace a char by another char

#help
print(help(str))