import pygame
import dice
pygame.init
boardColor = (133,100,55)
size = (1400,900)
corners = (66,30,6)
darker_corners = (42,19,4)
bla = (0,0,0)
whi = (255,255,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My game")
clock = pygame.time.Clock()
done = False

class Board:
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(boardColor)
        #krajní linie
        pygame.draw.line(screen,corners,(627,0),(627,900),90)
        pygame.draw.line(screen,corners,(0,0),(0,900),30)
        pygame.draw.polygon(screen,corners,[(1240,0),(1400,0),(1400,900),(1240,900)],0)
        #domečky
        pygame.draw.polygon(screen, darker_corners, [(1275,100), (1365,100), (1365,350), (1275,350)],0)
        pygame.draw.polygon(screen, darker_corners, [(1275,550), (1365,550), (1365,800), (1275,800)],0)
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
        pygame.draw.polygon(screen,whi,[(717.5, 350), (760, 0), (675, 0)],0)
        pygame.draw.polygon(screen,bla,[(812.5, 350), (855, 0), (770, 0)],0)
        pygame.draw.polygon(screen,whi,[(907.5, 350), (950, 0), (865, 0)],0)
        pygame.draw.polygon(screen,bla,[(1002.5, 350), (1045, 0), (960, 0)],0)
        pygame.draw.polygon(screen,whi,[(1097.5, 350), (1140, 0), (1055, 0)],0)
        pygame.draw.polygon(screen,bla,[(1192.5, 350), (1235, 0), (1150, 0)],0)
        #triangle dolní pravé
        pygame.draw.polygon(screen,bla,[(717.5, 550), (760, 900), (675, 900)],0)
        pygame.draw.polygon(screen,whi,[(812.5, 550), (855, 900), (770, 900)],0)
        pygame.draw.polygon(screen,bla,[(907.5, 550), (950, 900), (865, 900)],0)
        pygame.draw.polygon(screen,whi,[(1002.5, 550), (1045, 900), (960, 900)],0)
        pygame.draw.polygon(screen,bla,[(1097.5, 550), (1140, 900), (1055, 900)],0)
        pygame.draw.polygon(screen,whi,[(1192.5, 550), (1235, 900), (1150, 900)],0)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()