import board
import dice
import player

board = board.Board()
board_list = board.make_objects_list()
dice = dice.Dice()
AI = player.Player("AI", "K", "AI")
human = player.Player("You", "W", "human")

board.show()
dice.roll()
dice.show()
moves = dice.generate_moves()
print(moves)
board.show_history()
board_list[1].move_stone(board_list[2])
board.show()
board_list[1].move_stone(board_list[2])
board.show()
print(board.save_to_history())
board.show_history()