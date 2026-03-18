# Multiple Inheritance -> one child, Many Parents

class Prey:
    def move(self):
        print("This animal is moving")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Eagle(Predator):
    pass

class Frog(Prey,Predator):
    pass

rabbit=Rabbit()
eagle=Eagle()
frog=Frog()
prey=Prey()

rabbit.move()
eagle.hunt()
frog.move()
frog.hunt()
prey.move()

