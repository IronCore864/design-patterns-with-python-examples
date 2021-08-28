from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class HouseBuilder(ABC):
    @property
    @abstractmethod
    def house(self):
        pass

    def build_wall(self):
        self._house.add("walls")

    def build_door(self):
        self._house.add("doors")

    def build_window(self):
        self._house.add("windows")

    def build_roof(self):
        self._house.add("roof")

    @abstractmethod
    def build_other(self):
        pass


class HouseWithGarageBuilder(HouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    @property
    def house(self):
        house = self._house
        self.reset()
        return house

    def build_other(self):
        self._house.add("garage")


class HouseWithPoolBuilder(HouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    @property
    def house(self):
        house = self._house
        self.reset()
        return house

    def build_other(self):
        self._house.add("pool")


class House():
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"House has: {', '.join(self.parts)}")


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: HouseBuilder):
        self._builder = builder

    def go(self):
        self.builder.build_wall()
        self.builder.build_door()
        self.builder.build_window()
        self.builder.build_roof()
        self.builder.build_other()


if __name__ == "__main__":
    d = Director()

    garage_house_builder = HouseWithGarageBuilder()
    d.builder = garage_house_builder
    d.go()
    garage_house_builder.house.list_parts()
    print()

    pool_house_builder = HouseWithPoolBuilder()
    d.builder = pool_house_builder
    d.go()
    pool_house_builder.house.list_parts()
    print()

    # the builder pattern can be used without a Director class.
    print("Custom house:")
    garage_house_builder.build_door()
    garage_house_builder.build_wall()
    garage_house_builder.build_roof()
    print('No window, no garage, no pool, no life.')
    garage_house_builder.house.list_parts()
