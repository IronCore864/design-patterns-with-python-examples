from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Editor:
    def set_text(self, text):
        self.text = text

    def set_cursor(self, x, y):
        self.cur_X = x
        self.cur_Y = y

    def set_selection_width(self, width):
        self.selection_width = width

    def create_snapshot(self):
        return Snapshot(self, self.text, self.cur_X, self.cur_Y, self.selection_width)


class Snapshot:
    def __init__(self, editor, text, cur_X, cur_Y, selection_width):
        self.editor = editor
        self.text = text
        self.cur_X = cur_X
        self.cur_Y = cur_Y
        self.selection_width = selection_width

    def restore(self):
        self.editor.set_text(self.text)
        self.editor.set_cursor(self.cur_X, self.cur_Y)
        self.editor.set_selection_width(self.selection_width)


if __name__ == "__main__":
    editor = Editor()
    editor.set_text('hello world')
    editor.set_cursor(0, 5)
    editor.set_selection_width(5)

    print(f'editor text: {editor.text}')
    print('creating backup')
    backup = editor.create_snapshot()
    editor.set_text('changed')
    print(f'editor text: {editor.text}')
    print('undo')
    backup.restore()
    print(f'editor text: {editor.text}')
