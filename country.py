import pygame, pygame.gfxdraw
import constants

selectedCountry = None


def getTriangleArea(p1, p2, p3):
    '''
    This function gets the area of a triangle, given 3 of its vertices. It is purely mathematical and is not solely intended for this game. It is used to check whether the user's cursor is within a triangular Country (see documentation for Country.check() for more details).

    Parameters
    ----------
    p1 : tuple(int, int)
        The x and y coordinates of the first vertex.
    p2 : tuple(int, int)
        The x and y coordinates of the second vertex.
    p3 : tuple(int, int)
        The x and y coordinates of the third vertex.

    Returns
    -------
    int : The area of the triangle
    
    '''
  
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


class Country:
    '''
    This class represents a country in our game. It has several repeatedly used attributes and methods that play a key role in game functionality (see constructor documentation for more details).
    '''
  
    selected = False
    coords = []
    neighbours = []
    name = ""
    player = ""
    troops = 0

    def __init__(self, name, points, player, troops, neighbours):
        '''
    The constructor for the country class takes in key info that determines the object's subsequent behavior.

    Parameters
    ----------
    name : string
        The name of this country. Is used to check whether it is a neighbour for other countries, as well as identify it across files.
    points : tuple(tuple(int,int), tuple(int,int), tuple(int,int), [tuple(int,int)])
        The vertices of the country's shape on the game board. Each vertex has an x and y coordinate. 3 vertices creates a triangular country and 4 creates a rectangular country.
    player : string 
        Who owns this country. Can either be "p1" or "p2"
    troops : int
        How many troops occupy this country.
    neighbours : list(string)
        Which countries neighbour this country. Used to determine attack and fortify behavior.
    
    '''
      
        self.coords = points
        self.name = name
        self.player = player
        self.troops = troops
        self.neighbours = neighbours

    def draw(self, surface):
      '''
    This method draws the country on to screen every frame. Draws in red if player 1 owns this country or blue if player 2. Also if country is currently selected, its colour shade darkens. Draws country using the points specified from its constructor.

    Parameters
    ----------
    surface : pygame.Surface
        The surface which to draw the country on.
    
    '''
      if self.player == "p1":
        colour = pygame.Color("0xb51818") if self.selected else pygame.Color("red")
      elif self.player == "p2":
        colour = pygame.Color("0x014080") if self.selected else pygame.Color("0x0271ad")

      pygame.gfxdraw.filled_polygon(surface, self.coords, colour)
      
      pygame.draw.polygon(
            surface, "black", self.coords, width=5 if self.selected else 4)


    def check(self, mouseCoord, playerTurn):
      '''
      This method checks whether the user has clicked on this country. For rectangular countries, the method checks whether the cursor's x and y coordinates are within the bounds of the country's bottom leftmost point and top rightmost point. For triangular countries, the method firsts finds the area of this country, and then finds the area of three separate triangles made by combining the mouse's coordinates with two of three coordinates of the country. If the sum of those three triangles is equal to the original area of the country, then the cursor is within this country. Uses the aforementioned getTriangleArea() function.
  
      Parameters
      ----------
      mouseCoord : tuple(int,int)
          The x and y coordinates of the user's cursor.
      playerTurn : string
          Who's turn in the game it currently is. Cannot select a country that doesn't belong to you on your turn. Can either be "p1" or "p2".
     '''
    
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

  
      