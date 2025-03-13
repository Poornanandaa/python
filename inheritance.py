class Shape:
    def __init__(self, type)
        self._type = type
    def area(self):
        return 0
    def perimeter(self):
        return 0
class Rectangle(Shape):
    def __init__(self, width, height):   
        super().__init__("Rectangle")
        self._width = width
        self._height = height
    def area(self):
        return self._width * self._height 
    def perimeter(self):
        return 2 * (self._width + self._height)
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self._type = "Square"
shapes = [Rectangle(13, 21), Square(10)]
for shape in shapes:
    print(f"{shape._type} - Area: {shape.area()}, Perimeter: {shape.perimeter()}")
