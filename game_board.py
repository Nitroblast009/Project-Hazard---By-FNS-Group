import pygame

from constants import *
import country


def makeGameBoard(map=None):
    gameBoard = pygame.Surface((650, 600))
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


def checkGameBoard(map=None, mouse=None):
    if map == "All" or map == "Americas":
        Greenland.check(mouse)

        Nuvuk.check(mouse)
        Alaska.check(mouse)
        Northwest.check(mouse)
        BritishColumbia.check(mouse)
        Nunavut.check(mouse)
        Alberta.check(mouse)
        Ontario.check(mouse)
        Newfoundland.check(mouse)
        Quebec.check(mouse)
        PEI.check(mouse)

        Mexico.check(mouse)
        Caribbeans.check(mouse)

        Ecuador.check(mouse)
        Columbia.check(mouse)
        Venezuela.check(mouse)
        Peru.check(mouse)
        Brazil.check(mouse)
        Chile.check(mouse)
        Argentina.check(mouse)

    if map == "All" or map == "Afroeurasia":
        UK.check(mouse)
        France.check(mouse)
        Germany.check(mouse)
        Scandinavia.check(mouse)
        Ukraine.check(mouse)

        Turkey.check(mouse)
        Egypt.check(mouse)
        Nigeria.check(mouse)
        Ethiopia.check(mouse)
        SaudiArabia.check(mouse)
        Madagascar.check(mouse)

        Siberia.check(mouse)
        FarEast.check(mouse)
        China.check(mouse)
        Korea.check(mouse)
        India.check(mouse)
        Japan.check(mouse)

        Indonesia.check(mouse)
        Philippines.check(mouse)
        Australia.check(mouse)
        NewZealand.check(mouse)

        return "None" if country.selectedCountry == None else country.selectedCountry.name
