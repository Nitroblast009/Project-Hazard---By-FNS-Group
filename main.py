import pygame
import time
from pygame.locals import QUIT

from constants import *
from game_board import makeGameBoard, checkGameBoard

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Project Hazard")
screen.fill(mainScreenColour)
selectedCountry = "None"

running = True
while running:
    # aboutUs(screen)
    # menu()

    screen.blit(makeGameBoard(map="All"), (0, 0))

    font = pygame.font.SysFont('arial', 40)
    selectedCountryText = font.render(
        "Selected: " + selectedCountry, True, "black")
    selectedCountryRect = selectedCountryText.get_rect()
    selectedCountryRect.center = (380, 560)

    screen.blit(selectedCountryText, selectedCountryRect)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()

            selectedCountry = checkGameBoard(
                map="All", mouse=(mouseX, mouseY))

        elif event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()
