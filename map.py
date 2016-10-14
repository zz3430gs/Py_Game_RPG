import pygame
import random
import math
import colors
import sys
from pygame.locals import *
import pcdungeon as pcd


class Map_Maker:
    def __init__(self):

        # http://usingpython.com/adding-an-inventory/
        # Sort out how to make walls block movement
        WALL = 0
        HALL = 1
        DOOR = 2
        WATER = 3
        WOOD = 4
        PENT = 5

        # HERO = pygame.image.load('sprites/Hero.png')
        # hero_pos = [0, 0]

        self.textures = {
            WALL: pygame.image.load('sprites/dung_wall_25px.png'),
            HALL: pygame.image.load('sprites/dung_floor_25px.png'),
            DOOR: pygame.image.load('sprites/door_25px.png'),
            WATER: pygame.image.load('sprites/water_25px.png'),
            WOOD: pygame.image.load('sprites/wood_25px.png'),
            PENT: pygame.image.load('sprites/penta_25px.png')
        }
        # These variables comtrol the generation of rooms, how many, max and min size.
        # TODO: Make these reactive to the level of the hero?
        self.MAX_ROOMS = 20
        self.min_ROOMSIZE = 3
        self.max_ROOMSIZE = 8

        self.TILE_SIZE = 25
        self.MAP_WIDTH = 51
        self.MAP_HEIGHT = 51
        self.SCREEN_WIDTH = 22
        self.SCREEN_HEIGHT = 20

        self.resources = [WALL, WATER, DOOR, WOOD, HALL, PENT]
        # TODO: make sure starter map is renamed throughout document
        self.starter_map = [[WALL for w in range(self.MAP_WIDTH)] for h in range(self.MAP_HEIGHT)]

        # This places the rooms in the map, then checks each room against each other troom to make suyre it is not overlapping anotehr
        def place_rooms_in_map():
            all_rooms = []

            for r in range(self.MAX_ROOMS):
                w = self.min_ROOMSIZE + random.randint(0, self.max_ROOMSIZE - self.min_ROOMSIZE + 1)
                h = self.min_ROOMSIZE + random.randint(0, self.max_ROOMSIZE - self.min_ROOMSIZE + 1)
                x_pos = random.randint(0, self.MAP_WIDTH - w - 1) + 1
                y_pos = random.randint(0, self.MAP_HEIGHT - h - 1) + 1
                this_room = pcd.Room(x_pos, y_pos, w, h)
                check_fail = False
                # check for overlapping rooms

                for other_room in all_rooms:
                    if this_room.intersects(other_room):
                        check_fail = True
                        break
                if check_fail != True:
                    # TODO: for room in all_rooms: replace the wall sections with one of two types of floor sections(WOOD, HALL)
                    center = this_room.center
                    if len(all_rooms) != 0:
                        prev_center = all_rooms[len(all_rooms) - 1].center
                        if random.randint(1, 2) == 1:
                            h_corridors(prev_center[0], center[0], prev_center[1])
                            v_corridor(prev_center[1], center[1], prev_center[0])
                        else:
                            v_corridor(prev_center[1], center[1], prev_center[0])
                            h_corridors(prev_center[0], center[0], prev_center[1])
                if check_fail != True:
                    all_rooms.append(this_room)
            carve_all_rooms(all_rooms)

            for row in self.starter_map:
                print(row)

        def carve_all_rooms(all_rooms):

            for room in all_rooms:
                wood_or_hall = random.randint(1, 2)
                if wood_or_hall == 1:
                    tile_type = HALL
                else:
                    tile_type = WOOD
                for row in range(room.height):
                    for col in range(room.width):
                        self.starter_map[room.x1 + row][room.y1 + col - 1] = tile_type

        '''MAKE SOME CORRIDORS'''

        def h_corridors(x1, x2, y):
            for x in range(min(x1, x2) + 1, max(x1, x2) + 1):
                # Place a Hall Block in this cell.
                self.starter_map[x][y] = HALL

        def v_corridor(y1, y2, x):
            for y in range(min(y1, 2) + 1, max(y1, y2) + 1):
                # Place a hall in this location
                self.starter_map[x][y] = HALL

        # def modify_map_tiles(map_to_mod):
        #     for rw in range(self.MAP_HEIGHT):
        #         for cl in range(self.MAP_WIDTH):
        #             randNum = random.randint(0,30)
        #             if randNum == 0:
        #                 tile = WATER
        #             elif randNum in range(1,6):
        #                 tile = WALL
        #             elif randNum in range(7,18):
        #                 tile = HALL
        #             elif randNum in range(19,22):
        #                 tile = DOOR
        #             elif randNum == 30:
        #                 tile = PENT
        #             else:
        #                 tile = WOOD
        #             map_to_mod[rw][cl] = tile
        place_rooms_in_map()


mm = Map_Maker
mm()
# SURF.blit(textures[rand_tile_map[row][column]],(column*TILE_SIZE,row*TILE_SIZE))
