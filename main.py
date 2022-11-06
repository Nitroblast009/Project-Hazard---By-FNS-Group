import pygame
from pygame.locals import QUIT

from constants import *
from game_board import makeGameBoard

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Project Hazard")
screen.fill(mainScreenColour)

running = True
while running:
    # aboutUs(screen)
    # menu()

    screen.blit(makeGameBoard("All"), (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            break

    pygame.display.update()
