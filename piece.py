# třída kámen
import pygame
import variables

class Piece:
    def __init__(self, window, color, location) -> None:
        self.window = window
        self.color = color
        self.location = location # ještě nevím jak budeme určovat řadu a pozici
        self.size = 35 # poloměr kamene na hrací ploše (px)
        self.in_house = False # zda se nachází v domečku
        self.is_captured = False # zda je vyhozený
        self.is_movable = False # jde s ním momentálně hýbat?
        self.memory = [] # historie
        self.outline_color = variables.colors['outline_color']

    def draw(self):
        pygame.draw.circle(self.window, self.outline_color, None, self.size+2)
        pygame.draw.circle(self.window, self.color, None, self.size)
        #                                           ^ souřadnice středu DOPLNIT!!

    @property
    def get_color(self):
        return self.color