from map import Map_Maker
import pygame

class graphics_manager:
    global Map_Maker
    # needs to know about the map instances, so it can call the maps methods for tiling sprites
    def __init__(self):
        # This is the number of tiles the camera will be able to see on X-axis
        self.cam_width = 22
        # This is the number of tiles the camera will be able to see on Y-axis
        self.cam_height = 20

        # Camera move speeds in different directions in pixels
        self.cam_move_up = 1
        self.cam_move_dn = 14
        self.cam_move_rt = 14
        self.cam_move_lft = 1

        # This is the farthest the cameras screen can pan right/left (
        self.cam_max_pan_x = Map_Maker.MAP_WIDTH - self.cam_width
        # this is the farthest the cameras screen can pan up/dn
        self.cam_max_pan_y = Map_Maker.MAP_HEIGHT - self.cam_height

        self.mainSurf = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        # sprite listing
        '''------------------------------SPRITES------------------------------'''
        self.hero = pygame.image.load('sprites/Hero.png')
        '''----------ENVIRONMENT SPRITES----------'''
        self.wall = pygame.image.load('sprites/dung_wall_25px.png')
        self.hall = pygame.image.load('sprites/dung_floor_25px.png')
        self.door = pygame.image.load('sprites/door_25px.png')
        self.wood = pygame.image.load('sprites/wood_25px.png')
        self.pent = pygame.image.load('sprites/penta_25px.png')
        self.water = pygame.image.load('sprites/water_25px.png')
        # cameras location
        self.cam_loc_x = 0
        self.cam_loc_y = 0

        # TODO: Make camera following player METHOD(PASS CURRENT PLAYER X & Y)


    def make_possible_cells_cam_can_see(self):
        # make an array of rows of cells, so it will be an array 20 arrays tall, each of those 22 rectangles wide.
        # these rectangles will be the things that get blitted over by the sprites of world bits
        visible_tiles = []
        single_row = []
        # this offsets the tiles by 10 pixels from top and left
        insert_tile_start_x = 10
        insert_tile_start_y = 10
        for row in range(22):
            for column in range(20):
                this_tile = pygame.Rect(insert_tile_start_x, insert_tile_start_y, 25, 25)
                single_row.append(this_tile)
                insert_tile_start_x += 25
            #     append the row to the entirety
            visible_tiles.append(single_row)
            # reset variables
            single_row = []
            # make the tile appear one tile lower on the screen
            insert_tile_start_y += 25
            insert_tile_start_x = 10
        return visible_tiles

    def camera_chase_hero(self, hero_x, hero_y):
        # center based on cam_width
        # Never wander from the players position!!! NEVER!!
        self.cam_loc_x = hero_x - int(self.cam_width/2.0)
        self.cam_loc_y = hero_y - int(self.cam_height/2.0)
        # if the camera has wandered off to center
        if self.cam_loc_x < 0:
            # get it in line
            self.camera_x = 0
        elif self.cam_loc_x > 0:
            self.camera_x = self.cam_max_pan_x
        if self.cam_loc_y < 0:
            self.camera_y = 0
        elif self.cam_loc_y>self.cam_max_pan_y:
            self.camera_y = 0




