from stone import Stone
class Board:
    def __init__(self):
        self.stones = self.make_stones()
        self.stacks = self.make_stacks()
        self.history = []

    class Place:
        def __init__(self, stack):
            self.stack = stack

    def reset(self): # Reset celé desky
        self.stones = self.make_stones()
        self.stacks = self.make_stacks()


    def make_stones(self): # Vytvoří novou sadu kamenů
        stones = {
                    "W": [Stone("W"), Stone("W"), Stone("W"), Stone("W"), Stone("W"), Stone("W"), Stone("W"), Stone("W"),
                          Stone("W"), Stone("W"), Stone("W"), Stone("W"), Stone("W"), Stone("W"), Stone("W")],
                    "K": [Stone("K"), Stone("K"), Stone("K"), Stone("K"), Stone("K"), Stone("K"), Stone("K"), Stone("K"),
                          Stone("K"), Stone("K"), Stone("K"), Stone("K"), Stone("K"), Stone("K"), Stone("K")]
                  }
        return stones

    def make_stacks(self): # Vytvoří novou sadu vrcholů se začátečním rozpoložením kamenů
        place_1 = self.Place([self.stones["W"][0], self.stones["W"][1]])
        place_2 = self.Place([])
        place_3 = self.Place([])
        place_4 = self.Place([])
        place_5 = self.Place([])
        place_6 = self.Place([self.stones["K"][0], self.stones["K"][1], self.stones["K"][2], self.stones["K"][3], self.stones["K"][4]])
        place_7 = self.Place([])
        place_8 = self.Place([self.stones["K"][5], self.stones["K"][6], self.stones["K"][7]])
        place_9 = self.Place([])
        place_10 = self.Place([])
        place_11 = self.Place([])
        place_12 = self.Place([self.stones["W"][2], self.stones["W"][3], self.stones["W"][4], self.stones["W"][5], self.stones["W"][6]])
        place_13 = self.Place([self.stones["K"][8], self.stones["K"][9], self.stones["K"][10], self.stones["K"][11] ,self.stones["K"][12]])
        place_14 = self.Place([])
        place_15 = self.Place([])
        place_16 = self.Place([])
        place_17 = self.Place([self.stones["W"][7], self.stones["W"][8], self.stones["W"][9]])
        place_18 = self.Place([])
        place_19 = self.Place([self.stones["W"][10], self.stones["W"][11], self.stones["W"][12], self.stones["W"][13], self.stones["W"][14]])
        place_20 = self.Place([])
        place_21 = self.Place([])
        place_22 = self.Place([])
        place_23 = self.Place([])
        place_24 = self.Place([self.stones["K"][13], self.stones["K"][14]])
        bar_w = self.Place([])
        bar_k = self.Place([])
        off_w = self.Place([])
        off_k = self.Place([])

        stacks = [place_1, place_2, place_3, place_4, place_5, place_6,
                  place_7, place_8, place_9, place_10, place_11, place_12,
                  place_13, place_14, place_15, place_16, place_17, place_18,
                  place_19, place_20, place_21, place_22, place_23, place_24,
                  bar_w, bar_k, off_w, off_k]
        return stacks

    def move_stone(self, from_place, to_place, player): # Pohyb kamene na desce
        stacks = self.stacks
        color = player.color
        from_place = 25 if from_place == "BAR" and color == "W" else from_place
        from_place = 26 if from_place == "BAR" and color == "K" else from_place
        to_place = 25 if to_place == "BAR" and color == "W" else to_place
        to_place = 26 if to_place == "BAR" and color == "K" else to_place
        to_place = 27 if to_place == "OFF" and color == "W" else to_place
        to_place = 28 if to_place == "OFF" and color == "K" else to_place
        stacks[to_place-1].stack.append(stacks[from_place-1].stack.pop())

    def show(self, player_1, player_2): # Dynamické vrstvené tištění desky podle obsahu vrcholů
        print(f"\n{player_1.name if player_1.color == 'W' else player_2.name} BAR: {self.stacks[24].stack}")
        print("---------------------------------------")
        print("| 12 11 10  9  8  7  6  5  4  3  2  1 |")
        print(f"|-------------------------------------| {player_1.name if player_1.color == 'K' else player_2.name} END: {self.stacks[27].stack}")
        max_num = 5
        for i in range(0, 12):
            if len(self.stacks[i].stack) > max_num:
                max_num = len(self.stacks[i].stack)
        for i in range(0, max_num):
            layer = " "
            for j in range(11, -1, -1):
                place = self.stacks[j].stack
                if len(place) >= i + 1:
                    layer += (" " + str(place[i]) + " ")
                else:
                    layer += "   "
            print(f"|{layer}|")
        max_num = 5
        for i in range(12, 24):
            if len(self.stacks[i].stack) > max_num:
                max_num = len(self.stacks[i].stack)
        for i in range(max_num, -1, -1):
            layer = " "
            for j in range(12, 24):
                place = self.stacks[j].stack
                if len(place) >= i + 1:
                    layer += (" " + str(place[i]) + " ")
                else:
                    layer += "   "
            print(f"|{layer}|")
        print(f"|-------------------------------------| {player_1.name if player_1.color == 'W' else player_2.name} END: {self.stacks[26].stack}")
        print("| 13 14 15 16 17 18 19 20 21 22 23 24 |")
        print("---------------------------------------")
        print(f"{player_1.name if player_1.color == 'K' else player_2.name} BAR: {self.stacks[25].stack}\n")

    def check_options(self, player): # Výpočet možností pro hráče
        options = []
        stacks = self.stacks
        rolls = [roll for roll in player.dices.rolls if roll != 0]
        bar = stacks[24].stack if player.color == "W" else stacks[25].stack
        off = stacks[26].stack if player.color == "W" else stacks[27].stack
        home_board = range(18, 24) if player.color == "W" else range(0, 6)
        board = range(0, 24) if player.color == "W" else range(23, -1, -1)
        # Generování možností pro vracení kamenů hráče z baru
        if bar:
            for roll in rolls:
                place_i = board[roll-1]
                place = stacks[place_i].stack
                if len(place) == 1 and player.color != place[0].color:
                    options.append(["BAR", place_i+1, roll, "KILL"])
                elif len(place) == 1 and player.color == place[0].color:
                    options.append(["BAR", place_i+1, roll, "SAVE"])
                elif not place or (place and player.color == place[0].color):
                    options.append(["BAR", place_i+1, roll, "move"])
        # Kontrola, jestli má hráč všechny kameny na domácí ohradě
        sum = len(off)
        for index in home_board:
            home_place = stacks[index].stack
            sum += len(home_place) if home_place and home_place[0].color == player.color else 0
        home_board_check = True if sum == 15 else False
        # Výpočet indexu umístění nejvzdálenějšího kamene
        last_stone_i = board[0]
        for index in board:
            place = stacks[index].stack
            last_stone_i = index if place and place[0].color == player.color else last_stone_i
        # Generování možností pro pohyb z vrcholů na desce
        for num in range(1, 25):
            place_i = board[num-1]
            place = stacks[place_i].stack
            if place and place[0].color == player.color:
                for roll in rolls:
                    if num + roll > 24:
                        if home_board_check and (num + roll == 25 or (num + roll > 25 and place_i == last_stone_i)):
                            options.append([place_i + 1, "OFF", roll, "END"])
                    else:
                        to_place_i = board[num-1 + roll]
                        to_place = stacks[to_place_i].stack
                        if len(to_place) == 1 and player.color != to_place[0].color:
                            options.append([place_i + 1, to_place_i + 1, roll, "KILL"])
                        elif len(to_place) == 1 and player.color == to_place[0].color:
                            options.append([place_i + 1, to_place_i + 1, roll, "SAVE"])
                        elif not to_place or (to_place and to_place[0].color == player.color):
                            options.append([place_i + 1, to_place_i + 1, roll, "move"])
        # Odstranění duplicit v options
        final_options = []
        for option in options:
            if option not in final_options:
                final_options.append(option)
        player.options = final_options
        return final_options

    def print_options(self, player):
        options = self.check_options(player)
        if len(options) == 0:
            pass
        else:
            num = 1
            print(f"OPTIONS:")
            print("-----------------------------------------------")
            for option in options:
                print(f"{num}:   {option[0]} -> {option[1]}, [{option[2]}], {option[3]}")
                num += 1
            print("-----------------------------------------------")
