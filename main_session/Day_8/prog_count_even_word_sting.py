s = "This is my coding and I love coding coding"
word = "coding"
count = 0

words = s.split()

for w in words:
    if w == word:
        count += 1

print(f"Word is found {count} times")