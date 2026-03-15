#### {Key,Value} - pair

# ordered and changeble, No duplicates (keys)

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijng",
            "Russia":"Moscow"}

print(capitals)

print(capitals.get("Russia"))

if capitals.get("Russia123"):
    print("This capital exists")
else:
    print("This capital does not exists")

capitals.update({"Russia":"Moscow2"})
print(capitals)

#capitals.pop("China")
#print(capitals)

#capitals.clear()
#print(capitals)

for i in capitals.keys():
    print(i)

for val in capitals.values():
    print(val)

for key,val in capitals.items():
    print(f"{key} - {val}")