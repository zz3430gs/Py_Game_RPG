'''Here we will define the keyboard commands that will be active.
   THIS WILL BE STATEBASED I.E. if state != combat no attacking possible. etc...'''

import pygame
import sys
from pygame.locals import *
from map import *
from game import *

def key_listener():
    while True:
        # Listen for events, this is about to get a whole lot bigger
        for event in pygame.event.get():
            print(event)
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            # THIS BLOCK TO BE SEPERTED INTO THE INPUT CONTROLLER
            elif event.type == KEYDOWN:
                if(event.key == K_RIGHT) and hero_pos[0] < MAP_WIDTH-1:
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