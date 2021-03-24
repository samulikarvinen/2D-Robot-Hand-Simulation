import math
import numpy as np
from item import Item


# TODO: based on the suction, move the item with the end-effector

class Robot:
    # initializing the robot information
    def __init__(self, len1, len2):
        self.len1 = len1
        self.len2 = len2
        self.theta1 = 90  # in degrees
        self.theta2 = 90  # in degrees
        self.coord1 = np.array([0, self.len1])  # when in 90 degrees
        self.coord2 = np.array([self.len2, self.len1])  # when in 90 degrees
        self.suction = False

    def move_with_angles(self, window, theta1, theta2):
        # Window: window class
        # here the forward kinematics should be used and based on that the graphics will be updated
        # the other angle stays static in manual, where it is then just called as robot.theta 1 or 2.

        # updating the angles
        self.theta1 = theta1
        self.theta2 = theta2

        # updates the coordinates of the robot based on the new angles
        self.forward_kinematics(self.theta1, self.theta2)

        # update the graphics
        window.update_graphics

        pass

    def move_with_coordinates(self, window, x, y):
        # todo: Linear movement towards the destined coordinate; update graphics in each loop
        pass

    def forward_kinematics(self, theta1, theta2):
        # changing into radians for easier calculation
        theta1 = math.radians(theta1)
        theta2 = math.radians(theta2)

        # calculating the coordinates of the second joint
        x1 = self.len1 * math.cos(theta1)
        y1 = self.len1 * math.sin(theta1)

        # changing the coordinates of the second joint
        self.coord1 = np.array([x1, y1])

        # calculating the coordinates of the end-effector
        x2 = x1 + self.len2 * math.cos(theta1 + theta2)
        y2 = y1 + self.len2 * math.sin(theta1 + theta2)

        # changing the coordinates of the end-effector
        self.coord2 = np.array([x2, y2])

        # if suction is True, put the self.coord2 also for item: window.item.coord = self.coord2

        pass

    def inverse_kinematics(self, coordinates):
        # todo: return joint angles in degrees based on the current coordinates
        pass
