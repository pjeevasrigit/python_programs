#Super() = function used in child to call methods of parent

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
    def describe(self):
        super().describe()
        print(f"Area of circle is {3.14*self.radius*self.radius}")

circle=Circle("red",True,5)

print(circle.color)
circle.describe() #It is red and filled
