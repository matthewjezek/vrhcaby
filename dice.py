import random


class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.rolls = []
        self.total = 0
        self.total_rolls = 0
    
    def roll(self):
        roll = random.randint(1, self.sides)
        self.rolls.append(roll)
        self.total += roll
        self.total_rolls += 1
        return roll
    
kostka = Dice()
print(kostka.roll)