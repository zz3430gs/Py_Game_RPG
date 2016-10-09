import pygame, sys
from pygame.locals import *
from colors import *
import map
import math

class Main_Display:
    def __init__(self, Game):
        self.window_width = 800
        self.window_height = 600

        pygame.init()
        MAIN_SURFACE = pygame.display.set_mode((self.window_width,self.window_height))
        pygame.display.set_caption('Simple RPG')



    def render_inventory_menu(self,base_surf,hero):
        x_y_wid_hei = (550,400,250,200)
        inv = pygame.draw.rect(base_surf,Blue,x_y_wid_hei)
#         TODO: Create Subsurface that interfaces with Inventory of game

    # This will render a xp bar that is filled according to the Heros xp
    def render_xp_bar(self,base_surf, hero):
        x_y_wid_hei_for_outline = (575, 180, 200, 15)
        fill_width = self.determine_xp_bar(hero.xp, hero.next_lvl)
        x_y_wid_hei_for_fill = (576, 181, fill_width, 13)
        empty_bar = pygame.draw.rect(base_surf, Black, x_y_wid_hei_for_outline, 1)
        fill_bar = pygame.draw.rect(base_surf, White, x_y_wid_hei_for_fill)

    @staticmethod
    def determine_xp_bar(xp, next_lvl):
        #     198 pixels max length so... xp/nxt_lvl = percent
        percent = (xp / next_lvl)
        bar_width = math.floor(percent * 198)
        return bar_width

    def render_char_stat_display(self,base_surf,hero):
        x_y_wid_hei =(550,0,250,200)
        char_stats = pygame.draw.rect(base_surf,Green,x_y_wid_hei)
        # todo: put this in a thread that watches the Hero class for xp_events
        self.render_xp_bar(base_surf,hero)
#         TODO: Create this Subsurface for live updating from data

    def render_basic_commands(self,base_surf):
        x_y_wid_hei =(550,200,250,200)
        commands = pygame.draw.rect(base_surf,Yellow,x_y_wid_hei)
#         TODO: Create This subsurface to live update as game state changes
# TODO: Such as all those display methods you wrote, giving choices

    def render_world_event_log(self,base_surf):
        # TODO: This should have a thread that watches for events
        x_y_wid_hei = (0,500,550,100)
        event_log = pygame.draw.rect(base_surf,Brown,x_y_wid_hei)
#         TODO: Create this subsurface, it will be a world event log(Such as PLayer found 30 gold.
#           todo: or Player Rests for the night. ETC

    def render_battle_menu(self,base_surf,hero):
        x_y_wid_hei = (0,500,550,100)
        battle_menu = pygame.draw.rect(base_surf,Red,x_y_wid_hei)
# TODO:        This will render over the world log when combat occurs. Hopefully

    def visible_map(self,base_surf):
        x_pos = 0
        y_pos = 0
        height = 500
        width = 550



pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,600))
pygame.display.set_caption('Hello World')

fontObj = pygame.font.Font('freesansbold.ttf',12)
textSurfaceObj = fontObj.render('Hello World Text!', True, White, Black)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)
# x,y of top left corner and then w&h
char_stat_box_dimensions = (550,0,250,200)
command_box_dimensions = (550,200,250,200)
inventory_box_dimensions = (550,400,250,200)

battle_log = (0,500,550,100)

while True:
    DISPLAYSURF.fill(White)
    pygame.draw.rect(DISPLAYSURF, Red, char_stat_box_dimensions)
    pygame.draw.rect(DISPLAYSURF, Green, command_box_dimensions)
    pygame.draw.rect(DISPLAYSURF, Purple, inventory_box_dimensions)
    pygame.draw.rect(DISPLAYSURF, Blue, battle_log)
    # DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



def draw_char_status():

    '''THIS SECTION OF CODE MOVES A CAT IMAGE AROUND, BASIC Animation'''