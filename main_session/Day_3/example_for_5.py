
# Palidrome - Madam
word = input("Enter any word")
output = ""

if word == word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")