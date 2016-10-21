from characters.Character import Character
from characters import data


class Hero(Character):
    def __init__(self, name, start_pos):
        # TODO: Make the name max 16 characters
        super().__init__(name)
        # in the future a additional Class class will grant further inheritence
        # Which will make many of these happen there, not here.
        self.states = ['explore', 'combat', 'game_over', 'inventory', 'level_up', 'new_game']
        self.state = self.states[0]
        self.armor = 1  # Used to figure out if you missed
        self.strength = 3  # Used for the max on damage
        self.xp = 0
        self.level = 1
        self.money = 5
        self.next_level = 100
        # todo: Someday have multiple sprites for the hero.
        # self.image = 'sprites/Hero.png'
        # hero position  x, y
        self.hero_pos = [start_pos[0], start_pos[1]]
        self.set_starter_stats()
        self.inventory = []
        '''self.killcount = 0'''

    # TODO: Add a kill Counter for additional Highscore info

    def set_state(self, new_state):
        self.state = new_state
    #     This will only be used in the next version of the game for state checking so people cant fighrt when theyre at the merchant etc



    def set_starter_stats(self):
        self.armor = 1
        self.strength = 3
        self.max_hp = 10
        self.current_hp = 10

    def set_opened_save_stats(self,hp,max_hp,armor,strength,xp,level,money,next_level, inventory):
        self.current_hp = hp
        self.max_hp=max_hp
        self.armor = armor
        self.strength = strength
        self.xp = xp
        self.level = level
        self.money = money
        self.next_level = next_level
        self.sort_inventory(inventory)
        '''self.killcount=killcount'''

    def sort_inventory(self,inventory):
        for item in inventory:
            self.inventory.append(item)

    def gain_xp(self, xp):
        self.xp += xp
        if xp >= self.next_level:
            # If the Heros XP is more than the next level
            # Level him up
            self.gain_level()
        else:
            pass

    def gain_level(self):
        # Sort through the Dictionary of Levels,
        levels = data.get_levels()
        next_level_xp = levels[self.level+1]
        self.max_hp += 3
        self.strength += 1
        if self.level % 3 == 0:
            self.armor += 1
        self.level += 1
        self.next_level = next_level_xp


    def gain_hp_from_rest(self, full_rest):
        # full_rest is a boolean
        if full_rest:
            self.current_hp += self.level*2
            if self.current_hp>self.max_hp:
                self.current_hp = self.max_hp
        if full_rest == False:
            self.current_hp += self.level
            if self.current_hp>self.max_hp:
                self.current_hp = self.max_hp

