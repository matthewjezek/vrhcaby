import board_layers
from stone import Stone

class Place:
    def __init__(self, stack):
        self.stack = stack

class Board:
    def __init__(self):
        self.stones = self.make_stones()
        self.stacks = self.make_stacks()
        self.bar_W = self.stacks[24]
        self.bar_K = self.stacks[25]
        self.off_W = self.stacks[26]
        self.off_K = self.stacks[27]
        self.options = [""]

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
        place_1 = Place([self.stones["W"][0], self.stones["W"][1]])
        place_2 = Place([])
        place_3 = Place([])
        place_4 = Place([])
        place_5 = Place([])
        place_6 = Place([self.stones["K"][0], self.stones["K"][1], self.stones["K"][2], self.stones["K"][3], self.stones["K"][4]])
        place_7 = Place([])
        place_8 = Place([self.stones["K"][5], self.stones["K"][6], self.stones["K"][7]])
        place_9 = Place([])
        place_10 = Place([])
        place_11 = Place([])
        place_12 = Place([self.stones["W"][2], self.stones["W"][3], self.stones["W"][4], self.stones["W"][5], self.stones["W"][6]])
        place_13 = Place([self.stones["K"][8], self.stones["K"][9], self.stones["K"][10], self.stones["K"][11] ,self.stones["K"][12]])
        place_14 = Place([])
        place_15 = Place([])
        place_16 = Place([])
        place_17 = Place([self.stones["W"][7], self.stones["W"][8], self.stones["W"][9]])
        place_18 = Place([])
        place_19 = Place([self.stones["W"][10], self.stones["W"][11], self.stones["W"][12], self.stones["W"][13], self.stones["W"][14]])
        place_20 = Place([])
        place_21 = Place([])
        place_22 = Place([])
        place_23 = Place([])
        place_24 = Place([self.stones["K"][13], self.stones["K"][14]])
        bar_w = Place([])
        bar_k = Place([])
        off_w = Place([])
        off_k = Place([])

        stacks = [place_1.stack, place_2.stack, place_3.stack, place_4.stack, place_5.stack, place_6.stack,
                  place_7.stack, place_8.stack, place_9.stack, place_10.stack, place_11.stack, place_12.stack,
                  place_13.stack, place_14.stack, place_15.stack, place_16.stack, place_17.stack, place_18.stack,
                  place_19.stack, place_20.stack, place_21.stack, place_22.stack, place_23.stack, place_24.stack,
                  bar_w, bar_k, off_w, off_k]
        return stacks

    def move_stone(self, from_place, to_place):
        to_place.stack.append(from_place.stack.pop())

    def show(self):
        print(f"\nWhite BAR: {self.bar_W.stack}")
        print("---------------------------------------")
        print("| 12 11 10  9  8  7  6  5  4  3  2  1 |")
        print(f"|-------------------------------------| Black END: {self.off_K.stack}")
        board_layers.layers(self)
        print(f"|-------------------------------------| White END: {self.off_W.stack}")
        print("| 13 14 15 16 17 18 19 20 21 22 23 24 |")
        print("---------------------------------------")
        print(f"Black BAR: {self.bar_K.stack}\n")

    # def check_options(self, player):
    #     options = []
    #     player.generate_moves()
    #     if player.color == "W":
    #         place_index = 1
    #         if len(self.bar_W) >= 1:
    #             for number in player.moves:
    #                 if "K" not in self.make_stacks_list()[number -1]:
    #                     options.append(["BAR", number, number, "move"])
    #                 elif self.make_stacks_list()[number -1] == ["K"]:
    #                     options.append(["BAR", number, number, "KILL"])
    #         for place in self.make_stacks_list():
    #             if "W" in place:
    #                 for number in player.moves:
    #                     if (place_index + number) <= 24:
    #                         if "K" not in self.make_stacks_list()[place_index + number -1]:
    #                             options.append([place_index, place_index + number, number, "move"])
    #                         elif self.make_stacks_list()[place_index + number -1] == ["K"]:
    #                             options.append([place_index, place_index + number, number, "KILL"])
    #
    #                     else:
    #                         options.append([place_index, "OFF", number, "END"])
    #             place_index += 1
    #     elif player.color == "K":
    #         place_index = 24
    #         if len(self.bar_K) >= 1:
    #             for number in player.moves:
    #                 if "W" not in self.make_stacks_list()[24 - number -1]:
    #                     options.append(["BAR", 25 - number, number, "move"])
    #                 elif self.make_stacks_list()[24 - number -1] == ["W"]:
    #                     options.append(["BAR", 25 - number, number, "KILL"])
    #         for _ in range(0, 24):
    #             place = self.make_stacks_list()[place_index-1]
    #             if "K" in place:
    #                 for number in player.moves:
    #                     if (place_index - number) >= 1:
    #                         if "W" not in self.make_stacks_list()[place_index - number -1]:
    #                             options.append([place_index, place_index - number, number, "move"])
    #                         elif self.make_stacks_list()[place_index - number -1] == ["W"]:
    #                             options.append([place_index, place_index - number, number, "KILL"])
    #
    #                     else:
    #                         options.append([place_index, "OFF", number, "END"])
    #
    #             place_index -= 1
    #     self.options = options
    #     if self.options == []:
    #         pass
    #     else:
    #         num = 1
    #         print(f"OPTIONS for {player.color}:")
    #         moves = ""
    #         for move in player.moves:
    #             moves += ("[" + str(move) + "],")
    #         print(f"Available move numbers [x]: {moves[:-1]}")
    #         print("-----------------------------------------------")
    #         for option in self.options:
    #             print(f"{num}:   {option[0]} -> {option[1]}, [{option[2]}], {option[3]}")
    #             num += 1
    #         print("-----------------------------------------------")

    # def check_move(self, player):
    #         self.check_options(player)
    #         if self.options != []:
    #             return True
    #         else:
    #             return False
    #
    # def check_win(self):
    #     if len(self.off_W) == 15 or len(self.off_K) == 15:
    #         return True
    #     else:
    #         return False