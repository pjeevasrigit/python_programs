# input = "This is my first program"
# program first my is This

s=input("Enter the sentence")

words=s.split() # This [0],is[1],my[2],first[3],program[4]

#program = 5,0 1 2 3 4
# logic 1
for i in range(len(words)-1,-1,-1): # 4,-1,reverse -1
    print(words[i],end=" ")

print("____________________________-")
# Logic 2
words.reverse()
result = " ".join(words)
print(result)