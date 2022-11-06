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
        Greenland.draw(gameBoard)

        Nuvuk.draw(gameBoard)
        Alaska.draw(gameBoard)
        Northwest.draw(gameBoard)
        BritishColumbia.draw(gameBoard)
        Nunavut.draw(gameBoard)
        Alberta.draw(gameBoard)
        Ontario.draw(gameBoard)
        Newfoundland.draw(gameBoard)
        Quebec.draw(gameBoard)
        PEI.draw(gameBoard)

        Mexico.draw(gameBoard)
        Caribbeans.draw(gameBoard)

        Ecuador.draw(gameBoard)
        Columbia.draw(gameBoard)
        Venezuela.draw(gameBoard)
        Peru.draw(gameBoard)
        Brazil.draw(gameBoard)
        Chile.draw(gameBoard)
        Argentina.draw(gameBoard)

    if map == "All" or map == "Afroeurasia":
        UK.draw(gameBoard)
        France.draw(gameBoard)
        Germany.draw(gameBoard)
        Scandinavia.draw(gameBoard)
        Ukraine.draw(gameBoard)

        Turkey.draw(gameBoard)
        Egypt.draw(gameBoard)
        Nigeria.draw(gameBoard)
        Ethiopia.draw(gameBoard)
        SaudiArabia.draw(gameBoard)
        Madagascar.draw(gameBoard)

        Siberia.draw(gameBoard)
        FarEast.draw(gameBoard)
        China.draw(gameBoard)
        Korea.draw(gameBoard)
        India.draw(gameBoard)
        Japan.draw(gameBoard)

        Indonesia.draw(gameBoard)
        Philippines.draw(gameBoard)
        Australia.draw(gameBoard)
        NewZealand.draw(gameBoard)

    return gameBoard
