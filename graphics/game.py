import graphics_manager as GM
import pygame
from colors import *
from input_controller import input_controller as IC
from map import Map_Maker as MM

from characters.Hero import Hero
from graphics.main_display import Main_Display as MD
from text_manager import Text_Manager as TM


def main():
    while True:
        # make the screen object
        pygame.init()
        md = MD()
        mm = MM()
        # instantiate hero
        # TODO: Make this a DB lookup or a new Game
        hero = Hero('Grognak', mm.hero_start)
        gm = GM.graphics_manager(md.base_surface, hero)
        tm = TM(md.base_surface, hero)

        gm.update_game()
        tm.update()
        ic = IC(gm,tm, hero)

        # once text manager is working...
        # tm = TM()

        # initialize the pygame graphics module



        # main_display.keep_camera_focus
        # main_display_render_hero
        # get our key listener
        # TODO: Listener is working, make it do stuff

        pygame.display.update()


main()
# hero = {'xp': 330,
#         'next_lvl' : 500}
# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((800,600))
# pygame.display.set_caption('Hello World')
#
# fontObj = pygame.font.Font('freesansbold.ttf',12)
# textSurfaceObj = fontObj.render('Hello World Text!', True, White, Black)
# textRectObj = textSurfaceObj.get_rect()
# textRectObj.center = (200,150)
# # x,y of top left corner and then w&h
# char_stat_box_dimensions = (550,0,250,200)
# command_box_dimensions = (550,200,250,200)
# inventory_box_dimensions = (550,400,250,200)
#
# battle_log = (0,500,550,100)
#
# while True:
#     DISPLAYSURF.fill(White)
#     pygame.draw.rect(DISPLAYSURF, Red, char_stat_box_dimensions)
#     pygame.draw.rect(DISPLAYSURF, Green, command_box_dimensions)
#     pygame.draw.rect(DISPLAYSURF, Purple, inventory_box_dimensions)
#     pygame.draw.rect(DISPLAYSURF, Blue, battle_log)
#     render_xp_bar(DISPLAYSURF,hero)
#     # DISPLAYSURF.blit(textSurfaceObj, textRectObj)
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()



# pygame.init()
# FPS = 30
# fpsClock = pygame.time.Clock()
#
# displaySURF = pygame.display.set_mode((800,600),0,32)
# pygame.display.set_caption('Simple Expandible RPG')
# catImg = pygame.image.load('cat.png')
# catx = 10
# caty = 10
# direction = 'right'
#
# while True:
#     displaySURF.fill(White)
#     if direction == 'right':
#         catx += 5
#         if catx == 280:
#             direction = 'down'
#     elif direction == 'down':
#         caty += 5
#         if caty == 200:
#             direction = 'left'
#     elif direction == 'left':
#         catx -= 5
#         if catx == 10:
#             direction = 'up'
#     elif direction == 'up':
#         caty -= 5
#         if caty == 10:
#             direction = 'right'
#     displaySURF.blit(catImg, (catx, caty))
#
#
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#     pygame.display.update()
#     fpsClock.tick(FPS)
