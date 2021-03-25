from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RobotGraphicsItem(QGraphicsItemGroup):
    def __init__(self, robot):
        super(RobotGraphicsItem, self).__init__()
        self.robot = robot

        link1_thick = 20
        link2_thick = 18
        endeff_thick = 20

        # add the first link
        self.link1 = QGraphicsLineItem()
        self.link1.setLine(0, 0, self.robot.coord1[0], self.robot.coord1[1])
        self.link1.setPen(QPen(QBrush(QColor(0, 0, 0)), link1_thick, Qt.PenStyle(Qt.SolidLine), Qt.PenCapStyle(Qt.RoundCap)))
        self.addToGroup(self.link1)

        # add the second link
        self.link2 = QGraphicsLineItem()
        self.link2.setLine(self.robot.coord1[0], self.robot.coord1[1], self.robot.coord2[0], self.robot.coord2[1])
        self.link2.setPen(QPen(QBrush(QColor(255, 0, 0)), link2_thick, Qt.PenStyle(Qt.SolidLine), Qt.PenCapStyle(Qt.RoundCap)))
        self.addToGroup(self.link2)

        # add the end-effector
        self.endeff = QGraphicsEllipseItem()
        self.endeff.setRect(0, 0, endeff_thick, endeff_thick)
        self.endeff.setPos(self.robot.coord2[0]-endeff_thick/2, self.robot.coord2[1]-endeff_thick/2)
        self.endeff.setBrush(QBrush(QColor(0, 0, 255)))
        self.addToGroup(self.endeff)

    def update_pose(self):
        self.link1.setLine(0, 0, self.robot.coord1[0], self.robot.coord1[1])
        self.link2.setLine(self.robot.coord1[0], self.robot.coord1[1], self.robot.coord2[0], self.robot.coord2[1])
        self.endeff.setPos(self.robot.coord2[0]-10, self.robot.coord2[1]-10)

