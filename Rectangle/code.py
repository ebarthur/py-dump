from math import sqrt

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def diagonal_length(self):
        return sqrt(self.length**2 + self.width**2)

# Create an object from the class with length 40 and width 30
rectangle_object = Rectangle(40, 30)

# Calculate and print area, perimeter, and diagonal length
print("Area:", rectangle_object.area())
print("Perimeter:", rectangle_object.perimeter())
print("Diagonal Length:", rectangle_object.diagonal_length())
