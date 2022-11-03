import pygame, pygame_menu

pygame.init()

c1=136
c2=8
c3=8

#Resolution of screen
res = (800,600)

#Make screen appear 
screen = pygame.display.set_mode(res)

#Text colour for buttons
colour = (c1,c2,c3)

#Default shade of button
colour_shade = (220,220,200)

#Shade of button when hovered
color_hover_shade = (150,150,150)

#Screen width as a variable
width = screen.width()

#Screen height as a variable 
height = screen.height()

#Texts on screen
font = pygame.font.SysFont('freesansbold.ttf', 32)
text1 = font.render('Play', True, colour )
font2 = pygame.font.SysFont('freesansbold.ttf', 32)
text2 = font2.render('Quit', False, colour)
font3 = pygame.font.SysFont('freesansbold.ttf', 32)

While True:
 for b in 

#Background screen colour
screen.fill ((255,255,255))

#Store mouse location(coordinates)
mouse = pygamoue.mouse.getpos()

#Update display so the mouse is moving on screen 
pygame.display(update)