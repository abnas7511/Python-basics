import random

low  = 1
high  = 100

number = random.randint(low, high)
print("I'm thinking of a number between", low, "and", high)
print("Can you guess what it is?")
guess = 0
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess > number:
        print("Lower...")
    elif guess < number:
        print("Higher...")
    else:
        print("You guessed it!")
print("Thanks for playing the game.")



num = random.random() # 0.0 <= num < 1.0
print(num)

num = random.uniform(1, 100)   # this will generate a random float number between 1 and 100
print(num)

optons = ['rock', 'paper', 'scissors']
choice = random.choice(optons)
print(choice)

random.shuffle(optons)
print(optons)
