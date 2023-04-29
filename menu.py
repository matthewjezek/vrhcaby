import pygame as pg

# funkce pro výpočet souřadnic mid_pos(požadovaná pozice, šířka objektu, výška objektu)
def mid_pos(pos, w:int, h:int) -> tuple:
    x = pos[0] - (w//2)
    y = pos[1] - (h//2)
    return x, y

class Button():
    def __init__(self, window:pg.Surface, width:int, height:int, color:dict, text:str) -> None:
        self.window = window
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.clicked = False
        self.mouse_over = False

    def draw(self, pos = (700, 450)) -> bool:
        action = False
        # pozice kurzoru
        position = pg.mouse.get_pos()
        coords = mid_pos(pos, self.width, self.height)

        # generator textu
        font = pg.font.Font('BebasNeue-Regular.ttf', int(self.height*0.888))
        text = font.render(f'{self.text}', True, self.color)
        textRect = text.get_rect()

        # podklad tlačítka
        back = pg.draw.rect(self.window, (255,255,255), (coords[0], coords[1], self.width, self.height), 0, 5) 
        c = back.center
        textRect.center = (c)
        # vykresleni textu na podklad
        self.window.blit(text, textRect) 

        # kontrola pozice a kliknutí myši
        if back.collidepoint(position):
            if pg.mouse.get_pressed()[0] == True and self.clicked == False and action == False:
                self.clicked = True
                action = True
                return action
        
        if pg.mouse.get_pressed()[0] == False:
            self.clicked = False