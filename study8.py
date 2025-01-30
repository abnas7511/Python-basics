#for loop : iterating over a sequence
# can iterate over a string, list, tuple, set, dictionary, range, etc

for i in reversed(range(1, 11,2)):#range(start, stop, step)
    print(i, end=' ')
print()
print("Happy New Year!")


credit_card = '1234-5678-9012-3456'
for i in credit_card:
    if i == '-':
        continue #skip the rest of the code and go to the next iteration
    print(i, end=' ')

import time

yourtime = int(input("enter time in seconds: "))
for i in range(yourtime,0,-1):
    seconds = i % 60
    minutes = i // 60 % 60
    hours = i // 3600
    print(f'{hours:02}:{minutes:02}:{seconds:02}', end='\r')
    time.sleep(1)
print("time is up")

#nested loop
# outer loop iterates over a sequence, inner loop iterates over a sequence
# for each iteration of the outer loop, the inner loop iterates over its sequence
# inner loop completes all its iterations before the outer loop continues
# nested loops can be used to iterate over 2D data structures like lists of lists
# or to iterate over a list of lists of lists, etc.
# for example, to iterate over a 3D list of lists of lists, you would need
# three nested loops

# outer loop:
#        inner loop:

rows  = int(input("enter num of rows: "))
cols = int(input("enter num of columns: "))
symbol = input("enter symbol: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()
