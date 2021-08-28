from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self):
        pass


class Component(ComponentWithContextualHelp):
    def __init__(self):
        self.tooltip_text = ''
        self.container = None

    def show_help(self):
        if hasattr(self, 'tooltip_text') and self.tooltip_text:
            print(self.tooltip_text)
        else:
            print(
                f"{type(self).__name__} {self.name} has no help, showing its container's help: ")
            self.container.show_help()


class Container(Component):
    def __init__(self):
        super().__init__()
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.container = self


class Button(Component):
    def __init__(self, x1, y1, x2, y2, name):
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2
        self.name = name


class Panel(Container):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2

    def show_help(self):
        if self.modal_help_text:
            print(f'Showing panel help: {self.modal_help_text}')
        else:
            super().show_help()


class Dialog(Container):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def show_help(self):
        if self.wiki_page_URL:
            print(f'Opening wiki help page, URL: {self.wiki_page_URL}...')
        else:
            super().showHelp()


def client_code():
    dialog = Dialog("Budget Reports")
    dialog.wiki_page_URL = "https://wikipedia.com"

    panel = Panel(0, 0, 400, 800)
    panel.modal_help_text = "This panel does xyz."

    ok = Button(250, 760, 50, 20, "OK")
    ok.tooltip_text = "This is an OK button."

    cancel = Button(320, 760, 50, 20, "Cancel")

    panel.add(ok)
    panel.add(cancel)

    dialog.add(panel)

    # mouse on dialog:
    dialog.show_help()
    # mouse on OK button:
    ok.show_help()
    # mouse on Cancel button which doesn't have a tooltip_text, so showing its container's help:
    cancel.show_help()


if __name__ == "__main__":
    client_code()
