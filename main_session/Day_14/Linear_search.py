array = [10,28,31,42,52]

x= 31

for i in range(0,len(array)):
    if array[i] == x:
        print(i)
        break
else:
    print("X not found")