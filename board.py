import pygame
pygame.init
boardColor = (133,100,55)
size = (1200,900)
corners = (66,30,6)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(boardColor)
    pygame.draw.line(screen,corners,(600,0),(600,900),40)
    pygame.draw.line(screen,corners,(0,0),(0,900),30)
    pygame.draw.line(screen,corners,(1200,0),(1200,900),30)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()