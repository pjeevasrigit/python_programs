marks = {
    "Science": 80.5500000,
    "Maths": 90,
    "Physics": 85,
    "English": 75,
    "Hindi": 80
}

subjects = []
total = 0

for key, value in marks.items():
    print(f"{key:10} - {value:.2f}")
    total += value
    subjects.append(key)

print("Total Marks:", total)
print("Subjects:", subjects)