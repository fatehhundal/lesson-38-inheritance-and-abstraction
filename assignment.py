class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        print(self.width * self.height)
    
    def perimeter(self):
        print(2 * (self.width + self.height))
    
class Triangle(Shape):
    def __init__(self, base, height, slope):
        self.base = base
        self.height = height
        self.slope = slope
    
    def area(self):
        print(0.5 * (self.base * self.height))
    
    def perimeter(self):
        print(self.base + (2 * self.slope))

class Parallelogram(Shape):
    def __init__(self, width, height, slope):
        self.width = width
        self.height = height
        self.slope = slope
    
    def area(self):
        print(self.width * self.height)
    
    def perimeter(self):
        print(2 * (self.width + self.slope))

class Trapezium(Shape):
    def __init__(self, base1, base2, height, slope):
        self.baseone = base1
        self.basetwo = base2
        self.height = height
        self.slope = slope
    
    def area(self):
        print(0.5 * (self.baseone + self.basetwo) * self.height)
    
    def perimeter(self):
        print(self.baseone + self.basetwo + (2 * self.slope))

r = Rectangle(20, 13)
r.area()
r.perimeter()

print("\n")

tg = Triangle(8, 15, 17)
tg.area()
tg.perimeter()

print("\n")

p = Parallelogram(18, 22, 25)
p.area()
p.perimeter()

print("\n")

tz = Trapezium(13, 31, 25, 27)
tz.area()
tz.perimeter()