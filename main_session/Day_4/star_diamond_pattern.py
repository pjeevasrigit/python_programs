
n =5

for i in range(n-1):
    for j in range (i,n): # Decrement pattern
        print(".",end=" ")
    for k in range (i+1): # increment pattern
        print("*",end=" ")
    for k in range (i): # increment pattern
        print("*",end=" ")
    print()

for i in range(n):
    for k in range (i+1): # increment pattern
        print(".",end=" ")
    for j in range (i,n): # Decrement pattern
        print("*",end=" ")
    for j in range (i,n-1): # Decrement pattern
        print("*",end=" ")
    print()