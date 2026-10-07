# OOP:
    # Object Oriented Programming Paradigm:

    # class => Blueprints of Objects
    # Instance => A single object of a class

    # Claases contain:
        # Head of the class,
        # Constructor
        # different types of Input parameters
        # different types of methods
        # getters / setters
        # decorators

#------------------------Class

# class Circle:
#     pi = 3.14                     # Class Variable

#     def __init__(self, radius):    
#         self.radius = radius      # Instance Variable

#     def area(self):               # Instance Method
#         a = self.pi * (self.radius**2)
#         return a

#     def perimeter(self):          # Instance Method
#         p = 2* self.pi * self.radius
#         return p

# c1 = Circle(10)
# print(c1.area())
# print(c1.perimeter())


#-------------------- Types of Variables:

    # Instance Variable
        # Public Instance Variable
        # Protected Instance Variable
        # Private Instance Variable

    # Class Variable

    # Static Variable

# ---------------- Type of Methods:
    # Instance Method
        # Public
        # Protected
        # Private
    # Class Method

    # Static Method

#--------------------------class

class Cuboid:
    color = "Pink"
    company = "Valsad Cuboid Makers."

    def __init__(self, length, width, height):
        self.l = length   # public
        self._w = width   # protected
        self.__h = height # height

    def __area_of_side(self, side1, side2):
        a = side1 * side2
        return a

    def volume(self):
        area_l_w = self.__area_of_side(self.l, self._w)
        area_l_h = self.__area_of_side(self.l, self.__h)
        area_w_h = self.__area_of_side(self._w, self.__h)
        v = (2*area_l_w) + (2*area_l_h) + (2*area_w_h)
        return v
    
cu1 = Cuboid(5, 2, 3)
print(f"Volume of cu1: {cu1.volume()}")
print(cu1.l)
print(cu1._w)
print(cu1.__h)