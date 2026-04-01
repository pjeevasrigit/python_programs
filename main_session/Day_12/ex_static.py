# Static method - A method that belongs to class rather any objects from that class
# utlity

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return "{} : {}".format(self.name, self.position)

    @staticmethod
    def is_valid_position(position):   # ✅ added parameter + ()
        valid_positions = ["Manager", "Team lead", "Associate"]
        return position in valid_positions

# ✅ correct method call
print(Employee.is_valid_position("coook"))
employee1 = Employee("Mukesh","Manager")
employee2 = Employee("yukesh","Associate")

print(employee1.get_info())
print(employee2.get_info())