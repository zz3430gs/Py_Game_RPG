import pygame, sys
from pygame.locals import *
from colors import *
# import map
import math


def render_xp_bar( base_surf, hero):
    x_y_wid_hei_for_outline = (575, 180, 200, 15)
    fill_width = determine_xp_bar(hero['xp'], hero['next_lvl'])
    x_y_wid_hei_for_fill = (576, 181, fill_width, 13)
    empty_bar = pygame.draw.rect(base_surf, Black, x_y_wid_hei_for_outline, 1)
    fill_bar = pygame.draw.rect(base_surf, White, x_y_wid_hei_for_fill)


def determine_xp_bar( xp, next_lvl):
    #     198 pixels max length so... xp/nxt_lvl = percent
    percent = (xp / next_lvl)
    bar_width = math.floor(percent * 198)
    return bar_width


hero = {'xp':330,
        'next_lvl' : 500}
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
    render_xp_bar(DISPLAYSURF,hero)
    # DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()



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
