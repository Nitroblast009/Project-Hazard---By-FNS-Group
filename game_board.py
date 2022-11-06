import pygame
from constants import *


def makeGameBoard(map=None):
    gameBoard = pygame.Surface((700, 600))
    gameBoard.fill("white")

    for i in range(7):
        pygame.draw.rect(gameBoard, "black", (i * 100, 0, 1, 600))

    for i in range(6):
        pygame.draw.rect(gameBoard, "black", (0, i * 100, 700, 1))

    if map == "All" or map == "Americas":
        Nuvuk.draw(gameBoard)

    if map == "All" or map == "Afroeurasia":
        pass

    return gameBoard
