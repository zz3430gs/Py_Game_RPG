'''This combat Object handles the operatinos of a combat scene.
    It will be passed the Hero and The Monster and the battle will play out here.
    That way at every stage of combat each method only needs to reference itself.
    Making the Monster and The Hero 'Transient Global Variables'''

from characters.Monster import Monster
from characters.Hero import Hero
from random import shuffle
from database.db import Data_Manager as DM
from random import randint
from time import sleep
import pygame as pg
# from game.displays import *
# TODO: Add Combat Clock to try and establish some goddamn order for the turns. NOOTHIUNG ELSE IS WORKING
class Combat:
    def __init__(self, hero):
        self.hero = hero
        self.all_monsters = DM.generate_monster_list(hero)
        self.monster = None
        self.clock = pg.time.Clock()

    def is_it_battle_time(self,rest_or_not):
        if rest_or_not == False:
            # 20% chance of combat while wandering around
            if randint(1, 100) % 5:
                # TODO: 10/22/16:: WHY IS THIS CAUSING A INFINITE LOOP OF SOME KIND
                self.battle_time(self.hero)
        elif rest_or_not == True:
            # 10%chance of combat while resting
            if randint(1,100) % 10:
                self.battle_time(self.hero)
                return False
            else:
                return True

    def battle_time(self, hero):
        # get a monster from the list, remove it so if it dies it is gone
        self.monster = self.all_monsters.pop()
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
                # TODO: input controller resets this to false after executing the hero attacks
                self.hero.hero_turn_bool = True
                # pg.event.wait()
                # THIS DIDNT WORK
                # while self.hero.hero_turn_bool == True:
                #     print('waiting_on_player')
                # self.hero_turn()
            elif isinstance(participant, Monster) and self.hero.hero_turn_bool == False:

                self.monster_turn()

    def hero_turn(self, key):
        while True:
            # display_fight_menu()
            '''DISPLAY COMBAT OPTIONS'''
            if key == 1:
                self.hero.attack_enemy(self.monster)
            #     removed til written
            # if key == 2:
            #     self.hero.special_attack(self.monster)
            if key == 3:
                self.hero.state = self.hero.states[2]
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