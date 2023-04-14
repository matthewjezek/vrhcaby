import pygame
import board
import dice
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
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        main_board = board.Board(screen, clock, colors, size)
        main_board.make_board()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()