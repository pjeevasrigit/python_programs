# s = "This is my first program"
# T:1 i:3 m:1

s = input("Enter a sentence")
freq = {}

for ch in s: #----> T
    if ch in freq:
        freq[ch]+=1 # i = 2,s = 2,
    else:
        freq[ch] = 1 # T = 1,h = 1, i = 1, s=1

for key,value in freq.items():
    print(key,":",value)

