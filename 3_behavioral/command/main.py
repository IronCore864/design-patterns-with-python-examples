from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, app: Application, editor: Editor):
        self.app = app
        self.editor = editor
        self.backup = ""

    def save_backup(self):
        self.backup = self.editor.text

    def undo(self):
        self.editor.text = self.backup

    @abstractmethod
    def execute(self):
        pass


class CutCommand(Command):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True


class PasteCommand(Command):
    def execute(self):
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)
        return True


class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        return False


class Editor:
    def __init__(self, text):
        self.text = text

    def get_selection(self):
        return self.text

    def delete_selection(self):
        self.text = ''

    def replace_selection(self, text):
        self.text = text


class CommandHistory:
    def __init__(self):
        self.history = []

    def push(self, c):
        self.history.append(c)

    def pop(self):
        return self.history.pop()


class Application:
    def __init__(self, editor, history):
        self.editor = editor
        self.history = history
        self.clipboard = ""

    def cut(self):
        self.execute_command(CutCommand(self, self.editor))

    def paste(self):
        self.execute_command(PasteCommand(self, self.editor))

    def undo(self):
        self.execute_command(UndoCommand(self, self.editor))

    def test(self):
        print(f'current editor text: {self.editor.text}')
        print('select all words and press cut key or ctrl + x')
        self.cut()
        print(f'current editor text: {self.editor.text}')
        print(f'current clipboard: {self.clipboard}')
        print('press paste key or ctrl + v')
        self.paste()
        print(f'current editor text: {self.editor.text}')
        print('press undo key or ctrl + z')
        self.undo()
        print(f'current editor text: {self.editor.text}')

    def execute_command(self, command):
        if command.execute():
            self.history.push(command)

    def undo(self):
        command = self.history.pop()
        if command:
            command.undo()


if __name__ == "__main__":
    editor = Editor("hello")
    history = CommandHistory()
    app = Application(editor, history)
    app.test()
