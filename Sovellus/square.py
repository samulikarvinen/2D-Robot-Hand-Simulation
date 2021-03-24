import math
import random


class Square:
    def __init__(self, width, height, radius):
        self.width = width
        self.height = height

        # setting up random location inside the radius, which is in reach for the robot
        alpha = 2 * math.pi * random.random()
        r = radius * math.sqrt(random.random())
        x = r * math.cos(alpha)
        y = r * math.sin(alpha)
        self.location = x, y

    def set_location(self, location):
        self.location = location
