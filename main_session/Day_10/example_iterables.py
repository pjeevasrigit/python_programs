# Iterables -
# Membership operation - in, not in

number = [1,2,3,4,5]

for num in number:
    print(num)

grades = {"sandy":"a",
          "Tom":"B",
          "Jerry":"c"}

student = input("Enter name of the student")

if student in grades:
    print(f"{student} Grade is {grades[student]}")
else:
    print (f"{student} was not found")