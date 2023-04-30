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
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def player_move(self, player_type, board):

        if player_type == "human":
            choose_int("Choose option: ")
        if player_type == "AI":
            move = random.randint(1, len(board.options))

    def menu(self):
        print("\n1: PLay game.\n2: Quit game")
        while True:
            choose = choose_int("Choose option: ")
            if choose in [1,2]:
                return choose
                break
            else:
                print("Wrong choose!")






