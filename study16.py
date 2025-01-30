
#inheritance : allows to define a class that inherits all the methods and properties from another class
# parent class : the class being inherited from
# child class : the class that inherits from another class
# child(parent) / sub(super) class

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal): #child class
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal): #child class
    def speak(self):
        print(f"{self.name} is meowing")

class Rat(Animal): #child class
    def speak(self):
        print(f"{self.name} is squeaking")

dog = Dog('Spike')
cat= Cat('Tom')
rat = Rat('Jerry')

print(dog.name)
print(cat.name)
print(rat.name)
#accessing methods of parent class from child class
dog.eat()
cat.sleep()
rat.eat()
#accessing methods of child class
dog.speak()
cat.speak()
rat.speak()


#multiple inheritance : a class can be derived from more than one base classes
# class Child(Parent1,Parent2,Parent3):
#     pass
class Prey():
    def flee(self):
        print("Prey is fleeing")

class Predator():
    def hunt(self):
        print("Predator is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey): #multiple inheritance
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()


    