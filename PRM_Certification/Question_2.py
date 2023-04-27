class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def validate_triangle(self):
       
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            print("Invalid triangle")
        else:
            print("Valid Triangle")
            

class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
    
    def validate_rectangle(self):
       
        if self.l > 0 and self.b > 0 and self.l == self.b:
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")

triangle_sides = input().split()
rectangle_sides = input().split()


triangle = Triangle(int(triangle_sides[0]), int(triangle_sides[1]), int(triangle_sides[2]))
rectangle = Rectangle(int(rectangle_sides[0]), int(rectangle_sides[1]))


triangle.validate_triangle()
rectangle.validate_rectangle()
