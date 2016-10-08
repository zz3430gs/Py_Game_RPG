import pygame
import random
import colors
import sys
from pygame.locals import *


# http://usingpython.com/adding-an-inventory/
# Sort out how to make walls block movement
WALL = 0
HALL = 1
DOOR = 2
WATER = 3
WOOD = 4
PENT = 5

tile_map = [
    [WALL,WALL,WALL,WALL,WALL,WALL,WALL],
    [WALL,HALL,HALL,HALL,HALL,HALL,WALL],
    [WALL,HALL,WALL,WALL,WALL,DOOR,WALL],
    [WALL,HALL,DOOR,HALL,HALL,HALL,WALL],
    [WALL,HALL,WALL,HALL,HALL,HALL,WALL],
    [WALL,HALL,WALL,WALL,WALL,WALL,WALL],
    [WALL,WALL,WALL,WALL,WALL,WALL,WALL],
    [WOOD,WOOD,WOOD,WOOD,WOOD,WOOD,WOOD]
]
HERO = pygame.image.load('sprites/Hero.png')
textures = {
    WALL: pygame.image.load('sprites/dung_wall_25px.png'),
    HALL: pygame.image.load('sprites/dung_floor_25px.png'),
    DOOR: pygame.image.load('sprites/door_25px.png'),
    WATER: pygame.image.load('sprites/water_25px.png'),
    WOOD: pygame.image.load('sprites/wood_25px.png'),
    PENT: pygame.image.load('sprites/penta_25px.png')
}
hero_pos = [0, 0]

TILE_SIZE = 25
MAP_WIDTH = 20
MAP_HEIGHT = 20
resources = [WALL,WATER,DOOR,WOOD,HALL,PENT]
# Hard Coded for now, this will randomize poorly atm, but not check for
# rand_tile_map = [[random.choice(resources) for w in range(MAP_WIDTH)] for h in range(MAP_HEIGHT)]
rand_tile_map = [[WALL for w in range(MAP_WIDTH)] for h in range(MAP_HEIGHT)]

def modify_map_tiles(map_to_mod):
    for rw in range(MAP_HEIGHT):
        for cl in range(MAP_WIDTH):
            randNum = random.randint(0,30)
            if randNum == 0:
                tile = WATER
            elif randNum in range(1,6):
                tile = WALL
            elif randNum in range(7,18):
                tile = HALL
            elif randNum in range(19,22):
                tile = DOOR
            elif randNum == 30:
                tile = PENT
            else:
                tile = WOOD
            map_to_mod[rw][cl] = tile

modify_map_tiles(rand_tile_map)
print(rand_tile_map)


pygame.init()
SURF = pygame.display.set_mode((MAP_WIDTH*TILE_SIZE, MAP_HEIGHT*TILE_SIZE))
def check_walls_near_hero(map, hero_pos):

while True:
    # Listen for events, this is about to get a whole lot bigger
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        # THIS BLOCK TO BE SEPERTED INTO THE INPUT CONTROLLER

        # TODO: write a check for walls method that constantly runs, and checks if the four surrounding blocks are walls
        elif event.type == KEYDOWN:
            if(event.key == K_RIGHT) and hero_pos[0] < MAP_WIDTH-1 and hero_pos[0]+1 != WALL:
                hero_pos[0] += 1
            if (event.key == K_LEFT) and hero_pos[0] >= 1:
                hero_pos[0] -= 1
            if (event.key == K_UP) and hero_pos[1] >= 1:
                hero_pos[1] -= 1
            if (event.key == K_DOWN) and hero_pos[1] < MAP_HEIGHT-1:
                hero_pos[1] += 1
            if (event.key == K_a):
    #             ATTACK!
                print('ATTACKING!')
    # Rando gen the map
    for row in range(MAP_HEIGHT):
        for column in range(MAP_WIDTH):
            SURF.blit(textures[rand_tile_map[row][column]],(column*TILE_SIZE,row*TILE_SIZE))

    # display the Hero
    SURF.blit(HERO,(hero_pos[0]*TILE_SIZE, hero_pos[1]*TILE_SIZE))
    pygame.display.update()