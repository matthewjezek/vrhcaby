class Stone:
    def __init__(self, color, place):
        self.color = color
        self.deaths = 0
        self.place_history = [place]

    def __repr__(self):
        if self.color == "W":
            return "□"
        if self.color == "K":
            return "■"


