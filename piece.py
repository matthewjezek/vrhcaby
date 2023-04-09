# třída kámen
class Piece:
    def __init__(self, color, location) -> None:
        self.color = color
        self.location = location # ještě nevím jak budeme určovat řadu a pozici
        self.in_house = False # zda se nachází v domečku
        self.is_captured = False # zda je vyhozený
        self.is_movable = False # jde s ním momentálně hýbat?
        self.memory = [] # historie