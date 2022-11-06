import pygame
from constants import *


def makeGameBoard(map=None):
    gameBoard = pygame.Surface((700, 600))
    gameBoard.fill(white)

    if map == "All" or map == "Americas":
        Nuvak.draw(gameBoard)


    if map == "All" or map == "Afroeurasia":
        pass

    return gameBoard
