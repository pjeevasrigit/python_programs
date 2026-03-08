n = 5

for i in range(n):
    for j in range (i+1): # i = 0 -> 0 # i = 1 = 0 , 1
        print(' ',end = " ")
       # print('.', end=" ")
    for k in range (i,n): # i = 0 -> 0,5 i = 1 -> 1,2,3,4
        print('*',end = " ")
        #print(k, end=" ")
    print()