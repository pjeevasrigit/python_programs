import json

employee = {
    "name": "Jeevasri",
    "age": 20,
    "salary": 500,
    "job":"Associate"
}

file_path="file.json"

try:
    with open(file_path,"w") as file:
        json.dump(employee,file,indent=4)
        print("File created")
except IOError:
    print("File not created")
