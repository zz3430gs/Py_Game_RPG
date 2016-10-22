import math

import pygame

from graphics import colors as C


class Text_Manager:
    STAT_BOX_COL_X = 30
    STAT_BOX_COL_Y = .5

    BATTLE_BOX_X = 3
    BATTLE_BOX_Y = 26

    BLINK_SPEED_ON = 30
    BLINK_SPEED_OFF = 5

    def __init__(self, base_surf, hero):

        # statPageConstants
        self.RIGHT_MENU_GRID_WIDTH = 80
        self.RIGHT_MENU_GRID_HEIGHT = 30
        # Font found via print(pygame.font.match_font('berlinsansfbdemi'))
        self.FONT_NAME = 'C:\Windows\Fonts\BRLNSDB.TTF'
        self.LARGE_FONT_SIZE = 20
        self.small_FONT_SIZE = 14
        # self.base_surf = base_surf
        # For most Character stuff
        self.hero = hero
        self.LARGE_FONT = pygame.font.Font(self.FONT_NAME, self.LARGE_FONT_SIZE)
        # font size is returned as a list of two values
        self.LARGE_FONT_WIDTH = self.LARGE_FONT.size(' ')[0]
        self.LARGE_FONT_HEIGHT = self.LARGE_FONT.size(' ')[1]
        # For most Battlebox stuff
        self.SMALL_FONT = pygame.font.Font(self.FONT_NAME, self.small_FONT_SIZE)
        self.SMALL_FONT_WIDTH = self.SMALL_FONT.size(' ')[0]
        self.SMALL_FONT_HEIGHT = self.SMALL_FONT.size(' ')[1]
        # THIS IS THE TEXT SURFACE TO BE APPLIED TO THE MAIN SURFACE LATER
        self.base_surf = base_surf

        self.battle_box = pygame.Rect(10,600, 550,200)
        self.battle_box_surf = pygame.Surface((550,100))

        self.text_rect = pygame.Rect(550, 0, 250, 600)
        self.main_text_surface = pygame.Surface((250, 600))

        self.main_text_surface.fill(C.Blue)

        # THESSE ARE THE LINES OF TEXT THAT WILL SHOW UP IN THE BATTLE_BOX
        self.battle_box_lines = []

    # THIS METHOD ACTUALLY CREATES TEXT TO BE BLITTED ONTO THE GAME SURFACE VIA add_text()
    def update(self):
        # self.add_text(self.hero.name, C.Red, 400, 400, True)
        # display hero name
        '''RENDER THE HEROES STATS'''
        self.add_text(self.hero.name, C.Red, self.STAT_BOX_COL_X-5, self.STAT_BOX_COL_Y, True)

        # Hero level: Small Font
        self.add_text('Level: '+str(self.hero.level), C.Red, self.STAT_BOX_COL_X-20, self.STAT_BOX_COL_Y+2, False)
        # str, then armor

        self.add_text('Strength: ' + str(self.hero.strength), C.Red, self.STAT_BOX_COL_X + 5, self.STAT_BOX_COL_Y + 2, False)
        self.add_text('Armor:    ' + str(self.hero.armor), C.Red, self.STAT_BOX_COL_X + 5, self.STAT_BOX_COL_Y + 3, False)

        # HP & XP TEXT Numbers
        self.add_text('Health: '+str(self.hero.current_hp)+'/'+str(self.hero.max_hp), C.White, self.STAT_BOX_COL_X, self.STAT_BOX_COL_Y+5, False)
        self.add_text('Experience: ' + str(self.hero.xp) + '/' + str(self.hero.next_level), C.White, self.STAT_BOX_COL_X-5, self.STAT_BOX_COL_Y + 7, False)
        # After all Text is added, then blit to main surf
        self.base_surf.blit(self.main_text_surface, (550, 0))

        # then render the XP and HP bars
        # display movement options, and esc
        self.render_hp_bar(self.base_surf, self.hero)
        self.render_xp_bar(self.base_surf, self.hero)
        self.update_battle_box()
        pygame.display.update(self.text_rect)

    # TODO FIGURE THIS OUT! WHY DOESNT IT RENDER!?
    def update_battle_box(self):
        self.battle_box_surf.fill(C.Red)
        self.base_surf.blit(self.battle_box_surf, (0, 600))
        pygame.display.update(self.battle_box)


    # this method takes the string of text, the color, and two positional arguments, finally a large or small boolean
    def add_text(self, t, color, col_x, col_y, size_bool):
        if size_bool == True:
            the_text = self.LARGE_FONT.render(t, True, color)
            self.main_text_surface.blit(the_text, (col_x * self.LARGE_FONT_WIDTH, col_y * self.LARGE_FONT_HEIGHT))
            # print('This is large text')
        elif size_bool == False:
            the_text = self.SMALL_FONT.render(t, True, color)
            self.main_text_surface.blit(the_text, (col_x * self.SMALL_FONT_WIDTH, col_y * self.SMALL_FONT_HEIGHT))
            # print('This is small text')

    '''THIS IS WHERE THE XP_BAR and HP_BAR have been moved to.  Not ideal but only way I was able to figure it out.'''

    def render_xp_bar(self, base_surf, hero):
        x_y_wid_hei_for_outline = (578, 110, 200, 10)
        fill_width = self.determine_xp_bar(hero.xp, hero.next_level)
        x_y_wid_hei_for_fill = (579, 111, fill_width, 8)
        empty_bar = pygame.draw.rect(base_surf, C.White, x_y_wid_hei_for_outline, 1)
        fill_bar = pygame.draw.rect(base_surf, C.Green, x_y_wid_hei_for_fill)

    @staticmethod
    def determine_xp_bar(xp, next_lvl):
        #     198 pixels max length so... xp/nxt_lvl = percent
        percent = (xp / next_lvl)
        bar_width = math.floor(percent * 198)
        return bar_width

    def render_hp_bar(self, base_surf, hero):
        x_y_wid_hei_for_outline = (578, 75, 200, 12)
        fill_width = self.determine_hp_bar(hero.current_hp, hero.max_hp)
        x_y_wid_hei_for_fill = (579, 76, fill_width, 10)
        empty_bar = pygame.draw.rect(base_surf, C.White, x_y_wid_hei_for_outline, 1)
        fill_bar = pygame.draw.rect(base_surf, C.Red, x_y_wid_hei_for_fill)

    @staticmethod
    def determine_hp_bar(cur_hp, max_hp):
        #     198 pixels
        piece = math.floor(198 / max_hp)
        length = piece * cur_hp
        if cur_hp == max_hp:
            length = 198
        return length