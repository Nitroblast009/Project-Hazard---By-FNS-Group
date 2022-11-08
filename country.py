import pygame

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
    name = ""

    def __init__(self, name, points=None):
        self.coords = points
        self.name = name

    def draw(self, surface):
        pygame.draw.polygon(
            surface, "blue" if self.selected else "black", self.coords, width=4)

    def check(self, mouseCoord):
        global selectedCountry
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

    def attack():
        pygame.draw.rect(500,300)
