from abc import ABC, abstractmethod


class Shape:
    def __init__(self, source):
        self.X = source.X
        self.Y = source.Y
        self.color = source.color()

    @abstractmethod
    def clone():
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_from_source(self, source):
        return Rectangle(source.width, source.height)

    def clone(self):
        return self.create_from_source(self)


class Circle(Shape):
    def __init__(self, x, y, r):
        self.X = x
        self.Y = y
        self.radius = r

    def create_from_source(self, source):
        return Circle(source.X, source.Y, source.radius)

    def clone(self):
        return self.create_from_source(self)


def client_code():
    shapes = []

    circle = Circle(10, 10, 20)
    shapes.append(circle)

    another_circle = circle.clone()
    shapes.append(another_circle)

    rectangle = Rectangle(10, 20)
    shapes.append(rectangle)
    print(shapes)

    shapes_copy = []
    for shape in shapes:
        shapes_copy.append(shape.clone())

    print(shapes_copy)


if __name__ == '__main__':
    client_code()
