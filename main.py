import board
import dice
import player

board = board.Board()
board_list = board.make_objects_list()
dice = dice.Dice()
AI = player.Player("AI", "K", "AI")
human = player.Player("You", "W", "human")

dice.roll()
board.show()
dice.show()
board.check_options("W", dice)
board.show_history()
board.move_stone(board_list[24], board_list[3])
board.show_history()
board.show()
dice.show()
board.check_options("W", dice)