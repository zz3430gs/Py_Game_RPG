import pygame

import graphics.graphics_manager as GM
from characters.Hero import Hero
from database.db import Data_Manager as DB
from encounters.Combat import Combat as CM
from graphics.input_controller import input_controller as IC
from graphics.main_display import Main_Display as MD
from graphics.map import Map_Maker as MM
from graphics.text_manager import Text_Manager as TM


def main():
    while True:
        # init data soures
        dm = DB()
        # make the screen object
        pygame.init()
        md = MD()
        # make map
        mm = MM()
        # instantiate hero--> TODO: Make this a DB lookup or a new Game
        hero = Hero('Grognak', mm.hero_start)
        # make monsters for level
        cm = CM(hero)
        gm = GM.graphics_manager(md.base_surface,mm, hero,cm)
        tm = TM(md.base_surface, hero, cm)

        gm.update_game()
        tm.update()
        ic = IC(gm,tm,cm, hero)


        pygame.display.update()


main()

