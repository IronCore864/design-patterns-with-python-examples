from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class NavigationApp():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def navigate(self) -> None:
        self._strategy.get_route()


class Strategy(ABC):
    @abstractmethod
    def get_route(self):
        pass


class DrivingStrategy(Strategy):
    def get_route(self):
        print('Drive 1 km then your destination is on your right.')


class WalkingStrategy(Strategy):
    def get_route(self):
        print('Walk 10 minutes and your destination is on your right.')


class PublicTransportStrategy(Strategy):
    def get_route(self):
        print('No public transport available to your destination.')


if __name__ == "__main__":
    # client code
    app = NavigationApp(PublicTransportStrategy())
    app.navigate()

    app.strategy = WalkingStrategy()
    app.navigate()

    app.strategy = DrivingStrategy()
    app.navigate()
