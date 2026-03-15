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

while True:
    sub = input("Select a subject (q to quit): ")

    if sub == 'q':
        break

    if sub in marks:
        total += marks[sub]
        subjects.append(sub)
        print(f"{sub} added")
    else:
        print("Subject not found")

print()
print("Selected subjects:", subjects)
print(f"Total Marks is {total:.2f}")