# input = this    is my     coding


s=input("Enter your sentence")
count = 0

for ch in reversed(s):
    if ch==" " and count ==0:  # this is my  sen___ #___nes    ym    dfgsdfg
        continue
    if ch==" ":
        break
    count=count+1  #3
print("length of last word:",count) ## 3