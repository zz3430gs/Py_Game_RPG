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
        # For most Battlebox stuff
        self.SMALL_FONT = pygame.font.Font(self.FONT_NAME, self.small_FONT_SIZE)
        # THIS IS THE TEXT SURFACE TO BE APPLIED TO THE MAIN SURFACE LATER
        self.main_text_area = base_surf.convert()
        # THESSE ARE THE LINES OF TEXT THAT WILL SHOW UP IN THE BATTLE_BOX
        self.battle_box_lines = []

