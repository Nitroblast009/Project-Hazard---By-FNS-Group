import pygame, pygame.gfxdraw
import constants

selectedCountry = None


def getTriangleArea(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


class Country:
    selected = False
    coords = []
    neighbours = []
    name = ""
    player = ""
    troops = 0

    def __init__(self, name, points, player, troops, neighbours):
        self.coords = points
        self.name = name
        self.player = player
        self.troops = troops
        self.neighbours = neighbours

    def draw(self, surface):
      if self.player == "p1":
        colour = pygame.Color("0xb51818") if self.selected else pygame.Color("red")
      elif self.player == "p2":
        colour = pygame.Color("0x014080") if self.selected else pygame.Color("0x0271ad")

      pygame.gfxdraw.filled_polygon(surface, self.coords, colour)
      
      pygame.draw.polygon(
            surface, "black", self.coords, width=5 if self.selected else 4)


    def check(self, mouseCoord, playerTurn):
        global selectedCountry
        if self.player == playerTurn:
          if len(self.coords) == 3:
              baseArea = getTriangleArea(
                  self.coords[0], self.coords[1], self.coords[2])
  
              area1 = getTriangleArea(mouseCoord, self.coords[0], self.coords[1])
              area2 = getTriangleArea(mouseCoord, self.coords[1], self.coords[2])
              area3 = getTriangleArea(mouseCoord, self.coords[2], self.coords[0])
              checkArea = area1 + area2 + area3
  
              if baseArea == checkArea:
                  selectedCountry = self
                  self.selected = True
  
          elif len(self.coords) == 4:
              if mouseCoord[0] > self.coords[0][0] and mouseCoord[0] < self.coords[3][0] and mouseCoord[1] < self.coords[0][1] and mouseCoord[1] > self.coords[1][1]:
                  selectedCountry = self
                  self.selected = True

    
        