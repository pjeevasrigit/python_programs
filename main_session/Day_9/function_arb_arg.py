# Arbitary Arguments
# ** kwargs
# * args


def add(*args):
    total=0
    for arg in args:
        total +=arg
    return total



print(add(1,2,3,4,5))


def print_address(**kwargs):
    for key,val in kwargs.items():
        print(f"{key}: {val}")

print_address(street = "123 fake st",
              city="Bangalore",
            state="KN")