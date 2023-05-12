from time import sleep
from os_comands import clear
import board
import player

class Game:
    def __init__(self, player_1, player_2, board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
        self.history = []
    def player_round(self, player):
        player.dices.roll()
        while True:
            clear()
            print(f"TURN FOR {player.name}.")
            sleep(1)
            self.board.show()
            player.dices.show()
            self.board.print_options(player)
            if len(player.options) > 0:
                choose = player.choose_option("Choose option: ", 1, len(player.options))
            else:
                break
            print(f"{player.name} chose: {choose}")
            sleep(1) if player.type == "AI" else sleep(1)
            self.board.move_stone(player.options[choose-1][0], player.options[choose-1][1], player)
            index_replace = player.dices.rolls.index(player.options[choose-1][2])
            player.dices.rolls[index_replace] = 0

game = Game(player.Player("AI", "Joe", "K"),
            player.Player("AI", "Adam", "W"),
            board.Board())

while True:
    game.player_round(game.player_1)
    game.player_round(game.player_2)
    if game.board.stacks[24] == 15 or game.board.stacks[25] == 15:
        print("Somebody won!")
        break



