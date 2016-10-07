import pygame, sys
from pygame.locals import *
from colors import *



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
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


def draw_char_status():

    '''THIS SECTION OF CODE MOVES A CAT IMAGE AROUND, BASIC Animation'''
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
    '''THIS ENDS THE ANIMATION BASICS'''