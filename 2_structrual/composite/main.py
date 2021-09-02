from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Graphic(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def draw(self):
        pass


class Dot(Graphic):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print(f'Draw a dot at {self.x} and {self.y}.')


class Circle(Dot):
    def __init__(self, x, y, radius):
        self.x, self.y, self.radius = x, y, radius

    def draw(self):
        print(
            f'Draw a Circle at {self.x} and {self.y} with radius {self.radius}')


class CompoundGraphic(Graphic):
    def __init__(self):
        self.children = []

    def add(self, child: Graphic):
        self.children.append(child)

    def remove(self, child: Graphic):
        self.children.remove(child)

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        for child in self.children:
            child.draw()


class ImageEditor:
    def load(self, components: List[Graphic]):
        self.all = CompoundGraphic()
        for c in components:
            self.all.add(c)

    def show(self):
        self.all.draw()

    def group_selected(self, components: List[Graphic]):
        group = CompoundGraphic()
        for c in components:
            group.add(c)
            self.all.remove(c)
        self.all.add(group)
        self.all.draw()


def client_code():
    d1, d2, d3 = Dot(1, 2), Dot(3, 4), Dot(5, 6),
    c1, c2 = Circle(5, 3, 10), Circle(4, 2, 5)
    components = [d1, d2, d3, c1, c2]

    ie = ImageEditor()
    ie.load(components)
    ie.show()

    print()

    ie.group_selected([d1, d2])


if __name__ == "__main__":
    client_code()
