from map import Map_Maker
import pygame

class graphics_manager:
    global Map_Maker

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

        '''------------------------------SPRITES------------------------------'''
        self.hero = pygame.image.load('sprites/Hero.png')
        '''----------ENVIRONMENT SPRITES----------'''
        self.wall = pygame.image.load('sprites/dung_wall_25px.png')
        self.hall = pygame.image.load('sprites/dung_floor_25px.png')
        self.door = pygame.image.load('sprites/door_25px.png')
        self.wood = pygame.image.load('sprites/wood_25px.png')
        self.pent = pygame.image.load('sprites/penta_25px.png')
        self.water = pygame.image.load('sprites/water_25px.png')

        self.cam_loc_x = 0
        self.cam_loc_y = 0

        # TODO: Make camera following player METHOD(PASS CURRENT PLAYER X & Y)

    def make_possible_cells_cam_can_see(self):
        for
#         make an array of rows of cells, so it will be an array 20 arrays long, each of those 22 rectangles long.
#         these rectangles will be the things that get blitted over by the sprites of world bits



