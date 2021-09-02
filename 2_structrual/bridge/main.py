from __future__ import annotations
from abc import ABC, abstractmethod


class RemoteControl:
    def __init__(self, device):
        self.device = device

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)


class Device:
    def __init__(self):
        self.volume = 0

    def set_volume(self, v):
        self.volume = v

    def get_volume(self):
        return self.volume


class TV(Device):
    def __init__(self):
        super().__init__()


class Radio(Device):
    def __init__(self):
        super().__init__()


def client_code():
    tv = TV()
    remote = RemoteControl(tv)
    remote.volume_up()
    print(tv.get_volume())

    radio = Radio()
    remote = AdvancedRemoteControl(radio)
    remote.volume_up()
    print(radio.get_volume())
    remote.mute()
    print(radio.get_volume())


if __name__ == "__main__":
    client_code()
