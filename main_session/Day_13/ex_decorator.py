#Decorator - A function extends without modifying the behaviour of the existing function

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_chocolate(func):
    def wrapper(*args, **kwargs):
        print("Adding chocolate")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_chocolate
def ice_cream(flavor):
    print ("This is Ice Cream")

ice_cream("vanilla")