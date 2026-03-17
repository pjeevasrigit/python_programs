import random

low = 1
high = 100

#number = random.randint(1,20)

number = random.randint(low,high)
print(number)

options = ("rock","paper","scissor")
option = random.choice(options)
print(option)