# Encapsulation:
    # Bundling Data and the methods that operate on it.
    # and restricting direct access to it.

# Abstraction:
    # Hiding Implementation details and exposing only
    # what's necessary. python uses "abc" module for this.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        a = self.length * self.width
        return f"Area of Rectangle is {a}"

    def perimeter(self):
        p = (2*self.length) + (2*self.width)
        return f"Perimeter of Rectangle is {p}"
s1 = Rectangle(5, 3)
# print(s1.area()) 

#-----------------------------------

class Shape:
    from math import pi
    def __init__(self, type_of_shape):
        self.tos = type_of_shape

    def area(self):
        if self.tos == "Square":
            side = eval(input("Enter side: "))
            a = side * 4
        elif self.tos == "Circle":
            radius = eval(input("enter a radius of circle: "))
            a = self.pi * (radius ** 2 )
        return f"Area : {a}"

# class Circle(Shape):
#     pass

# c1 = Circle("Circle")
# print(c1.area())
        

# class Square(Shape):
#     pass

# s1 = Square("Square")
# print(s1.area())
