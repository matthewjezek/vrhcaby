import pygame as pg

class Board:
    def __init__(self, window: pg.display, clock, color, size) -> None:
        self.window = window
        self.clock = clock
        self.color = color
        self.size = size

    def make_board(self) -> None:
        self.window.fill(self.color['board_color'])
        #krajní linie
        pg.draw.line(self.window,self.color['corners'],(627,0),(627,900),90)
        pg.draw.line(self.window,self.color['corners'],(0,0),(0,900),30)
        pg.draw.polygon(self.window,self.color['corners'],[(1240,0),(1400,0),(1400,900),(1240,900)],0)
        #domečky
        pg.draw.polygon(self.window, self.color['dark_corners'], [(1275,100), (1365,100), (1365,350), (1275,350)],0)
        pg.draw.polygon(self.window, self.color['dark_corners'], [(1275,550), (1365,550), (1365,800), (1275,800)],0)
        #triangle horní levé
        pg.draw.polygon(self.window,self.color['whi'],[(62.5, 350), (105, 0), (20, 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(157.5, 350), (200, 0), (115, 0)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(252.5, 350), (295, 0), (210, 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(347.5, 350), (390, 0), (305, 0)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(442.5, 350), (485, 0), (400, 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(537.5, 350), (580, 0), (495, 0)],0)
        #triangle dolní levé
        pg.draw.polygon(self.window,self.color['bla'],[(62.5, 550), (105, 900), (20, 900)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(157.5, 550), (200, 900), (115, 900)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(252.5, 550), (295, 900), (210, 900)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(347.5, 550), (390, 900), (305, 900)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(442.5, 550), (485, 900), (400, 900)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(537.5, 550), (580, 900), (495, 900)],0)
        #triangle horní pravé
        pg.draw.polygon(self.window,self.color['whi'],[(717.5, 350), (760, 0), (675, 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(812.5, 350), (855, 0), (770, 0)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(907.5, 350), (950, 0), (865, 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(1002.5, 350), (1045, 0), (960, 0)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(1097.5, 350), (1140, 0), (1055, 0)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(1192.5, 350), (1235, 0), (1150, 0)],0)
        #triangle dolní pravé
        pg.draw.polygon(self.window,self.color['bla'],[(717.5, 550), (760, 900), (675, 900)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(812.5, 550), (855, 900), (770, 900)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(907.5, 550), (950, 900), (865, 900)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(1002.5, 550), (1045, 900), (960, 900)],0)
        pg.draw.polygon(self.window,self.color['bla'],[(1097.5, 550), (1140, 900), (1055, 900)],0)
        pg.draw.polygon(self.window,self.color['whi'],[(1192.5, 550), (1235, 900), (1150, 900)],0)