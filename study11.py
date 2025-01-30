#dictionaries are key value pairs {key:value}
# ordered and changable, no duplicates

capitals = {"France":"Paris",
            "Germany":"Berlin",
            "Italy":"Rome",
            "Spain":"Madrid",
            "Portugal":"Lisbon"}


print(capitals)
print(capitals.get("France"))
capitals.update({"France":"Marseille"})
print(capitals)
capitals.update({"Greece":"Athens"})
print(capitals)
capitals.pop("France")
print(capitals)
capitals.popitem()
print(capitals)
#capitals.clear()
#print(capitals)

keys  = capitals.keys()
print(keys)

for key in keys:
    print(key)

values = capitals.values()
print(values)

for value in values:
    print(value)

items = capitals.items() #returns a list of tuples
print(items)


for key,value in items:
    print(f"{key} : {value}")


#concession stand example

menu = {"hotdog":2.50,
        "popcorn":3.00,
        "soda":1.50,
        "candy":2.00}

cart = []
total = 0

print("------Menu------")
for key,value in menu.items():
    print(f"{key:10} : ${value:.2f}")
print("---------------")

while True:
    item = input("Enter an item (q to quit): ").lower()
    if item == 'q':
        break
    elif menu.get(item) is not None:
        cart.append(item)

print()     
print("------Cart------")
for item in cart:
    total += menu[item]
    print(item, end=" ")

print()
print(f"Total: ${total:.2f}")


