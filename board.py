import pygame as pg

class Board:
    def __init__(self, window: pg.display, clock, color, size) -> None:
        self.window = window
        self.clock = clock
        self.color = color
        self.size = size
        # inicializace desky na počáteční nastavení
        self.board = [-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, -5, 2,
                       5, -3, 0, 0, -5, 0, 0, 0, 0, 2, 0, -5]
        self.player_bar = 0 # počet kamenů hráče na baru
        self.player_off = 0 # počet kamenů hráče mimo desku
        self.opponent_bar = 0 # počet kamenů soupeře na baru
        self.opponent_off = 0 # počet kamenů soupeře mimo desku

    def make_board(self) -> None:
        k = (self.size[1]/18) # výška / 18
        l = (self.size[0]/35) # šířka / 35
        m = (self.size[0]/560) # šířka / 560
        x = (38*m) # vzdálenost mezi dvěma sousedními středovými vrcholy trojúhelníků
        gap = ((x*2)-10) # vzdálenost vždy mezi dvěma trojúhelníky na stejné pozici ale na druhé straně baru
        a = (0.5*l) # základní souřadnice šířky pravého vrcholu trojúhelníků
        b = (40*m) # základní souřadnice šířky levého vrcholu trojůhelníků
        c = (25*m) # základní souřadnice šířky středového vrcholu trojúhelníků
        self.window.fill(self.color['board_color'])
        #krajní linie
        pg.draw.line(self.window,self.color['corners'],((15.65*l),0),((15.65*l),self.size[1]),int(36*m))
        pg.draw.line(self.window,self.color['corners'],(0,0),(0,self.size[1]),30)
        pg.draw.polygon(self.window,self.color['corners'],[(l*31,0),(self.size[0],0),(self.size[0],self.size[1]),(l*31,self.size[1])],0)
        #domečky
        pg.draw.polygon(self.window, self.color['dark_corners'], [(l*32,2*k), (l*34,2*k), (l*34,7*k), (l*32,7*k)],0)
        pg.draw.polygon(self.window, self.color['dark_corners'], [(l*32,11*k), (l*34,11*k), (l*34,16*k), (l*32,16*k)],0)
        #triangle horní levé
        pg.draw.polygon(self.window,self.color['whi'],[(c, 7*k), (b, 0), (a, 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+x, 7*k), (b+x, 0), (a+x, 0)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+(2*x), 7*k), (b+(2*x), 0), (a+(2*x), 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+(3*x), 7*k), (b+(3*x), 0), (a+(3*x), 0)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+(4*x), 7*k), (b+(4*x), 0), (a+(4*x), 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+(5*x), 7*k), (b+(5*x), 0), (a+(5*x), 0)],0)
        #triangle dolní levé
        pg.draw.polygon(self.window,self.color['bla'],[(c, 11*k), (b, self.size[1]), (a, self.size[1])],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+x, 11*k), (b+x, self.size[1]), (a+x, self.size[1])],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+(2*x), 11*k), (b+(2*x), self.size[1]), (a+(2*x), self.size[1])],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+(3*x), 11*k), (b+(3*x), self.size[1]), (a+(3*x), self.size[1])],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+(4*x), 11*k), (b+(4*x), self.size[1]), (a+(4*x), self.size[1])],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+(5*x), 11*k), (b+(5*x), self.size[1]), (a+(5*x), self.size[1])],0)
        #triangle horní pravé
        pg.draw.polygon(self.window,self.color['whi'],[(c+gap+(5*x), 7*k), (b+gap+(5*x), 0), (a+gap+(5*x), 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+gap+(6*x), 7*k), (b+gap+(6*x), 0), (a+gap+(6*x), 0)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+gap+(7*x), 7*k), (b+gap+(7*x), 0), (a+gap+(7*x), 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+gap+(8*x), 7*k), (b+gap+(8*x), 0), (a+gap+(8*x), 0)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+gap+(9*x), 7*k), (b+gap+(9*x), 0), (a+gap+(9*x), 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+gap+(10*x), 7*k), (b+gap+(10*x), 0), (a+gap+(10*x), 0)],0)
        #triangle dolní pravé
        pg.draw.polygon(self.window,self.color['bla'],[(c+gap+(5*x), 11*k), (b+gap+(5*x), self.size[1]), (a+gap+(5*x), self.size[1])],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+gap+(6*x), 11*k), (b+gap+(6*x), self.size[1]), (a+gap+(6*x), self.size[1])],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+gap+(7*x), 11*k), (b+gap+(7*x), self.size[1]), (a+gap+(7*x), self.size[1])],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+gap+(8*x), 11*k), (b+gap+(8*x), self.size[1]), (a+gap+(8*x), self.size[1])],0)
        pg.draw.polygon(self.window,self.color['bla'],[(c+gap+(9*x), 11*k), (b+gap+(9*x), self.size[1]), (a+gap+(9*x), self.size[1])],0)
        pg.draw.polygon(self.window,self.color['whi'],[(c+gap+(10*x), 11*k), (b+gap+(10*x), self.size[1]), (a+gap+(10*x), self.size[1])],0)
        pg.display.flip()

    def is_valid_move(self, move):
        # vrátí True, pokud je tah platný podle pravidel hry, jinak False
        # tady bude logika pro kontrolu platnosti tahu
        return True
    def make_move(self, move):
        # provede tah na desce a aktualizuje počty kamenů na baru a mimo desku
        # zde bude logika pro provedení tahů podle barvy hráče a soupeře
        pass

    def evaluate_winner(self):
        # vyhodnotí vítěze hry podle počtu kamenů mimo desku
        if self.player_off == 15:  # pokud má hráč všechny kameny mimo desku, vyhrál
            return "player"
        elif self.opponent_off == 15:  # pokud má soupeř všechny kameny mimo desku, vyhrál
            return "opponent"
        else:  # jinak ještě není rozhodnuto
            return None