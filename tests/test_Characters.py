import unittest
import characters.Character as C
import characters.Hero as H
import characters.Monster as M
import database.db as db

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_base_char_classes)
    suite.addTest(test_db)

class test_base_char_classes(unittest.TestCase):

    def test_inits(self):
        char = C.Character('Grognak')
        # YOU MADE A CHARACTER
        self.assertIsInstance(char,C.Character)
        # You made a hero
        hero = H.Hero('Grognak', [20, 20])
        self.assertIsInstance(hero, H.Hero)
        # You made a monster
        monster = M.Monster('Goblin', 5, 5, 1)
        self.assertIsInstance(monster,M.Monster)

    def test_hero_methods(self):
        # check that the set_starter_stats consistently sets the stats
        hero1 = H.Hero('Grognak', [1, 1])
        hero1.set_starter_stats()
        self.assertTrue(hero1.current_hp,10)
        self.assertTrue(hero1.max_hp, 10)
        self.assertTrue(hero1.armor, 1)
        self.assertTrue(hero1.strength, 3)
#         Check that leveling works
        hero1.gain_xp(101)
        self.assertEqual(hero1.xp, 101)
        self.assertEqual(hero1.level, 2)
        # Check that set_opened_save_stats does the same
        hero1.set_opened_save_stats(8, 16, 3, 4, 150, 2, 1, 200, 23, 24)
        self.assertEqual(hero1.current_hp,8)
        self.assertEqual(hero1.max_hp, 16)
        self.assertEqual(hero1.armor, 3)
        self.assertEqual(hero1.strength, 4)
        self.assertEqual(hero1.xp, 150)
        self.assertEqual(hero1.level, 2)
        self.assertEqual(hero1.money, 1)
        self.assertEqual(hero1.next_level, 200)
        self.assertEqual(hero1.hero_pos, [23, 24])
        # check for hp gains
        hero1.gain_hp_from_rest(True)
        self.assertEqual(hero1.current_hp, 12)
        # check that not only does this heal, but not more than it should
        hero1.gain_hp_from_rest(False)
        self.assertEqual(hero1.current_hp, 14)
        # make sure 'overhealing' isnt possible
        hero1.gain_hp_from_rest(True)
        self.assertEqual(hero1.current_hp, 16)

        monster = M.Monster('Goblin', 5, 5, 1)
        monster.attack_enemy(hero1)
        # The goblin is too weak to harm the hero.
        self.assertEqual(hero1.current_hp,16)
        # The reverse is not true however
        hero1.attack_enemy(monster)
        self.assertLess(monster.current_hp, 1)

class test_db(unittest.TestCase):

    def make_db_handler(self):
        DB = db.Data_Manager()
        self.assertIsInstance(DB, db.Data_Manager)

    def check_generators(self):
        # Check the monster list generator
        hero = db.Hero('Grognak', [1, 1])
        list_mons = db.Data_Manager.generate_monster_list(hero)
        self.assertIsInstance(list_mons, list)
