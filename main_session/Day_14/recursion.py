def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1) #5*4!, 4*3!, 3*2!,2*1!
                           # 2, 6, 24, 120

print(fact(5))