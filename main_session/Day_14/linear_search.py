arr = [1,3,4,6,7,8]
x = 3

for i in range(0,len(arr)):
    if arr[i] == x:
        print(i)
        break
else:
    print("Element not found")