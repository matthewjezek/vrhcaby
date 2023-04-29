import random

class Player:
    def __init__(self, name, color, type):
        # inicializuje hráče s daným jménem, barvou kamenů a typem
        self.name = name # řetězec
        self.color = color # "X" nebo "O"
        self.type = type # "human" nebo "computer"

    def input_name(self):
        # zadá jméno hráče z klávesnice
        self.name = input(f"Enter the name of the {self.color} player: \n")

    def choose_color(self):
        # vybere barvu kamenů náhodně
        self.color = random.choice(["X", "O"])

    def input_move(self, board, dice):
        # zadá tah hráče podle typu
        if self.type == "human": # pokud je hráč člověk, zadá tah z klávesnice
            move = input(f"{self.name}, enter your move: \n")
            # zde by měla být validace a převod vstupu na seznam čísel
            return move
        else: # pokud je hráč počítač, vygeneruje tah pomocí AI
            move = self.generate_move(board, dice)
            return move

    def generate_move(self, board, dice):
        # vygeneruje tah hráče pomocí AI
        # zde by měl být algoritmus pro výběr nejlepšího tahu podle hodnocení pozice
        return move