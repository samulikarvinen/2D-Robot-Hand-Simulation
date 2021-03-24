from PyQt5.QtWidgets import *


class RobotGraphicsItem(QGraphicsItemGroup):
    def __init__(self, robot):
        super(RobotGraphicsItem, self).__init__()
        self.robot = robot

        # add the first link
        self.link1 = QGraphicsLineItem(0, 0, self.robot.coord1[0], self.robot.coord1[1])
        self.addToGroup(self.link1)

        # add the second link
        self.link2 = QGraphicsLineItem(self.robot.coord1[0], self.robot.coord1[1], self.robot.coord2[0], self.robot.coord2[1], self.link1)
        self.addToGroup(self.link2)

    def update_pose(self):
        self.link1.setRotation(self.robot.theta1)
        pass

