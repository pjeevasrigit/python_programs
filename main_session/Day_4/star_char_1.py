
n = 5

for i in range(n):
    p = 97
    for j in range(i+1):
        print(chr(p),end=" ")
        p=p+1
    print()


# A - Z -----> 65 - 90
# a - z -----> 97 - 122
# 0 - 9 -----> 48 - 52