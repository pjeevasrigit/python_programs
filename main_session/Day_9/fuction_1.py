# function = block of reusable code

name = "Teju"
print(f"Happy Birthday {name}")

def happy_birthday(firstname):
    print(f"Happy Birthday {firstname}")

happy_birthday("Jeevasri")
happy_birthday("Mukesh")
happy_birthday("Tejasvi")

def happy_birthday(fname,age):
    print(f"Happy Birthday {fname}:")
    print(f"Your age is {age}:")

happy_birthday("Jeeva",20)
happy_birthday("Mukesh",21)
happy_birthday("Tejasvi",8)