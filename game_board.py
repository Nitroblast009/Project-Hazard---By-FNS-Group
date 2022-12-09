import pygame
from constants import *
import country


def makeGameBoard(map):
    gameBoard = pygame.Surface((650, 600))
    gameBoard.fill("white")

    """ Gridlines:
    for i in range(7):
        pygame.draw.rect(gameBoard, "black", (i * 100, 0, 1, 600))

    for i in range(6):
        pygame.draw.rect(gameBoard, "black", (0, i * 100, 700, 1))
    """
   

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

    try:
        country.selectedCountry.draw(gameBoard)
    except:
        pass
    return gameBoard


def checkGameBoard(map, mouse, playerTurn):
    if country.selectedCountry != None:
        country.selectedCountry.selected = False
        country.selectedCountry = None

    if map == "All" or map == "Americas":
        Greenland.check(mouse, playerTurn)

        Nuvuk.check(mouse, playerTurn)
        Alaska.check(mouse, playerTurn)
        Northwest.check(mouse, playerTurn)
        BritishColumbia.check(mouse, playerTurn)
        Nunavut.check(mouse, playerTurn)
        Alberta.check(mouse, playerTurn)
        Ontario.check(mouse, playerTurn)
        Newfoundland.check(mouse, playerTurn)
        Quebec.check(mouse, playerTurn)
        PEI.check(mouse, playerTurn)

        Mexico.check(mouse, playerTurn)
        Caribbeans.check(mouse, playerTurn)

        Ecuador.check(mouse, playerTurn)
        Columbia.check(mouse, playerTurn)
        Venezuela.check(mouse, playerTurn)
        Peru.check(mouse, playerTurn)
        Brazil.check(mouse, playerTurn)
        Chile.check(mouse, playerTurn)
        Argentina.check(mouse, playerTurn)

    if map == "All" or map == "Afroeurasia":

        UK.check(mouse, playerTurn)
        France.check(mouse, playerTurn)
        Germany.check(mouse, playerTurn)
        Scandinavia.check(mouse, playerTurn)
        Ukraine.check(mouse, playerTurn)

        Turkey.check(mouse, playerTurn)
        Egypt.check(mouse, playerTurn)
        Nigeria.check(mouse, playerTurn)
        Ethiopia.check(mouse, playerTurn)
        SaudiArabia.check(mouse, playerTurn)
        Madagascar.check(mouse, playerTurn)

        Siberia.check(mouse, playerTurn)
        FarEast.check(mouse, playerTurn)
        China.check(mouse, playerTurn)
        Korea.check(mouse, playerTurn)
        India.check(mouse, playerTurn)
        Japan.check(mouse, playerTurn)

        Indonesia.check(mouse, playerTurn)
        Philippines.check(mouse, playerTurn)
        Australia.check(mouse, playerTurn)
        NewZealand.check(mouse, playerTurn)

    return country.selectedCountry

# GAME PHASE FUNCTIONS
  
def fortify(baseCountry, targetCountry):
  targetCountry.troops += baseCountry.troops - 1
  baseCountry.troops = 1
  
def attack(defendCountry,attackCountry):
    print("hi")
    if attackCountry.troops > defendCountry.troops:
        attackingTroops = attackCountry.troops 
        defendingTroops = defendCountry.troops
        defendingTroops -= attackingTroops
        if defendingTroops <= 0:
            if attackCountry.player == "p1":
                defendCountry.player = "p1"
                print(defendCountry.player)
            elif attackCountry.player == "p2":
                defendCountry.player = "p2"
                print(defendCountry.player)
                

        
    




    
#     minus troops and change colour of countries here
#     gets called from main, and under mouse click state if current gamephase == attackPhase, set coutnry that is getting attacked as another mouseclick, pass that into this function and this function changes the colour and troop count

