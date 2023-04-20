import random
from typing import Iterator
import pygame as pg

side_1 = pg.image.load("Dice/Side_1_Pip.png", "Side 1")
side_2 = pg.image.load("Dice/Side_2_Pips.png", "Side 2")
side_3 = pg.image.load("Dice/Side_3_Pips.png", "Side 3")
side_4 = pg.image.load("Dice/Side_4_Pips.png", "Side 4")
side_5 = pg.image.load("Dice/Side_5_Pips.png", "Side 5")
side_6 = pg.image.load("Dice/Side_6_Pips.png", "Side 6")

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