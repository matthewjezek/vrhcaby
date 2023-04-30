class Place:
    def __init__(self, stack):
        self.stack = stack

    def add_stone(self, stone):
        self.stack.append(stone)

    def remove_stone(self):
        self.stack.pop(len(self.stack)-1)

    def move_stone(self, to_place):
        to_place.add_stone(self.stack[0])
        self.remove_stone()


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

    def make_objects_list(self): # nastaví seznam objektů vrcholů od jedné
        board = ["None", place_1, place_2, place_3, place_4, place_5, place_6, place_7, place_8, place_9, place_10, place_11, place_12,
                 place_13, place_14, place_15, place_16, place_17, place_18, place_19, place_20, place_21, place_22, place_23, place_24]
        return board

    def make_stacks_list(self):
        stacks = [place_1.stack, place_2.stack, place_3.stack, place_4.stack, place_5.stack, place_6.stack,
                  place_7.stack, place_8.stack, place_9.stack, place_10.stack, place_11.stack, place_12.stack,
                  place_13.stack, place_14.stack, place_15.stack, place_16.stack, place_17.stack, place_18.stack,
                  place_19.stack, place_20.stack, place_21.stack, place_22.stack, place_23.stack, place_24.stack]
        return stacks
    def __init__(self):
        self.reset_stones()
        self.history = []
        self.history.append(self.make_stacks_list())

    def save_to_history(self):
        self.history.append(self.make_stacks_list())

    def show(self):
        i = 1
        for place in self.make_stacks_list():
            print(f"{i}: {place}")
            i += 1

    def show_history(self):
        i = 0
        for place in self.history:
            print(f"{i}: {place}")
            i += 1
