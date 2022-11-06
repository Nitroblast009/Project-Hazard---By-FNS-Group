import pygame


class Country:
    coords = []

    def __init__(self, points=None):
        self.coords = points

    def draw(self, surface):
        pygame.draw.polygon(surface, "black", self.coords, width=4)
