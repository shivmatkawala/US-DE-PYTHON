class A:
    def a(self):
        print("I am A")

class B(A):
    def b(self):
        print("I am B")

class C(B):
    def c(self):
        print("I am C")

c1 = C()
c1.c()
c1.b()
c1.a()

# print(C.mro())

#-------------------------------

class Car:
    country = "India"
    def __init__(self, model, brand, color):
        self.m = model
        self.b = brand
        self.c = color

    @classmethod
    def car_orgin_country(cls):
        return f"Car is originated in {cls.country}"

    @staticmethod
    def greet(name):
        return f"Hello {name}"    

    def car_info(self):
        return f"Model:{self.m}\nBrand:{self.b}\nColor:{self.c}"
    