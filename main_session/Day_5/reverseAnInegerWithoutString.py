num = 123

reverse_num = 0

while num!=0:
    digit = num % 10 # digit = 3, digit = 2, digit = 1
    reverse_num = reverse_num * 10 + digit # reverse_num = 3, 30 + 2 = 32, 320 + 1 = 321
    num = num // 10 # num = 12 , num = 1, 0
print(reverse_num)