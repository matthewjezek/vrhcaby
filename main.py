from time import sleep
import os_comands as os
import board
import player
import json

def exit_apps():
    with open('exit.json', 'w') as f:
        data = True
        json.dump(data, f)
    sleep(1)
    with open('exit.json', 'w') as f:
        data = False
        json.dump(data, f)
    os.set_color("0F")
    os.clear()

class Game:
    def __init__(self, board):
        self.player_1 = None
        self.player_2 = None
        self.board = board
        self.close = False

    def write_history(self, player, option):
        with open("progress.txt", "a") as file:
            file.write(str(f"{player.name}: {option[0]} -> {option[1]}, [{option[2]}] - {option[3]}\n"))

    def reset_history(self):
        with open("progress.txt", "w") as file:
            file.write("PROGRESS:\n--------------------\n")

    def won(self):
        if len(self.board.stacks[26].stack) == 15 or len(self.board.stacks[27].stack) == 15:
            return True
        return False

    def winner(self):
        off_W = self.board.stacks[26].stack
        off_K = self.board.stacks[27].stack
        if self.won():
            win_off = off_W if len(off_W) == 15 else off_K
            winner = self.player_1 if win_off[0].color == self.player_1.color else self.player_2
            loose_off = off_K if len(off_W) == 15 else off_W
            if loose_off:
                win_type = "Single win"
            elif not loose_off:
                win_type = "Gammon"
            os.clear()
            self.board.show(self.player_1, self.player_2)
            print(f"{winner.name} won -> {win_type}.\n")
            self.statistics()

    def player_round(self, player):
        player.dices.roll()
        while True:
            if max(player.dices.rolls) == 0: break
            os.clear()
            print(f"TURN FOR {player.name}.")
            self.board.show(self.player_1, self.player_2)
            sleep(1)
            player.dices.show()
            self.board.print_options(player)
            if len(player.options) > 0:
                choose = player.choose_option("Choose option: ", player.options)
            else:
                print(f"NO OPTIONS FOR {player.name}")
                sleep(2)
                break
            print(f"{player.name} chose: {choose}")
            sleep(1) if player.type == "AI" else sleep(1)
            move_type = player.options[choose - 1][3]
            if move_type == "KILL":
                self.board.move_stone(player.options[choose-1][1], "BAR", self.player_2 if player == self.player_1 else self.player_1)
            self.board.move_stone(player.options[choose-1][0], player.options[choose-1][1], player)
            self.write_history(player, player.options[choose-1])
            rolls = player.dices.rolls
            roll = player.options[choose-1][2]
            rolls[rolls.index(roll)] = 0

    def choose_num(self, text, options):
        while True:
            user_input = input(text)
            if user_input.isdigit():
                choose = int(user_input)
                if 1 <= choose <= len(options):
                    break
                else:
                    print("Wrong option!")
            else:
                print("Choose number!")
        return choose

    def set_player(self, num_of_player):
        os.clear()
        print(f"Player num {num_of_player}.\n")
        p_type_num = self.choose_num(f"Choose player{num_of_player} type (1-human, 2-AI): ", [1, 2])
        p_type = "human" if p_type_num == 1 else "AI"
        p_name = input("Choose name: ")
        if num_of_player == 1:
            p_color_num = self.choose_num(f"Choose player{num_of_player} color (1-White, 2-Black): ", [1, 2])
            p_color = "W" if p_color_num == 1 else "K"
        else:
            p_color = "W" if self.player_1.color == "K" else "K"
        new_player = player.Player(p_type, p_name, p_color)
        return new_player

    def save_game(self):
        data = {
            "board": {
                "layout": self.board.save_layout()
            },
            "player_1": {
                "name": self.player_1.name,
                "type": self.player_1.type,
                "color": self.player_1.color
            },
            "player_2": {
                "name": self.player_2.name,
                "type": self.player_2.type,
                "color": self.player_2.color
            }
        }
        with open('save_file.json', 'w') as f:
            json.dump(data, f)

    def load_game(self):
        os.clear()
        with open('save_file.json', 'r') as f:
            data = json.load(f)
        os.set_color("0F")
        self.reset_history()
        self.board.stacks = self.board.make_stacks(data["board"]["layout"])
        self.player_1 = player.Player(data["player_1"]["type"], data["player_1"]["name"], data["player_1"]["color"])
        self.player_2 = player.Player(data["player_2"]["type"], data["player_2"]["name"], data["player_2"]["color"])

    def new_game(self):
        os.clear()
        self.reset_history()
        self.board.reset()
        self.player_1 = self.set_player(1)
        self.player_2 = self.set_player(2)

    def play(self):
        os.clear()
        os.set_color("F0")
        os.start("progress.py")
        while True:
            self.player_round(self.player_1)
            if game.won():
                break
            self.player_round(self.player_2)
            if game.won():
                break
            self.save_game()
        self.winner()
    def statistics(self):
        os.set_color("B0")
        print("   STATISTICS\n   ------------\n")
        for stone in self.board.stones["W"]:
            print("W")
            print(stone.place_history)
            print(stone.deaths)
        for stone in self.board.stones["K"]:
            print("K")
            print(stone.place_history)
            print(stone.deaths)
        input("PRESS ENTER TO MENU")

    def menu(self):
        try:
            while True:
                exit_apps()
                print(" 1. New Game\n 2. Load\n 3. Exit\n")
                choose = self.choose_num("Choose option: ", [1, 2, 3])
                match choose:
                    case 1:
                        self.new_game()
                        self.play()
                    case 2:
                        self.load_game()
                        self.play()
                    case 3:
                        exit_apps()
                        exit()
        except KeyboardInterrupt:
            self.menu()

if __name__ == '__main__':
    board = board.Board()
    game = Game(board)
    game.menu()



