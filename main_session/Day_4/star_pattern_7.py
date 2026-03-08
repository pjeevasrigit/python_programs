n = 5

for i in range(n):
    for j in range(i,n): # i = 0 -> j = 0,1,2,3,4 | # i = 1 -> j = 0,1,2,3
        #print(" ",end=" ")
        print(".", end=" ")
    for l in range(i): # i = 0 -> l = 0
        #print(l, end=" ")
        print("*",end=" ")
    for k in range(i+1): # k = 0 -> l =
        print("*",end=" ")
        # print(k, end=" ")
    print()