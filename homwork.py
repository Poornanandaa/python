import math
class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
    def perimeter(self): pass
    def describe(self):
        print(f"This is a {self.name} shape.")
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def describe(self):
        print(f"This is a rectangle with width {self.width} and height {self.height}.")
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def describe(self):
        print(f"This is a square with side {self.width}.")
def print_shape_info(shape):
    shape.describe()
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
    print()
shapes = [Rectangle(5,10), Square(4)] 
for shape in shapes:
    print_shape_info(shape)   

