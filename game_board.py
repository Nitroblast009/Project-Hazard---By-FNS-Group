import pygame
from constants import *
import country
import random


def makeGameBoard(map):
    '''
    This function is used to create the gameboard. There are several maps including the Americas, Afroeurasia or all. These can be changed in the map parameter.

    Parameters
    ----------
    map : string
        Which map the player wants to play on (All, Americas, Afroeurasia)

    Returns
    -------
    pygame.surface : Returns the gameboard object that enables the game to run
    
    '''
    gameBoard = pygame.Surface((650, 600))
    gameBoard.fill("white")

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
    '''
    This function checks the gameboard using the mouse input, player turn and the gameboard object.

    Parameters
    ----------
    map : string
        Which map the player wants to play on (All, Americas, Afroeurasia)
    mouse : tuple
        What coordinate the mouse is starting at
    playerTurn : string 
        Which player's turn it is when the function is called 

    Returns
    -------
    country object : Returns the country object that is selected by the player 
    
    '''
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

def checkGameWin(map):
    '''
    This function checks the map to see if a player has won the game

    Parameters
    ----------
    map : string
        Which map the player wants to play on (All, Americas, Afroeurasia)
    
    Returns
    -------
    boolean : Returns True or False indicating the player has either won or has not won yet

    '''
    if map == "All" or map == "Americas":
      americasWon = Greenland.player == Nuvuk.player ==  Alaska.player ==  Northwest.player ==  BritishColumbia.player ==  Nunavut.player ==  Alberta.player ==  Ontario.player ==  Newfoundland.player ==  Quebec.player ==  PEI.player == Mexico.player ==  Caribbeans.player == Ecuador.player ==  Columbia.player ==  Venezuela.player ==  Peru.player ==  Brazil.player ==  Chile.player ==  Argentina.player
      
      if map == "Americas": return americasWon
  
    if map == "All" or map == "Afroeurasia":
        afroeurasiaWon = UK.player ==  France.player ==  Germany.player ==  Scandinavia.player ==  Ukraine.player == Turkey.player ==  Egypt.player ==  Nigeria.player ==  Ethiopia.player ==  SaudiArabia.player ==  Madagascar.player == Siberia.player ==  FarEast.player ==  China.player ==  Korea.player == India.player ==  Japan.player == Indonesia.player ==  Philippines.player ==  Australia.player ==  NewZealand.player
    if map == "Afroeurasia": return afroeurasiaWon

  
    if americasWon and afroeurasiaWon: return True
    return False

# GAME PHASE FUNCTIONS
  
def fortify(baseCountry, targetCountry):
    '''
    This function is used during the fortify phase of the game, this function moves troops from one country to another.

    Parameters
    ----------
    baseCountry : country object
        The country that the troops are getting removed from
    targetCountry : country object
        The country that the troops are moving to

    Returns
    -------
    None

    '''
    targetCountry.troops += baseCountry.troops - 1
    baseCountry.troops = 1
  
def attack(defendCountry,attackCountry):
    '''
    This function is used during the attack phase of the game, this function subtracts troops from the attacking and defending country to determine the winner

    Parameters
    ----------
    defendCountry : country object
        The country that is defending the attack
    attackCountry : country object
        The country that is attacking the opposing country 

    Returns
    -------
    None

    '''
    if attackCountry.troops > defendCountry.troops:
        attackingTroops = attackCountry.troops 
        defendingTroops = defendCountry.troops
        difference = attackingTroops - defendingTroops
        defendingTroops -= attackingTroops
        if defendingTroops <= 0:
            if attackCountry.player == "p1":
                defendCountry.player = "p1"
                attackCountry.troops = difference
                attackCountry.troops -= 1
                defendCountry.troops = 1
            elif attackCountry.player == "p2":
                defendCountry.player = "p2"
                attackCountry.troops = difference
                attackCountry.troops -= 1
                defendCountry.troops = 1
                
    if attackCountry.troops < defendCountry.troops:
        result =random.randint(1,2)
        if result == 1:
            if attackCountry.player == "p1":
                attackCountry.player = "p2"
            if attackCountry.player == "p2":
                attackCountry.player = "p1"
    
