from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
from collections import defaultdict


class EventManager:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_type, listener):
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        self.listeners[event_type].remove(listener)

    def notify(self, event_type, data):
        for listener in self.listeners[event_type]:
            listener.update(data)


class Editor:
    def __init__(self):
        self.events = EventManager()

    def open_file(self, name):
        self.file = name
        self.events.notify("open", self.file)

    def save_file(self):
        self.events.notify("save", self.file)


class EventListener(ABC):
    @abstractmethod
    def update(self, filename):
        pass


class LoggingListener(EventListener):
    def __init__(self, log_filename, message):
        self.log = log_filename
        self.message = message

    def update(self, filename):
        print(f'{self.message} {filename}')


class EmailAlertsListener(EventListener):
    def __init__(self, email, message):
        self.email = email
        self.message = message

    def update(self, filename):
        print(f'{self.message} {filename}, sending email to {self.email}')


if __name__ == "__main__":
    editor = Editor()

    logger = LoggingListener(
        "/path/to/log.txt",
        "Someone has opened the file:")
    email_alerts = EmailAlertsListener(
        "admin@example.com",
        "Someone has changed the file:")
    editor.events.subscribe("open", logger)
    editor.events.subscribe("save", email_alerts)

    editor.open_file("test.txt")
    editor.save_file()
