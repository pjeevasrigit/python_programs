#Property - Decorator used to define method as property, getter, setter, deleter

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return "Your width is {}".format(self._width)

    @property
    def height(self):
        return "Your height is {}".format(self._height)

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Your width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print("Your width must be greater than 0")

    @height.deleter
    def height(self):
        del self._height
        print("Height is deleted")


rectangle = Rectangle(-1, 200)
print(rectangle.width)
print(rectangle.height)

del rectangle.height

print(rectangle.width)
print(rectangle.height)