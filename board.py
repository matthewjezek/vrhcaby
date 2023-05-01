import board_layers

class Place:
    def __init__(self, stack):
        self.stack = stack

    def add_stone(self, stone):
        self.stack.append(stone)

    def remove_stone(self):
        self.stack.pop(len(self.stack)-1)


class Board:
    def reset_stones(self):
        # Vrcholy 1-12
        global place_1, place_2, place_3, place_4, place_5, place_6, place_7, place_8, place_9, place_10, place_11, place_12
        place_1 = Place(["W", "W"])
        place_2 = Place([])
        place_3 = Place([])
        place_4 = Place([])
        place_5 = Place([])
        place_6 = Place(["K", "K", "K", "K", "K"])
        place_7 = Place([])
        place_8 = Place(["K", "K", "K"])
        place_9 = Place([])
        place_10 = Place([])
        place_11 = Place([])
        place_12 = Place(["W", "W", "W", "W", "W"])
        # Vrcholy 13-24
        global place_13, place_14, place_15, place_16, place_17, place_18, place_19, place_20, place_21, place_22, place_23, place_24
        place_13 = Place(["K", "K", "K", "K", "K"])
        place_14 = Place([])
        place_15 = Place([])
        place_16 = Place([])
        place_17 = Place(["W", "W", "W"])
        place_18 = Place([])
        place_19 = Place(["W", "W", "W", "W", "W"])
        place_20 = Place([])
        place_21 = Place([])
        place_22 = Place([])
        place_23 = Place([])
        place_24 = Place(["K", "K"])

    def make_objects_list(self): # nastaví seznamu objektů vrcholů od jedné
        stones = ["None", place_1, place_2, place_3, place_4, place_5, place_6, place_7, place_8, place_9, place_10, place_11, place_12,
                 place_13, place_14, place_15, place_16, place_17, place_18, place_19, place_20, place_21, place_22, place_23, place_24]
        return stones

    def make_stacks_list(self):
        stacks = [place_1.stack, place_2.stack, place_3.stack, place_4.stack, place_5.stack, place_6.stack,
                  place_7.stack, place_8.stack, place_9.stack, place_10.stack, place_11.stack, place_12.stack,
                  place_13.stack, place_14.stack, place_15.stack, place_16.stack, place_17.stack, place_18.stack,
                  place_19.stack, place_20.stack, place_21.stack, place_22.stack, place_23.stack, place_24.stack]
        return stacks
    def __init__(self, dice):
        self.reset_stones()
        self.history = []
        self.history.append(self.make_stacks_list())
        self.options = [""]
        self.bar_W = []
        self.bar_K = []
        self.off_W = []
        self.off_K = []
        self.board_list = self.make_objects_list()
        self.dice = dice

    def save_to_history(self):
        self.history.append(self.make_stacks_list())

    def check_options(self, player):
        options = []
        player.generate_moves()
        if player.color == "W":
            place_index = 1
            if len(self.bar_W) >= 1:
                for number in player.moves:
                    if "K" not in self.make_stacks_list()[number -1]:
                        options.append(["BAR", number, number, "move"])
                    elif self.make_stacks_list()[number -1] == ["K"]:
                        options.append(["BAR", number, number, "KILL"])
            for place in self.make_stacks_list():
                if "W" in place:
                    for number in player.moves:
                        if (place_index + number) <= 24:
                            if "K" not in self.make_stacks_list()[place_index + number -1]:
                                options.append([place_index, place_index + number, number, "move"])
                            elif self.make_stacks_list()[place_index + number -1] == ["K"]:
                                options.append([place_index, place_index + number, number, "KILL"])

                        else:
                            options.append([place_index, "OFF", number, "END"])
                place_index += 1
        elif player.color == "K":
            place_index = 24
            if len(self.bar_K) >= 1:
                for number in player.moves:
                    if "W" not in self.make_stacks_list()[24 - number -1]:
                        options.append(["BAR", 25 - number, number, "move"])
                    elif self.make_stacks_list()[24 - number -1] == ["W"]:
                        options.append(["BAR", 25 - number, number, "KILL"])
            for _ in range(0, 24):
                place = self.make_stacks_list()[place_index-1]
                if "K" in place:
                    for number in player.moves:
                        if (place_index - number) >= 1:
                            if "W" not in self.make_stacks_list()[place_index - number -1]:
                                options.append([place_index, place_index - number, number, "move"])
                            elif self.make_stacks_list()[place_index - number -1] == ["W"]:
                                options.append([place_index, place_index - number, number, "KILL"])

                        else:
                            options.append([place_index, "OFF", number, "END"])

                place_index -= 1
        self.options = options
        if self.options == []:
            pass
        else:
            num = 1
            print(f"OPTIONS for {player.color}:")
            moves = ""
            for move in player.moves:
                moves += ("[" + str(move) + "],")
            moves[:-1]
            print(f"Available move numbers [x]: {moves}")
            for option in self.options:
                print(f"{num}:   {option[0]} -> {option[1]}, [{option[2]}], {option[3]}")
                num += 1

    def check_move(self, player):
            self.check_options(player)
            if self.options != []:
                return True
            else:
                return False

    def move_stone(self, from_place, to_place, player):
        if to_place == "OFF" and player.color == "W":
            self.off_W.append("W")
        elif to_place == "OFF" and player.color == "K":
            self.off_K.append("K")
        elif to_place == "BAR" and player.color == "W":
            self.bar_W.append("W")
        elif to_place == "BAR" and player.color == "K":
            self.bar_K.append("K")
        else:
            self.board_list[to_place].add_stone(player.color)
        if from_place == "BAR" and player.color == "W":
            self.bar_W.remove("W")
        elif from_place == "BAR" and player.color == "K":
            self.bar_K.remove("K")
        else:
            self.board_list[from_place].remove_stone()
        self.save_to_history()

    def show(self, board):
        print(f"\nWhite BAR: {self.bar_W}")
        print("---------------------------------------")
        print("| 12 11 10  9  8  7  6  5  4  3  2  1 |")
        print(f"|-------------------------------------| Black END: {self.off_K}")
        board_layers.layers(board)
        print(f"|-------------------------------------| White END: {self.off_W}")
        print("| 13 14 15 16 17 18 19 20 21 22 23 24 |")
        print("---------------------------------------")
        print(f"Black BAR: {self.bar_K}\n")

    def show_history(self):
        i = 0
        for place in self.history:
            print(f"{i}: {place}")
            i += 1

    def check_win(self):
        if len(self.off_W) == 15:
            return True
        elif len(self.off_K) == 15:
            return True