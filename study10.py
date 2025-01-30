#2dlists: 2d lists are lists of lists. 
#   They are useful for representing matrices or tables.
#   The elements of a 2d list are arranged in rows and columns.
#   The first index is the row and the second index is the column.
#   The first element is at index 0.
#   The first row is at index 0.
#   The first column is at index 0.
#   The last row is at index -1.
#   The last column is at index -1.
#   The last element is at index -1.
#   The number of rows is len(list).
#   The number of columns is len(list[0]).
#   The number of elements is len(list) * len(list[0]).
#   The number of elements in a row is len(list[0]).
#   The number of elements in a column is len(list).



friuts = [['apple', 'banana', 'cherry'], 
          ['date', 'fig', 'grape'], 
          ['kiwi', 'lemon', 'mango']]

print(friuts)
print(friuts[0])
print(friuts[1])
print(friuts[2])
print(friuts[0][0])
print(friuts[0][1])

for collection in friuts:
    for item in collection:
        print(item, end=" ")
    print()

numpad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ("*",0,"#"))

for row in numpad:
    for key in row:
        print(key, end=" ")
    print()


#python quiz

questions = ("What is the capital of France?",
             "What is the capital of Italy?",
             "What is the capital of Spain?",
             "What is the capital of Germany?",
             "What is the capital of Portugal?")

options = (("A.Paris", "B.Marseille", "C.Lyon"),
           ("A.Rome", "B.Milan", "C.Naples"),
           ("A.Madrid", "B.Barcelona", "C.Valencia"),
           ("A.Berlin", "B.Hamburg", "C.Munich"),
           ("A.Lisbon", "B.Porto", "C.Faro"))

answers = ("A", "A", "A", "A", "A")

guesses = []
score = 0 
question_num  = 0

#for question,option in zip(questions,options):
    #print(question)
    #for opt in option:
        #print(opt)




for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("(A , B , C , D): ").upper()
    guesses.append(guess)
    print()
    if guess == answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print("The correct answer is: ", answers[question_num])
    question_num+=1
    print()


print("-----------------")
print("Your score is: ", score, "/", len(questions))
print("-----------------")