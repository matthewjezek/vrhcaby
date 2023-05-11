from time import sleep
from os_comands import clear
import board
import player

board = board.Board()
human = player.Player("human", "Joe", "W")

board.show()
human.dice.roll()
human.dice.show()


