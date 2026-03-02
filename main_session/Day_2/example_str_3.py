username = input("Enter valid user name")

if len(username) > 12:
    print(" your name should not be more than 12")
elif username.find(" ")!= -1:
    print("Please remove white space")
else:
    print("Your username is valid")

username = "testingproject"
n = username.find(" ")
print(n)