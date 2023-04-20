import random
from typing import Iterator
import pygame as pg
import os

side_1 = pg.image.load(os.path.join("Side_1_Pip.png"))
side_2 = pg.image.load(os.path.join("Side_2_Pips.png"))
side_3 = pg.image.load(os.path.join("Side_3_Pips.png"))
side_4 = pg.image.load(os.path.join("Side_4_Pips.png"))
side_5 = pg.image.load(os.path.join("Side_5_Pips.png"))
side_6 = pg.image.load(os.path.join("Side_6_Pips.png"))

class Dice:
    def __init__(self, sides=6) -> None:
        self.sides = sides # počet stran, defaultně 6
        self.rolls = [] # historie hodů
        self.total = 0 # celkový počet hodů
        self.total_rolls = 0 # součet všech hodů
    
    def roll(self) -> int:
        roll = random.randint(1, self.sides)
        self.rolls.append(roll)
        self.total += roll
        self.total_rolls += 1
        return roll
    
    def __repr__(self) -> str:
        return f'Dice[rolls={self.rolls},total_rolls={self.total_rolls},total={self.total}]'

    def __str__(self) -> str:
        return f'Hozeno {self.total}'
    
    def __len__(self) -> int:
        return self.sides
    
    def __add__(self, value: int):
        self.total = self.total + value
        return self

    def __contains__(self, value: int) -> bool:
        return value in self.rolls
    
    def __iter__(self) -> Iterator: # list(), for cyklus
        return iter(self.rolls)