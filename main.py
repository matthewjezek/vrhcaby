from time import sleep
from os_comands import clear
import board
import player

board = board.Board()
human = player.Player("human", "Joe", "W")
AI = player.Player("AI", "Adam", "W" if human.color == "K" else "K")

board.show()
human.dices.roll()
human.dices.show()
board.print_options(human)


