# Inheritance = Allows a class to inherit the attributes and method from another class

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF")
class Cat(Animal):
    def speak(self):
        print("MEOw")
class Mouse(Animal):
    def speak(self):
        print("Squeakkkk")

dog=Dog("Rocky")

dog.eat()
dog.sleep()
dog.speak()

cat=Cat("Tom")
cat.eat()
cat.speak()

mouse=Mouse("Jerry")
mouse.eat()
mouse.sleep()
mouse.speak()