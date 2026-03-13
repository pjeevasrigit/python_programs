
# 0,1,1,2,3,5,8

num1= 0
num2=1

series = int(input("Enter your range"))
print (num1 , num2 )

for i in range(0,series):
    num3 = num1 + num2
    print(num3, end =" ")
    num1 = num2
    num2=num3