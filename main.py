import pygame
import board
import dice
from menu import Button 
pygame.init()

def main() -> None:
    colors = {
        'board_color': (133,100,55),
        'corners': (66,30,6),
        'dark_corners': (42,19,4),
        'whi': (255,255,255),
        'bla': (0,0,0),
    }
    size = (1400,900)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My game")
    clock = pygame.time.Clock()
    done = False
    game_started = False
    
    # hlavní loop
    while done == False:
        # sběr eventů
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # vyvolání hrací plochy / menu
        if game_started:
            main_board = board.Board(screen, clock, colors, size)
            main_board.make_board()
            clock.tick(60)
        else:
            pygame.display.set_caption("Main menu")
            screen.fill(colors['board_color'])
            start = Button(screen, 300, 112.5, colors['bla'], 'START')
            if start.draw((700,350)):
                game_started = True
            quit = Button(screen, 200, 112.5, colors['bla'], 'QUIT')
            if quit.draw((700, 550)):
                done = True
            pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()