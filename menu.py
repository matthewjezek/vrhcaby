class Button():
    def __init__(self, window, x, y, color, text) -> None:
        self.window = window
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.clicked = False