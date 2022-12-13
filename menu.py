import pygame

class Menu():
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
        Constructor to the character main screen object

        Parameters
        ----------
        game : object
            This attribute is the game we have created in previous lines of code
    
        '''
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.charactersx, self.charactersy = self.mid_w, self.mid_h + 50
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
            self.game.draw_text('Hazard', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start", 20, self.startx, self.starty)
            self.game.draw_text("Characters", 20, self.charactersx, self.charactersy)
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
                self.cursor_rect.midtop = (self.charactersx + self.distance, self.charactersy)
                self.state = 'Characters'
            elif self.state == 'Characters':
                self.cursor_rect.midtop = (self.creditsx + self.distance, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.distance, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.distance, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Characters':
                self.cursor_rect.midtop = (self.startx + self.distance, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.charactersx + self.distance, self.charactersy)
                self.state = 'Characters'

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
            elif self.state == 'Characters':
                self.game.curr_menu = self.game.characters
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class CharactersMenu(Menu):
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
        self.state = 'Snake'
        self.snakex, self.snakey = self.mid_w, self.mid_h + 20
        self.kangaroox, self.kangarooy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.snakex + self.distance, self.snakey)

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
            self.game.draw_text('Characters [Coming Out in Patch 1.01]', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Snake", 20, self.snakex, self.snakey)
            self.game.draw_text("Kangaroo", 20, self.kangaroox, self.kangarooy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        '''
        This method checks the mouse to see which character was chosen

        Returns
        -------
        None
        
        '''
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Snake':
                self.state = 'Kangaroo'
                self.cursor_rect.midtop = (self.kangaroox + self.distance, self.kangarooy)
            elif self.state == 'Kangaroo':
                self.state = 'Snake'
                self.cursor_rect.midtop = (self.snakex + self.distance, self.snakey)
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
          


