import pygame
import board
import dice
import variables
from menu import Button 
pygame.init()

def game_loop() -> None:
    size = variables.size
    colors = variables.colors
    screen = pygame.display.set_mode(size)
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
            pygame.display.set_caption("Vrhcaby")
            main_board = board.Board(screen, clock, colors, size)
            main_board.make_board()

            roll = Button(screen, 200, 112.5, colors['bla'], 'ROLL')
            if roll.draw((size[0]*0.449, size[1]*0.5)):
                pass
        else:
            pygame.display.set_caption("Main menu")
            screen.fill(colors['board_color'])
            start = Button(screen, 300, 112.5, colors['bla'], 'START')
            if start.draw((size[0]//2, size[1]*0.3888)):
                game_started = True
            quit = Button(screen, 200, 112.5, colors['bla'], 'QUIT')
            if quit.draw((size[0]//2, size[1]*0.6111)):
                done = True

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()
#přidat game_loop() pro spuštění

game_loop()