# Multi level Inheritance -> one child, Many Parents
class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} animal is eating")
    def sleep(self):
        print(f"{self.name} animal is sleeping")

class Prey(Animal):
    def move(self):
        print("This animal is moving")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass

class Eagle(Predator):
    pass

class Frog(Prey, Predator):
    pass

rabbit = Rabbit("child rabbit")
eagle = Eagle("child eagle")
frog = Frog("greenFrog")
prey = Prey("parent prey")

rabbit.move()
eagle.hunt()
frog.move()
frog.hunt()
prey.move()
rabbit.eat()


