#While loop - Indefinite loop

name = input("Enter your name")

while name=="":
    print("You did not enter any valid name, Try again")
    name = input("Enter your name")
print(f"Hello {name}")