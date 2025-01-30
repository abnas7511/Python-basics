#multithreading : multiple threads are running concurrently
#                 good for I/O bound tasks like reading files or fetching data from APIs
#                 threadind.Thread(tarfet = my_fnc)


import threading
import time

def walk_dog(first,last):
    time.sleep(8)
    print(f"you finish walking the {first} {last}")

def take_outtrash():
    time.sleep(3)
    print("you take out the trash.")

def get_mail():
    time.sleep(5)
    print("you get the mail.")


#walk_dog()
#take_outtrash()
#get_mail()


chore1 = threading.Thread(target = walk_dog, args = ("Scooby","Doo")) #if we dont add comma after "scooby" it will be a string not a tuple and it'll return an error
chore1.start()

chore2 = threading.Thread(target = take_outtrash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

#by using thread we can run all the functions concurrently and it will take 8 seconds to finish all the functions 
#instead of 16 seconds

chore1.join()
chore2.join() #join() will wait for the thread to finish
chore3.join()

print("all chores are done")