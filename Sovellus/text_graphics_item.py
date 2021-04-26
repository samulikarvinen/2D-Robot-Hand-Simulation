from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np


class TextGraphicsItem(QGraphicsItemGroup):
    def __init__(self, robot, square):
        super(TextGraphicsItem, self).__init__()
        self.robot = robot
        self.square = square

        # add the coordinate of the end-effector as a text item
        text = "(" + str(round(self.robot.coord2[0])) + ", " + str(round(self.robot.coord2[1])) + ")"
        self.endeff_text = QGraphicsSimpleTextItem(text)
        self.endeff_text.setBrush(QBrush(QColor("cyan")))
        self.endeff_text.setPos(self.robot.coord2[0], self.robot.coord2[1])
        self.addToGroup(self.endeff_text)

        # add the first joint angle as a text item
        text = "{:.2f}\u00B0".format(self.robot.theta1)
        self.theta1_text = QGraphicsSimpleTextItem(text)
        self.theta1_text.setBrush(QBrush(QColor("cyan")))
        self.theta1_text.setPos(0, 0)
        self.addToGroup(self.theta1_text)

        # add the second joint angle as a text item
        text = "{:.2f}\u00B0".format(self.robot.theta2)
        self.theta2_text = QGraphicsSimpleTextItem(text)
        self.theta2_text.setBrush(QBrush(QColor("cyan")))
        self.theta2_text.setPos(self.robot.coord1[0], self.robot.coord1[1])
        self.addToGroup(self.theta2_text)

        # add the coordinate of the square as a text item
        text = "(" + str(round(self.square.location[0])) + ", " + str(round(self.square.location[1])) + ")"
        self.square_text = QGraphicsSimpleTextItem(text)
        self.square_text.setBrush(QBrush(QColor("red")))
        self.square_text.setPos(self.square.location[0], self.square.location[1])
        self.addToGroup(self.square_text)

    def update_text(self):
        # update the coordinate text of the end-effector
        self.endeff_text.setText("(" + str(round(self.robot.coord2[0])) + ", " + str(round(self.robot.coord2[1])) + ")")
        self.endeff_text.setPos(self.robot.coord2[0], self.robot.coord2[1])

        # update the first joint angle
        self.theta1_text.setText("{:.2f}\u00B0".format(self.robot.theta1))

        # update the second joint angle
        self.theta2_text.setText("{:.2f}\u00B0".format(self.robot.theta2))
        self.theta2_text.setPos(self.robot.coord1[0], self.robot.coord1[1])

        # update the coordinate text of the square
        self.square_text.setText("(" + str(round(self.square.location[0])) + ", "
                                 + str(round(self.square.location[1])) + ")")
        self.square_text.setPos(self.square.location[0], self.square.location[1])

