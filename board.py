from objects import *

class Place:
    def __init__(self, stack):
        self.stack = stack

    def add_stone(self, stone):
        self.stack.append(stone)

    def remove_stone(self, stone):
        self.stack.pop(stone)

    def stack(self):
        return self.stack

    def move_stone(self, to_place):
        to_place.add_stone(self.stack()[0])
        self.remove_stone(self.stack()[0])
        # přidat zápis do historie

class Board:
    def __init__(self):
        reset_stones()
        self.history = []




