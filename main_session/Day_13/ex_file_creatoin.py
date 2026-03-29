#Write to a file

employee = ["Mukesh","Rajesh","Suresh","Venky"]

test_data = "This is my first notepad"

file_path = "output1.txt"
#file_path="C:/Users/ADMIN/OneDrive/Desktop/testfile.txt" #Absolute path

try:
    with open(file_path, "w") as file: # W - write, r - read, a - append
        for employee in employee:
            file.write(employee + "\n")
        #file.write(test_data)
        print("File created")
except IOError:
    print("File already exists")