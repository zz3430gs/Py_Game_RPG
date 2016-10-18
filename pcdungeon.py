'''This is my attempt at a procedural dungeon generator,
once one is made, blitting it to the suface should be pretty e4asy.
this file will be full of classes for the purpose of creating this dungeon... no idea how it will go.'''
import math


class Room:
    # room coordinates
    # TILE SIZE WILL ALWAYS BE 25px
    def __init__(self, x, y, width, height):
        self.x1 = x
        self.x2 = self.x1 + width
        self.y1 = y
        self.y2 = self.y1 + height
        # room size, l x w
        self.width = width
        self.height = height
        # center of room
        self.center = self.find_center(self.x1, self.x2, self.y1, self.y2)

    @staticmethod
    def find_center(x1, x2, y1, y2):
        center = (math.floor((x1 + x2) / 2), math.floor((y1 + y2) / 2))
        return center

    def intersects(self, room):
        if self.x1 <= room.x2 and self.x2 >= room.x1 and self.y1 <= room.y2 and room.y2 >= room.y1:
            return True
        else:
            return False
