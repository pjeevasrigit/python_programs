#1534 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3

# check given number is armstrong number
number = int(input("Enter the number"))
length = len(str(number))

temp = number
s = 0 #sum of digits

while temp > 0:
    digit = temp % 10
    s = s + digit ** length
    temp = temp // 10

if s==number:
    print("It is Armstrong number")
else:
    print("It is not Armstrong number")

# print valid Armstrong number from 0 t0 200
