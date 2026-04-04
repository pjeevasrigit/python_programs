# File exists
import os

#file_path = "test.txt" #Releative path

file_path="C:/Users/ADMIN/OneDrive/Desktop/t8hjbkjhjh.txt.txt" #Absolute path

if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")

