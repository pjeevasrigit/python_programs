#Insertion sort - split and sort

arr = [7,14,5,3,2]
# 5,7,14,3,2
# 3,5,7,14,2

for i in range(1,len(arr)):
    curr = arr[i] # 5
    j = i-1 # 0

    while j>=0 and curr<arr[j]:
        arr[j+1] = arr[j] # 14
        j-=1
    arr[j+1] = curr

print(arr)