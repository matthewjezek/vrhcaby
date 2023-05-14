class Stone:
    def __init__(self, color):
        self.color = color
        self.deaths = 0
        self.place_history = []

    def __repr__(self):
        if self.color == "W":
            return "□"
        if self.color == "K":
            return "■"

    def place_history_append(self, place_num):
        self.place_history.append(place_num)


