import board
import dice
import player

board = board.Board()
board_list = board.make_objects_list()
dice = dice.Dice()
AI = player.Player("AI", "K", "AI")
human = player.Player("You", "W", "human")


board.show(board)
dice.roll()
dice.show()
board.check_options("W", dice)
board.show(board)
dice.roll()
dice.show()
board.check_options("K", dice)