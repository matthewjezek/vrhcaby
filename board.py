import pygame
pygame.init
boardColor = (133,100,55)
size = (1200,900)
corners = (66,30,6)
bla = (0,0,0)
whi = (255,255,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(boardColor)
    #krajní linie
    pygame.draw.line(screen,corners,(602,0),(602,900),40)
    pygame.draw.line(screen,corners,(0,0),(0,900),30)
    pygame.draw.line(screen,corners,(1200,0),(1200,900),30)
    #triangle horní levé
    pygame.draw.polygon(screen,whi,[(62.5, 350), (105, 0), (20, 0)],0)
    pygame.draw.polygon(screen,bla,[(157.5, 350), (200, 0), (115, 0)],0)
    pygame.draw.polygon(screen,whi,[(252.5, 350), (295, 0), (210, 0)],0)
    pygame.draw.polygon(screen,bla,[(347.5, 350), (390, 0), (305, 0)],0)
    pygame.draw.polygon(screen,whi,[(442.5, 350), (485, 0), (400, 0)],0)
    pygame.draw.polygon(screen,bla,[(537.5, 350), (580, 0), (495, 0)],0)
    #triangle dolní levé
    pygame.draw.polygon(screen,bla,[(62.5, 550), (105, 900), (20, 900)],0)
    pygame.draw.polygon(screen,whi,[(157.5, 550), (200, 900), (115, 900)],0)
    pygame.draw.polygon(screen,bla,[(252.5, 550), (295, 900), (210, 900)],0)
    pygame.draw.polygon(screen,whi,[(347.5, 550), (390, 900), (305, 900)],0)
    pygame.draw.polygon(screen,bla,[(442.5, 550), (485, 900), (400, 900)],0)
    pygame.draw.polygon(screen,whi,[(537.5, 550), (580, 900), (495, 900)],0)
    #triangle horní pravé
    pygame.draw.polygon(screen,whi,[(667.5, 350), (710, 0), (625, 0)],0)
    pygame.draw.polygon(screen,bla,[(762.5, 350), (805, 0), (720, 0)],0)
    pygame.draw.polygon(screen,whi,[(857.5, 350), (900, 0), (815, 0)],0)
    pygame.draw.polygon(screen,bla,[(952.5, 350), (995, 0), (910, 0)],0)
    pygame.draw.polygon(screen,whi,[(1047.5, 350), (1090, 0), (1005, 0)],0)
    pygame.draw.polygon(screen,bla,[(1132.5, 350), (1182.5, 0), (1100, 0)],0)
    #triangle dolní pravé
    pygame.draw.polygon(screen,bla,[(667.5, 550), (710, 900), (625, 900)],0)
    pygame.draw.polygon(screen,whi,[(762.5, 550), (805, 900), (720, 900)],0)
    pygame.draw.polygon(screen,bla,[(857.5, 550), (900, 900), (815, 900)],0)
    pygame.draw.polygon(screen,whi,[(952.5, 550), (995, 900), (910, 900)],0)
    pygame.draw.polygon(screen,bla,[(1047.5, 550), (1090, 900), (1005, 900)],0)
    pygame.draw.polygon(screen,whi,[(1132.5, 550), (1182.5, 900), (1100, 900)],0)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()