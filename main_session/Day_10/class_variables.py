#Class Variables
class Student:
    class_year = 2024
    num_of_students = 0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_of_students+=1

student1 = Student("Jeeva",25)
student2 = Student("Mukesh",26)
student3 = Student("Yukesh",26)
student4 = Student("Teju",26)

print(student1.name)
print(student2.name)
print(student2.class_year)
print(student1.class_year)
print(Student.class_year)
print(Student.num_of_students)