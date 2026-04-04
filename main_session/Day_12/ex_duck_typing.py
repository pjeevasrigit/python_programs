#Duck Typing - another way to achecive polymorphishm
# object must have minimum necessadry attirbutes / method
# I tlooks like a duck and quacks like a duck
class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!!")

class Cat(Animal):
    def speak(self):
        print("MEOW!!")

class Car:
    alive = False
    def speak(self):
        print("Horn!!!")

animals = [Dog(),Cat(),Car()]
for animal in animals:
    animal.speak()