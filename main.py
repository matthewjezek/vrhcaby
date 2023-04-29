import board
import dice
import player

board = board.Board()
dice = dice.Dice()
AI = player.Player("AI", "K", "AI")

board.show()
dice.roll()
dice.show()
moves = dice.generate_moves()
print(moves)

