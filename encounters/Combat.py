'''This combat Object handles the operatinos of a combat scene.
    It will be passed the Hero and The Monster and the battle will play out here.
    That way at every stage of combat each method only needs to reference itself.
    Making the Monster and The Hero 'Transient Global Variables'''

from characters.Monster import Monster
from characters.Hero import Hero
from random import shuffle
from database.db import Data_Manager as DM
from random import randint

import pygame as pg
from pygame import key

# TODO: Add Combat Clock to try and establish some goddamn order for the turns. NOOTHIUNG ELSE IS WORKING

class Combat:
    def __init__(self, hero):
        self.hero = hero
        self.all_monsters = DM.generate_monster_list(hero)
        self.monster = None
        self.clock = pg.time.Clock()



    def is_it_battle_time(self, rest_or_not):
        if rest_or_not == False:
            # 20% chance of combat while wandering around
            randomThing = randint(1, 100)
            if randomThing % 5 == 0:
                # TODO: 10/22/16:: WHY IS THIS CAUSING A INFINITE LOOP OF SOME KIND
                self.hero.state = self.hero.states[1]
                self.battle_time(self.hero)
            else:
                pass
        elif rest_or_not == True:
            # 10%chance of combat while resting
            if randint(1, 100) % 10 == 0:
                self.battle_time(self.hero)
                return False
            else:
                return True



    def battle_time(self, hero):
        # get a monster from the list, remove it so if it dies it is gone

        if len(self.all_monsters)==0:
            self.all_monsters = DM.generate_monster_list(self.hero)
        try:
            self.monster = self.all_monsters.pop()
        except IndexError:
            print('out of monsters')
            self.hero.state = self.hero.states[4]
        # set to combat state so graphics will change
        self.hero.state = self.hero.states[1]
        list_of_participants = [self.hero, self.monster]
        shuffle(list_of_participants)
        # TODO: send a call to Text_Manager to display the combat options

        # While they both have life, keep battle going
        while self.hero.current_hp >= 1 and self.monster.current_hp >= 1:
            round_counter = 0
            # for each person in combat, let them take their turn
            for participant in list_of_participants:
                if hero.state == 'flee':
                    self.all_monsters.append(self.monster)
                    # randomize again
                    shuffle(self.all_monsters)
                    break
                else:
                    # This variable is for implementatino of potions and special attacks (since they last a limited time)
                    # THERE IS A LOOP THAT IS GOING FOREVER
                    self.take_a_turn(participant)
                    round_counter += 1
            #         if you are dead... exit combat after calling a HighScoreSave() method
        if self.hero.current_hp <= 0:
            # TODO: this becomes a call to text_manager --> GAME OVER SCREEN
            '''hero state set for game over mode'''
            hero.state = hero.states[3]
            '''This part here will be where the hall of fame stuff happens.  To be figured out later.
            My need to add 'state' to the DB in order to track who has died and who hasnt.'''
        #     If the monster is dead, get that cash and xp
        if self.monster.current_hp <= 0:
            self.hero.gain_xp(self.monster.xp_val)
            self.hero.money += self.monster.money
            # reset game_state to explore
            self.hero.state = hero.states[0]


    def take_a_turn(self, participant):

        # is it the monsters turn or the players turn?
        # check if they are dead
        if participant.current_hp <= 0:
            pass
        else:
            if isinstance(participant, Hero):
                # this is so input controller only accepts combat input when heros turn.
                self.hero.hero_turn_bool = True

                while self.hero.hero_turn_bool:
                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_a:
                                self.hero_turn(1)
                                self.hero.hero_turn_bool = False
                                break
                            #     TODO: Make fleeing work
                            # elif event.key == pg.K_f:
                            #     self.hero.state = self.hero.states[2]
                            #     self.hero.hero_turn_bool = False
                            #     break
            elif isinstance(participant, Monster) and self.hero.hero_turn_bool == False:
                self.hero.hero_turn_bool = False
                self.monster_turn()
                self.hero.hero_turn_bool = True

    def hero_turn(self, key):

        # display_fight_menu()
        '''DISPLAY COMBAT OPTIONS'''
        if key == 1:
            self.hero.attack_enemy(self.monster)
            self.clock.tick(30)
        #     removed til written
        # if key == 2:
        #     self.hero.special_attack(self.monster)
        if key == 3:
            self.hero.state = self.hero.states[2]
            self.clock.tick(30)
        # try:

        #     choice = int(input('| This legendary hero is going to :                                            |'
        #                        ).format(self.hero.name))
        #     if choice == 1:
        #         #     '|   1) Attack   2) Drink Potion   3) Check Hero Status    4) Flee the Battle   |'
        #         print('|                             Combat Begins!                                   |')
        #         self.hero.attack_enemy(self.monster)
        #         break
        #     if choice == 2:
        #         print('Potion Drinking Menu')
        #         # TODO: Fred's Potion Drinking
        #         break
        #     if choice == 3:
        #         self.hero.status()
        #
        #     if choice == 4:
        #         print('RUN AWAYYY')
        #         # This is where threading could be useful.  Send message to a other thread telling it the player has fled
        #         break
        # except ValueError or choice not in range(4):
        #     print('{} is baffled by your choice, and looks beseechingly towards the sky for guidance.'.format(
        #         self.hero.name))


    def monster_turn(self):
        self.monster.attack_enemy(self.hero)
        # TODO: CALL TEXT MANAGER FOR RESULTS TO DISPLAY