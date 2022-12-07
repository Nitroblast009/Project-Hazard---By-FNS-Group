import pygame
import time

from constants import *
from game_board import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Project Hazard")
selectedCountry = None
selectedCountryName = "None"
playerTurn = "p2"
gamePhase =  "DRAFT"
running = True

while running:
  screen.fill((255, 99, 51))
  # Add main game board
  gameBoard = makeGameBoard("All"), (0, 0)
  screen.blit(makeGameBoard("All"), (0, 0))

  # Selected text
  font = pygame.font.SysFont('arial', 30)
  selectedCountryText = font.render(
      "Selected: " + selectedCountryName, True, "black")
  selectedCountryRect = selectedCountryText.get_rect()
  selectedCountryRect.center = (380, 560)

  # Player turn text
  font = pygame.font.SysFont('arial', 21)
  playerTurnText = font.render(
      "Player Turn: " + playerTurn[-1], True, "black")
  playerTurnRect = playerTurnText.get_rect()
  playerTurnRect.center = (727, 10)

  # Game phase text
  gamePhaseText = font.render(
      gamePhase, True, "black")
  gamePhaseRect = gamePhaseText.get_rect()
  gamePhaseRect.center = (727, 60)

  screen.blit(selectedCountryText, selectedCountryRect)
  screen.blit(playerTurnText, playerTurnRect)
  screen.blit(gamePhaseText, gamePhaseRect)

  for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          mouseX, mouseY = pygame.mouse.get_pos()

          selectedCountry = checkGameBoard(
              "All", (mouseX, mouseY), playerTurn)
          
          selectedCountryName = "None" if selectedCountry == None else selectedCountry.name + " (" + str(country.selectedCountry.troops) + ")"
          
      elif gamePhase == "ATTACK" or gamePhase == "FORTIFY":
            selectedCountry2 = checkGameBoard(
                "All", (mouseX, mouseY), playerTurn)
            selectedCountryName = "None" if selectedCountry == None else selectedCountry.name + " (" + str(country.selectedCountry.troops) + ")"

    
      
      elif event.type == pygame.QUIT:
          running = False
          break
      
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        
        # For DRAFT Phase
        if gamePhase == "DRAFT" and selectedCountry != None:
          selectedCountry.troops += 2
          selectedCountryName = selectedCountry.name + " (" + str(country.selectedCountry.troops) + ")"
          gamePhase = "ATTACK"
          
          selectedCountry.selected = False
          selectedCountry = None
          selectedCountryName = "None"
        
        
        
  pygame.display.update()