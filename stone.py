class Stone:
    def __init__(self, color):
        self.color = color
        self.deaths = 0

    def __repr__(self):
        if self.color == "W":
            return "□"
        if self.color == "K":
            return "■"
