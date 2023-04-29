class Stone:
    def __init__(self, color, position):
        # inicializuje kámen s danou barvou a pozicí
        self.color = color # "X" nebo "O"
        self.position = position # Číslo od 1 do 24 nebo "BAR" nebo "OFF"

    def move(self, pips):
        # pohne kamenem podle daného počtu políček
        if self.position == "BAR": # pokud je kámen na baru, musí vstoupit na desku
            if self.color == "X": # pokud je kámen "X", vstoupí na horní polovinu desky
                self.position = 25 - pips
            else: # pokud je kámen "O", vstoupí na dolní polovinu desky
                self.position = pips
        elif self.position == "OFF": # pokud je kámen mimo desku, nemůže se pohnout
            pass
        else: # jinak se kámen posune podle své barvy
            if self.color == "X": # pokud je kámen X, posune se směrem dolů
                self.position -= pips
                if self.position < 1: # pokud je kámen mimo desku, nastaví se na OFF
                    self.position = "OFF"
            else: # pokud je kámen O, posune se směrem nahoru
                self.position += pips
                if self.position > 24: # pokud je kámen mimo desku, nastaví se na OFF
                    self.position = "OFF"

    def is_on_bar(self):
        # vrátí True, pokud je kámen na baru, jinak False
        return self.position == "BAR"

    def is_off_board(self):
        # vrátí True, pokud je kámen mimo desku, jinak False
        return self.position == "OFF"

    def is_in_home(self):
        # vrátí True, pokud je kámen v domovské oblasti své barvy, jinak False
        if self.color == "X": # domovská oblast pro X je od 1 do 6
            return 1 <= self.position <= 6
        else: # domovská oblast pro O je od 19 do 24
            return 19 <= self.position <= 24