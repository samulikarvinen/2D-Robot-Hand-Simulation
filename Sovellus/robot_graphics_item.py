from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RobotGraphicsItem(QGraphicsItemGroup):
    def __init__(self, robot):
        # grouping up two lines, one square and three circles to build a graphical robot
        super(RobotGraphicsItem, self).__init__()
        self.robot = robot

        # dimensions of the graphic items
        self.platform_thick = 40
        self.link1_thick = 28
        self.joint1_thick = 20
        self.link2_thick = 25
        self.joint2_thick = 18
        self.endeff_thick = 18

        # add platform
        self.platform = QGraphicsRectItem()
        self.platform.setRect(0, 0, self.platform_thick, self.platform_thick)
        self.platform.setPos(0-self.platform_thick/2, 0-self.platform_thick/2)
        self.platform.setBrush(QBrush(QGradient(QGradient.RichMetal)))
        self.addToGroup(self.platform)

        # add the first link
        self.link1 = QGraphicsLineItem()
        self.link1.setLine(0, 0, self.robot.coord1[0], self.robot.coord1[1])
        self.link1.setPen(QPen(QBrush(QColor("black")), self.link1_thick, Qt.PenStyle(Qt.SolidLine), Qt.PenCapStyle(Qt.RoundCap)))
        self.addToGroup(self.link1)

        # add the first joint
        self.joint1 = QGraphicsEllipseItem()
        self.joint1.setRect(0, 0, self.joint1_thick, self.joint1_thick)
        self.joint1.setPos(0-self.joint1_thick/2, 0-self.joint1_thick/2)
        self.joint1.setBrush(QBrush(QGradient(QGradient.RichMetal)))
        self.addToGroup(self.joint1)

        # add the second link
        self.link2 = QGraphicsLineItem()
        self.link2.setLine(self.robot.coord1[0], self.robot.coord1[1], self.robot.coord2[0], self.robot.coord2[1])
        self.link2.setPen(QPen(QBrush(QBrush(QGradient(QGradient.RichMetal))), self.link2_thick, Qt.PenStyle(Qt.SolidLine), Qt.PenCapStyle(Qt.RoundCap)))
        self.addToGroup(self.link2)

        # add the second joint
        self.joint2 = QGraphicsEllipseItem()
        self.joint2.setRect(0, 0, self.joint2_thick, self.joint2_thick)
        self.joint2.setPos(self.robot.coord1[0]-self.joint2_thick/2, self.robot.coord1[1]-self.joint2_thick/2)
        self.joint2.setBrush(QBrush(QColor("black")))
        self.addToGroup(self.joint2)

        # add the end-effector
        self.endeff = QGraphicsEllipseItem()
        self.endeff.setRect(0, 0, self.endeff_thick, self.endeff_thick)
        self.endeff.setPos(self.robot.coord2[0]-self.endeff_thick/2, self.robot.coord2[1]-self.endeff_thick/2)
        self.endeff.setBrush(QBrush(QColor("black")))
        self.addToGroup(self.endeff)

    def update_pose(self):
        # update with the new updated information
        self.link1.setLine(0, 0, self.robot.coord1[0], self.robot.coord1[1])
        self.link2.setLine(self.robot.coord1[0], self.robot.coord1[1], self.robot.coord2[0], self.robot.coord2[1])
        self.joint2.setPos(self.robot.coord1[0]-self.joint2_thick/2, self.robot.coord1[1]-self.joint2_thick/2)
        self.endeff.setPos(self.robot.coord2[0]-self.endeff_thick/2, self.robot.coord2[1]-self.endeff_thick/2)

