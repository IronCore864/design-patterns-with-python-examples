from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def accept(self, v: Visitor):
        pass


class Dot(Shape):
    def accept(self, v: Visitor):
        v.visit_dot(self)


class Circle(Shape):
    def accept(self, v: Visitor):
        v.visit_circle(self)


class Rectangle(Shape):
    def accept(self, v: Visitor):
        v.visit_rectangle(self)


class CompoundShape(Shape):
    def accept(self, v: Visitor):
        v.visit_compound_shape(self)


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, d: Dot):
        pass

    @abstractmethod
    def visit_circle(self, c: Circle):
        pass

    @abstractmethod
    def visit_rectangle(self, r: Rectangle):
        pass

    @abstractmethod
    def visit_compound_shape(self, cs: CompoundShape):
        pass


class XMLExportVisitor(Visitor):
    def visit_dot(self, d: Dot):
        print("Exporting the dot's ID and center coordinates in XML format.")

    def visit_circle(self, c: Circle):
        print("Exporting the circle's ID, center coordinates and, radius in XML format.")

    def visit_rectangle(self, r: Rectangle):
        print("Exporting the rectangle's ID, left-top coordinates, width and height in XML format.")

    def visit_compound_shape(self, cs: CompoundShape):
        print("Exporting the shape's ID as well as the list of its children's IDs in XML format.")


class JSONExportVisitor(Visitor):
    def visit_dot(self, d: Dot):
        print("Exporting the dot's ID and center coordinates in JSON format.")

    def visit_circle(self, c: Circle):
        print("Exporting the circle's ID, center coordinates and, radius in JSON format.")

    def visit_rectangle(self, r: Rectangle):
        print("Exporting the rectangle's ID, left-top coordinates, width and height in JSON format.")

    def visit_compound_shape(self, cs: CompoundShape):
        print("Exporting the shape's ID as well as the list of its children's IDs in JSON format.")


def client_code():
    all_shapes = [Dot(), Dot(), Circle(), Rectangle(), Rectangle()]

    export_visitor = XMLExportVisitor()
    for shape in all_shapes:
        shape.accept(export_visitor)

    print()

    export_visitor = JSONExportVisitor()
    for shape in all_shapes:
        shape.accept(export_visitor)


if __name__ == "__main__":
    client_code()
