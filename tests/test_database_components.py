import unittest
import database.db as db

class test_db(unittest.TestCase):

    def make_db_handler(self):
        DB = db.Data_Manager()
        self.assertIsInstance(DB, db.Data_Manager)

    def check_generators(self):
        # Check the monster list generator
        hero = db.Hero('Grognak', [1, 1])
        list_mons = db.Data_Manager.generate_monster_list(hero)
        self.assertIsInstance(list_mons, list)
