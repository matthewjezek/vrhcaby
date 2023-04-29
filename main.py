import board
import dice

board = board.Board()
dice = dice.Dice()

board.show()
dice.roll()
dice.show()
moves = dice.generate_moves()
print(moves)


