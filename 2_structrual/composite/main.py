from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Item(ABC):
    @property
    def parent(self) -> Item:
        return self._parent

    @parent.setter
    def parent(self, parent: Item):
        self._parent = parent

    def add(self, Item: Item) -> None:
        pass

    def remove(self, Item: Item) -> None:
        pass

    @abstractmethod
    def price(self) -> int:
        pass


class Phone(Item):
    def price(self) -> int:
        return 5000


class Charger(Item):
    def price(self) -> int:
        return 200


class Receipt(Item):
    def price(self) -> int:
        return 0


class Box(Item):
    def __init__(self) -> None:
        self._children: List[Item] = []

    def add(self, Item: Item) -> None:
        self._children.append(Item)
        Item.parent = self

    def remove(self, Item: Item) -> None:
        self._children.remove(Item)
        Item.parent = None

    def price(self) -> str:
        res = 10 if len(self._children) == 1 else 30
        for child in self._children:
            res += child.price()
        return res


if __name__ == "__main__":
    box = Box()

    small_box1 = Box()
    small_box1.add(Phone())
    small_box1.add(Charger())

    small_box2 = Box()
    small_box2.add(Receipt())

    box.add(small_box1)
    box.add(small_box2)

    print(box.price())
