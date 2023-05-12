from stone import Stone
class Board:
    def __init__(self):
        self.stones = self.make_stones()
        self.stacks = self.make_stacks()

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

    def move_stone(self, from_place, to_place, color): # Pohyb kamene na desce
        stacks = self.stacks
        from_place = 25 if from_place == "BAR" and color == "W" else from_place
        from_place = 26 if from_place == "BAR" and color == "K" else from_place
        to_place = 25 if to_place == "BAR" and color == "W" else to_place
        to_place = 26 if to_place == "BAR" and color == "K" else to_place
        to_place = 27 if to_place == "OFF" and color == "W" else to_place
        to_place = 28 if to_place == "OFF" and color == "K" else to_place
        stacks[to_place-1].stack.append(stacks[from_place-1].stack.pop())

    def show(self): # Dynamické vrstvené tištění desky podle obsahu vrcholů
        print(f"\nWhite BAR: {self.stacks[24].stack}")
        print("---------------------------------------")
        print("| 12 11 10  9  8  7  6  5  4  3  2  1 |")
        print(f"|-------------------------------------| Black END: {self.stacks[27].stack}")
        max_num = 5
        for i in range(0, 24):
            if len(self.stacks[i].stack) > max_num:
                max_num = len(self.stacks[i].stack)
        for i in range(0, max_num):
            layer = " "
            for j in range(11, -1, -1):
                place = self.stacks[j].stack
                if len(place) >= i + 1:
                    layer += (" " + place[i].color + " ")
                else:
                    layer += "   "
            print(f"|{layer}|")
        for i in range(max_num, -1, -1):
            layer = " "
            for j in range(12, 24):
                place = self.stacks[j].stack
                if len(place) >= i + 1:
                    layer += (" " + place[i].color + " ")
                else:
                    layer += "   "
            print(f"|{layer}|")
        print(f"|-------------------------------------| White END: {self.stacks[26].stack}")
        print("| 13 14 15 16 17 18 19 20 21 22 23 24 |")
        print("---------------------------------------")
        print(f"Black BAR: {self.stacks[25].stack}\n")

    def check_options(self, player): # Výpočet možností pro hráče
        options = []
        rolls = player.dices.rolls
        if player.color == "W":
            if len(self.stacks[24].stack) > 0:
                for roll in rolls:
                    if len(self.stacks[roll-1].stack) > 0 and "K" == self.stacks[roll-1].stack[0].color:
                        if len(self.stacks[roll - 1].stack) == 1:
                            options.append(["BAR", roll - 1, roll, "KILL"])
                    else:
                        options.append(["BAR", roll-1, roll, "move"])
            sum = 0
            for i in range(18, 24):
                sum += len(self.stacks[i].stack)
            end = True if sum == 15 else False
            for place_index in range(0, 24):
                if len(self.stacks[place_index].stack) > 0 and self.stacks[place_index].stack[0].color == "W":
                    for roll in rolls:
                        if end and place_index + roll > 23:
                            options.append([place_index, "OFF", roll, "END"])
                        elif place_index + roll <= 23 and len(self.stacks[place_index + roll].stack) > 0 and "K" == self.stacks[place_index + roll].stack[0].color:
                            if len(self.stacks[place_index + roll].stack) == 1:
                                options.append([place_index, place_index + roll, roll, "KILL"])
                        else:
                            options.append([place_index, place_index + roll, roll, "move"])
        elif player.color == "K":
            if len(self.stacks[25].stack) > 0:
                for roll in rolls:
                    if len(self.stacks[24 - roll].stack) > 0 and "W" == self.stacks[24 - roll].stack[0].color:
                        if len(self.stacks[24 - roll].stack) == 1:
                            options.append(["BAR", 24 - roll, roll, "KILL"])
                    else:
                        options.append(["BAR", 24 - roll, roll, "move"])
            sum = 0
            for i in range(0, 6):
                sum += len(self.stacks[i].stack)
            end = True if sum == 15 else False
            for place_index in range(23, -1, -1):
                if len(self.stacks[place_index].stack) > 0 and self.stacks[place_index].stack[0].color == "K":
                    for roll in rolls:
                        if end and place_index - roll < 0:
                            options.append([place_index, "OFF", roll, "END"])
                        elif place_index - roll >= 0 and len(self.stacks[place_index - roll].stack) > 0 and "W" == self.stacks[place_index - roll].stack[0].color:
                            if len(self.stacks[place_index - roll].stack) == 1:
                                options.append([place_index, place_index - roll, roll, "KILL"])
                        else:
                            options.append([place_index, place_index - roll, roll, "move"])
        final_options = []
        for option in options: # Odstraní duplicity
            if option not in final_options:
                final_options.append(option)
        return final_options

    def print_options(self, player):
        options = self.check_options(player)
        if len(options) == 0:
            pass
        else:
            num = 1
            print(f"OPTIONS for {player.color}:")
            print("-----------------------------------------------")
            for option in options:
                print(f"{num}:   {option[0]+1} -> {option[1]+1}, [{option[2]}], {option[3]}")
                num += 1
            print("-----------------------------------------------")
