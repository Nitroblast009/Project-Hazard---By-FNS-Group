import pygame
from constants import *
import country


def makeGameBoard(map, screen):
    gameBoard = pygame.Surface((650, 600))
    gameBoard.fill("white")

    """ Gridlines:
    for i in range(7):
        pygame.draw.rect(gameBoard, "black", (i * 100, 0, 1, 600))

    for i in range(6):
        pygame.draw.rect(gameBoard, "black", (0, i * 100, 700, 1))
    """
   

    if map == "All" or map == "Americas":
        Greenland.draw(gameBoard, screen)

        Nuvuk.draw(gameBoard, screen)
        Alaska.draw(gameBoard, screen)
        Northwest.draw(gameBoard, screen)
        BritishColumbia.draw(gameBoard, screen)
        Nunavut.draw(gameBoard, screen)
        Alberta.draw(gameBoard, screen)
        Ontario.draw(gameBoard, screen)
        Newfoundland.draw(gameBoard, screen)
        Quebec.draw(gameBoard, screen)
        PEI.draw(gameBoard, screen)

        Mexico.draw(gameBoard, screen)
        Caribbeans.draw(gameBoard, screen)

        Ecuador.draw(gameBoard, screen)
        Columbia.draw(gameBoard, screen)
        Venezuela.draw(gameBoard, screen)
        Peru.draw(gameBoard, screen)
        Brazil.draw(gameBoard, screen)
        Chile.draw(gameBoard, screen)
        Argentina.draw(gameBoard, screen)

    if map == "All" or map == "Afroeurasia":
        UK.draw(gameBoard, screen)
        France.draw(gameBoard, screen)
        Germany.draw(gameBoard, screen)
        Scandinavia.draw(gameBoard, screen)
        Ukraine.draw(gameBoard, screen)

        Turkey.draw(gameBoard, screen)
        Egypt.draw(gameBoard, screen)
        Nigeria.draw(gameBoard, screen)
        Ethiopia.draw(gameBoard, screen)
        SaudiArabia.draw(gameBoard, screen)
        Madagascar.draw(gameBoard, screen)

        Siberia.draw(gameBoard, screen)
        FarEast.draw(gameBoard, screen)
        China.draw(gameBoard, screen)
        Korea.draw(gameBoard, screen)
        India.draw(gameBoard, screen)
        Japan.draw(gameBoard, screen)

        Indonesia.draw(gameBoard, screen)
        Philippines.draw(gameBoard, screen)
        Australia.draw(gameBoard, screen)
        NewZealand.draw(gameBoard, screen)

    try:
        country.selectedCountry.draw(gameBoard, screen)
    except:
        pass
    return gameBoard


def checkGameBoard(map=None, mouse=None):
    if country.selectedCountry != None:
        country.selectedCountry.selected = False
        country.selectedCountry = None

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

    return "None" if country.selectedCountry == None else country.selectedCountry.name + " (" + str(country.selectedCountry.troops) + ")"
