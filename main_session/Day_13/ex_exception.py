#Exception - An event that interrupts a flow of the code

try:
    number = int(input("Enter any number"))
    print (1/number)

except ZeroDivisionError:
    print("Division by zero is invalid")
except NameError:
    print("Invalid input")
finally:
    print("Goodbye")