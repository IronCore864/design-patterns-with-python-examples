from abc import ABC, abstractmethod
from random import randint


class GameAI(ABC):
    def turn(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    def collect_resources(self):
        print('Collecting resources from built structures.')

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    def attack(self):
        """
        yet another template method of the same class
        """
        r1 = "No enemy found. Sending scouts."
        r2 = "Enemies found! Sending warriors."
        if randint(0, 1):
            print(r1)
        else:
            print(r2)

    def send_scouts(position):
        print('Default sending scout function.')

    def send_warriors(position):
        print('Default sending warrior function.')


class OrcsAI(GameAI):
    def build_structures(self):
        r1 = "Building farms, then barracks, then stronghold."
        r2 = "Not enough gold."
        if randint(0, 1):
            print(r1)
        else:
            print(r2)

    def build_units(self):
        r1 = "Build peon, add it to scouts group."
        r2 = "Build grunt, add it to warriors group."
        if randint(0, 1):
            print(r1)
        else:
            print(r2)

    def send_scouts(self, position):
        r1 = "Send scouts to position."
        r2 = "No scout available."
        if randint(0, 1):
            print(r1)
        else:
            print(r2)

    def send_warriors(position):
        r1 = "Send warriors to position."
        r2 = "No warrior available."
        if randint(0, 1):
            print(r1)
        else:
            print(r2)


class MonstersAI(GameAI):
    def collect_resources(self):
        print("Monsters don't collect resources.")

    def build_structures(self):
        print("Monsters don't build structures.")

    def build_units(self):
        print("Monsters don't build units.")


def client_code():
    orcs = OrcsAI()
    monsters = MonstersAI()
    steps = 5
    for i in range(1, steps+1):
        print(f'Turn {i}:')
        orcs.turn()
        print()
        monsters.turn()
        print()


if __name__ == "__main__":
    client_code()
