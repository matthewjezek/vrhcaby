import random


class Dice:
    def __init__(self):
        self.dice1 = 0
        self.dice2 = 0

    def roll(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)

    def show(self):
        print(f"┌───┐ ┌───┐")
        print(f"│ {self.dice1} │ │ {self.dice2} │")
        print(f"└───┘ └───┘")

    def generate_moves(self):
        # vygeneruje možné tahy podle hodnot kostek
        moves = []
        if self.dice1 == self.dice2: # pokud kostky jsou stejné, můžeš hrát čtyřikrát
            moves.append((self.dice1, self.dice1, self.dice1, self.dice1))
        else: # jinak můžeš hrát dvakrát
            moves.append((self.dice1, self.dice2))
            moves.append((self.dice2, self.dice1))
        return moves
