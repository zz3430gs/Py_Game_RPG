'''Here we will define the keyboard commands that will be active.
   THIS WILL BE STATEBASED I.E. if state != combat no attacking possible. etc...'''

import sys

import pygame
from pygame.locals import *


class input_controller:
    def __init__(self, gm,tm,cm, hero):
        self.key_listener(gm,tm,cm, hero)
        # self.hero = hero

    def key_listener(self, gm,tm,cm, hero):
        while True:
            # Listen for events, this is about to get a whole lot bigger
            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit
                # THIS BLOCK TO BE SEPERTED INTO THE INPUT CONTROLLER

                elif event.type == KEYDOWN:
                    '''EXPLORATION OPTIONS'''
                    if hero.state == 'explore':
                        # THIS APPEARS TO BE WORKING.  ONLY APPEARS TO BE THOUGH SINCE I DONT HAVE THE CAMERA TRACKING WORKING
                        if(event.key == K_RIGHT) and gm.MM.is_valid_move(hero.hero_pos[0]+1, hero.hero_pos[1], hero):
                            hero.hero_pos[0] += 1
                            # cm.is_it_battle_time(False)
                            print(hero.hero_pos)
                        if (event.key == K_LEFT) and gm.MM.is_valid_move(hero.hero_pos[0]-1, hero.hero_pos[1], hero):
                            hero.hero_pos[0] -= 1
                            # cm.is_it_battle_time(False)
                            print(hero.hero_pos)
                        if (event.key == K_UP) and gm.MM.is_valid_move(hero.hero_pos[0], hero.hero_pos[1]-1, hero):
                            hero.hero_pos[1] -= 1
                            # cm.is_it_battle_time(False)
                            print(hero.hero_pos)
                        if (event.key == K_DOWN) and gm.MM.is_valid_move(hero.hero_pos[0], hero.hero_pos[1]+1, hero):
                            hero.hero_pos[1] += 1
                            # cm.is_it_battle_time(False)
                            print(hero.hero_pos)
                        if (event.key == K_r):
                            print('resting')
                            # combat_occurred = cm.is_it_battle_time()
                            # hero.gain_hp_from_rest(combat_occurred)
                        # TODO: ADD RESTING
                        gm.camera_chase_hero(hero.hero_pos[0], hero.hero_pos[1])
                        gm.update_game()

                    if hero.state == 'combat':
                        if hero.hero_turn_bool:
                            if (event.key == K_a):
                                cm.hero_turn(1)
                                hero.hero_turn_bool = False
                    #             ATTACK!
                                print('ATTACKING!')
                            elif (event.key == K_f):
                                cm.hero_turn(3)
                                print('flee')
                        else:
                            print('not heroes turn to act')

                    gm.update_game()
                    tm.update()


    # def is_valid_move(self,x,y,map):
    #     if map[y][x]!=
