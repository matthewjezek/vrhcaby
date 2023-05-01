from time import sleep
from os_comands import clear
import board
import dice
import player

dice = dice.Dice()
board = board.Board(dice)
AI = player.Player("AI", "K", "AI", board, dice)
human = player.Player("You", "W", "human", board, dice)

while True:
    clear()
    print("Welcome to my backgammon!\n")
    menu = human.menu()
    if menu == 1:
        pass
    elif menu == 2:
        break
    sleep(1)
    while True:
        # player choose
        clear()
        dice.roll()
        while True:
            clear()
            board.show(board)
            sleep(1)
            print("Player move!")
            dice.show(human)
            board.check_options(human)
            sleep(1)
            move = human.player_move()
            sleep(2)
            board.move_stone(move[0], move[1])




