import random

def choose_int(text):
    while True:
        user_input = input(text)
        if user_input.isdigit():
            choose = int(user_input)
            break
        else:
            print("Choose number!")
    return choose

class Player:
    def __init__(self, name, color, type, board, dice):
        self.name = name
        self.color = color
        self.type = type
        self.board = board
        self.dice = dice
        self.moves = []
        self.dice_chooses = []

    def generate_moves(self):
        dices = [self.dice.dice1, self.dice.dice2, self.dice.dice3, self.dice.dice4]
        sums = []
        for i in range(0, 4):
            for j in range(0, 4):
                if i != j and (dices[i] != 0 or dices[j] != 0):
                    sums.append(dices[i] + dices[j])
        moves = dices + sums
        self.moves = []
        for move in moves:
            if move != 0 and move not in self.moves:
                self.moves.append(move)

    def player_move(self):
        if self.type == "human":
            while True:
                option = choose_int("Choose option: ")
                if 0 < option <= len(self.board.options):
                    break
                else:
                    print("Wrong option!")
        if self.type == "AI":
            option = random.randint(1, len(self.board.options))
        move = self.board.options[option - 1]
        self.dice_chooses.append(move[2])
        if self.dice.dice1 == move[2]:
            self.dice.dice1 = 0
        elif self.dice.dice2 == move[2]:
            self.dice.dice2 = 0
        elif self.dice.dice3 == move[2]:
            self.dice.dice3 = 0
        elif self.dice.dice4 == move[2]:
            self.dice.dice4 = 0
        elif move[2] == (self.dice.dice1 + self.dice.dice2) and (self.dice.dice1 != 0 or self.dice.dice2 != 0):
            self.dice.dice1 = 0
            self.dice.dice2 = 0
        elif move[2] == (self.dice.dice1 + self.dice.dice3) and (self.dice.dice1 != 0 or self.dice.dice3 != 0):
            self.dice.dice1 = 0
            self.dice.dice3 = 0
        elif move[2] == (self.dice.dice1 + self.dice.dice4) and (self.dice.dice1 != 0 or self.dice.dice4 != 0):
            self.dice.dice1 = 0
            self.dice.dice4 = 0
        elif move[2] == (self.dice.dice2 + self.dice.dice3) and (self.dice.dice2 != 0 or self.dice.dice3 != 0):
            self.dice.dice2 = 0
            self.dice.dice3 = 0
        elif move[2] == (self.dice.dice2 + self.dice.dice4) and (self.dice.dice2 != 0 or self.dice.dice4 != 0):
            self.dice.dice2 = 0
            self.dice.dice4 = 0
        elif move[2] == (self.dice.dice3 + self.dice.dice4) and (self.dice.dice3 != 0 or self.dice.dice4 != 0):
            self.dice.dice3 = 0
            self.dice.dice4 = 0
        print(f"{self.type} choose: {option}: {move[0]} -> {move[1]}, [{move[2]}]")
        return move

    def menu(self):
        print("\n1: PLay game.\n2: Quit game")
        while True:
            choose = choose_int("Choose option: ")
            if choose in [1,2]:
                return choose
                break
            else:
                print("Wrong choose!")






