import pygame


class Text_Manager:

    STAT_BOX_COL_X = 52
    STAT_BOX_COL_Y = 2

    BATTLE_BOX_X = 3
    BATTLE_BOX_Y = 26

    BLINK_SPEED_ON = 30
    BLINK_SPEED_OFF = 5

    def __init__(self, base_surf):

        # statPageConstants
        self.RIGHT_MENU_GRID_WIDTH = 80
        self.RIGHT_MENU_GRID_HEIGHT = 30
        # FONT STUFF
        self.FONT_NAME = 'berlinsansfbdemi'
        self.LARGE_FONT_SIZE = 20
        self.small_FONT_SIZE = 12
        # self.base_surf = base_surf
        # For most Character stuff
        self.LARGE_FONT = pygame.font.Font(self.FONT_NAME, self.LARGE_FONT_SIZE)
        # font size is returned as a list of two values
        self.LARGE_FONT_WIDTH = self.LARGE_FONT.size(' ')[0]
        self.LARGE_FONT_HEIGHT = self.LARGE_FONT.size(' ')[1]
        # For most Battlebox stuff
        self.SMALL_FONT = pygame.font.Font(self.FONT_NAME, self.small_FONT_SIZE)
        self.SMALL_FONT_WIDTH = self.SMALL_FONT.size(' ')[0]
        self.SMALL_FONT_HEIGHT = self.SMALL_FONT.size(' ')[1]
        # THIS IS THE TEXT SURFACE TO BE APPLIED TO THE MAIN SURFACE LATER

        self.main_text_area = base_surf.convert()
        # THESSE ARE THE LINES OF TEXT THAT WILL SHOW UP IN THE BATTLE_BOX
        self.battle_box_lines = []

    # THIS METHOD ACTUALLY BLITS TEXT ONTO THE GAME SURFACE
    # def update(self):
    #
    #
    # this method takes the string of text, the color, and two positional arguments, finally a large or small boolean
    def add_text(self, t, color, col_x, col_y,size_bool):
        if size_bool == True:
            the_text = self.LARGE_FONT.render(t,True, color)
            self.main_text_area.blit(the_text, (col_x*self.LARGE_FONT_WIDTH, col_y*self.LARGE_FONT_HEIGHT))
            # print('This is large text')
        elif size_bool == False:
            the_text = self.SMALL_FONT.render(t, True, color)
            self.main_text_area.blit(the_text, (col_x * self.SMALL_FONT_WIDTH, col_y * self.SMALL_FONT_HEIGHT))
            # print('This is small text')
