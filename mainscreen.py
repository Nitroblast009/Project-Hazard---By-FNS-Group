import pygame
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        #Default values for keyboard binds
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        #Create screen
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        #Create window for user
        #self.background = pygame.image.load("Menu Bckgrnd.png")
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.settings = SettingsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
      
    def game_loop(self):
        while self.playing:
            self.user_input()
            if self.START_KEY:
              self.running, self.playing = False, False
              self.curr_menu.run_display = False


    def user_input(self):
        for input in pygame.event.get():
            if input.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if input.type == pygame.KEYDOWN:
                if input.key == pygame.K_RETURN:
                    self.START_KEY = True
                if input.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if input.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if input.key == pygame.K_UP:
                    self.UP_KEY = True

    def default_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)




