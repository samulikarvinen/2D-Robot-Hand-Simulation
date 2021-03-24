from PyQt5.QtWidgets import *


class RobotGraphicsItem(QGraphicsItem):
    def __init__(self, robot):
        super(RobotGraphicsItem, self).__init__()
        # todo: add information from the robot class so that the robot can be drawn to the scene
        pass

    def update_pose(self):
        # todo: change some values based on the information from robot class
        pass
