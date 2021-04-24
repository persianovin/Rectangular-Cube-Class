class Rectangle:

    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def circumference(self):
        return 2*(self.l + self.w)

    def cube_volume(self, h):
        return self.area()*h

    def cube_surface(self, h):
        return 2*(self.l*h + self.l*self.w + self.w*h)


length, width, height = map(float, input('Enter dimensions: ').split())

shape = Rectangle(length, width)

print('Area:', shape.area())
print('Circumference:', shape.circumference())
print('Cube volume:', shape.cube_volume(height))
print('Cube surface:', shape.cube_surface(height))
