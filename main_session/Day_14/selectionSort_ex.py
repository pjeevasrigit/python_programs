#Selection sort

arr = [4,5,2,3,1]
# 2,4,5,3,1 ----> Iteration 2
# 2,3,4,5,1 ----> Iteration 3
# 1,2,3,4,5 ----> Iteration 4

# 1,2,3,4,5

for pos in range(len(arr)-1):
    min = pos # 0
    for i in range(pos+1,len(arr)):
        if arr[i]<arr[min]:
            min = i
    arr[min],arr[pos] = arr[pos],arr[min]
print(arr)