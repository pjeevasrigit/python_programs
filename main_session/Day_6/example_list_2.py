
groceries = (("apple", "banana", "pineapple", "cherry"),
             ("carrot", "beans", "radish",    "tomato"),
             ("lotus",  "lily",   "rose",     "jasmine"))

for items in groceries:
    for food in items:
        print(food) #print indivual items

for items in groceries:
    print(items) #print seperate rows