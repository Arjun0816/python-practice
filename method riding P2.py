class Shape:
    def area(self):
        print("area of shape")
class Circle(Shape):
    def area(self):
        print("pi r square")
class Square(Shape):
    def area(self):
        print("side square")
c1 = Circle()
s1 = Square()
c1.area()
s1.area()
