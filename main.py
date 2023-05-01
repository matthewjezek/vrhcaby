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
        dice.roll(human)
        while board.check_move(human):
            clear()
            board.show(board)
            sleep(1)
            print("Player move!")
            dice.show(human)
            board.check_options(human)
            sleep(1)
            move = human.player_move()
            sleep(2)
            if move[3] == "KILL":
                board.move_stone(move[1], "BAR", AI)
            board.move_stone(move[0], move[1], human)
        # AI choose
        if board.check_win():
            break
        dice.roll(AI)
        while board.check_move(AI):
            clear()
            board.show(board)
            sleep(1)
            print("AI move!")
            dice.show(AI)
            board.check_options(AI)
            sleep(1)
            move = AI.player_move()
            sleep(3)
            if move[3] == "KILL":
                board.move_stone(move[1], "BAR", human)
            board.move_stone(move[0], move[1], AI)
        if board.check_win():
            break
    if board.off_W == 15:
        if human.color == "W":
            winner = human.name
        else:
            winner = AI.name
    elif board.off_K == 15:
        if human.color == "K":
            winner = human.name
        else:
            winner = AI.name
    if board.check_win():
        clear()
        board.show(board)
        print(f"{winner} won!")




