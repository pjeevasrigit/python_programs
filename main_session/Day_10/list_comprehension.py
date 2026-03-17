doubles = []
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

# doubles = [expression for value in iterable if condition ]

triples = [x*3 for x in range(1,11)]
print(triples)

number = [1,-2,3,-4,5,-6]
positive_numbers = [num for num in number if num>=0]
print(positive_numbers)