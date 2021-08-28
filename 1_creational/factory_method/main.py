from __future__ import annotations
from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

    def go(self):
        print('Creating plan ...')
        self.create_transport()
        print('Starting to deliver ...')
        self.deliver()


class RoadLog(Logistics):
    def create_transport(self):
        self.t = Truck()
        print('A truck is created.')

    def deliver(self):
        self.t.deliver()


class SeaLog(Logistics):
    def create_transport(self):
        self.s = Ship()
        print('A ship is created.')

    def deliver(self):
        self.s.deliver()


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        print('The good is delivered by a **truck**!')


class Ship(Transport):
    def deliver(self):
        print('The good is delivered by a **ship**!')


def client_code(log: Logistics):
    log.go()


if __name__ == "__main__":
    client_code(RoadLog())
    print()
    client_code(SeaLog())
