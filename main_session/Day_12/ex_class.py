# Class Method: Allow operations related to the class
class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1   

    # instance method
    def get_info(self):
        return "{} : {}".format(self.name, self.gpa)

    # class method
    @classmethod
    def get_count(cls):
        return cls.count

# Before creating objects
print(Student.get_count())  # Output: 0

# Create objects
s1 = Student("Teju", 3.2)
s2 = Student("Maya", 3.8)

# After creating objects
print(Student.get_count())  # Output: 2