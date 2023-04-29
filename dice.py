import random
from typing import Iterator
import pygame as pg
import os

side_1 = pg.image.load(os.path.join("IMG/Side_1_Pip.png"))
side_2 = pg.image.load(os.path.join("IMG/Side_2_Pips.png"))
side_3 = pg.image.load(os.path.join("IMG/Side_3_Pips.png"))
side_4 = pg.image.load(os.path.join("IMG/Side_4_Pips.png"))
side_5 = pg.image.load(os.path.join("IMG/Side_5_Pips.png"))
side_6 = pg.image.load(os.path.join("IMG/Side_6_Pips.png"))

class Dice:
    def __init__(self) -> None:
        self.rolls = [] # historie hodů
        self.total_rolls = 0 # celkový počet hodů
    
    def roll(self) -> int:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        self.total_rolls += 1
        if roll1 == roll2:
            self.rolls.append((roll1, roll1, roll1, roll1))
            roll = roll1 * 4
            return roll
        else:
            self.rolls.append((roll1, roll2))
            roll = roll1 + roll2
            return roll
    
    def __repr__(self) -> str: # nějaké insider info
        return f'Dice[rolls={self.rolls},total_rolls={self.total_rolls}]'

    def __str__(self) -> str: # vypíše poslední hozenou dvojici
        return f'Hozeno {self.rolls[-1]}'
    
    def __len__(self) -> int: # vrátí počet hodů
        return self.total_rolls
    
    def __iter__(self) -> Iterator: # list(), for cyklus
        return iter(self.rolls)