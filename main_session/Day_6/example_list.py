# List - [], order, changeable, Duplicates
# Set - {} - unordered, immutable, Add / Remove, No Duplicates
# Tuples - () order, unchangable, Duplicates

n = [1,2,2,4,5]
fruits = ["Cherry","Apple","Banana","Manago","Orange","Cherry"]

print(fruits)

for fruit in fruits:
    print(fruit)

print(f"First element is {fruits[0]}")

print(len(fruits))

#fruits.append("pineApple")
#print(fruits)

#fruits.remove("Apple")
#print(fruits)

fruits.insert(2,"Tomato")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

#fruits.clear()
#print(fruits)

print(fruits.index("Apple"))
#print(fruits.index("Apple234234234"))

print(fruits.count("Cherry"))

fruits.pop()
print(fruits)