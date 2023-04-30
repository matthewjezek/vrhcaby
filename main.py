from time import sleep
from os_comands import clear
import board
import dice
import player


board = board.Board()
board_list = board.make_objects_list()
dice = dice.Dice()
AI = player.Player("AI", "K", "AI")
human = player.Player("You", "W", "human")

while True:
    clear()
    print("Welcome to my backgammon!\n")
    menu = human.menu()
    if menu == 1:
        pass
    elif menu == 2:
        break
    sleep(1)
    clear()
    board.show(board)
    sleep(2)

