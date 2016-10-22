#same thing, don't see the need to inherit from other classes (maybe Item?)

# TODO MOVE THIS TO SEPERATE DIRECTORY
class Inventory():
    def __init__(self, owner):
        self.inventory = []
        self.owner = owner

    def add_item(self, item):
        self.inventory[item.name] = item

#     POTION OF ATTACK, POTION OF HEALTH, POTION OF ARMOR

#    TODO: A method to print the inventory