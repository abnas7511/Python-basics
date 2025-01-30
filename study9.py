# collection  : single variable used to store multiple values
# collection types: list, tuple, set, dictionary
#
# list: [] ordered, mutable, allows duplicates
# tuple: () ordered, immutable, allows duplicates
# set: {} unordered, mutable, does not allow duplicates
# dictionary: {} unordered, mutable, does not allow duplicate keys

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits[0])  # prints: apple
print(fruits[1])  # prints: banana
print(fruits[2:5])  # prints: cherry
print(fruits[-1])  # prints: elderberry
print(fruits[1:5:2])  # prints: date
print(fruits[:3])  # prints: ['apple', 'banana', 'cherry']
print(fruits[3:])  # prints: ['date', 'elderberry']
print(fruits[-3:-1])  # prints: ['cherry', 'date']
print(fruits[-1:-3])  # prints: []
print(fruits[-3:-1])  # prints: ['cherry', 'date']
print(fruits[-1:-3:-1])  # prints: ['elderberry', 'date']

for x in fruits:
    print(x)

#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("apple" in fruits)
fruits[0] = "apricot"
print(fruits)
fruits.append("fig")
print(fruits)
fruits.insert(2, "cantaloupe")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
#fruits.clear()
#print(fruits)  # prints: []
#print(fruits.copy())  # prints: ['apple', 'apricot', 'cantal
print(fruits.count("fig"))  # prints: 1
print(fruits.index("date"))  # prints: 0


fruits2 = {'apple', 'banana', 'cherry', 'date', 'elderberry'}
print(fruits2)
print("apple" in fruits2)
fruits2.add("fig")
print(fruits2)
fruits2.update(["grape", "honeydew"])
print(fruits2)
fruits2.remove("banana")
print(fruits2)

#fruit2[0] = "apricot"  # TypeError: 'set' object does not support item assignment

#fruits2 = {'apple', 'banana', 'cherry', 'date', 'elderberry', 'banana'}
#print(fruits2)  # prints: {'banana', 'apple', 'cherry', 'elderberry', 'date'} # no duplicates

food = []
prices = []
total = 0

while True:
    item = input("Enter food item (q to quit): ")
    if item.lower() == 'q':
        break
    else:
        price = float(input("Enter price: "))
        food.append(item)
        prices.append(price)

print("-----------------YOUR CART ITEMS-----------------")
for f, p in zip(food, prices):
    print(f"{f} : {p}")
    total += p
print("-----------------YOUR TOTAL PRICE-----------------")
print(total)  # prints: 0.0

