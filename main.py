import pygame
import time

from constants import *
from game_board import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 99, 51))
pygame.display.set_caption("Project Hazard")
selectedCountry = "None"
playerTurn = "p2"

running = True
while running:

    # Add main game board
    screen.blit(makeGameBoard("All"), (0, 0))

    # Selected text
    font = pygame.font.SysFont('arial', 30)
    selectedCountryText = font.render(
        "Selected: " + selectedCountry, True, "black")
    selectedCountryRect = selectedCountryText.get_rect()
    selectedCountryRect.center = (380, 560)

    # Player turn text
    font = pygame.font.SysFont('arial', 21)
    playerTurnText = font.render(
        "Player Turn: " + playerTurn[-1], True, "black")
    playerTurnRect = playerTurnText.get_rect()
    playerTurnRect.center = (727, 10)

    screen.blit(selectedCountryText, selectedCountryRect)
    screen.blit(playerTurnText, playerTurnRect)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()

            selectedCountry = checkGameBoard(
                "All", (mouseX, mouseY), playerTurn)

        elif event.type == pygame.QUIT:
            running = False
            break

    pygame.display.update()
