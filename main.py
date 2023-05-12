from time import sleep
from os_comands import clear, start
import board
import player

class Game:
    def __init__(self, player_1, player_2, board):
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = board
        self.won = False
        self.reset_history()
        start("progress.py")

    def write_history(self, player, option):
        with open("progress.txt", "a") as file:
            file.write(str(f"{player.name}: {option[0]} -> {option[1]}, [{option[2]}] - {option[3]}\n"))

    def reset_history(self):
        with open("progress.txt", "w") as file:
            file.write("PROGRESS:\n--------------------\n")

    def winner(self):
        if len(self.board.stacks[26].stack) == 15:
            winner = self.player_1.name if self.player_1.color == "W" else self.player_2.name
            self.won = True
            print(f"\n!!!!! {winner} WON !!!!!\n")
        elif len(self.board.stacks[27].stack) == 15:
            winner = self.player_1.name if self.player_1.color == "K" else self.player_2.name
            self.won = True
            print(f"\n!!!!! {winner} WON !!!!!\n")

    def player_round(self, player):
        player.dices.roll()
        while True:
            if max(player.dices.rolls) == 0: break
            clear()
            print(f"TURN FOR {player.name}.")
            sleep(1)
            self.board.show()
            player.dices.show()
            self.board.print_options(player)
            if len(player.options) > 0:
                choose = player.choose_option("Choose option: ", 1, len(player.options))
            else:
                print(f"NO OPTIONS FOR {player.name}")
                sleep(2)
                break
            print(f"{player.name} chose: {choose}")
            sleep(1) if player.type == "AI" else sleep(1)
            move_type = player.options[choose - 1][3]
            if move_type == "KILL":
                self.board.move_stone(player.options[choose-1][1], "BAR", self.player_2 if player == self.player_1 else self.player_1)
            self.board.move_stone(player.options[choose-1][0], player.options[choose-1][1], player)
            self.write_history(player, player.options[choose-1])
            rolls = player.dices.rolls
            roll = player.options[choose-1][2]
            rolls[rolls.index(roll)] = 0



game = Game(player.Player("AI", "Joe", "K"),
            player.Player("AI", "Adam", "W"),
            board.Board())

while True:
    game.player_round(game.player_1)
    if game.won: break
    game.player_round(game.player_2)
    if game.won: break
game.winner()



