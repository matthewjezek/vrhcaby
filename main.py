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

print(board_list)
print(board_list[1].stack)
board_list[1].move_stone(board_list[12])
print(board_list[1].stack)
print(board_list[12].stack)

