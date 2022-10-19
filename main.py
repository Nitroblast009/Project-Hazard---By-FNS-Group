import pygame
from menuscreen import menu
from colours import *
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Project Hazard')
screen.fill(mainScreenColour)


running = True
while running:
    pygame.draw.rect(screen, landColour, pygame.Rect(30, 30, 140, 300))
    pygame.draw.rect(screen, landColour, pygame.Rect(180, 30, 140, 300))
    pygame.draw.rect(screen, landColour, pygame.Rect(330, 30, 140, 300))
    pygame.draw.rect(screen, landColour, pygame.Rect(480, 30, 140, 300))

    menu()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break
    pygame.display.update()

pygame.quit()