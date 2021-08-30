from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: Component, event: str):
        pass


class AuthenticationDialog(Mediator):
    def __init__(self):
        self.title = ''

    def notify(self, sender, event):
        if sender.name == 'login_or_register_checkbox' and event == 'check':
            if randint(0, 1):
                self.title = 'Log in'
                print('Showing login form components.')
                print('Hiding registration form components.')
            else:
                print('Showing registration form components.')
                print('Hiding login form components.')

        if sender.name == 'ok_button' and event == 'click':
            if randint(0, 1):
                print('Trying to find a user using login credentials.')
                print('Logged in.')
            else:
                print('Create a user account using data from the registration fields.')
                print('Log that user in.')


class Component:
    def __init__(self, dialog, name):
        self.dialog = dialog
        self.name = name

    def click(self):
        self.dialog.notify(self, 'click')

    def keypress(self):
        self.dialog.notify(self, 'keypress')


class Button(Component):
    def check(self):
        self.dialog.notify(self, 'click')


class Checkbox(Component):
    def check(self):
        self.dialog.notify(self, 'check')


def client_code():
    d = AuthenticationDialog()
    login_or_register_checkbox = Checkbox(d, 'login_or_register_checkbox')
    ok_button = Button(d, 'ok_button')

    tests = 3
    for i in range(1, tests+1):
        print(f'Test {tests}')
        login_or_register_checkbox.check()
        ok_button.click()
        print()


if __name__ == '__main__':
    client_code()
