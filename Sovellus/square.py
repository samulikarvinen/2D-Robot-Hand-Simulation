import math
import random


class Square:
    def __init__(self, width, height, radius):
        # giving the 'physical' information about the square.
        self.width = width
        self.height = height

        # setting up random location inside the radius, which is in reach for the robot (radius = len1+len2)
        alpha = 2 * math.pi * random.random()
        r = radius * math.sqrt(random.random())
        x = r * math.cos(alpha)
        y = r * math.sin(alpha)
        self.location = x, y

    def set_location(self, location):
        # setting a new location based on the updated location
        self.location = location
