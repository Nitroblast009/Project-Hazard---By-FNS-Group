import pygame
from constants import white
pygame.init()

def aboutUs(screen):
    '''
    This function creates our about us page

    Parameters
    ----------
    screen : pygame.surface 
        The screen the about us page resides in


    Returns
    -------
    None

    '''
    font = pygame.font.SysFont('arial', 50)
    text = font.render('About us', True, white)
    font2 = pygame.font.SysFont('arial', 15)
    text2 = font2.render('A game designed by: Faizaan, Ninghan And Sarim', False, white)
    font3 = pygame.font.SysFont('arial', 15)
    text3 = font3.render('Our github link: https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group', False, white)
    font4 = pygame.font.SysFont('arial', 15)
    text4 = font4.render('We are just a team of students doing their assignment. B) ', False, white)
    screen.blit(text, (35,40))
    screen.blit(text2, (35, 100))
    screen.blit(text3, (35, 125))
    screen.blit(text4, (35, 150))

    pygame.display.update()

    
pygame.quit()