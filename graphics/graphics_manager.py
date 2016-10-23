import pygame

from graphics import map


class graphics_manager:
    # needs to know about the map instances, so it can call the maps methods for tiling sprites
    def __init__(self, base_surf,mm,hero):
        # This is the number of tiles the camera will be able to see on X-axis
        self.base_surf = base_surf
        self.cam_width = 20
        self.Hero = hero
        # This is the number of tiles the camera will be able to see on Y-axis
        self.cam_height = 20
        # self.starter_map = starter_map
        # Camera move speeds in different directions in pixels
        self.cam_move_up = 1
        self.cam_move_dn = 1
        self.cam_move_rt = 1
        self.cam_move_lft = 1
        self.MM = mm
        # This is the farthest the cameras screen can pan right/left (
        self.cam_max_pan_x = self.MM.MAP_WIDTH - self.cam_width
        # this is the farthest the cameras screen can pan up/dn
        self.cam_max_pan_y = self.MM.MAP_HEIGHT - self.cam_height

        self.mainSurf = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        # sprite listing
        '''------------------------------SPRITES------------------------------'''
        self.hero_image = pygame.image.load('sprites/Hero.png')
        '''----------ENVIRONMENT SPRITES----------'''
        self.visible_tiles = self.make_possible_tiles_cam_can_see()
        # cameras location
        self.cam_loc_x = 0
        self.cam_loc_y = 0
        self.camera_chase_hero(hero.hero_pos[0],hero.hero_pos[1])
        WALL = 0
        WATER = 1
        DOOR = 2
        WOOD = 3
        HALL = 4
        PENT = 5

        self.textures = {
            WALL: pygame.image.load('sprites/dung_wall_25px.png'),
            WATER: pygame.image.load('sprites/water_25px.png'),
            DOOR: pygame.image.load('sprites/door_25px.png'),
            WOOD: pygame.image.load('sprites/wood_25px.png'),
            HALL: pygame.image.load('sprites/dung_floor_25px.png'),
            PENT: pygame.image.load('sprites/penta_25px.png')
        }
        # SURF.blit(textures[rand_tile_map[row][column]],(column*TILE_SIZE,row*TILE_SIZE))
        # TODO: Make camera following player METHOD(PASS CURRENT PLAYER X & Y)

    def make_possible_tiles_cam_can_see(self):
        # make an array of rows of cells, so it will be an array 20 arrays tall, each of those 22 rectangles wide.
        # these rectangles will be the things that get blitted over by the sprites of world bits
        visible_tiles = []
        single_row = []
        # this offsets the tiles by 10 pixels from top and left
        insert_tile_start_x = 10
        insert_tile_start_y = 10
        for row in range(self.cam_width):
            for column in range(self.cam_height):
                this_tile = pygame.Rect(insert_tile_start_x, insert_tile_start_y, 25, 25)
                single_row.append(this_tile)
                insert_tile_start_x += 25
            # append the row to the entirety
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
        self.cam_loc_x = hero_x - int(self.cam_width / 2.0)
        # the Y axias works, x doesnt.
        self.cam_loc_y = hero_y - int(self.cam_height / 2.0)
        # if the camera has wandered off to center
        if self.cam_loc_x < 0:
            # get it in line
            self.cam_loc_x = 0
        elif self.cam_loc_x > 0:
            self.cam_loc_x = self.cam_max_pan_x
        if self.cam_loc_y < 0:
            self.cam_loc_y = 0
        elif self.cam_loc_y > self.cam_max_pan_y:
            self.cam_loc_y = 0

    def legal_camera_move(self, hero):
        x = hero.hero_pos[0]
        y = hero.hero_pos[1]
        # pan up, or not
        if y == (self.cam_loc_y + self.cam_move_up) and self.cam_loc_y > 0:
            self.cam_loc_y -= 1
            #     pan down or not
        elif y == (self.cam_loc_y + self.cam_move_dn) and self.cam_loc_y < self.cam_max_pan_y:
            self.cam_loc_y += 1
            #     pan right or not
        elif x == (self.cam_loc_x + self.cam_move_rt) and self.cam_loc_x < self.cam_max_pan_x:
            self.cam_loc_x += 1
        elif x == (self.cam_loc_x + self.cam_move_lft) and self.cam_loc_x > 0:
            self.cam_loc_x -= 1

    def update_game(self):
        self.base_surf.fill((0,0,0))
        #     call text_manager updater here too
        # # SURF.blit(textures[rand_tile_map[row][column]],(column*TILE_SIZE,row*TILE_SIZE))
        # this should render only tiles that are in the camers view
        # if the hero is exploring render the exploration map
        if self.Hero.state =='explore':
            for row in range(self.cam_height):
                for col in range(self.cam_width):
                    y, x = self.visible_tiles[col][row].topleft
                    # IF IT IS A WALL
                    try:
                        if self.MM.starter_map[col + self.cam_loc_x][row + self.cam_loc_y] == self.MM.resources[0]:
                            # found a wall tile
                            self.base_surf.blit(self.textures[0], (x, y))
                        elif self.MM.starter_map[col + self.cam_loc_x][row + self.cam_loc_y] == self.MM.resources[1]:
                            # found a hall tile
                            self.base_surf.blit(self.textures[1], (x, y))
                        elif self.MM.starter_map[col + self.cam_loc_x][row + self.cam_loc_y] == self.MM.resources[2]:
                            # found a door
                            self.base_surf.blit(self.textures[2], (x, y))
                        elif self.MM.starter_map[col + self.cam_loc_x][row + self.cam_loc_y] == self.MM.resources[3]:
                            # if it is water tile
                            self.base_surf.blit(self.textures[3], (x, y))
                        elif self.MM.starter_map[col + self.cam_loc_x][row + self.cam_loc_y] == self.MM.resources[4]:
                            # If it is wood
                            self.base_surf.blit(self.textures[4], (x, y))
                        elif self.MM.starter_map[col + self.cam_loc_x][row + self.cam_loc_y] == self.MM.resources[5]:
                            self.base_surf.blit(self.textures[5], (x, y))
                    except IndexError as e:
                        print(e)

                    ex = row+self.cam_loc_y
                    why = col+self.cam_loc_x
                    if ex == self.Hero.hero_pos[1] and why == self.Hero.hero_pos[0]:
                        # print('this is ex: '+ex+', this is why: '+why+', this is row:'+row+', this is col:'+col+',hero_pos[0]'+self.Hero.hero_pos[0]+'hero_pos[1]:',self.Hero.hero_pos[1])
                        self.base_surf.blit(self.hero_image, (x, y))
                # self.base_surf.blit(self.hero_image, ((self.Hero.hero_pos[0]*25)+10, (self.Hero.hero_pos[1]+10)))
                    # self.mainSurface.blit(self.sprite_door_open, (x, y))
                    # this way didn't work. Trying others now.
                    # self.base_surf.blit(self.textures[self.MM.starter_map[x][y]], (col*self.MM.TILE_SIZE, row*self.MM.TILE_SIZE))
                    #             draw gameboard
        pygame.display.update()

