class Rectangle:
    type = 'quadrilateral'

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return f"Area : {self.length * self.breadth}"

    def perimeter(self):
        return f"Perimeter : {(self.length + self.breadth) * 2}"

    def update_length(self, newlength):
        self.length = newlength


rect1 = Rectangle(12, 10)
rect2 = Rectangle(2, 2)

rect1.update_length(90992)
print(rect1.length)
print(rect1.area())
print(rect1.perimeter())
print(rect2.perimeter())
