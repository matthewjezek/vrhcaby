import random
from time import sleep

class Player:
    def __init__(self, player_type, player_name, player_color):
        self.name = player_name
        self.color = player_color
        self.type = player_type
        self.dices = self.Dices()
        self.options = []

    class Dices:
        def __init__(self):
            self.rolls = [0, 0]
            self.double = False

        def roll(self):
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            self.rolls = [dice_1, dice_2, 0, 0]
            self.double = False
            if dice_1 == dice_2:
                self.double = True
                self.rolls = [dice_1, dice_2, dice_1, dice_2]

        def show(self):
            if self.double:
                print(f"┌───┐ ┌───┐ ┌───┐ ┌───┐")
                print(f"│ {self.rolls[0]} │ │ {self.rolls[1]} │ │ {self.rolls[2]} │ │ {self.rolls[3]} │")
                print(f"└───┘ └───┘ └───┘ └───┘")
            else:
                print(f"┌───┐ ┌───┐")
                print(f"│ {self.rolls[0]} │ │ {self.rolls[1]} │")
                print(f"└───┘ └───┘")

    def choose_option(self, text, from_int, to_int):
        if self.type == "AI":
            sleep(1)
            choose = random.randint(from_int, to_int)
        else:
            while True:
                user_input = input(text)
                if user_input.isdigit():
                    choose = int(user_input)
                    if from_int <= choose <= to_int:
                        break
                    else:
                        print("Wrong option!")
                else:
                    print("Choose number!")
        return choose








