#input = "This is my goals"

s = "python is a programming language"

words = s.split()  # python[0], is[1], a[2], programming[3],
for word in words:
    if len(word) % 2 == 0:
        print(word)