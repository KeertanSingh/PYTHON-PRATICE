# inheritence


class Quadrilateral:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print("Quadrilateral is created")

    def get_type(self):
        return 'Quadrilateral'


class Rectangle(Quadrilateral):
    def __init__(self, length, breadth):
        Quadrilateral.__init__(self, length, breadth)
        print("Rectangle is created!!")

    def get_area(self):
        return self.length * self.breadth

    def get_type(self):
        return 'rectangle'


class Square(Quadrilateral):
    def __init__(self, length, breadth):
        # Quadrilateral.__init__(self, length, breadth)
        super(Square, self).__init__(length, breadth)
        self.length = self.breadth
        print("Square is created!!")

    def get_area(self):
        return self.length * self.breadth

    def get_type(self):
        return 'square'


rect = Rectangle(100, 30)
sq = Square(10, 10)

print(sq.get_area())
area = rect.get_area()
print(area)
print(rect.get_type())
print(sq.get_type())
