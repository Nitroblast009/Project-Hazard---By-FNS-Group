import pygame
from game_board import *

class Menu():
    map = "All"
    '''
    An object that contains the main screen information, game loop, user input, and draws texts 
    
    Attributes
    -------
    None

    Methods
    -------
    __init__() -> None

    draw_cursor() -> None
      Creates a cursor on the screen
    blit_screen() -> None
      Blits screen 
    
    '''
  
    def __init__(self, game):
        '''
        Constructor that sets up the cursor

        Parameters
        -------
        None
        
        '''
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.distance = - 50

    def draw_cursor(self):
        '''
        Draws the cursor on the screen

        Returns
        -------
        None
        
        '''
        self.game.draw_text('>', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        '''
        Method that blits the screen

        Returns
        -------
        None
        
        '''
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.default_keys()

class MainMenu(Menu):
    '''
    Main menu object is created

    Attributes
    ----------
    Menu : object
        Created in the previous part of the code

    Methods
    -------
    display_menu() -> None
        Displays the main menu
    move_cursor() ->
        moves the cursor up or down
    check_input() -> None
        Checks which menu the user has selected
    
    '''
    def __init__(self, game):
        '''
        Constructor to the map main screen object

        Parameters
        ----------
        game : object
            This attribute is the game we have created in previous lines of code
    
        '''
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.mapsx, self.mapsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.distance, self.starty)

    def display_menu(self):
        '''
        Displays the main menu

        Returns
        -------
        None

        '''
        self.run_display = True
        while self.run_display:
            self.game.user_input()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Hazard', 20, self.game.DISPLAY_W / 2,       self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start", 20, self.startx, self.starty)
            self.game.draw_text("Maps", 20, self.mapsx, self.mapsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        '''
        Moves the cursor up and down 

        Returns
        -------
        None
        
        '''
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.mapsx + self.distance, self.mapsy)
                self.state = 'Maps'
            elif self.state == 'Maps':
                self.cursor_rect.midtop = (self.creditsx + self.distance, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.distance, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.distance, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Maps':
                self.cursor_rect.midtop = (self.startx + self.distance, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.mapsx + self.distance, self.mapsy)
                self.state = 'Maps'

    def check_input(self):
        '''
        User input takes to another specific screen

        Returns
        -------
        None

        '''
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Maps':
                self.game.curr_menu = self.game.maps
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class MapsMenu(Menu):
    '''
    Character menu object is created 
    
    Attributes
    ----------
    menu : object
        This attribute is the game we have created in previous lines of code

    Methods
    -------
    display_menu() -> None
        Displays the actual about us screen
    check_input() -> None
        Checks which character was selected 
    
    '''
    def __init__(self, game):
        '''
        Constructor to the character menu screen object

        Parameters
        ----------
        game : object
            This attribute is the game we have created in previous lines of code
    
        '''
        Menu.__init__(self, game)
        self.state = 'All'
        self.allx, self.ally = self.mid_w, self.mid_h + 20
        self.afroeurasiax, self.afroeurasiay = self.mid_w, self.mid_h + 50
        self.americasx, self.americasy = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.allx + self.distance, self.ally)

    def display_menu(self):
        '''
        Displays the character menu

        Returns
        -------
        None

        '''
        self.run_display = True
        while self.run_display:
            self.game.user_input()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Maps', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("All", 20, self.allx, self.ally)
            self.game.draw_text("Afroeurasia", 20, self.afroeurasiax, self.afroeurasiay)
            self.game.draw_text("Americas", 20, self.americasx, self.americasy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        '''
        This method swithes between which map you want to chose

        Returns
        -------
        None
        
        '''
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'All':
                self.cursor_rect.midtop = (self.afroeurasiax + self.distance, self.afroeurasiay)
                self.state = 'Afroeurasia'
            elif self.state == 'Afroeurasia':
                self.cursor_rect.midtop = (self.americasx + self.distance, self.americasy)
                self.state = 'Americas'
            elif self.state == 'Americas':
                 self.cursor_rect.midtop = (self.allx + self.distance, self.ally)
                 self.state = 'All'
        elif self.game.START_KEY:
          Menu.map = self.state
        
    
              
        elif self.game.START_KEY:
          
            pass

class CreditsMenu(Menu):
    '''
    A credits menu object gets created through the aboutUsMenu method

    Attributes
    ----------
    menu : object
        This attribute is the game we have created in previous lines of code

    Methods
    -------
    display_menu() -> None
        Displays the actual about us screen
    
    '''
    def __init__(self, game):
        '''
        Constructor to build the about us page

        Parameters
        ----------
        game : object 
            The place the about us page will be put
        
        '''
        Menu.__init__(self, game)

    def display_menu(self):
        '''
        This function creates our about us page

        Returns
        -------
        None

        '''
        self.run_display = True
        while self.run_display:
            self.game.user_input()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Sarim, Faizaan and Ninghan', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('Our github link: https://github.com/Nitroblast009/Project-Hazard---By-FNS-Group', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40)
            self.blit_screen()
          


