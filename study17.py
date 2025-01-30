#multilevel inheritance : a class can be derived from another derived class
# C(B) <- B(A) <- A()

class Animal(): #base class
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f" {self.name} is eating")

    def sleep(self):
        print(f" {self.name} is sleeping")

class Prey(Animal): #child class
    def flee(self):
        print(f" {self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f" {self.name} is hunting")

class Rabbit(Prey): #grand-child class
    pass

class Hawk(Predator):
    pass

class Fish(Predator,Prey): #multiple inheritance
    pass


#rabbit = Rabbit()
#hawk = Hawk()
#fish = Fish()

#rabbit.flee() #accessing methods of parent class from child class
#hawk.hunt()
#fish.flee() 
#fish.hunt() 

#rabbit.eat() #accessing methods of grand-parent class from child class
#hawk.eat()
#fish.eat()
#rabbit.sleep()
#hawk.sleep()
#fish.sleep()


rabbit2 = Rabbit('Bugs')
hawk2 = Hawk('Tweety')
fish2 = Fish('Nemo')

rabbit2.eat()
hawk2.eat()
fish2.sleep()


