num = int(input("Enter number between 1 to 10"))

while num<1 or num>10:
    print(f"You have not entered a valid number")
    num = input("Enter number between 1 to 10")

print(f"You have entered a valid number {num}")