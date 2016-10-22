#Not importing anything since it doesn't need to inherit from the other classes



class Item:
   # TODO MOVE THIS TO SEPERATE DIRECTORY
   def __init__(self, name, atk_value, arm_value, weight, special_prop, price):
        self.name = name
        self.atk_value = atk_value
        self.arm_value = arm_value
        self.weight = weight
        self.special_prop = special_prop
        self.price = price