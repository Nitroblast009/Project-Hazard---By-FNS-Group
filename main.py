import pygame
#from menuscreen import menu
from colours import *
from about_us import aboutUs
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Project Hazard')
screen.fill(mainScreenColour)


running = True
while running:
    #aboutUs(screen)
    #menu()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break


    pygame.display.update()

pygame.quit()