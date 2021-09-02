from __future__ import annotations
from abc import ABC, abstractmethod


class FurnitureFactory(ABC):
    @abstractmethod
    def build_sofa(self):
        pass

    @abstractmethod
    def build_chair(self):
        pass


class VictorianFactory(FurnitureFactory):
    def build_sofa(self):
        return VictorianSofa()

    def build_chair(self):
        return VictorianChair()


class ModernFactrory(FurnitureFactory):
    def build_sofa(self):
        return ModernSofa()

    def build_chair(self):
        return ModernChair()


class Sofa(ABC):
    @abstractmethod
    def describe(self):
        pass


class VictorianSofa(Sofa):
    def describe(self):
        print('I am a victorian style sofa.')


class ModernSofa(Sofa):
    def describe(self):
        print('I am a modern style sofa.')


class Chair(ABC):
    @abstractmethod
    def describe(self):
        pass


class VictorianChair(Chair):
    def describe(self):
        print('I am a victorian style chair.')


class ModernChair(Chair):
    def describe(self):
        print('I am a modern style chair.')


def client_code(f: FurnitureFactory):
    # the client doesn't need to know what type of the factory it is
    # it calls the same function

    sofa = f.build_sofa()
    sofa.describe()

    chair = f.build_chair()
    chair.describe()


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(VictorianFactory())
    print()

    print("Client: Testing the same client code with the second factory type:")
    client_code(ModernFactrory())
