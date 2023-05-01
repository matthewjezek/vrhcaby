import random
import player


class Dice:
    def __init__(self):
        self.dice1 = 0
        self.dice2 = 0
        self.dice3 = 0
        self.dice4 = 0
        self.dices = []
        self.clone = False

    def roll(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        if self.dice1 == self.dice2:
            self.clone = True
            self.dice3 = self.dice1
            self.dice4 = self.dice1
        self.dices = [self.dice1, self.dice2, self.dice3, self.dice4]

    def show(self, player):
        moves = ""
        for move in player.dice_chooses:
            moves += ("[" + str(move) + "],")
        moves[:-1]
        if self.dice1 == self.dice2:
            print(f"┌───┐ ┌───┐ ┌───┐ ┌───┐")
            print(f"│ {self.dices[0]} │ │ {self.dices[1]} │ │ {self.dices[2]} │ │ {self.dices[3]} │  Used move numbers [x]: {moves}")
            print(f"└───┘ └───┘ └───┘ └───┘")
        else:
            print(f"┌───┐ ┌───┐")
            print(f"│ {self.dices[0]} │ │ {self.dices[1]} │  Used move numbers [x]: {player.dice_chooses}")
            print(f"└───┘ └───┘")

